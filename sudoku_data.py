easy = [[0,8,0,7,0,9,0,0,2],
        [0,3,4,0,1,0,0,9,0],
        [0,0,0,3,0,8,0,0,0],
        [0,0,6,4,3,0,8,0,1],
        [0,0,1,2,7,6,0,4,0],
        [0,0,3,0,0,1,2,5,6],
        [0,0,0,0,9,0,0,2,7],
        [3,4,0,8,6,7,9,0,0],
        [0,9,0,5,0,4,0,0,3]]


# def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism, initial_sudoku, global_optimum, n_elite=10,
#                max_same_fitness=89):
#         best_individual = None
#         same_fitness_counter = 0
#         old_fitness = None

#         for gen in range(gens):
#             new_pop = []

#             # Copying the n_elite best individuals in the initial population for each generation
#             if elitism:
#                 if self.optim == "max":
#                     elite = deepcopy(sorted(self.individuals, key=attrgetter("fitness"), reverse=True))[:n_elite]
#                 elif self.optim == "min":
#                     elite = deepcopy(sorted(self.individuals, key=attrgetter("fitness")))[:n_elite]

#             while len(new_pop) < self.size:
#                 parent1, parent2 = select(self), select(self)
#                 # Crossover
#                 if random() < co_p:
#                     offspring1, offspring2 = crossover(parent1, parent2)
#                 else:
#                     offspring1, offspring2 = parent1, parent2
#                 # Mutation
#                 if random() < mu_p:
#                     offspring1 = mutate(offspring1)
#                 if random() < mu_p:
#                     offspring2 = mutate(offspring2)

#                 new_pop.append(Individual(representation=offspring1, initial_sudoku=initial_sudoku))
#                 if len(new_pop) < self.size:
#                     new_pop.append(Individual(representation=offspring2, initial_sudoku=initial_sudoku))

#             # Replacing the n_elite worst individuals in the population by the n_elite best from the
#             # previous population
#             if elitism:
#                 if self.optim == "max":
#                     least = sorted(new_pop, key=attrgetter("fitness"))[:n_elite]
#                 elif self.optim == "min":
#                     least = sorted(new_pop, key=attrgetter("fitness"), reverse=True)[:n_elite]
#                 for i in range(n_elite):
#                     new_pop.pop(new_pop.index(least[i]))
#                     new_pop.append(elite[i])

#             self.individuals = new_pop

#             # Returning the best individual in each population
#             if self.optim == "max":
#                 print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
#                 new_best_individual = deepcopy(max(self, key=attrgetter("fitness")))
#                 if best_individual is None or new_best_individual.fitness > best_individual.fitness:
#                     best_individual = deepcopy(new_best_individual)
#                     fitness = best_individual.get_fitness()
#                     if fitness == global_optimum:
#                         break
#             elif self.optim == "min":
#                 print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')
#                 new_best_individual = deepcopy(min(self, key=attrgetter("fitness")))
#                 if best_individual is None or new_best_individual.fitness < best_individual.fitness:
#                     best_individual = deepcopy(new_best_individual)
#                     fitness = best_individual.get_fitness()
#                     if fitness == global_optimum:
#                         break

#             print(f"Generation " + str(gen + 1) + " out of " + str(gens))

#             # Comparing fitness values to see if the new one is better than the previous one
#             if old_fitness == new_best_individual.fitness:
#                 same_fitness_counter += 1
#             else:
#                 same_fitness_counter = 0
#                 old_fitness = new_best_individual.fitness

#             # For cases where the program gets stuck in the same fitness value for max_same_fitness
#             # iterations, re-initialize the population
#             if same_fitness_counter > max_same_fitness:
#                 print("Population renewed\n\n")
#                 self.individuals = []
#                 self.init_pop()
#                 same_fitness_counter = 0
#                 old_fitness = None

#         # Returning the fitness of the best individual in all generations, its representation, and the
#         # total number of duplicates per column and row
#         print("Final best individual: " + str(best_individual.fitness))
#         print(best_individual.print_rep())
#         print("Number of duplicates of final sudoku: " + str(best_individual.get_total_duplicates()))
