class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

Peg = Pegasus()

print(Peg.get_pos())
Peg.move(10, 15)
print(Peg.get_pos())
Peg.move(-5, 20)
print(Peg.get_pos())

Peg.voice()
