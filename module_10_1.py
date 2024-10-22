import time
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f"Какое-то слово №{i+1}\n")
        time.sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")
    return

start1 = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
fin1 = datetime.now()
timetaken1 = fin1-start1
print(timetaken1)
start2 = datetime.now()
w1 = Thread(target=write_words, args=(10, "example5.txt"))
w2 = Thread(target=write_words, args=(30, "example6.txt"))
w3 = Thread(target=write_words, args=(200, "example7.txt"))
w4 = Thread(target=write_words, args=(100, "example8.txt"))

w1.start()
w2.start()
w3.start()
w4.start()

w1.join()
w2.join()
w3.join()
w4.join()
fin2 = datetime.now()
timetaken2 = fin2-start2
print(timetaken2)