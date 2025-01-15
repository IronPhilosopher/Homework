from fastapi import FastAPI, Path
from typing import Annotated

app1 = FastAPI()

@app1.get('/')
async def main_page():
    return {"Главная страница"}

@app1.get('/user/admin')
async def admin_page():
    return {"Вы вошли как администратор"}

@app1.get('/user/{user_id}')
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=42)]):
    return {f"Вы вошли как пользователь № {user_id}"}

@app1.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='User')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=42)]):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}."}
