import faiss
import numpy as np
from openai import OpenAI
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.utils import crud
from app.core.log import logger
from app.core.config import settings
from app.utils.database import get_db

router = APIRouter()
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_embedding_vector(text):
    response = client.embeddings.create(input=[text], model="text-embedding-ada-002")
    return response.data[0].embedding


@router.post("/search/")
def search(query: str = "marketing", db: Session = Depends(get_db)):
    logger.info("Performing semantic search")
    users = crud.get_all_users(db)[:50]

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    query_embedding = get_embedding_vector(query)
    # Create embeddings for user data
    user_data = [f"{user.fname} {user.pnoun} {user.location} {user.profile_bio or ''}" for user in users]
    user_embeddings = [get_embedding_vector(data) for data in user_data]
    # Create FAISS index
    index = faiss.IndexFlatL2(len(query_embedding))
    index.add(np.array(user_embeddings).astype("float32"))
    # Perform search - top 5 results or less if fewer users
    k = min(5, len(users))
    D, I = index.search(np.array([query_embedding]).astype("float32"), k=k)
    # Prepare results
    results = [
        {
            "id": users[i].id,
            "fname": users[i].fname,
            "pnoun": users[i].pnoun,
            "location": users[i].location,
            "profile_bio": users[i].profile_bio,
            "score": float(D[0][j]),
        }
        for j, i in enumerate(I[0])
    ]

    return results


@router.post("/reindex/")
def reindex_documents(db: Session = Depends(get_db)):
    documents = crud.get_all_users(db)
    for doc in documents:
        embedding = get_embedding_vector(doc.content)
        doc.embedding = ",".join(map(str, embedding))
        db.add(doc)
    db.commit()
    return {"message": "Reindexing completed", "total_documents": len(documents)}


@router.post("/get_embedding/")
def get_embedding_route(text: str):
    embedding = get_embedding_vector(text)
    return {"embedding": ",".join(map(str, embedding))}
