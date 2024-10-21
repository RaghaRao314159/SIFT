def get_column(image, column_index):
    return [image[i][column_index] for i in range(len(image))]

def add_column(image, column_vector):
    if len(image) == 0:
        for element in column_vector:
            image.append([element])
    else:
        for i, element in enumerate(column_vector):
            image[i].append(element)
    return image

