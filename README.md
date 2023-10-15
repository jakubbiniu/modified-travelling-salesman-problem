# modified-travelling-salesman-problem
language used: python
### Introduction
The Travelling Salesman Problem involves finding the minimum Hamiltonian cycle in a complete weighted graph. 
It is an optimisation problem and belongs to the group of NP-hard problems. 
The history of this problem dates back to the 19th century and was formally formulated by Austrian mathematician Karl Menger in 1930. 
Merrill Flood also attempted to solve this problem by wanting to determine routes for school buses.
The problem is computationally difficult despite its simple description.
### Description and modifications
While in the classical comoving problem we are looking for a minimal Hamiltonian cycle, where each edge has one weight,
so in the modification used, we will add a second weight to each edge and also assign a number to each vertex.
This will allow us to optimise the journey in the following interpetation. Each vertex is a city in which there is a tankless station.
The amount of fuel that can be refuelled at most is described by the number assigned to the vertex. 
The edges, in turn, are the roads connecting the cities, where the numbers assigned to them represent the distance and the fuel burned by the car. 
The car has a specific tank capacity and always starts the journey when fully fueled.
Two approaches are used: in the first, we optimise the distance so that it is as short as possible and so that there is enough fuel, 
in the second, we optimise both the distance (which we care most about) and the fuel so that the value of the expression 2⋅distance+fuel is as small as possible.
Three algorithms were used to solve the problem: the exact (//brute force//) algorithm (we check each permutation and choose the one with the optimal value of the distance travelled),
a greedy algorithm, which for each vertex selects the next one according to a specified criterion, and a genetic algorithm.
### Implementation
The algorithms were implemented in Python and the graphs were implemented using neighbourhood matrices. 
Two n x n matrices were randomly generated: the ''distance'' matrix describes the distances between cities, the ''fuel'' the fuel burned while driving between cities.
In addition, a random ''station'' vector describing how much can be refuelled at each of the n vertices. 
The ranges of values of the numbers drawn into the matrix or vector containing the refuelling information can also be controlled with appropriate parameters.
The libraries used were random, itertools, numpy, matplotlib, and networkx.
### meaning of variables
  * n - number of cities
  * capacity - tank capacity
  * fuel - matrix containing fuel consumption
  * station - vector informing how much fuel can be refuelled
  * distance - matrix containing distances between cities
  * fuel_lb - lower limit of numbers in fuel matrix
  * fuel_ub - upper limit of the numbers in the fuel matrix
  * station_lb - lower limit of numbers in station vector
  * station_ub - upper limit of the numbers in the station vector
  * distance_lb - lower limit of numbers in distance matrix
  * distance_ub - upper limit of the numbers in the distance matrix
### Brute force algorithm
This algorithm generates all possible permutations of the order in which the vertices are visited, 
and then checks which of them will generate the smallest distance travelled while assuming that we will not run out of fuel. 
Thus, at each vertex in the permutation, we check whether, after refuelling, there is enough unrefuelled gasoline to reach the next town, and if so, we continue driving by adding the distance covered
This algorithm has a complexity of O(n!), since that is how many permutations we are able to generate having n vertices.
In algorithms.py there is the exact algorithm (brute force) in 2 versions: optimising the road, optimising the expression 2⋅road+fuel.
### Greedy algorithm - nearest neighbour algorithm in modified version
Here it is assumed that we start with a randomly selected vertex. Then we choose the vertex with the smallest positive quotient of the expression: distance to the next/(fuel to be refuelled in the next - fuel burnt)
When all quotients are negative we choose the one with the smallest absolute value. Its complexity is O(n²).
In algorithms.py there is the greedy algorithm in 2 versions: optimisation of the road, optimisation of the expression 2-road+fuel.
### Genetic algorithm
This algorithm is a genetic algorithm for solving a Traveling Salesman Problem (TSP) with fuel consumption. It involves several functions:

* fitness(chromosome): Calculates the fitness score for a solution.
* selection(pop, fitness): Selects two chromosomes based on their fitness.
* crossover(parent1, parent2): Combines two parents to create a child.
* mutation(chromosome): Introduces randomness by swapping two genes.
* generate_new_population(pop, fitness): Creates a new population using selection, crossover, and mutation.
* genetic_algorithm(population): Iteratively evolves the population to find the best solution and returns it along with a history of best fitness scores.
### Example
Below the example of graph:

![Figure_1](https://github.com/jakubbiniu/modified-travelling-salesman-problem/assets/101418523/047d95a5-b076-4675-b847-4ee13ebbac72)


The solution from brute force: 19 [3, 2, 1, 0]

The solution from greedy algorithm: 22 [2, 0, 3, 1]
### Accuracy
The exact algorithm (brute force) will always find the optimal solution, but due to its high computational complexity it can only be used with small graphs.
The greedy algorithm, on the other hand, can be used with larger data. The accuracy of the algorithm is therefore crucial. 
For the optimisation of the path alone with 100 measurements, the average value of the expression l/b is 2.03, where b is the result of the exact algorithm (brute force) and l is the result of the greedy algorithm. 
In contrast, for the optimisation of the expression 2⋅road+fuel, the average l/b is 1.43, so in this case the result of the greedy algorithm is less far from the optimum.
In contrast, the genetic algorithm is even more precise, with an accuracy of 1.20. 
### Files
Description of files in repo:
* data.json - data in json file
* data_generating.py - generating of example data
* reading_from_json.py - loading data from json file
* algorithms.py - brute force and greedy algorithm in two versions
* genetic_algorithm.py - genetic algorithm
* graph_visualisation.py - code which generates a simple visualisation of given graph
