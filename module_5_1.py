class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > 0 and new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i+1)
        else:
            print("Такого этажа не существует")

H1 = House("ЖК Олимп", 40)
H2 = House("Частный дом", 3)
H1.go_to(33)
H2.go_to(0)
H2.go_to(4)
