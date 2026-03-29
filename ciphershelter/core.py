#Encrpytion/Decryption Logic
from cryptography.fernet import Fernet, MultiFernet
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

f = MultiFernet([key1, key2])

token = f.encrypt(b"Secret message!")
plaintext = f.decrypt(token)

print(plaintext, token)
