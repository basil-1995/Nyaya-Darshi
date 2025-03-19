from app.database.db import users_collection
from app.models.user_model import UserSchema
from fastapi import HTTPException, status


async def get_users():
    users = []
    async for user in users_collection.find():
        user["id"] = str(user["_id"])  # Convert ObjectId to string
        del user["_id"]  # Remove original ObjectId field
        users.append(UserSchema(**user))
    return users


async def create_user(user: dict):
    try:

        result = await users_collection.insert_one(user)
        
        if result.inserted_id:
            return {
                "id": str(result.inserted_id),  # Convert ObjectId to string
                "message": "User created successfully",
                "status": status.HTTP_201_CREATED
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to insert user"
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )