import os
from pathlib import Path


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "hfc-search")
    DATA_DIR: Path = Path(os.getenv("DATA_DIR", "/app/data"))
    ELASTICSEARCH_URL: str = os.getenv("ELASTICSEARCH_URL", "http://elasticsearch:9200")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
