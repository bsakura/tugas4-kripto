import random
import rsa
import elgamal
import paillier

def generatePrime(n):
   odds = range(3, n+1, 2)
   sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds], []))
   return [2] + [p for p in odds if p not in sieve]

primeList = generatePrime(1000)

print('Tugas 4 Kripto')
print('Kalkulator Enkripsi Dekripsi RSA, ElGamal, Paillier, ECC')
print()

def menuAlgo():
  print('Algoritma:')
  print('1. RSA')
  print('2. ElGamal')
  print('3. Paillier')
  print('4. ECC')

def menuOp():
  print('Operasi:')
  print('1. Enkripsi')
  print('2. Dekripsi')
  print('3. Keluar')

flag = True
while (flag):
  menuAlgo()
  algo = input('Pilih algoritma yang akan digunakan: ')
  print()

  menuOp()
  op = input('Pilih operasi yang akan dilakukan: ')
  print()

  if (op == '1'): # enkripsi
    text = input('Pesan yang ingin dienkripsi: ')
    print('Kunci privat dan kunci publik sedang dibangkitkan...')
    print('Kunci privat dan kunci publik berhasil dibangkitkan!')

    if (algo == '1'): #rsa
      p = random.choice(primeList)
      q = random.choice(primeList)
      pub, priv = rsa.generate_key_pair(p, q)
      print(f'Public Key: {pub}')
      print(f'Private Key: {priv}')
      encryptedText = rsa.encrypt(pub, text)
      print(f'Pesan hasil enkripsi: {encryptedText}')

    elif (algo == '2'): # elgamal
      q = random.randint(pow(10, 20), pow(10, 50))
      g = random.randint(2, q)
      key = elgamal.generate_key(q)
      h = elgamal.power(g, key, q)
      encryptedText, p = elgamal.encrypt(text, q, h, g)
      print(f'Nilai p: {p}')
      print(f'Nilai q: {q}')
      print(f'Nilai key: {key}')
      print(f'Pesan hasil enkripsi: {encryptedText}')

    elif (algo == '3'): # paillier
      pub, priv = paillier.generateKey()
      print(f'Public g: {pub.g}')
      print(f'Public n: {pub.n}')
      print(f'Private l: {priv.l}')
      print(f'Private mu: {priv.mu}')
      encryptedText = paillier.encrypt(text, pub.g, pub.n)
      print(f'Pesan hasil enkripsi: {encryptedText}')

    elif (algo == '4'): # ecc
      print('Kami menyerah :(')

    else:
      print('Opsi tidak sesuai')

    print()
  elif (op == '2'): # dekripsi
    text = input('Pesan yang ingin didekripsi: ')

    if (algo == '1'): #rsa
      priv = input('Masukkan private key: ')
      priv = tuple(int(x) for x in priv.split(','))
      text = text.split(',')
      text = list(map(int, text))
      decryptedText = rsa.decrypt(priv, text)
      print(f'Pesan hasil dekripsi: {decryptedText}')

    elif (algo == '2'): # elgamal
      p = int(input('Masukkan nilai p: '))
      q = int(input('Masukkan nilai q: '))
      key = int(input('Masukkan nilai key: '))
      text = text.split(',')
      text = list(map(int, text))
      decryptedText = elgamal.decrypt(text, p, key, q)
      print(f'Pesan hasil dekripsi: {decryptedText}')

    elif (algo == '3'): # paillier
      pubN = int(input('Masukkan nilai Public n: '))
      privL = int(input('Masukkan nilai Private l: '))
      privMu = int(input('Masukkan nilai Private mu: '))
      text = text.split(',')
      text = list(map(int, text))
      decryptedText = paillier.decrypt(text, privL, pubN, privMu)
      print(f'Pesan hasil dekripsi: {decryptedText}')

    elif (algo == '4'): # ecc
      print('Kami menyerah :(')

    else:
      print('Opsi tidak sesuai')

    print()
  elif (op == '3'): # exit
    print('Program selesai')
    flag = False
  
  else:
    print('Opsi tidak sesuai')