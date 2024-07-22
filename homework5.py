immutable_var=(1,"sting",True)
print(immutable_var)
#immutable_var[0]=1 Вызывает ошибку. Данные в кортеже нельзя менять, если они не в изменяемом списке.
mutable_list=(2,[3],"numeral",[False])
mutable_list[1][0] = True
mutable_list[3][0] = "float"
print(mutable_list)