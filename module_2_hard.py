n = int (input('Введите число от 3 до 20 '))
def solve():
    result = []
    for i in range (1, n):
        for j in range (1, n):
            if i != j and j > i and n % (i + j) == 0:
                result += (str(i), str(j))
    result = (int (''.join (result) ) )
    print (result)
solve()
