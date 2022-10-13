# inverso modular de a em relação a b
def modinv(a, b):
    #if (r == 0): return
    (r0, m0, n0) = a, 1, 0
    (r1, m1, n1) = b, 0, 1

    while(r0 % r1 > 0):
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        m0, m1 = m1, m0 - m1*q
        n0, n1 = n1, n0 - n1*q
    
    return m1

def mdc(a, b):
    if(not b): return a
    return mdc(b, a % b)