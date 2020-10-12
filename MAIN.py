from ENCRYPTION import ENCRYPTION

for i in range(2):

    Encrypter = ENCRYPTION()

    print(Encrypter)

    raw_msg = input("Enter a message to encrypt: ")

    encrypted_msg = Encrypter.encrypt(raw_msg)

    print("Encrypted message: " + encrypted_msg)

    decrypted_msg = Encrypter.decrypt(encrypted_msg)

    print("Decrypted message: " + decrypted_msg)