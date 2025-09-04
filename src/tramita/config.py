# tramita/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # Keep base URLs env-driven to avoid hardcoding surprises
    camara_base_url: str = Field(..., description="Base URL for the Camara API")
    senado_base_url: str = Field(..., description="Base URL for the Senado API")
    camara_rate: float = Field(10.0, description="req/sec")
    senado_rate: float = Field(5.0, description="req/sec")
    http_timeout: float = 30.0
    user_agent: str = "tramita/0.1 (+contact: you@example.com)"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="tramita_")


settings = Settings()  # type: ignore
