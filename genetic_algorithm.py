def fitness(chromosome):
    total_score = 0
    num_cities = len(chromosome)
    for i in range(num_cities):
        j = (i + 1) % num_cities
        city_i = chromosome[i]
        city_j = chromosome[j]
        total_score += 2*dist[city_i, city_j]
        total_score += fuel[city_i, city_j]
    return total_score

def selection(pop, fitness):
    idx = np.random.choice(np.arange(len(pop)), size=2, replace=False, p=fitness/fitness.sum())
    return [pop[i] for i in idx]

def crossover(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    for i in range(startGene, endGene):
        childP1.append(parent1[i])
    childP2 = [item for item in parent2 if item not in childP1]
    child = childP1 + childP2
    return child

def mutation(chromosome):
    mutated_chromosome = list(chromosome)
    num_genes = len(chromosome)
    gene1 = int(random.random() * num_genes)
    gene2 = int(random.random() * num_genes)
    mutated_chromosome[gene1], mutated_chromosome[gene2] = mutated_chromosome[gene2], mutated_chromosome[gene1]
    return mutated_chromosome

def generate_new_population(pop, fitness):
    new_population = []
    elite = np.argmax(fitness)
    new_population.append(pop[elite])
    while len(new_population) < len(pop):
        parent1, parent2 = selection(pop, fitness)
        child = crossover(parent1, parent2)
        if random.random() < 0.05:
            child = mutation(child)
        new_population.append(child)
    return new_population

def genetic_algorithm(population):
    num_generations = 200
    best_fitness = []
    for _ in range(num_generations):
        fitness_scores = np.array([fitness(chromosome) for chromosome in population])
        best_fitness.append(np.min(fitness_scores))
        population = generate_new_population(population, fitness_scores)
    best_chromosome = population[np.argmin(fitness_scores)]
    return best_chromosome, best_fitness