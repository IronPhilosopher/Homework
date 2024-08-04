def print_params(a = False, b = 42, c = 'аргумент'):
    print(a, b, c)
print_params()
print_params('alpha', True, 77)
print_params(b='gamma')
print_params(c=33.3)
print_params(c='or', a=22)

values_list = ['Питон', 17, True]
values_dict = {'a':9.7, 'b':'code', 'c':'dict'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [66, "delta"]
print_params(*values_list_2, 'omega')