def phi(n):
    result = n
    i = 2
    while i*i <=n:
        if n %i == 0:
            result //= i
            result *= i-1            

            while n %i == 0:
                n //= i
        i += 1
    if n > 1:
        result //= n
        result *= n-1
    return result 

def phi_until(n):
    sieve = [i for i in range(n+1)]
    for i in range(2,n+1):
        if sieve[i] == i:
            for j in range(i, n+1, i):
                sieve[j] //= i
                sieve[j] *= i-1

    return sieve

def test_phi(n=10):
    for i in range(2,n+1):
        print(i, "=", phi(i))

def test_sieve_phi(n=10):
    sieve = phi_until(n)
    for i in range(2,n+1):
        print(i, "=", sieve[i])

print("test_phi")
test_phi()
print("==============")
print("test_sieve_phi")
test_sieve_phi()