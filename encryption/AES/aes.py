from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import os

# AES encryption function
def aes_encrypt(key, plaintext):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return iv + ciphertext

# AES decryption function
def aes_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext

# Function to encrypt an image
def encrypt_image(input_file, output_file, key):
    with Image.open(input_file) as img:
        img_data = img.tobytes()

    encrypted_data = aes_encrypt(key, img_data)

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

# Function to decrypt an image
def decrypt_image(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = aes_decrypt(key, encrypted_data)

    with open(output_file, 'wb') as img:
        img.write(decrypted_data)

if __name__ == "__main__":
    # Example usage
    input_image = "input3d.jpg"
    encrypted_image = "encrypted_image.jpg"
    decrypted_image = "decrypted_image.jpg"

    # Generate a random 256-bit key
    key = get_random_bytes(32)

    # Encrypt the image
    encrypt_image(input_image, encrypted_image, key)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key)

    print("Image encryption and decryption complete.")
