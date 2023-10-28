#!/opt/homebrew/bin/python3.11
# opening the key
from cryptography.fernet import Fernet
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to encrypt
with open('nba.csv', 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
 
# opening the file in write mode and 
# writing the encrypted data
with open('nba-enc.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
