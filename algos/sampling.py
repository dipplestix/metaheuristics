import random
import math

def truncation_selection(population, n):
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:n]

def tournament_selection(population, n, p):
    winners = []
    for i in range(n):
        if p%1 != 0:
            if random.random() < p%1:
                loop_p = math.ceil(p)
            else:
                loop_p = math.floor(p)
        else:
            loop_p = p
        contestants = random.sample(population, loop_p)
        contestants.sort(key=lambda x: x.fitness, reverse=True)
        winners.append(contestants[0])
    return winners
