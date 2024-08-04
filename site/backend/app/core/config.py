import os
from pathlib import Path


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "hfc-search")
    DATA_DIR: Path = Path(os.getenv("DATA_DIR", "/app/data"))


settings = Settings()
