import os
import time
directory = '.'
walk = []
for i in os.walk(directory):
    walk.append(i)
os.chdir(directory)
files = [f for f in os.listdir(directory) if os.path.isfile(f)]
dirs = [d for d in os.listdir(directory) if os.path.isdir(d)]
d2 = os.getcwd()
path = os.path.join(d2)
root = os.path.dirname(d2)
for file in files:
    f_time = os.path.getmtime(file)
    f_size = os.path.getsize(file)
    print(f'Обнаружен файл: {file}, Путь: {path}, Размер: {f_size}, Время изменения: {f_time}, Родительская директория: {root}')
