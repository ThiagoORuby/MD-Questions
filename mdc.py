from decomposite import decompose

def mdc(a, b):
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
    print(mdc)

def mmc(a, b):
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
    print(mmc)


mmc(84, 450)
mdc(84, 450)


    