from fermat import brute_force

def next_prime(n):
    if(brute_force(n)): return n
    return next_prime(n+1)

def get_array(n, p, decompos):
    if(brute_force(n)):
        if n not in decompos.keys():
            decompos[n] = 1
        else:
            decompos[n] += 1
        return
    if(n % p == 0): 
        if p not in decompos.keys():
            decompos[p] = 1
        else:
            decompos[p] += 1
        return get_array(n // p, p, decompos)
    p = next_prime(p+1)
    return get_array(n, p, decompos)

def decompose(n):
    decomp =  dict()
    get_array(n, 2, decomp)
    return decomp

d = decompose(456598)
print(d)