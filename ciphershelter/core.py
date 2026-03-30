#Encrpytion/Decryption Logic
import base64
import os
from pathlib import Path
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_SIZE = 16
KEY_LENGTH = 32

def derive_key(password: str, salt: bytes) -> bytes:
  kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=KEY_LENGTH, salt=salt, iterations=1_200_000)
  return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(input_path, output_path, password): 
  salt = os.urandom(SALT_SIZE)
  
  input_path = Path(input_path)
  output_path = Path(output_path)

  #Validate input/output paths
  if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

  if input_path.is_dir():
    raise IsADirectoryError("encrypt_file expects a file, not a directory.")

  if output_path.exists():
    raise FileExistsError(f"Output already exists: {output_path}. Will not overwrite.")

  #derive key from PBKDF2
  key = derive_key(password, salt)
  f = Fernet(key)
  plaintext = input_path.read_bytes()
  ciphertext = f.encrypt(plaintext)

  output_path.write_bytes(salt + ciphertext)


def decrypt_file(input_path, output_path, password): 
  input_path = Path(input_path)
  output_path = Path(output_path)

  #Validate input/output paths
  if not input_path.exists():
    raise FileNotFoundError(f"Encrypted file not found: {input_path}")

  if input_path.is_dir():
    raise IsADirectoryError("encrypt_file expects a file, not a directory.")
  
  if output_path.exists():
    raise FileExistsError(f"Output already exists: {output_path}. Will not overwrite.")

  raw = input_path.read_bytes()
  salt, ciphertext = raw[:SALT_SIZE], raw[SALT_SIZE:]
  key = derive_key(password, salt)
  
  f  = Fernet(key)
  plaintext = f.decrypt(ciphertext)

  #verify, decrypt, and write output
  output_path.write_bytes(b"-- Decrypted Password -- \n"+ plaintext)


encrypt_file(r"tests\input.txt", r"tests\hash.txt","Squad")
decrypt_file(r"tests\hash.txt",r"tests\output.txt","Squad")