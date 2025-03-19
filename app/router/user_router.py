from fastapi import HTTPException, status,APIRouter
from app.models.user_model import UserSchema
from app.services.user_service import create_user, get_users

sample_users = [
    {"name": "John Doe", "email": "johndoe@example.com"},
    {"name": "James Johnson", "email": "james.johnson@example.com"},
    {"name": "Jack Smith", "email": "jack.smith@example.com"},
    {"name": "Charlie K", "email": "charlie.K@example.com"},
    {"name": "Honey Prince", "email": "honey.prince@example.com"},
    {"name": "Ethan Hunt", "email": "ethan.hunt@example.com"},
    {"name": "Fiona Adams", "email": "fiona.adams@example.com"},
    {"name": "George Miller", "email": "george.miller@example.com"},
    {"name": "Hannah Lee", "email": "hannah.lee@example.com"},
    {"name": "Ian Wright", "email": "ian.wright@example.com"}
]

router = APIRouter()



@router.get("/users", tags=["Users"])
async def fetch_users():
    users = await get_users()
    return {"users": users}


@router.post("/createusers", tags=["Create User"])
async def create_users(user:UserSchema):
    try:
        user_data = user.dict()
        result = await create_user(user_data)
        print(result,"result");
        return {
           "id": result["id"],  # Convert MongoDB ObjectId to string
            "message": "User created successfully",
            "status": status.HTTP_201_CREATED
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )