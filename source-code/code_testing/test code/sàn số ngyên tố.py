# liệt kê các số nguyên tố trong [1, n]


def sievep1(n):
    prime = [True] * (n + 1)
    prime_init = 2
    
    while prime_init * prime_init <= n:
        if prime[prime_init] == True:
            
            for i in range(prime_init * prime_init, n + 1, prime_init):
                prime[i] = False
                
        prime_init += 1
        
    primes = []
    
    for prime_init in range(2, n + 1):
        if prime[prime_init] == True:
            primes.append(prime_init)
    return primes
    
# liệt kê các số nguyên tố trong [L, R]
def sieve2(n):
    prime = [True] * (n + 1)
    p = 2
    
    while p * p <= n:
        if prime[p] == True:
            
            for i in range(p * p, n + 1, p):
                prime[i] = False
                
        p += 1

    return prime

n = int(input("nhập"))
print(sievep1(n))
print(sieve2(n))