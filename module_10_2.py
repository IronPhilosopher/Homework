from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name=str, power=int ):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        day = 0
        while enemies > 0:
            enemies -= self.power
            day += 1
            sleep(1)
            print(f'{self.name},сражается {day} день, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Dinadan' , 20)
second_knight = Knight('Sir Gawain', 25)

first_knight.start()
sleep(0.01)
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы выиграны!")