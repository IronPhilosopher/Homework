from fastapi import FastAPI, Path
from typing import Annotated

users = {
    '1': 'Имя: Example, возраст: 18'
}

app2 = FastAPI()

@app2.get("/users")
async def user_list():
    return users

@app2.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='User')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=42)]):
    new_id = int(max(users))+1
    new_user = {f'{new_id}': f'Имя: {username}, возраст: {age}'}
    users.update(new_user)
    return {f'The user {new_id} is registered'}

@app2.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=42)],
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description='Enter username', example='User')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=42)]):
    try:
        upd_user = {f'{str(user_id)}': f'Имя: {username}, возраст: {age}'}
        users.update(upd_user)
        return {f'The user {user_id} is updated'}
    except KeyError:
        return {'User not found'}

@app2.delete('/user/{user_id}')
async def del_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=42)]):
    try:
        users.pop(str(user_id))
        return {'User is deleted'}
    except:
        return {'User was already deleted'}

