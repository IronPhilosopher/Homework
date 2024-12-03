import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(10):
    cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i+1}', f'examlpe{i+1}@gmail.com', f'{(i+1)*10}', '1000'))

cursor.execute('UPDATE Users SET balance = ? WHERE age % 20 != 0', (500,))
cursor.execute('DELETE FROM Users WHERE (age-10) % 3 == 0')
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
all_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
sumb = cursor.fetchone()[0]
print(sumb/all_users)

connection.close()