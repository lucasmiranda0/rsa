from dictionaries import primeNumbers
from random import randint
from math import gcd

def encrypting(e, n, text):
    textEncrypting = []
    for i in range(len(text)):
        value = ord(text[i])
        mod = (value ** e) % n
        textEncrypting.append(mod)
    return textEncrypting        

def mdc(n):
    x = 0
    b = 1
    while x != 1:
        b = b + 1
        x = gcd(n, b)        
    return b 

def totient(p0, p1):
    t = (p0 - 1) * (p1 - 1)
    return t

def caculateN(p0, p1):
    n = p0 * p1
    return n

def generatePrimes():
    primesList = primeNumbers()
    x = randint(0, len(primesList) - 1)
    y = randint(0, len(primesList) - 1)
    while x == y:
        y = randint(0, len(primesList) - 1)
    primesGenerated = [primesList[x], primesList[y]]        
    return primesGenerated

if __name__ == '__main__':
    primes = generatePrimes()
    p0 = primes[0]
    p1 = primes[1]
    print(primes)
    n = caculateN(p0, p1)
    print(n)
    t = (totient(p0, p1))
    print(t)
    b = (mdc(t))
    print(b)
    x = encrypting(b, t, 'meu passaro')
    print(x)