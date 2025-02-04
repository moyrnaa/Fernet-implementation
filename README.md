# Fernet Encryption  
This is Python Implementation of Fernet Encryption (Symmetric Encryption), a way to **securely lock and unlock messages** using the same secret key. It's great for protecting sensitive data like passwords, messages, or files.  

⚠️ Note: Keep your key for yourself ! If someone gets access to it, they can decrypt your messages.  

## What’s Fernet Encryption?  
Fernet is a way to turn **plain text into unreadable text** (encryption) and back to normal (decryption) using a secret key. If you have the key, you can unlock the message. If not, it stays **completely unreadable**.  

## How It Works  
1. You **generate a secret key** (like a password).  
2. You **encrypt a message**, turning it into something unreadable.  
3. Later, you can **decrypt it** using the same key to get the original message back.  

### Example  
Plaintext: `"Hello, world!"`  
Key: `"KJHs73hdi..."`  
Encrypted: `"gAAAAA...sdfD"`  
Decrypted: `"Hello, world!"`  

## How to Use Fernet Encryption  
### Install the Required Library  
You need to install the **cryptography** package first:  

pip install cryptography

**for more info ** : https://cryptography.io/en/latest/fernet/

