from fastapi import FastAPI
from app.routers import crm

app = FastAPI(title="FastAPI Ecodes API")

app.include_router(crm.router)