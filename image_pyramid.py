
from convolution import convolve_2d_gaussian
from gaussian import get_gaussian_kernel_1d
from image import get_greyscale_image, show_image_greyscale
import math


def subsample(image):
    """
    @param image: 2d matrix
    """
    # subsamples by a factor of 2
    reduced_rows = int(len(image)/2)
    reduced_cols = int(len(image[0])/2)

    # create subsampled image
    subsampled_image = [
        [image[2*i][2*j] for j in range(reduced_cols)] 
        for i in range(reduced_rows)
    ]

    return subsampled_image

def get_number_of_octaves(image):
    """
    @param image: 2d matrix
    """
    number_of_rows = len(image)
    number_of_cols = len(image[0])

    largest_dimension = max(number_of_rows, number_of_cols)

    # ensure last octave is atleast 16 x 16
    number_of_octaves = int(math.log(largest_dimension, 2) - 4)

    if number_of_octaves < 1:
        print("image is too small for SIFT !")

    return number_of_octaves

def filter_bank(sigma_0 = 1, s = 3):
    """
    @param sigma_0: initial blur
    @param s: size of an octave
    """
    # image pyramid is implemented efficiently using incremental blurs
    # the filters are sigma_i * sqrt(2^(2/s) - 1)
    bank = []
    sigmas = []

    for i in range(0,s):
        sigma_i = sigma_0 * (2**(i/s))
        sigmas.append(sigma_i)

        sigma_ki = sigma_i * (2**(2 / s) - 1)**0.5
        filter_i = get_gaussian_kernel_1d(sigma_ki)
        bank.append(filter_i)
    
    sigma_i = sigma_0 * 2
    sigmas.append(sigma_i)

    return bank, sigmas[1:]

def get_pyramid(image, sigma_0 = 1, s = 3):
    """
    @param image: 2d matrix
    @param sigma_0: initial blur
    @param s: size of an octave
    """
    # number of octaves = height of octaves
    octaves = get_number_of_octaves(image)

    # initialise pyramid
    pyramid = [[] for _ in range(octaves)]
    # linear_pyramid = []
    actual_sigmas = [[] for _ in range(octaves)]
    actual_sigma = sigma_0

    # deep copy used to ensure original image is not affected
    image_copy = image.copy()

    # same filters used for every octave thanks to subsampling
    filters, sigmas = filter_bank(sigma_0, s)

    # initial filter from sigma_0
    initial_filter = get_gaussian_kernel_1d(sigma_0)
    image_copy = convolve_2d_gaussian(image_copy, initial_filter)

    for octave in range(octaves):
        # add to pyramid
        pyramid[octave].append(image_copy.copy())
        # linear_pyramid.append(image_copy.copy())

        # consolidate actual sigmas 
        actual_sigmas[octave].append(actual_sigma)

        print("Octave number :", octave)
        print("Octave Sigma: ", sigma_0)
        print("Actual Sigma: ", actual_sigma)
        show_image_greyscale(image_copy)

        for idx, filter in enumerate(filters):

            # small incremental blur
            image_copy = convolve_2d_gaussian(image_copy, filter)

            # add to pyramid
            pyramid[octave].append(image_copy.copy())
            # linear_pyramid.append(image_copy.copy())

            #calculate actual sigma
            actual_sigma = sigmas[idx] * 2**octave
            actual_sigmas[octave].append(actual_sigma)

            print("Octave number :", octave)
            print("Octave Sigma: ", sigmas[idx])
            print("Actual Sigma: ", actual_sigma)
            show_image_greyscale(image_copy)
        
        print("---------------------------------------------------------------")

        # reduce image size by 4 (half each dimension)
        image_copy = subsample(image_copy)
        
    
    return pyramid, actual_sigmas

        

#-----------------------------------------------------------------------------


def filter_bank2(sigma_0 = 1, s = 3):
    """
    @param sigma_0: initial blur
    @param s: size of an octave
    """
    # image pyramid is implemented efficiently using incremental blurs
    # the filters are sigma_0(2^(2i/s) - 1)
    bank = []
    sigmas = []

    #initial_filter = get_gaussian_kernel_1d(sigma_0)
    #bank.append(initial_filter)
    #sigmas.append(sigma_0)

    for i in range(1,s+1):
        sigma = sigma_0 * (2**(2 * i / s) - 1)**0.5

        filter_i = get_gaussian_kernel_1d(sigma)
        bank.append(filter_i)
        sigmas.append((sigma_0**2 + sigma**2)**0.5)
    
    return bank, sigmas 


def get_pyramid2(image, sigma_0 = 1, s = 3):
    """
    @param image: 2d matrix
    @param sigma_0: initial blur
    @param s: size of an octave
    """
    # number of octaves = height of octaves
    octaves = get_number_of_octaves(image)

    # initialise pyramid
    pyramid = [[] for _ in range(octaves)]
    # linear_pyramid = []
    actual_sigmas = [[] for _ in range(octaves)]
    actual_sigma = sigma_0

    # deep copy used to ensure original image is not affected
    image_copy = image.copy()

    # same filters used for every octave thanks to subsampling
    filters, sigmas = filter_bank(sigma_0, s)

    # initial filter from sigma_0
    initial_filter = get_gaussian_kernel_1d(sigma_0)
    image_copy = convolve_2d_gaussian(image_copy, initial_filter)

    for octave in range(octaves):
        # add to pyramid
        pyramid[octave].append(image_copy.copy())
        # linear_pyramid.append(image_copy.copy())

        # consolidate actual sigmas 
        actual_sigmas[octave].append(actual_sigma)

        print("Octave number :", octave)
        print("Octave Sigma: ", sigma_0)
        print("Actual Sigma: ", actual_sigma)
        show_image_greyscale(image_copy)

        for idx, filter in enumerate(filters):

            # small incremental blur
            image_copy = convolve_2d_gaussian(image_copy, filter)

            # add to pyramid
            pyramid[octave].append(image_copy.copy())
            # linear_pyramid.append(image_copy.copy())

            #calculate actual sigma
            actual_sigma = sigmas[idx] * 2**octave
            actual_sigmas[octave].append(actual_sigma)

            print("Octave number :", octave)
            print("Octave Sigma: ", sigmas[idx])
            print("Actual Sigma: ", actual_sigma)
            show_image_greyscale(image_copy)
        
        print("---------------------------------------------------------------")

        # reduce image size by 4 (half each dimension)
        image_copy = subsample(image_copy)
        
    
    return pyramid, actual_sigmas
        

    







