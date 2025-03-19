from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING

MONGO_URL = "mongodb+srv://basilsajupallath:Basil%408943@nyayadarshi-clustor.o317k.mongodb.net/"  # Update if using MongoDB Atlas
DB_NAME = "nyayadarshidb"

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URL)
database = client[DB_NAME]
users_collection = database["Users"]

# Ensure indexes for faster queries
async def init_db():
    await users_collection.create_index([("email", ASCENDING)], unique=True)
