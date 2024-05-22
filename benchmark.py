from charles import Population, Individual
from sudoku_data import easy
from mutation import swap_mutation_column, swap_mutation_row, insertion_mutation
from selection import tournament_selection, fitness_proportionate_selection, ranking_selection
from crossover import single_point_crossover, two_point_crossover, uniform_crossover
import csv




mutation = [swap_mutation_column, swap_mutation_row, insertion_mutation]
selection = [tournament_selection, fitness_proportionate_selection, ranking_selection]
crossover = [single_point_crossover, two_point_crossover, uniform_crossover]
elitism = [True, False]

with open('benchmark.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Mutation', 'Selection', 'Crossover', 'Elitism', 'Fitness'])
    
    for m in mutation:
        for s in selection:
            for c in crossover:
                for e in elitism:
                    fitnesses = []
                    for _ in range(15): 
                        pop = Population(size=500, optim="min", initial_sudoku=easy, replacement = False)
                        ev = pop.evolve(gens=200, xo_prob=0.8, mut_prob=0.2, select=s, xo=c, mutate=m, elitism=e)
                        fitnesses.append(ev.get_fitness())
                        print(ev.print())
                        print(f'Fitness: {ev.get_fitness()}')
                    
                    writer.writerow([m.__name__, s.__name__, c.__name__, e, fitnesses])

