# QUESTION 5
# MDC OF TWO NUMBERS
from discrete_math.arithmetic import euclidian_mdc

print("###  ENCONTRANDO O MDC DE DOIS VALORES A & B ###")
print(" ")

a = int(input("Digite um numero para A: "))
b = int(input("Digite um numero para B: "))
mdc = euclidian_mdc(a, b)

print(" ")
print(f"O mdc de {a} e {b} é {mdc}")