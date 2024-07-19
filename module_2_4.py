numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i < 2:
        continue
    else:
        f = i
    for a in range(2, f):
        if i % a == 0:
            is_prime = False
            break
    if not is_prime:
        not_primes.append(i)
    else:
        primes.append(i)

print(primes)
print(not_primes)
