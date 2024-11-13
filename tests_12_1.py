import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Adam = Runner('Adam')
        for i in range(10):
            Adam.walk()
        self.assertEqual(Adam.distance, 50)

    def test_run(self):
        Eve = Runner('Eve')
        for i in range(10):
            Eve.run()
        self.assertEqual(Eve.distance, 100)

    def test_challange(self):
        Cain = Runner('Cain')
        Abel = Runner('Abel')
        for i in range(10):
            Cain.walk()
            Abel.run()
        self.assertNotEqual(Cain.distance, Abel.distance)

# Поменял значение. Результат: Ran 3 tests in 0.044s
# FAILED (failures=1)
# 1100 != 100