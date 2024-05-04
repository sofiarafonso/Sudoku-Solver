from charles import Population, Individual
from sudoku_data import easy #, medium, hard, expert
from mutation import swap_mutation_box, swap_mutation_column, swap_mutation_row, insertion_mutation
from selection import tournament_selection
from crossover import single_point_crossover, two_point_crossover, uniform_crossover


# Creating a population of 100 individuals

# Evolving the population for 100 generations
fitness = -1

while fitness != 0:
    pop = Population(size=100, optim="min", replacement=False, initial_sudoku=easy)
    best = pop.evolve(gens=1000, xo_prob=0.8, mut_prob=0.2, select=tournament_selection, xo=single_point_crossover, mutate=swap_mutation_box, elitism=True)
    fitness = best.get_fitness()
    print(f"Best fitness: {best.get_fitness()}")
    print(f"Best representation: {best.print()}")
    
