from threading import Lock, Thread
import random
from time import sleep
class Bank:
    def __init__(self, balance:int, lock=Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            add = random.randint(50, 500)
            self.balance += add
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            print(f'Пополнение: {add}. Баланс: {self.balance}')
         sleep(0.001)

    def take(self):
        for i in range(100):
            dec = random.randint(50, 500)
            print(f'Запрос на {dec}.')
            if dec <= self.balance:
                self.balance -= dec
                print(f'Снятие: {dec}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств.')
                self.lock.acquire()

bk = Bank(100)
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
