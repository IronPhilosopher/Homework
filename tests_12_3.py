import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __repr__(self):
        #repr, а не str!
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

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Adam = Runner('Adam')
        for i in range(10):
            Adam.walk()
        self.assertEqual(Adam.distance, 50)

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        Eve = Runner('Eve')
        for i in range(10):
            Eve.run()
        self.assertEqual(Eve.distance, 100)

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_challange(self):
        Cain = Runner('Cain')
        Abel = Runner('Abel')
        for i in range(10):
            Cain.walk()
            Abel.run()
        self.assertNotEqual(Cain.distance, Abel.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.__all_results = {}

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.u = Runner('Усейн', 10)
        self.a = Runner("Андрей", 9)
        self.n = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.__all_results:
            print(cls.__all_results.get(i))

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        t = Tournament(90, self.u, self.n)
        r = t.start()
        self.__all_results.update({'1.': r})
        r2 = self.__all_results.get('1.')
        self.assertTrue(r2.get(2), "Ник")

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        t = Tournament(90, self.a, self.n)
        r = t.start()
        self.__all_results.update({'2.': r})
        r2 = self.__all_results.get('2.')
        self.assertTrue(r2.get(2), "Ник")

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        t = Tournament(90, self.u, self.a, self.n)
        r = t.start()
        self.__all_results.update({'3.': r})
        r2 = self.__all_results.get('3.')
        self.assertTrue(r2.get(3), "Ник")

