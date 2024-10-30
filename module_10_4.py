from threading import Thread
import random
import time
from queue import Queue

class Guest(Thread):
    def __init__(self, name:str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Table():
    def __init__(self, number:int, guest:Guest=None):
        self.number = number
        self.guest = guest

class Cafe():
    def __init__(self, *tables:Table):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests:Guest):
        for g in guests:
            te = False
            for ta in self.tables:
                if ta.guest is None:
                    te = True
            if te:
                for t in self.tables:
                    if t.guest is None:
                        t.guest = g
                        t.guest.start()
                        print(f"{g.name} сел за стол номер {t.number}")
                        break
            else:
                self.queue.put(g)
                print(f"{g.name} в очереди")

    def discuss_guests(self):
        to = False
        for ta in self.tables:
            if ta.guest is not None:
                to = True
        while to or not self.queue.empty():
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest.name} покушал(-а) и ушел(ушла)')
                    print(f"Стол номер {t.number} свободен")
                    t.guest = None
                    to = False
                    for ta in self.tables:
                        if ta.guest is not None:
                            to = True
                if not self.queue.empty():
                    for t in self.tables:
                        if t.guest is None:
                            t.guest = self.queue.get()
                            print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                            t.guest.start()

tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()