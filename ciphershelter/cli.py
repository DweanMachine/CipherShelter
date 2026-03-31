#Execution: python -m ciphershelter.cli
from ciphershelter.core import encrypt_file, decrypt_file, CipherShelterError
import getpass
import string

def check_password_strength(password: str) -> bool:
  rules = [ #List of password requirements
    (len(password) >= 8, "at least 8 characters"),
    (any(char.isdigit() for char in password), "at least one number"),
    (any(char.isupper() for char in password), "at least one capital letter"),
    (any(char in string.punctuation for char in password), "at least one special character")
  ]

  failed = [msg for passed, msg in rules if not passed]
  if failed:
    print("Password must contain: " + ", ".join(failed) + ".")
    return False
  return True

def main():
  print("Welcome to CipherShelter!")
  print("This tool allows you to encrypt and decrypt files using a password.")
  print("Please choose an option:")
  print("[1] Encrypt a file")
  print("[2] Decrypt a file")
  print("[3] Exit")

  while True:
    choice = input("Enter your choice: ")
    if choice in ("1", "2", "3"):
        break
    print("\n-- INVALID CHOICE! PLEASE ENTER 1, 2, OR 3 --")

  if choice == "1":
    input_path = input("Enter the path of the file to encrypt: ")
    output_path = input("Enter the path for the encrypted file: ")
    while True:
      password = getpass.getpass(prompt="Enter the password to encrypt with: ")
      if check_password_strength(password): #check password strength before proceeding
        break
    try:
      encrypt_file(input_path, output_path, password)
      print(f"File encrypted successfully: {output_path}")
    except CipherShelterError as e:
      print(f"Error encrypting file: {e}")

  elif choice == "2":
    input_path = input("Enter the path of the file to decrypt: ")
    output_path = input("Enter the path for the decrypted file: ")
    password = getpass.getpass(prompt="Enter the password for decryption: ")
    try:
      decrypt_file(input_path, output_path, password)
      print(f"File decrypted successfully: {output_path}")
    except CipherShelterError as e:
      print(f"Error decrypting file: {e}")

  elif choice == "3":
    print("Exiting CipherShelter. Goodbye!")
    
if __name__ == "__main__":
  main()