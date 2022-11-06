# QUESTION 7
# INVERSE Of A MOD B
from discrete_math.arithmetic import modinv
print(">>>>  ENCONTREANDO A INVERSA DE A MOD B")
print(" ")

a = int(input("Digite um numero para A: "))
b = int(input("Digite um numero para B: "))
a_ = modinv(a, b)

print(" ")
print(f"O inverso de {a} mod {b} eh igual a {a_}")