numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in numbers:
        if i % j == 0:
            if j != i and j != 1:
                is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
    is_prime = True
print (primes)
print (not_primes)