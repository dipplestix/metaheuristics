import time
import random
import numpy as np

class Individual():
    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness
    def __gt__(self, other):
        return self.fitness > other.fitness
    def __eq__(self, other):
        return self.fitness == other.fitness and self.genome == other.genome

class ES():
    #Evolutionary strategies
    def __init__(self, mu, lambda_, initialize, fitness, mutate, sample, plus=True, optimal_fitness=None, timer=10, visualizer=None):
        self.mu = mu
        self.lambda_ = lambda_
        self.initialize = initialize
        self.fitness = fitness
        self.mutate = mutate
        self.sample = sample
        #(mu, lambda_) algorithm if False, mu+lambda_ algorithm if true
        self.plus = plus
        self.population = []
        self.timer = timer
        self.visualizer = visualizer
        if optimal_fitness is None:
            self.optimal_fitness = np.inf
        else:
            self.optimal_fitness = optimal_fitness
        
    def solve(self):
        for i in range(0, self.mu):
            genome = self.initialize()
            self.population.append(Individual(genome, self.fitness(genome)))
        best = self.population[0]
        start_time = time.time()
        gen = 0
        while best.fitness < self.optimal_fitness and time.time() < start_time + self.timer:
            for individual in self.population:
                if individual > best:
                    best = individual
            keep = self.sample(self.population, self.mu)
            new_pop = []
            for individual in keep:
                for i in range(int(self.lambda_/self.mu)):
                    new_pop.append(self.mutate(individual))
            if self.plus:
                new_pop.extend(keep)
            self.population = new_pop
            gen += 1
            if self.visualizer is not None:
                visualizer(best)
        return best   
