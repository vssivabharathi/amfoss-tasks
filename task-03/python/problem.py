def is_prime(n):
    if n < 2: return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

N = int (input ("Enter a  number:"))
for n in range (2, N):
    if is_prime(n):
        print(n)
















