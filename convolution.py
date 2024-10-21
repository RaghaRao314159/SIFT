from column import add_column, get_column
from gaussian import get_gaussian_kernel_1d


def convolve_1d(image, kernel):
    # 1-d convolution with odd length kernel
    mid = int((len(kernel) - 1)/2)

    output = [0 for i in image]
    for i in range(len(image)):
        for j in range(len(kernel)):

            image_idx = i - mid + j

            if image_idx < 0 or image_idx >= len(image):
                # padding of 0
                pixel = 0
            else:
                pixel = image[i - mid + j]

            output[i] += pixel * kernel[-j-1]

        # output[i] = round(output[i])
    return output

def convolve_2d_gaussian(image, kernel):
    # 2-d convolution = 2 1-d convolution 
    # kernel input is 1d gaussian
    # image is 2d input
    image_after_convx = []
    image_after_convy = []
    for row in image:
        image_after_convx.append(convolve_1d(row, kernel))
    
    for column_index in range(len(image[0])):
        columnx = get_column(image_after_convx, column_index)
        add_column(image_after_convy, convolve_1d(columnx, kernel))
    
    return image_after_convy
