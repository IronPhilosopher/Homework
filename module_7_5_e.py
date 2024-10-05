import os
import time
directory = '.'
walk_r = []
walk_d = []
walk_f = []
for r, d, f in os.walk(directory):
    walk_r.append(r)
    walk_d.append(d)
    walk_f.append(f)

for root in walk_r:
    r = walk_r.index(root)
    for file in walk_f[r]:
        file_time = os.path.getmtime(file)
        f_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        f_size = os.path.getsize(file)
        path = os.path.join(root, file)
        print(f'Обнаружен файл: {file}, Путь: {path}, Размер: {f_size}, Время изменения: {f_time}, Родительская директория: {root}')
print()