from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.utils import crud
from app.core.log import logger
from app.utils.database import get_db
from app.utils.elasticsearch_client import es

router = APIRouter()


@router.get("/search/es/")
def search_es(query: str):
    results = es.search(
        index="users",
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["fname", "pnoun", "location", "profile_bio"],
                },
            },
        },
    )
    return results


@router.post("/search/sqlite/")
def search_sqlite(query: str, db: Session = Depends(get_db)):
    logger.info("Searching sqlite")
    users = crud.get_all_users(db)

    filtered_users = [
        user
        for user in users
        if query.lower() in user.fname.lower()
        or query.lower() in user.pnoun.lower()
        or query.lower() in user.location.lower()
        or (user.profile_bio and query.lower() in user.profile_bio.lower())
    ]

    return filtered_users
