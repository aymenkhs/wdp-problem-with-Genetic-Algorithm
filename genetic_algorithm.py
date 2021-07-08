import random

from instance import *

class Population:

    def __init__(self, pop_size, nb_generations, wdp):
        self.wdp = wdp
        self._population_size = pop_size
        self._nb_generation = nb_generations
        self._current_generation = 0
        self.population = []
        self._generate_population()
        self.__check_parameters()

    def __check_parameters(self):
        if self._population_size < 4:
            raise ValueError("the population size must be at least 4")
        if self._nb_generation < 2:
            raise ValueError("there must be at least 2 generations")

    @property
    def current_generation(self):
        return self._current_generation

    @property
    def best_individual(self):
        self.__sort_based_score()
        return self.population[0]

    def _generate_population(self):
        """ methode to generate the population by generating individuals """
        for _ in range(self._population_size):
            self.population.append(Individual.generate_individual(self.wdp))

    def is_it_last_generation(self):
        return self._current_generation == self._nb_generation

    def build_next_generation(self):
        """ methode that generate the individuals of the next generation """
        self.__remove_conflicted_items()
        if len(self.population) == 0:
            self._generate_population()
            return

        self.__sort_based_score()
        best_individual = self.population[0]

        next_generation = []
        best_in_this_generation = self.__select_bests_in_current_generation()
        for individual_i in best_in_this_generation:
            if len(next_generation) >= self._population_size:
                break
            for individual_j in best_in_this_generation:
                next_generation.append(individual_i + individual_j)
                next_generation.append(individual_j + individual_i)

        if len(next_generation) >= self._population_size:
            rest = self._generate_random_individuals(self._population_size//10)
        else:
            rest = self._generate_random_individuals(self._population_size - len(next_generation))

        print(len(next_generation))
        next_generation += rest
        print(len(next_generation))
        self.population = next_generation
        self.__mutations()
        next_generation.append(best_individual)
        self._current_generation += 1

    def __remove_conflicted_items(self):
        self.population = [individual for individual in self.population if individual.score != 0]

    def __select_bests_in_current_generation(self):
        """ methode that select the bests individuals in the current generation """
        return self.population[30:]
        # a revoir


    def _generate_random_individuals(self, nb_individuals):
        """ methode that generae a certain number of individuals """
        rest = []
        if nb_individuals > 0:
            for _ in range(nb_individuals):
                rest.append(Individual.generate_individual(self.wdp))
        return rest

    def __sort_based_score(self):
        """ methode that sort the current generation based on their score """
        self.population = sorted(self.population, key=lambda individual: individual.score)

    def __mutations(self):
        for individual in self.population:
            individual.mutation()


class Individual:
    """ class that represent an indivudual in the GA """
    def __init__(self, genome, wdp):
        self.genome = genome
        self.wdp = wdp
        self.score = self._fitness_function()

    def __str__(self):
        return str(self.genome)

    def __repr__(self):
        return str(self)

    def __add__(self, individual):
        """
            methode for a unipoint crossover between two individuals by adding them like
                individual1 + individual2
            the result will be an new individual
        """
        new_genome = []

        to_take = int(len(self.genome) / 2)
        if len(self.genome) % 2 != 0:
            to_take += 1

        for gene in range(to_take):
            new_genome.append(self.genome[gene])

        for gene in range(to_take, len(self.genome)):
             new_genome.append(individual.genome[gene])

        # crossover

        return Individual(new_genome, self.wdp)

    def _fitness_function(self):
        """ methode that calcul the score of an indivudual """
        if self._detect_conflict():
            return 0
        somme = 0
        for index, gene in enumerate(self.genome):
            if gene:
                somme += self.wdp[index].price
        return somme

    def _detect_conflict(self):
        for i in range(len(self.genome)):
            if self.genome[i]:
                for bid in self.wdp[i].concurent_bids:
                    if self.genome[bid.bider]:
                        return True
        return False


    def mutation(self):
        " make a mutation randomlly in one of the genome genes"
        mutation_proba = 0 # in percent
        rand_num = random.randint(0,99)
        if rand_num < mutation_proba:
            rand_num = random.randint(0, self.wdp.n - 1)
            self.genome[rand_num] = not self.genome[rand_num]

    @classmethod
    def generate_individual(cls, wdp):
        """ methode to generate an individual"""
        # generate r (wdp.n float elements)
        r = [random.random() for _ in range(wdp.n)]
        # at first our genome is all false we'll start filling it later
        genome = [False for _ in range(wdp.n)]
        conflicts = [False for _ in range(wdp.n)]

        continue_find = True
        while continue_find:
            # select the max of r
            i = 0
            max_i = i
            max_val = r[i]
            while i < wdp.n:
                if max_val < r[i] and not genome[i] and not conflicts[i]:
                    max_i = i
                    max_val = r[i]
                i+=1

            for bid in wdp[max_i].concurent_bids:
                if genome[bid.bider]:
                    conflicts[max_i] = True
                    break
            if not conflicts[max_i]:
                genome[max_i] = True

            continue_find = False
            for i in range(wdp.n):
                if not genome[i] and not conflicts[i]:
                    all_checked = True
                    break

        return Individual(genome, wdp)



class GeneticAlgorithm:

    def __init__(self, pop_size, nb_generation, wdp):
        self._pop_size = pop_size
        self._nb_generation = nb_generation
        self.genetic = Population(pop_size, nb_generation, wdp)


    def process(self):
        """ method to execute the Algorithm """
        while not self.genetic.is_it_last_generation():
            print(self.genetic._current_generation, len(self.genetic.population))
            self.genetic.build_next_generation()

        self.best_individual = self.genetic.best_individual
