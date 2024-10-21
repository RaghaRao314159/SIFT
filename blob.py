import numpy as np

from image import *
from matrix_operations import *

def laplacian_of_gaussian(pyramid, s = 3):
    """
    @param pyramid: image pyramid
    @param s: size of an octave
    @return laplacians: laplacian pyramid
    """
    # difference of gaussian is used to approximate scaled laplacian
    laplacians = [[] for _ in range(len(pyramid))]

    # iterate through pyramid 
    for idx, octave in enumerate(pyramid):
        for i in range(len(octave) - 1):
            # difference of consecutive gaussian
            difference_of_gaussian = subtract(octave[i+1], octave[i])

            # scale matrix element wise
            scaled_laplacian = scale(difference_of_gaussian, 1/(2**(1/s) - 1))

            # create a pyramid of laplacians as well
            laplacians[idx].append(scaled_laplacian)
    
    return laplacians

def visualise_blobs(laplacians, sigmas):
    """
    @param laplacians: laplacian pyramid
    @param sigmas: sigma pyramid
    @return NULL
    """
    # loop through pyramid of laplacians 
    for idx, octave in enumerate(laplacians):
        for i in range(len(octave)):
            # laplacia matrices may have negative values and not between 0 and 255
            # to visualise them, they have to be min-max scaled to be between 0 and 255
            visualisable_laplacian = abs_scale_to_image(octave[i])
            print("Actual Sigma: ", sigmas[idx][i])
            show_image_greyscale(visualisable_laplacian)


def get_features(laplacians, pyramid, sigmas, feature_size):
    """
    @param laplacians: laplacian pyramid
    @param pyramid: image pyramid
    @param sigmas: sigma pyramid
    @param feature_size: int
    @return dictionary where key:value = sigma:feature 
    """
    # get maximums/minimums in laplacians
    # these are considered features
    features = {}

    for idx, octave in enumerate(laplacians):
        for i in range(len(octave)):
            max_value, index = abs_max(octave[i])
            is_max = True
            if idx > 0:
                is_max = is_max and local_abs_upper_bound(max_value, laplacians[idx-1], index, 3)
            if idx < len(laplacians) - 1:
                is_max = is_max and local_abs_upper_bound(max_value, laplacians[idx+1], index, 3)
            
            if is_max:
                feature = sample(pyramid[idx][i],index, feature_size)
                features[sigmas[idx][i]] = feature

    return features

def visualise_features(features):
    """
    @param laplacians: laplacian pyramid
    @param sigmas: sigma pyramid
    @return NULL
    """
    # loop through pyramid of laplacians 
    for sigma in features:
        print("Actual Sigma: ", sigma)
        show_image_greyscale(features[sigma])