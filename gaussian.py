import math
PI = math.pi
e = math.e

def ln(x):
    return math.log(x)

def standard_gaussian_pdf_1d(sigma, x):
    return (1/(sigma * (2*PI)**0.5)) * e**(-0.5*(x/sigma)**2)

def standard_gaussian_pdf_2d(sigma, x, y):
    return (1/((2*PI) * (sigma**2))) * e**(-(x**2 + y**2) / (2 * sigma**2))


def get_gaussian_kernel_1d(sigma):
    # a 1-d truncation of 1/1000 of peak value = 1 is used
    n = int(((-2 * ln(1 / 1000))**0.5) * sigma)

    # a 2-d truncation of 1/1000 of peak value = 1 is used
    # n = int(((-1 * ln((sigma**2) * 2*PI / 1000))**0.5) * sigma)

    # let kernel be of size 2n+1
    kernel = [standard_gaussian_pdf_1d(sigma, i) for i in range(-n, n+1, 1)]

    return kernel





