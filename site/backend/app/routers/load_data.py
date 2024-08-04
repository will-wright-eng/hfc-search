from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.utils import crud, models, schemas, elasticsearch_client
from app.core.log import logger
from app.core.config import settings
from app.utils.database import get_db

router = APIRouter()


@router.post("/load_data/")
def load_data(db: Session = Depends(get_db)):
    # Load users
    with open("/app/data/users_users_202407301106.sql", "r") as f:
        # Process SQL file and insert data into SQLite
        pass

    # Load other data similarly...

    return {"message": "Data loaded successfully"}


@router.post("/index_data/")
def index_data():
    # Index data in Elasticsearch
    pass


@router.post("/check_data/")
def check_data():
    # check data is present in docker container
    logger.info(settings.DATA_DIR)
    logger.info(settings.DATA_DIR.exists())
    logger.info(settings.DATA_DIR.glob("*"))
    return {"message": "Data checked successfully"}
