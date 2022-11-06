# QUESTION 3
# DECOMPOSE A NUMBER IN YOURS PRIME FACTORS

from discrete_math.decomposite import decompose

print("##### DECOMPOSIÇÃO EM PRIMOS #####\n")

number = int(input("Digite o número: "))

res_dict = decompose(number)

res_string = ""
for key, value in res_dict.items(): res_string += f"{key}^{value} * "

print(f'\nO número {number} pode ser decomposto da seguinte forma:')
print(res_string[:-2])


