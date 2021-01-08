def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return print(False)

    return print(True)

is_prime(5)
is_prime(10)
is_prime(11)