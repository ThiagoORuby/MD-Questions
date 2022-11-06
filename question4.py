# QUESTION 4
# MDC MMC


from discrete_math.arithmetic import decomp_mdc

from discrete_math.arithmetic import decomp_mmc


print("##### MMC E MDC #####\n")

number1, number2 = int(input().split(" "))
res_mdc = decomp_mdc(number1,number2)
res_mmc = decomp_mmc(number1,number2)

print("MDC :{res_mdc}, MMC : {res_mmc}")
