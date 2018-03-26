import sys
import random


class GA:

    def __init__(self):
        self.sentinel = True
        self.targetSum = 36
        self.targetProduct = 360
        self.popSize = 30
        self.memberLength = 10
        self.population = []
        self.children = [0 for x in range(self.popSize)]
        self.fitness = []
        self.averageFitness = 0.0
        self.best = sys.maxsize

    def compute_fitness(self):
        sum = 0
        product = 1
        for x in self.population:
            for y in range(self.memberLength):
                if x[y] == 0:
                    sum += y+1
                else:
                    product *= y+1
            sum_error = sum - self.targetSum
            prod_error = (product - self.targetProduct) / self.targetProduct
            combined_error = abs(sum_error) + abs(prod_error)
            self.averageFitness += combined_error
            self.fitness.append(combined_error)
            if combined_error < self.best:
                if combined_error == 0.0:
                    self.sentinel = False
                self.best = combined_error
                print(x)
                print(combined_error)
            sum = 0
            product = 1

        self.averageFitness /= self.popSize

    def offspring(self):
        prior = 0.0
        index = 0
        count = 0
        average_fitness = self.averageFitness
        r = random.uniform(0,1)
        prior = self.fitness[0] / average_fitness
        self.fitness[0] = prior
        for i in range(1,self.popSize):
            self.fitness[i] = (float(self.fitness[i])/average_fitness) + prior
            prior = self.fitness[i]

        self.fitness[self.popSize-1] = float(self.popSize+1)
        while count<self.popSize:
            if r < self.fitness[index]:
                self.children[index] += 1
                count += 1
                r += 1.0
            else:
                index += 1

    def create_new_population(self):
        index = 0
        temp_population = []
        for i in range(self.popSize):
            for j in range(self.children[i]):
                temp = []
                for k in range(self.memberLength):
                    temp.append(self.population[i][k])
                index += 1
                temp_population.append(temp)
        self.population = temp_population

    # this method randomly mutates the population by adding or subtracting a value to
    def mutation(self):
        random.seed()
        for x in range(self.popSize):
            flips = random.randint(0,self.memberLength - 1)
            for y in range(flips):
                p = random.randint(0,self.memberLength - 1)
                self.population[x][p] = 0 if self.population[x][p] == 1 else 1

    # initializes the population to random values
    def init_population(self):
        random.seed()
        for x in range(self.popSize):
            temp = []
            for y in range(self.memberLength):
                temp.append(random.randint(0,1))
            self.population.append(temp)


    # this method clears data that needs to be reset
    def clear_data(self):
        self.fitness.clear()
        for x in range(self.popSize):
            self.children[x] = 0
        self.averageFitness = 0.0

    def run_ga(self):
        self.init_population()

        while self.sentinel:
            self.compute_fitness()
            self.offspring()
            self.create_new_population()
            self.mutation()
            self.clear_data()


x = GA()
x.run_ga()