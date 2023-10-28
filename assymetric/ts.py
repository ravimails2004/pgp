#!/usr/local/bin/python3
import json
import gnupg
gpg = gnupg.GPG()

import gnupg._parsers
gnupg._parsers.Verify.TRUST_LEVELS["ENCRYPTION_COMPLIANCE_MODE"] = 23

import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, './public.pgp')
file_path_priv = os.path.join(script_dir, './private.pgp')
print(file_path)
print(file_path_priv)
filehandle = open(file_path)
filehandle2 = open(file_path_priv)
#print(filehandle.read())

#file_path_encdata = os.path.join(script_dir, './enc-file.gpg')
#filehandle3 = open(file_path_encdata)

def gpg_encrypt_data(data, key):
    data_string = json.dumps(data)
    print(data_string)
    gpg = gnupg.GPG()
    imported_keys = gpg.import_keys(key)
    encrypted = gpg.encrypt(
        data_string,
        imported_keys.fingerprints[0],
        armor=True,
        always_trust=True)
    print("printing output of encryption phase")
    print(encrypted.data)
    print("=====================================")
    gpg = gnupg.GPG()
    gpg.import_keys(filehandle2.read())
    gpg_data = gpg.decrypt(encrypted.data)
    data = json.loads(gpg_data.data)
    print("printing output of decryption phase")
    print(data)
    print("=====================================")

data={
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}

key=filehandle.read()

gpg_encrypt_data(data, key)
