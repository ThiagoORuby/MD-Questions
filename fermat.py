from random import randint
from math import gcd, sqrt, log10
import time
import os

def mdc(a, b):
    if(not b): return a
    return mdc(b, a % b)

def fermat_test(n):
    d = [3, 5, 7, 11]
    for a in d:
        if(mdc(n, a) != 1): return 0
        if(pow(a, n-1, n) != 1): return 0
    return 1

def brute_force(n):
    #if(n == 0 or n == 1): return 0
    for i in range(3, int(sqrt(n))+1, 2):
        if (not(n % i)): return 0
    return 1



init_time = time.time()
n_primes = 1
for i in range(3, 100000000):
    if(brute_force(i)): 
        n_primes+=1
        #print(i, end=' ')
    #os.system('cls')
    print(time.time() - init_time)
    if(time.time() - init_time >= 60): break
    #if(not (i % 10)): print()

print()
print("Numero de primos achados em 60 segundos: ", n_primes) 

#20517

# brute : 24696"""