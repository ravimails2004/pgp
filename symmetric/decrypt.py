#!/opt/homebrew/bin/python3.11
from cryptography.fernet import Fernet
# using the key

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)
 
# opening the encrypted file
with open('nba-enc.csv', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('nba-dec.csv', 'wb') as dec_file:
    dec_file.write(decrypted)
