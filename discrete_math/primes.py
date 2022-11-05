# Primality Test

def brute_force(n):
    if(n <= 1): return 0
    if(n == 2): return 1
    for i in range(2, n, 1):
        if (n % i == 0): return 0
        if(i * i > n): break
    return 1

#20517
#for i in range(100):
#    if(brute_force(i)): print(i, end=' ')
# brute : 24696"""