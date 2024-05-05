from charles import Population, Individual
from sudoku_data import easy #, medium, hard, expert
from mutation import swap_mutation_box, swap_mutation_column, swap_mutation_row, insertion_mutation
from selection import tournament_selection, fitness_proportionate_selection, ranking_selection
from crossover import single_point_crossover, two_point_crossover, uniform_crossover


pop = Population(size=1000, optim="min", replacement=False, initial_sudoku=easy)
best = pop.evolve(gens=500, xo_prob=0.9, mut_prob=0.1, select=fitness_proportionate_selection, xo=single_point_crossover, mutate=insertion_mutation, elitism=True)
fitness = best.get_fitness()

print(f"Best fitness: {best.get_fitness()}")
print(f"Best representation: {best.print()}")
