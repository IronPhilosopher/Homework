import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner tests.log', encoding='utf-8',
                    format='%(asctime)s │ %(levelname)s │ %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_challange(self):
        cain = Runner('Cain')
        abel = Runner('Abel')
        for i in range(10):
            cain.walk()
            abel.run()
        self.assertNotEqual(cain.distance, abel.distance)

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            lilith = Runner('Lilith', -2)
            for i in range(10):
                lilith.walk()
            self.assertEqual(lilith.distance, -20)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            ad4m = Runner(4)
            for i in range(10):
                ad4m.run()
            self.assertEqual(ad4m.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')


logging.debug('d')
logging.info('i')
logging.warning('w')
logging.error('e')
logging.critical('ce')