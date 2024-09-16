class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __repr__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(f'{self.__file_name}', 'r')
        info = file.read()
        file.close()
        return info

    def add(self, *products):
        s_list = self.get_products()
        file = open(f'{self.__file_name}', 'a')
        for i in products:
            if str(i) in s_list:
                print(f'Продукт {i} уже есть в магазине')
            else:
                file.write(f'\n{i}')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetable')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())