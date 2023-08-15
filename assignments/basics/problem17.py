# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

def get_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


print(get_primes(50))
