from discrete_math.arithmetic import euclidian_mdc, modinv

# Solution for ax = b (mod m) -> x
def linear_solution(a, b, m):
    d = euclidian_mdc(a, m)
    if(d == 1):
        ainv = modinv(a, m)
        return (ainv*b) % m
    elif(b % d == 0):
        a, b, m = a//d, b//d, m//d
        first = (modinv(a, m)*b) % m
        return [first + m*i for i in range(0, d)]
    else:
        return False

# Solution for systems x = r (mod m) -> x 
def system_solution(arr):
    # Get M
    M = 1
    for i in arr: M *= i[1]
    M_list = [M//i[1] for i in arr]
    m_list = [i[1] for i in arr]
    r_list = [i[0] for i in arr]
    s_list = [modinv(M_list[i], m_list[i]) for i in range(len(M_list))]
    solution = sum([m*r*s for m, r, s in zip(M_list, r_list, s_list)]) % M
    return solution