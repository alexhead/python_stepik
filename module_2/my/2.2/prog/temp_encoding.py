from simplecrypt import encrypt, decrypt

password = 'secret'
message = 'wow wow wow'
ciphertext = encrypt(password, message)



print(decrypt('secret', ciphertext))

