class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound = "I train, eat, sleep, and repeat"
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        self.x_distance = 0
        self.y_distance = 0

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(super().sound)

Peg = Pegasus()

print(Peg.get_pos())
Peg.move(10, 15)
print(Peg.get_pos())
Peg.move(-5, 20)
print(Peg.get_pos())

Peg.voice()
# Пегас издает 'Frrr', т.к. по наследованию сначала Horse. В условии/решении задачи ошибка.
