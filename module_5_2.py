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
    def __len__(self):
        return (self.number_of_floors)
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

H1 = House("ЖК Олимп", 40)
H2 = House("Частный дом", 3)
# __str__
print(H1)
print(H2)

# __len__
print(len(H1))
print(len(H2))