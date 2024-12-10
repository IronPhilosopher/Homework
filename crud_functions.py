import sqlite3

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

def get_all_products():
    connection = sqlite3.connect('medbot.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


connection.commit()
connection.close()