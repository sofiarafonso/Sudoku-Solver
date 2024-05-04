import random
from charles import Individual

def single_point_crossover(parent1, parent2):
    # Perform single-point crossover between two parents
    crossover_point = len(parent1) // 2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    child1 = Individual(representation=child1, initial_sudoku=parent1.initial_sudoku)
    child2 = Individual(representation=child2, initial_sudoku=parent2.initial_sudoku)
    return child1, child2

def two_point_crossover(parent1, parent2):
    # Perform two-point crossover between two parents
    crossover_point1 = len(parent1) // 3
    crossover_point2 = 2 * len(parent1) // 3
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
    child1 = Individual(representation=child1, initial_sudoku=parent1.initial_sudoku)
    child2 = Individual(representation=child2, initial_sudoku=parent2.initial_sudoku)
    return child1, child2

def uniform_crossover(parent1, parent2):
    # Perform uniform crossover between two parents, randomly chosen genes from each parent
    child1 = []
    child2 = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    
    child1 = Individual(representation=child1, initial_sudoku=parent1.initial_sudoku)
    child2 = Individual(representation=child2, initial_sudoku=parent2.initial_sudoku)
    return child1, child2