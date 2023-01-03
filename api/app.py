from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from .handlers.users.users import get_all_users_data, get_user

app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
    "https://localhost:8000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    tg_id: int = Body(..., example={'tg_id': 755989898})


@app.get("/get_all_users/")
async def get_all_users():
    all_users: list = await get_all_users_data()
    data = {
        "users":
            [
                {
                    "tg_id": user_id,
                    "register_time": reg_time
                } for user_id, reg_time in all_users
            ]
    }
    return data


@app.get("/get_user_data/")
async def get_user_data(item: Data):
    user_data: list = await get_user(item.tg_id)
    return {
        "name": user_data[0][0],
        "city": user_data[0][1],
        "phone": user_data[0][2],
        "files": [
            {
                "file_category": file_category,
                "file_id": file_id,
            } for _, _, _, file_category, file_id in user_data
        ]
    }
