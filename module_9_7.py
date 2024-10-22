result = 0
def is_prime(func):
    def wrapper(a, b, c):
        summ = func(a, b, c)
        result = 0
        for i in range(summ):
            if summ % (i+1) == 0:
                result += 1
        if result == 2:
            print('Простое')
        else:
            print("Составное")
        return summ
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)