import random
from math import pow

a = random.randint(2, 10)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_key(q):
	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key

def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c
		y = (y * y) % c
		b = int(b / 2)

	return x % c

def encrypt(plaintext, q, h, g):

	ciphertext = []

	k = generate_key(q)# Private key for sender
	s = power(h, k, q)
	p = power(g, k, q)
	
	for i in range(0, len(plaintext)):
		ciphertext.append(plaintext[i])

	for i in range(0, len(ciphertext)):
		ciphertext[i] = s * ord(ciphertext[i])

	return ciphertext, p

def decrypt(ciphertext, p, key, q):

	plaintext = []
	h = power(p, key, q)
	for i in range(0, len(ciphertext)):
		plaintext.append(chr(int(ciphertext[i]/h)))

	plaintext = ''.join(plaintext)
		
	return plaintext


# msg = 'encryption'
# print("Original Message :", msg)

# q = random.randint(pow(10, 20), pow(10, 50))
# g = random.randint(2, q)

# key = generate_key(q)
# h = power(g, key, q)
# print("g used : ", g)
# print("g^a used : ", h)

# en_msg, p = encrypt(msg, q, h, g)
# dr_msg = decrypt(en_msg, p, key, q)
# dmsg = ''.join(dr_msg)
# print("Decrypted Message :", dmsg)