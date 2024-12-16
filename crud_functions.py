import sqlite3
import asyncio

connection = sqlite3.connect('medbot.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);            
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')

def get_all_products():
    connection = sqlite3.connect('medbot.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


def add_user(username:str, email:str, age:int):
    connection = sqlite3.connect('medbot.db')
    cursor = connection.cursor()
    exist = is_included(username)
    if not exist:
        cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
        connection.commit()
        connection.close()
        return


def is_included(username:str):
    connection = sqlite3.connect('medbot.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM Users WHERE username = ?', (username,))
    t = cursor.fetchone()
    connection.close()
    return t is not None


connection.commit()
connection.close()