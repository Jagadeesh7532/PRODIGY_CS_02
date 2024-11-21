from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))

    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Decrypt by subtracting the key from each pixel value
    decrypted_pixels = (pixels - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))

    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    action = input("Do you want to 'encrypt' or 'decrypt' the image? ").strip().lower()
    image_path = input("Enter the path of the image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    key = int(input("Enter the key (integer value): "))

    if action == 'encrypt':
        encrypt_image(image_path, output_path, key)
    elif action == 'decrypt':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
