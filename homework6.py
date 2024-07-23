my_dict={"Анна":1992,"Давид":1875,"Саша":2002}
print(my_dict.get("Анна"))
print(my_dict.get("Антон"))
my_dict.update({"Джим":2011,"Валерия":1986})
print(my_dict.pop("Саша"))
print(my_dict)

my_set={9,0,'A','B',True,0,True,'A'}
print(my_set)
my_set.update((7, 'Z'))
my_set.discard('B')
print(my_set)