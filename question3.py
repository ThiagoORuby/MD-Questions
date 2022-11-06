# QUESTION 3
# DECOMPOSE A NUMBER IN YOURS PRIME FACTORS

from discrete_math.decomposite import decompose

print("##### DECOMPOSIÇÃO EM PRIMOS #####\n")

number = int(input("Digite o número: "))

res = decompose(number)

print("{res}")


