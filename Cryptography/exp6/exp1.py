from pycipher import Vigenere

plaintext = input("Enter plaintext: ")
key = input("Enter key: ").upper()

ciphertext = Vigenere(key).encipher(plaintext)
decrypted = Vigenere(key).decipher(ciphertext)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)