from fastapi import FastAPI

app1 = FastAPI()

@app1.get('/')
async def main_page():
    return {"Главная страница"}

@app1.get('/user/admin')
async def admin_page():
    return {"Вы вошли как администратор"}

@app1.get('/user/{user_id}')
async def user_page(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}

@app1.get('/user')
async def user_info(username: str = 'user', age: int = 22):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}."}