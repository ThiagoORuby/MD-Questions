# QUESTION 4
# MDC MMC


from discrete_math.arithmetic import decomp_mdc, decomp_mmc



print("##### MMC E MDC #####\n")

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
res_mdc = decomp_mdc(number1,number2)
res_mmc = decomp_mmc(number1,number2)

print(f"MDC :{res_mdc}, MMC : {res_mmc}")
