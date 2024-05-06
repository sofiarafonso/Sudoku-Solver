from random import sample, choices
from operator import attrgetter

def tournament_selection(population, tournament_size=5):
    """ Perform tournament selection on the population """
    tournament = sample(population.individuals, tournament_size)
    if population.optim == "max":
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == "min":
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise ValueError("Invalid fitness_optim value. Must be 'max' or 'min'.")

def fitness_proportionate_selection(population):
    """ Perform fitness proportionate selection on the population """
    fitnesses = [ind.fitness for ind in population.individuals]
    if population.optim == "max":
        return choices(population.individuals, weights=fitnesses)[0]
    elif population.optim == "min":
        return choices(population.individuals, weights=[1/fit for fit in fitnesses])[0]
    else:
        raise ValueError("Invalid fitness_optim value. Must be 'max' or 'min'.")

def ranking_selection(population):
    """ Perform ranking selection on the population """
    sorted_pop = sorted(population.individuals, key=attrgetter("fitness"))
    ranks = [i for i in range(1, len(sorted_pop) + 1)]
    if population.optim == "max":
        return choices(sorted_pop, weights=ranks)[0]
    elif population.optim == "min":
        return choices(sorted_pop, weights=[1/rank for rank in ranks])[0]
    else:
        raise ValueError("Invalid fitness_optim value. Must be 'max' or 'min'.")