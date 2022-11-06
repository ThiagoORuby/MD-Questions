# QUESTION 10
# FIND THE SOLUTION FOR N LINEAR CONGRUENCES

from discrete_math.applications import system_solution, euclidian_mdc
from itertools import combinations

print("##### SOLUÇÃO PARA SISTEMA DE N CONGRUÊNCIAS LINEARES #####\n")

qnt = int(input("Digite a quantidade de congruências: "))
if qnt <= 1:
    print("Um sistema precisa ter mais de uma congruência")
else:
    print("A seguir, digite os valores de b e m para as congruências -> x = b (mod m)\n")
    congruences = []
    n_values = []


    for i in range(qnt):
        print(f"Congruência {i+1}:")
        b = int(input("Valor de b: "))
        n = int(input("Valor de n: "))
        congruences.append([b,n])
        n_values.append(n)
        print("")

    # check if is coprime
    isCoprime = True
    comb = combinations(n_values, 2)
    for c in comb:
        if(euclidian_mdc(c[0], c[1]) != 1):
            isCoprime = False
            break


    if isCoprime:
        res = system_solution(congruences)
        print(f"A solução para o sistema dado é: {res}")
    else:
        print(f"O sistema não tem solução pois seus módulos não são coprimos")