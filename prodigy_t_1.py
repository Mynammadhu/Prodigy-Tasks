# -*- coding: utf-8 -*-
"""Prodigy T-1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qJ2CATOLisbBLiwVXKRKOe1-ynnjyRVV
"""

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
      choice = input("Do you want to (e)ncrypt, (d)ecrypt or (q)uit? ").lower()
      if choice == 'e':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_encrypt(text, shift)
            print(f"Encrypted message: {encrypted_message}")
      elif choice == 'd':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_decrypt(text, shift)
            print(f"Decrypted message: {decrypted_message}")
      elif choice == 'q':
            print("Goodbye!")
            break
      else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()