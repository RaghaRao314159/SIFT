from PIL import Image, ImageOps 
import numpy as np
import matplotlib.pyplot as plt

def get_greyscale_image(image_path):
    # creating a image1 object 
    im1 = Image.open("sample.jpg") 
    
    # applying grayscale method 
    im2 = ImageOps.grayscale(im1) 

    return np.array(im2)


def show_image_greyscale(image_array):
    image = Image.fromarray(np.array(image_array))
    plt.imshow(image, cmap='gray') 
    plt.show()   


def scale_to_image(matrix):
    # scales an arbitrary 2d matrix into an image (using min-max)
    image = matrix.copy()
    # initialise max and min pixel
    max_pixel = image[0][0]
    min_pixel = image[0][0]

    # loop through to determine max and min pixel
    for row in image:
        for pixel in row:
            max_pixel = max(pixel, max_pixel)
            min_pixel = min(pixel, min_pixel)

    # scale every pixel by setting max and min values as 0 and 255
    scale =  255 / (max_pixel - min_pixel)

    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            image[i][j] = (pixel - min_pixel) * scale
    
    return image

def abs_scale_to_image(matrix):
    # scales the absolute values of a 2d matrix into an image (using min-max)
    image = matrix.copy()

    for i in range(len(image)):
        for j  in range(len(image[0])):
            image[i][j] = abs(image[i][j])
    
    return scale_to_image(image)

def scale(image_array, k):
    """
    @param image_array: 2d matrix
    @param k: element wise scaling factor 
    """
    if k < 0:
        raise ValueError("scaling factor cannot be negative")
            
    return [[min(i * k, 255) for i in j] for j in image_array]

def add(image_array1, image_array2):
    """
    @param image_array1: 2d matrix
    @param image_array2: 2d matrix
    """
    if (len(image_array1) != len(image_array2)) or (len(image_array1[0]) != len(image_array2[0])):
        raise ValueError("dimension mismatch, cannot add")

    return [[min(image_array1[i][j] + image_array2[i][j], 255)
               for j in range(len(image_array1[0]))]
             for i in range(len(image_array1))]

def subtract(image_array1, image_array2):
    """
    @param image_array1: 2d matrix
    @param image_array2: 2d matrix
    @return image_array1 - image_array2
    """
    if (len(image_array1) != len(image_array2)) or (len(image_array1[0]) != len(image_array2[0])):
        raise ValueError("dimension mismatch, cannot add")

    return [[max(image_array1[i][j] - image_array2[i][j], 0)
               for j in range(len(image_array1[0]))]
             for i in range(len(image_array1))]



    