from fastapi import FastAPI
from app.database.db import init_db
from app.router import gov_router, legal_router, user_router

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await init_db() 


@app.get("/")
async def root():
    return {"message": "Welcome to Nyaya Darshi API"}


app.include_router(user_router.router)
app.include_router(legal_router.router)
app.include_router(gov_router.router)