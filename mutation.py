from random import randint

def swap_mutation_column(individual):
    """ Swaps two elements in the same column """
    matrix = individual.set_representation()
    col = randint(0, 8)
    row1 = randint(0, 8)
    row2 = randint(0, 8)
    while row1 == row2:
        row2 = randint(0, 8)
    matrix[row1][col], matrix[row2][col] = matrix[row2][col], matrix[row1][col]
    return matrix

def swap_mutation_row(individual):
    """ Swaps two elements in the same row """
    matrix = individual.get_representation()
    row = randint(0, 8)
    col1 = randint(0, 8)
    col2 = randint(0, 8)
    while col1 == col2:
        col2 = randint(0, 8)
    matrix[row][col1], matrix[row][col2] = matrix[row][col2], matrix[row][col1]
    return matrix

def swap_mutation_box(individual):
    """ Swaps two elements in the same box """
    matrix = individual.get_representation()
    box = randint(0, 8)
    row1 = randint(0, 8)
    col1 = randint(0, 8)
    row2 = randint(0, 8)
    col2 = randint(0, 8)
    while row1 == row2 and col1 == col2:
        row2 = randint(0, 8)
        col2 = randint(0, 8)
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


def insertion_mutation(individual):
    """ Inserts a random element in a random position """
    print(type(individual))
    matrix = individual.get_representation()
    row = randint(0, 8)
    col = randint(0, 8)
    element = randint(1, 9)
    matrix[row][col] = element
    return matrix

