from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field

users = []

app3 = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

@app3.get("/users")
async def user_list():
    return users

@app3.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                                 description='Enter username', example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=42)]):
    new_id = max((u.id for u in users), default=0)+1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app3.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=1)],
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanTest')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u
    raise HTTPException(status_code=404, detail="User was not found")

@app3.delete('/user/{user_id}')
async def del_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=2)]):
    for i, u in enumerate(users):
       if u.id == user_id:
           deleted = users[i]
           del users[i]
           return deleted
    raise HTTPException(status_code=404, detail="User was not found")

