# tests/test_http_client.py
import pytest
import httpx
import respx

from tramita.http.client import HttpClient


@pytest.mark.asyncio
async def test_get_text_ok():
    with respx.mock(base_url="https://api.example.com") as mock:
        mock.get("/ping").respond(200, text="pong")
        async with HttpClient("https://api.example.com", rate_per_sec=100, timeout=5, user_agent="x") as hc:
            txt = await hc.get_text("/ping")
            assert txt == "pong"


@pytest.mark.asyncio
async def test_get_text_retry_then_ok():
    with respx.mock(base_url="https://api.example.com") as mock:
        route = mock.get("/flaky")
        route.side_effect = [
            httpx.Response(503, text="nope"),
            httpx.Response(200, text="ok"),
        ]
        async with HttpClient("https://api.example.com", rate_per_sec=100, timeout=5, user_agent="x") as hc:
            txt = await hc.get_text("/flaky")
            assert txt == "ok"
