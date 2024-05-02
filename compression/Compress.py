import os

import cv2


# Function to compress image
def compress_image(input_image_path, output_image_path, compression_quality):
    # Read image
    image = cv2.imread(input_image_path)

    # Compress image
    cv2.imwrite(output_image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), compression_quality])
    print(f"Image compressed successfully to {output_image_path}")


# Function to decompress image
# Function to decompress image
def decompress_image(compressed_image_path, output_image_path):
    # Check if the file exists
    if not os.path.exists(compressed_image_path):
        print(f"Error: The file '{compressed_image_path}' does not exist.")
        return

    # Read compressed image
    compressed_image = cv2.imread(compressed_image_path)

    # Check if the image is empty
    if compressed_image is None:
        print(f"Error: Unable to read the image file '{compressed_image_path}'.")
        return

    # Write decompressed image
    cv2.imwrite(output_image_path, compressed_image)
    print(f"Image decompressed successfully to {output_image_path}")


# Main function
if __name__ == "__main__":
    # Prompt user for compression or decompression
    operation = input("Enter 'c' for compression or 'd' for decompression: ")

    if operation == 'c':
        # Compression
        input_image_path = input("Enter the path of the image to compress: ")
        output_image_path = input("Enter the path to save the compressed image: ")
        compression_quality = int(input("Enter the compression quality (0-100): "))
        compress_image(input_image_path, output_image_path, compression_quality)

    elif operation == 'd':
        # Decompression
        compressed_image_path = input("Enter the path of the compressed image: ")
        output_image_path = input("Enter the path to save the decompressed image: ")
        decompress_image(compressed_image_path, output_image_path)

    else:
        print("Invalid operation. Please enter 'c' for compression or 'd' for decompression.")
