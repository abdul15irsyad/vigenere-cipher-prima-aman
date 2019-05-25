def is_prima(angka):
    faktor = 0
    i = 1
    while i <= angka and faktor <= 2:
        if angka % i == 0:
            faktor += 1
        i += 1
    if faktor == 2:
        return True
    return False

def is_prima_aman(angka):
    return is_prima((angka-1)/2)

# array bilangan ascii baru
i = 48
ascii_list = [" "]
while i < (65+58):
    if (i > 57 and i < 65) or (i > 90 and i < 97):
        i += 1
        continue
    ascii_list.append(chr(i))
    i += 1
        
def ascii(huruf):
    return ascii_list.index(huruf)

def chr_ascii(angka):
    return ascii_list[angka]

# array bilangan prima aman
i = 0
prima_aman = []
while len(prima_aman) < 63:
    if is_prima_aman(i):
        prima_aman.append(i)
    i += 1

def key_prima_aman(angka):
    return prima_aman[angka]

def encrypt(plaintext, key):
    key_length = len(key)
    key_ascii_as_int = [ascii(i) for i in key]
    key_as_int = [key_prima_aman(i) for i in key_ascii_as_int] 
    plaintext_int = [ascii(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 63
        ciphertext += chr_ascii(value)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_ascii_as_int = [ascii(i) for i in key]
    key_as_int = [key_prima_aman(i) for i in key_ascii_as_int]
    ciphertext_int = [ascii(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 63
        plaintext += chr_ascii(value)
    return plaintext

# main
print("plaintext : ")
plaintext = input()
print("key : ")
key = input()
print("ciphertext : "+encrypt(plaintext,key))
print("plaintext : "+decrypt(encrypt(plaintext,key),key))