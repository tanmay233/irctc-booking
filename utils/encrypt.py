from cryptography.fernet import Fernet


# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a message using the provided key
def encrypt_message(message):
    key: str = "aBcD1eFgH2iJkL3mNoP4qRsT5uVwX6yZ7aBcD8eFgH9iJkL0mNoP1qRsT2uVwX3yZ4" # This is a sample key, please replace it with your own key
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt an encrypted message using the provided key
def decrypt_message(encrypted_message):
    key: str = "aBcD1eFgH2iJkL3mNoP4qRsT5uVwX6yZ7aBcD8eFgH9iJkL0mNoP1qRsT2uVwX3yZ4" # This is a sample key, please replace it with your own key
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


