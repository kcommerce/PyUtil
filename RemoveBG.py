import rembg
import numpy as np
from PIL import Image
import os

def remove_background(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the input image
            input_image = Image.open(input_path)

            # Convert the input image to a numpy array
            input_array = np.array(input_image)

            # Apply background removal using rembg
            output_array = rembg.remove(input_array)

            # Create a PIL Image from the output array
            output_image = Image.fromarray(output_array)

            # Save the output image
            output_image.save(output_path)

if __name__ == "__main__":
    input_folder = "/content/drive/MyDrive/INPUT_IMAGES"
    output_folder = "/content/drive/MyDrive/OUTPUT_IMAGES"

    remove_background(input_folder, output_folder)
