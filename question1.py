# QUESTION 1
# CHECK IF A NUMBER IS PRIME
from discrete_math.primes import brute_force

print("##### TESTE DE PRIMALIDADE #####\n")

number = int(input("Digite o número: "))
print('')
if (brute_force(number)):
    print(f"O número {number} é primo")
else:
    print(f"O número {number} não é primo")