def scale(matrix, k):
    """
    @param matrix: general 2d tensor
    @param k: element wise scaling factor 
    """
    if k < 0:
        raise ValueError("scaling factor cannot be negative")
            
    return [[i * k for i in j] for j in matrix]

def add(matrix1, matrix2):
    """
    @param matrix1: general 2d tensor
    @param matrix2: general 2d tensor
    """
    if (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0])):
        raise ValueError("dimension mismatch, cannot add")

    return [[matrix1[i][j] + matrix2[i][j]
               for j in range(len(matrix1[0]))]
             for i in range(len(matrix1))]

def subtract(matrix1, matrix2):
    """
    @param matrix1: general 2d tensor
    @param matrix2: general 2d tensor
    @return matrix1 - matrix2
    """
    if (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0])):
        raise ValueError("dimension mismatch, cannot add")

    return [[matrix1[i][j] - matrix2[i][j]
                for j in range(len(matrix1[0]))]
                for i in range(len(matrix1))]

def abs_max(matrix):
    """
    @param matrix: general 2d tensor
    @return (max(abs(element)), index of max element) 
    """
    abs_max = 0
    abs_max_index = (0,0)

    # loop through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            abs_max = max(abs(matrix[i][j]), abs_max)
            abs_max_index = (i,j)

    return abs_max, abs_max_index

def local_abs_upper_bound(upper_bound, matrix, index, window_size):
    """
    @param upper_bound: int
    @param matrix: general 2d tensor
    @param index: (x,y)
    @param window_size: odd int
    @return bool
    """
    # checks if upper_bound is the upper bound of 
    # window_size x window_size neighbourhood of index 
    k =  int((window_size-1)/2) # half width
    for i in range(max(index[0] - k, 0), 
                   min(index[0] + k + 1, len(matrix))):
        
        for j in range(max(index[1] - k, 0), 
                   min(index[1] + k + 1, len(matrix[0]))):
            
            print(i,j, matrix[i][j])
            if upper_bound < matrix[i][j]:
                return False
            
    return True
        

def sample(matrix, index, window_size):
    """
    @param matrix: general 2d tensor
    @param index: (x,y)
    @param window_size: int
    @return window_size x window_size matrix centered about index
    """
    k =  int((window_size-1)/2) # half width

    sample = [[0 for j in range(window_size)] for i in range(window_size)]

    for sample_i,i in zip(range(window_size),
                          range(index[0] - k, 
                                index[0] - k + window_size)):
        
        for sample_j,j in zip(range(window_size),
                              range(index[1] - k,
                                    index[1] - k + window_size)):
            
            if i < 0 or i >= len(matrix):
                sample[sample_i][sample_j] = 0

            elif j < 0 or j >= len(matrix):
                sample[sample_i][sample_j] = 0
            
            else:
                sample[sample_i][sample_j] = matrix[i][j]
    
    return sample
    
    