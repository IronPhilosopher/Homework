def cuastom_write(file_name, strings):
    file = open(f'{file_name}', 'w', encoding='utf-8')
    a = 0
    string_positions = {}
    for i in strings:
        a += 1
        string_positions.update({(a, file.tell()): i})
        file.write(f'{i}\n')
    file.close()
    return string_positions

info = [
    'Text for tell.',
    "Используйте кодировку utd-8.",
    "Beause there are 2 languages!",
    "Спасибо!"
]

result = cuastom_write('text.txt', info)
for elem in result.items():
    print(elem)