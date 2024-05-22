from charles import Individual, Population
from mutation import insertion_mutation
from crossover import uniform_crossover
from selection import fitness_proportionate_selection
from sudoku_data import easy, medium, hard, expert
import csv

#Finetuning mutation and crossover probabilities
xo_probs = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
mut_probs = [0.01, 0.02, 0.05, 0.1, 0.15, 0.2]

# with open('finetuning.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Crossover', 'Mutation', 'Fitness'])
    
#     for xo_prob in xo_probs:
#         for mut_prob in mut_probs:
#             fitnesses = []
#             for _ in range(5):
#                 pop = Population(size=1000, optim="min", initial_sudoku=easy, replacement = False)
#                 ev = pop.evolve(gens=400, xo_prob=xo_prob, mut_prob=mut_prob, select=fitness_proportionate_selection, xo=uniform_crossover, mutate=insertion_mutation, elitism=True)
#                 fitnesses.append(ev.get_fitness())
#                 print(ev.print())
#                 print(f'Fitness: {ev.get_fitness()}')

#             writer.writerow([xo_prob, mut_prob, fitnesses])


# #Easy
# pop = Population(size=1000, optim="min", initial_sudoku=easy)
# ev = pop.evolve(gens=400, xo_prob=0.85, mut_prob=0.2, select=fitness_proportionate_selection, xo=uniform_crossover, mutate=insertion_mutation, elitism=True)
# a = ev.get_fitness()
# print(ev.print())
# print(f'Fitness: {ev.get_fitness()}')


# #Medium 
# pop = Population(size=2000, optim="min", initial_sudoku=medium, replacement = False)
# ev = pop.evolve(gens=400, xo_prob=0.85, mut_prob=0.2, select=fitness_proportionate_selection, xo=uniform_crossover, mutate=insertion_mutation, elitism=True)
# print(ev.print())
# print(f'Fitness: {ev.get_fitness()}')

# #Hard
# pop = Population(size=2000, optim="min", initial_sudoku=hard, replacement = False)
# ev = pop.evolve(gens=600, xo_prob=0.85, mut_prob=0.2, select=fitness_proportionate_selection, xo=uniform_crossover, mutate=insertion_mutation, elitism=True)
# print(ev.print())
# print(f'Fitness: {ev.get_fitness()}')







    