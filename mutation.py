from random import randint

def swap_mutation_column(individual):
    """ Swaps two elements in the same column """
    matrix = individual.get_representation()
    col = randint(0, 8)
    row1 = randint(0, 8)
    row2 = randint(0, 8)
    while row1 == row2:
        row2 = randint(0, 8)
    # Check if the swap involves an element from the initial sudoku
    while matrix[row1][col] in individual.initial_sudoku or matrix[row2][col] in individual.initial_sudoku:
        row1 = randint(0, 8)
        row2 = randint(0, 8)
        while row1 == row2 or matrix[row2][col] in individual.initial_sudoku:
            row2 = randint(0, 8)
    matrix[row1][col], matrix[row2][col] = matrix[row2][col], matrix[row1][col]
    return matrix

def swap_mutation_row(individual):
    """ Swaps two elements in the same row """
    matrix = individual.get_representation()
    row = randint(0, 8)
    col1 = randint(0, 8)
    col2 = randint(0, 8)
    while matrix[row][col1] in individual.initial_sudoku or matrix[row][col2] in individual.initial_sudoku:
        col1 = randint(0, 8)
        col2 = randint(0, 8)
        while col1 == col2 or matrix[row][col2] in individual.initial_sudoku:
            col2 = randint(0, 8)
    matrix[row][col1], matrix[row][col2] = matrix[row][col2], matrix[row][col1]
    return matrix

def insertion_mutation(individual):
    """ Inserts a random element in a random position """
    matrix = individual.get_representation()
    row = randint(0, 8)
    col = randint(0, 8)
    element = randint(1, 9)
    while matrix[row][col] in individual.initial_sudoku:
        element = randint(1, 9)
    matrix[row][col] = element
    return matrix

