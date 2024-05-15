from copy import deepcopy
from random import shuffle, choice, sample, random, randint, uniform
from operator import attrgetter


class Individual:
    def __init__(
            self,
            initial_sudoku,
            representation=None,
            size=81,
            valid_set=range(0, 10)):
        self.initial_sudoku = initial_sudoku

        if representation is None:
            self.representation = self.get_representation()
        else:
            self.representation = representation

        self.fitness = self.get_fitness()

        self.size = size

        self.valid_set = valid_set

    def get_columns(self, matrix):
        """ returns a 9x9 matrix, 
        where each list is a column of the self.representation """
        columns = [[matrix[j][i] for j in range(9)] for i in range(9)]
        return columns

    def get_box(self, matrix):
        """ returns a 9x9 matrix,
        where each list is a 3x3 box of the given matrix """
        boxes = [[0 for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                box_row = (i // 3) * 3 + j // 3
                box_col = (i % 3) * 3 + j % 3
                boxes[box_row][box_col] = matrix[i][j]
        return boxes

    def print(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self[i][j], end=" ")
                if j == 8:
                    print()    

    def get_values(self, list):
        """ for each value in a "list" (array that could be a row, a collumn or a box) 
        returns the possible values according to the ones that were already there """
        values = [i for i in range(1,10)]
        for i in list:
            if i != 0:
                values.remove(i)
        return values
    
    def set_box(self, box_index, box):
        """ Set the contents of a box at the given index """
        self.representation[box_index * 9 : (box_index + 1) * 9] = box

    def get_representation(self):
        """ returns a 9x9 matrix, where each cell is filled with a value that is possible for that cell"""
        representation = [[0 for i in range(9)] for i in range(9)]   
        for i in range(9):
            for j in range(9):   
                if self.initial_sudoku[i][j] != 0:
                    representation[i][j] = self.initial_sudoku[i][j]
                else:
                    row = self.get_values(self.initial_sudoku[i])
                    column = self.get_values(self.get_columns(self.initial_sudoku)[j])
                    box = self.get_values(self.get_box(self.initial_sudoku)[(i // 3) * 3 + j // 3])
                    possible_values = list(set(row) & set(column) & set(box))
                    representation[i][j] = choice(possible_values)
        return representation
    
    def count_duplicates(self, matrix):
        """ counts the number of duplicates in each "list" in the sudoku"""
        duplicates = sum(9 - len(set(l)) for l in matrix)
        return duplicates
    
    def get_fitness(self):
        """ returns the fitness of the individual """
        #sum of 1 per each number of duplicates in rows, collumns and boxes and 5 per each value different from the initial_sudoku
        fitness = 0
        rows = self.representation
        columns = self.get_columns(self.representation)
        boxes = self.get_box(self.representation)
        row_dups = self.count_duplicates(rows)
        column_dups = self.count_duplicates(columns)
        box_dups = self.count_duplicates(boxes)
        if row_dups > 0:
            fitness += row_dups
        if column_dups > 0:
            fitness += column_dups  
        if box_dups > 0:
            fitness += box_dups
        if row_dups == 0 and column_dups == 0 and box_dups == 0:
            fitness = 0
        self.fitness = fitness
        return fitness

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Fitness: {self.fitness}"

###############################

class Population:
    def __init__(self, size, optim, **kwargs):
        self.size = size
        self.individuals = []
        self.initial_sudoku = kwargs["initial_sudoku"]
        self.optim = optim
        self.init_pop()

    # Initializing a new population
    def init_pop(self):
        for _ in range(self.size):
            self.individuals.append(
                Individual(
                    initial_sudoku=self.initial_sudoku
                )
            )

    def evolve(self, gens, xo_prob, mut_prob, select, xo, mutate, elitism):
        for i in range(gens):
            new_pop = []

            if elitism:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))
                new_pop.append(elite)

            while len(new_pop) < self.size:
                parent1 = select(self)
                parent2 = select(self)

                if random() < xo_prob:
                    offspring1, offspring2 = xo(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2

                if random() < mut_prob:
                    offspring1 = mutate(offspring1)
                if random() < mut_prob:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1, initial_sudoku=self.initial_sudoku))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2, initial_sudoku=self.initial_sudoku))

            if elitism:
                if self.optim == "max":
                    least = sorted(new_pop, key=attrgetter("fitness"))[:1]
                elif self.optim == "min":
                    least = sorted(new_pop, key=attrgetter("fitness"), reverse=True)[:1]
                for j in range(1):
                    new_pop.pop(new_pop.index(least[j]))
                    new_pop.append(elite)

            self.individuals = new_pop

            if self.optim == "max":
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
                new_best_individual = deepcopy(max(self, key=attrgetter("fitness")))
            elif self.optim == "min":
                print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')
                new_best_individual = deepcopy(min(self, key=attrgetter("fitness")))

            print(f"Generation " + str(i + 1) + " out of " + str(gens))

        return new_best_individual
    
    def get_individuals(self):
        return self.individuals

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
       return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"
    
