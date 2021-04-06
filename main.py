from crypto import Cryptography

crypto = Cryptography()

# value = input('Digite a palavra: ')
# key = int(input('Digite a chave: '))
value = 'carlos eduardo de borba machado'
key = 10

enc_value = crypto.encrypt(value, key)
dec_value = crypto.decrypt(enc_value, key)

print('Palavra original:', value)
print('Palavra encryptada:', enc_value)
print('Palavra decryptada:', dec_value)
