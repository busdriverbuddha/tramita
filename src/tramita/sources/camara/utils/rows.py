# tramita/sources/camara/utils/rows.py

import json

from typing import TypedDict


class BronzeRow(TypedDict):
    source: str
    entity: str
    year: int
    id: str
    url: str
    payload_json: str


def _row(
    entity: str,
    year: int,
    id: str,
    url: str,
    dados: list[dict] | dict,
    wrap_dados: bool = True,
) -> BronzeRow:
    payload = {"dados": dados} if wrap_dados else dados
    return {
        "source": "camara",
        "entity": entity,
        "year": year,
        "id": str(id),
        "url": url,
        "payload_json": json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ),
    }
