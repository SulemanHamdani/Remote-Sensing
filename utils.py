import numpy as np
import cv2

def remove_noise(image):
  padding = 1

  # Create an empty padded image with the required dimensions
  padded_image = cv2.copyMakeBorder(
    image, padding, padding, padding, padding, cv2.BORDER_REPLICATE
  )

  # Create an empty output image with the same dimensions as the input image
  output_image = np.zeros_like(padded_image)

  # Slide a 3x3 kernel over the padded image
  for i in range(padding, padded_image.shape[0] - padding):
    for j in range(padding, padded_image.shape[1] - padding):
        # Extract the 3x3 kernel
        kernel = padded_image[i - padding : i + padding + 1, j - padding : j + padding + 1]

        # Flatten the kernel to a 1D array
        kernel_flat = kernel.flatten()

        # Find the most occurring pixel value in the kernel
        most_occuring_pixel = np.bincount(kernel_flat).argmax()

        # Replace the pixel in the output image with the most occurring pixel
        output_image[i, j] = most_occuring_pixel

  # Remove the padding from the output image
  output_image = output_image[padding:-padding, padding:-padding]
  return np.expand_dims(output_image, axis=2)

def replace_intensity(image, old_intensity, new_intensity):

    # Create a copy of the image
    replaced_image = np.copy(image)
    
    # Find the pixels with the old intensity
    pixels_to_replace = (replaced_image == old_intensity)
    
    # Replace the old intensity with the new intensity
    replaced_image[pixels_to_replace] = new_intensity
    return replaced_image

from numpy.core.numeric import binary_repr
kernel_size = (3, 3)
def perform_closing(image, kernel_size):
    # Create a structuring element for the morphological operation
    bin = replace_intensity(image, 24, 1)
    bin = replace_intensity(bin, 255, 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    
    # Perform closing operation on the image
    closed_image = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)
    
    closed_image = replace_intensity(closed_image, 1, 24)
    closed_image = replace_intensity(closed_image, 0, 255)
    return closed_image