from fastapi import FastAPI, Request

from app.core.log import logger
from app.core.config import settings
from app.routers.search import router as search_router
from app.utils.database import Base, engine
from app.routers.load_data import router as load_data_router
from app.routers.semantic_search import router as semantic_search_router

app = FastAPI(title=settings.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")
Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting backend")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down backend")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Routers
app.include_router(
    load_data_router,
    prefix="/v1/data",
    tags=["load_data"],
)
app.include_router(
    search_router,
    prefix="/v1/search",
    tags=["search"],
)
app.include_router(
    semantic_search_router,
    prefix="/v1/semantic_search",
    tags=["semantic_search"],
)
