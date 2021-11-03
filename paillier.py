import random
from math import gcd, lcm

def generatePrime(n):
   odds = range(3, n+1, 2)
   sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds], []))
   return [2] + [p for p in odds if p not in sieve]

primeList = generatePrime(10000)

def generateKey():
  p = random.choice(primeList)
  q = random.choice(primeList)

  while (gcd(p*q, (p-1)*(q-1))!=1 or p==q):
    print ('loop')
    p = random.choice(primeList)
    q = random.choice(primeList)

  n = p*q
  return PublicKey(n), PrivateKey(p, q, n)

def L(x, n):
  return (x-1)/n

class PublicKey:
  def __init__(self, n):
    self.g = n+1 
    self.n = n

class PrivateKey:
  def __init__(self, p, q, n):
    self.l = lcm(p-1, q-1)
    self.mu = self.modinv(self.l, n)
  
  def modinv(a, p, iter=1000000):
    if (a==0):
      print(f'0 no inverse mod {p}')
      return 0
    
    r, d = a, 1
    for i in range(min(p, iter)):
      d = ((p//r+1)*d) % p
      r = (d*a) % p
      if (r==1):
        break
    else:
      print(f'{a} no inverse mod {p}')
    
    return d

def encrypt(plaintext, g, n):
  r = random.randint(0, n)
  while (gcd(r, n)!=1):
    r = random.randint(0, n-1)
  
  ciphertext = []
  for p in plaintext:
    pi = ord(p)
    ci = (pow(g, pi) * pow(r, n)) % (pow(n, 2))
    ciphertext.append(ci)
  
  return ciphertext

def decrypt(ciphertext, l, n, mu):
  plaintext = []
  for c in ciphertext:
    p = (L((pow(c, l)) % (pow(n, 2)), n) * mu) % n
    plaintext.append(p)
  
  return "".join([chr(int(x)) for x in plaintext])

if (__name__=='__main__'):
  pub, priv = generateKey()
  plaintext = 'aku suka membaca'
  encryptedText = encrypt(plaintext, pub.g, pub.n)
  print(encryptedText)

  decryptedText = decrypt(encryptedText, priv.l, pub.n, priv.mu)
  print(decryptedText)