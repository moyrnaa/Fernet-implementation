from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Key:", key)

f = Fernet(key)

message = input("WWhats your message : ")
b_message = message.encode()  # Message to be encrypted (must be bytes)

# Encrypt the message
encrypted_message = f.encrypt(b_message)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = f.decrypt(encrypted_message)
print("Decrypted:", decrypted_message)
