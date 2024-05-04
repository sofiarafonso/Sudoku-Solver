from charles import Population  
from sudoku_data import easy, medium, hard, expert
from mutation import swap_mutation_box, swap_mutation_column, swap_mutation_row, insertion_mutation
from selection import tournament_selection
from crossover import pmx


# Creating a population of 100 individuals
pop = Population(size=100, optim="min", replacement=False, initial_sudoku=easy)

# Evolving the population for 100 generations
#pop.evolve(gens=100, xo_prob=0.8, mut_prob=0.2, select=tournament_selection, xo=pmx, mutate=insertion_mutation, elitism=True)
