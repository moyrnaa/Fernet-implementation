from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print("Key:", key)

f = Fernet(key)

message = b"Secret message for encryption" # Message to be encrypted (must be bytes)

# Encrypt the message
encrypted_message = f.encrypt(message)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = f.decrypt(encrypted_message)
print("Decrypted:", decrypted_message)
