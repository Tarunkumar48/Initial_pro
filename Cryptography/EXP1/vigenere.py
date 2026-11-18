# # Vigenere cipher

# def vigenere_encrypt(plaintext, key):
#     ciphertext = ""
#     key_length = len(key)
#     key_index = 0

#     for char in plaintext:
#         if char.isalpha():
#             # Determine if the character is uppercase or lowercase
#             is_upper = char.isupper()
#             char_lower = char.lower()
#             # Get the corresponding key character
#             key_char = key[key_index % key_length].lower()
#             # Calculate the shift
#             shift = ord(key_char) - ord('a')
#             # Encrypt the character
#             encrypted_char = chr((ord(char_lower) - ord('a') + shift) % 26 + ord('a'))
#             # Convert back to uppercase if necessary
#             if is_upper:
#                 encrypted_char = encrypted_char.upper()
#             ciphertext += encrypted_char
#             key_index += 1
#         else:
#             # Non-alphabetic characters are not changed
#             ciphertext += char
            
#     return ciphertext

# def vigenere_decrypt(ciphertext, key):
#     plaintext = ""
#     key_length = len(key)
#     key_index = 0

#     for char in ciphertext:
#         if char.isalpha():
#             # Determine if the character is uppercase or lowercase
#             is_upper = char.isupper()
#             char_lower = char.lower()
#             # Get thA corresponding key character
#             key_char = key[key_index % key_length].lower()
#             # Calculate the shift
#             shift = ord(key_char) - ord('a')
#             # Decrypt the character
#             decrypted_char = chr((ord(char_lower) - ord('a') - shift) % 26 + ord('a'))
#             # Convert back to uppercase if necessary
#             if is_upper:
#                 decrypted_char = decrypted_char.upper()
#             plaintext += decrypted_char
#             key_index += 1
#         else:
#             # Non-alphabetic characters are not changed
#             plaintext += char
            
#     return plaintext

# # Example usage
# if __name__ == "__main__":
#     message = "HelloWorld!"
#     key = "keyword"

#     encrypted_message = vigenere_encrypt(message, key)
#     print(f"Encrypted: {encrypted_message}")
#     decrypted_message = vigenere_decrypt(encrypted_message, key)
#     print(f"Decrypted: {decrypted_message}")


from pycipher import Vigenere

plaintext = input("Enter plaintext: ")
key = input("Enter key: ").upper()

ciphertext = Vigenere(key).encipher(plaintext)
decrypted = Vigenere(key).decipher(ciphertext)

print("\nCiphertext: , ciphertext)
print("Decrypted text:", decrypted)



from pycipher import Caesar
plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift value: "))

ciphertext = Caesar(shift).encipher(plaintext)
decrypted = Caesar(shift).decipher(ciphertext)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)



from pycipher import Railfence
plaintext = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

ciphertext = Railfence(rails).encipher(plaintext)
decrypted = Railfence(rails).decipher(ciphertext)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)







import string

plain_alphabet = string.ascii_uppercase
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

plaintext = input("Enter plaintext: ")

encrypt = str.maketrans(plain_alphabet + plain_alphabet.lower(),cipher_alphabet + cipher_alphabet.lower())

decrypt = str.maketrans(cipher_alphabet + cipher_alphabet.lower(), lain_alphabet + plain_alphabet.lower())

ciphertext = plaintext.translate(encrypt)
decrypted = ciphertext.translate(decrypt)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)