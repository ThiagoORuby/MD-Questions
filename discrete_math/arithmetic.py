from discrete_math.decomposite import decompose

# Euclidian MDC
def euclidian_mdc(a, b):
    if(not b): return a
    return euclidian_mdc(b, a % b)

# MDC with Decomposition
def decomp_mdc(a, b):
    da = decompose(a)
    db = decompose(b)

    for i in da.keys():
        if i not in db.keys():
            db[i] = 0
    for i in db.keys():
        if i not in da.keys():
            da[i] = 0

    dmdc = dict()
    for i in da.keys():
        dmdc[i] = min(da[i], db[i])
    mdc = 1
    for i in dmdc.keys():
        mdc *= i**dmdc[i]
    return mdc

# MMC
def decomp_mmc(a, b):
    da = decompose(a)
    db = decompose(b)

    for i in da.keys():
        if i not in db.keys():
            db[i] = 0
    for i in db.keys():
        if i not in da.keys():
            da[i] = 0

    dmmc = dict()
    for i in da.keys():
        dmmc[i] = max(da[i], db[i])
    mmc = 1
    for i in dmmc.keys():
        mmc *= i**dmmc[i]
    return mmc

# Extended Euclides
def extended_euclides(a, b):
    #if (r == 0): return
    (r0, m0, n0) = a, 1, 0
    (r1, m1, n1) = b, 0, 1

    while(r0 % r1 > 0):
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        m0, m1 = m1, m0 - m1*q
        n0, n1 = n1, n0 - n1*q
    
    return m1, n1

# Modular inverse
def modinv(a, b):
    m1, _ = extended_euclides(a, b)
    return m1