# -*- coding: utf-8 -*-
"""prodigy T-2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FqO6U5arFXl9YMyowtTy4FDoNLR2d5Q
"""

from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    try:
        # Print the path to ensure it's correct
        print(f"Attempting to open image at path: {image_path}")
        # Open the image
        img = Image.open(image_path)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # Convert image to numpy array
    img_array = np.array(img)

    # Encrypt the image by applying XOR with the key
    encrypted_array = img_array ^ key

    # Convert numpy array back to image
    encrypted_img = Image.fromarray(encrypted_array)

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # Convert image to numpy array
    img_array = np.array(img)

    # Decrypt the image by applying XOR with the key
    decrypted_array = img_array ^ key

    # Convert numpy array back to image
    decrypted_img = Image.fromarray(decrypted_array)

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

# Use a relative path to an image in the same directory as the script
image_path = 'test_image.jpg'
key = 50

# Create a test image if it doesn't exist
if not os.path.exists(image_path):
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(image_path)

encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)