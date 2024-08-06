from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.utils import crud, schemas
from app.core.log import logger
from app.core.config import settings
from app.utils.database import get_db
from app.utils.elasticsearch_client import es

router = APIRouter()


@router.post("/index_users_data/")
def index_users_data(db: Session = Depends(get_db)):
    logger.info("Indexing users data")
    users = crud.get_all_users(db)
    for user in users:
        es.index(index="users", id=user.id, body=schemas.User.from_orm(user).dict())

    return {"message": "Data indexed successfully"}


@router.post("/check_data/")
def check_data():
    logger.info("Checking data")
    try:
        return {
            "message": "Data checked successfully",
            "DATA_DIR": settings.DATA_DIR,
            "DATA_DIR-exists": settings.DATA_DIR.exists(),
            "files-in-DATA_DIR": [str(file.name) for file in settings.DATA_DIR.glob("*")],
        }
    except Exception as e:
        return {"message": "Data check failed", "error": str(e)}


@router.post("/get_users_sample/")
def get_users_sample(db: Session = Depends(get_db)):
    logger.info("Getting users sample")
    users = crud.get_all_users(db)
    return users[:10]
