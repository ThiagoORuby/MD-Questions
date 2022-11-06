# QUESION 6
# FIND THE COEFFICIENTS S AND T
from discrete_math.arithmetic import extended_euclides

print(">>  COEFICIENTES S & T DA COMBINACAO LINEAR  <<")
print(">>  COMBINACAO LINEAR => mdc(a, b) = s * a + t * b <<")
print(" ")

a = int(input("Digite um numero para A: "))
b = int(input("Digite um numero para B: "))
m, n = extended_euclides(a, b)

print(" ")
print(f"Os coeficientes s e t são iguais a {m} e {n}, RESPECTIVAMENTE!")
