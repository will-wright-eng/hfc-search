from fastapi import APIRouter

from app.utils.elasticsearch_client import search_index

router = APIRouter()


@router.get("/search/")
def search(query: str):
    results = search_index("my_index", query)
    return results
