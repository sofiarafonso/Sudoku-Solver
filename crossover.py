import random

def single_point_crossover(parent1, parent2):
    # Perform single-point crossover between two parents
    crossover_point = len(parent1) // 2
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def two_point_crossover(parent1, parent2):
    # Perform two-point crossover between two parents
    crossover_point1 = len(parent1) // 3
    crossover_point2 = 2 * len(parent1) // 3
    child = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    return child

def uniform_crossover(parent1, parent2):
    # Perform uniform crossover between two parents
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child