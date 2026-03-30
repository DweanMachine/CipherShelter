from core import *

def checkPasswordStrength(password):
  has_number = any(char.isdigit() for char in password)
  if len(password) >= 8 and has_number:
    return True
  print("Password must be at least 8 characters long and contain at least one number.")
  return False

def main():
  print("Welcome to CipherShelter!")
  print("This tool allows you to encrypt and decrypt files using a password.")
  print("Please choose an option:")
  print("[1] Encrypt a file")
  print("[2] Decrypt a file")
  print("[3] Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    input_path = input("Enter the path of the file to encrypt: ")
    output_path = input("Enter the path for the encrypted file: ")
    while True:
      password = input("Enter the password for decryption: ")
      if checkPasswordStrength(password): #check password strength before proceeding
        break
    try:
      encrypt_file(input_path, output_path, password)
      print(f"File encrypted successfully: {output_path}")
    except Exception as e:
      print(f"Error encrypting file: {e}")

  elif choice == "2":
    input_path = input("Enter the path of the file to decrypt: ")
    output_path = input("Enter the path for the decrypted file: ")
    password = input("Enter the password for decryption: ")
    try:
      decrypt_file(input_path, output_path, password)
      print(f"File decrypted successfully: {output_path}")
    except Exception as e:
      print(f"Error decrypting file: {e}")

  elif choice == "3":
    print("Exiting CipherShelter. Goodbye!")
  else:
    print("\n-- INVALID CHOICE! PLEASE ENTER 1, 2, OR 3! --\n")
    main()

main()

