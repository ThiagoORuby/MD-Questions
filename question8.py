# QUESTION 8
# FIND THE SOLUTION FOR LINEAR CONGRUENCE ax = b (mod m)

from discrete_math.applications import linear_solution

print("##### ENCONTRANDO A SOLUÇÃO PARA CONGRUÊNCIA LINEAR #####\n")

print("A seguir, defina os valores de a, b e m para ax = b (mod m)")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
m = int(input("Digite o valor de m: "))

res = linear_solution(a, b, m)

if res:
    print(f"\nAs possíveis soluções entre 0 e {m} são: {res}")
else:
    print("\nNão há solução para essa congruência linear")