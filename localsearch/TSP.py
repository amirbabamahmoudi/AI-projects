import random
import time
import math

def generateRandomSolotion(citiesMatrix):
    cities_name = [*range(0 , len(citiesMatrix) , 1)]
    answer = []
    for i in range(len(citiesMatrix)):
        rCity = cities_name[random.randint(0 , len(cities_name) - 1)]
        answer.append(rCity)
        cities_name.remove(rCity)
    return answer


def stateCost(citiesMatrix , answer):
    stateCost = 0
    for i in range(len(answer)):
        stateCost += citiesMatrix[answer[i-1]][answer[i]]
    return stateCost

def neighborStates(answer):
    neighbors = []
    for i in range(len(answer)):
        for j in range(len(answer)):
            copy = answer.copy()
            copy[i] , copy[j] = copy[j] , copy[i]
            neighbors.append(copy)
    return neighbors


def findBestNeighbor(citiesMatrix, neighbors):
    bestNeighborCost = stateCost(citiesMatrix , neighbors[0])
    bestNeighbor = neighbors[0]
    for i in range(len(neighbors)):
        temp = stateCost(citiesMatrix , neighbors[i])
        if temp < bestNeighborCost:
            bestNeighborCost = temp
            bestNeighbor = neighbors[i]
    return bestNeighborCost , bestNeighbor


def hillAlgorithm(citiesMatrix):
    counter = 0 
    startState = generateRandomSolotion(citiesMatrix)
    startStateCost = stateCost(citiesMatrix , startState)
    neighbors = neighborStates(startState)
    bestNeighborCost , bestNeighbor = findBestNeighbor(citiesMatrix , neighbors)

    while bestNeighborCost < startStateCost:
        counter += 1
        startState = bestNeighbor
        startStateCost = bestNeighborCost
        neighbors = neighborStates(startState)
        bestNeighborCost , bestNeighbor = findBestNeighbor(citiesMatrix , neighbors)

    return startStateCost , startState , counter 

def scheduleFunc(temp = 100, scale = 1.01):
    # iter = 1
    new_temp = temp
    while True:
        new_temp = new_temp/scale
        # iter += 1
        yield new_temp

def simulatedAnnealingAlgorithm(citiesMatrix , schedule = scheduleFunc() , temp = 100):
    counter = 0
    startState = generateRandomSolotion(citiesMatrix)
    startStateCost = stateCost(citiesMatrix , startState)
    iteration = 0
    for t in scheduleFunc(100 , 1.01):
        if iteration >= 1000 or t < 1e-6 :
            return startStateCost , startState , counter
        iteration += 1
        neighbors = neighborStates(startState)
        randomNeighbor = neighbors[random.randint(0 , len(neighbors) - 1)]
        randomNeighborCost = stateCost(citiesMatrix, randomNeighbor)

        delta_E = randomNeighborCost - startStateCost
        if delta_E < 0:
            startState = randomNeighbor
            startStateCost = randomNeighborCost
            counter += 1
            continue
        else :
            p = math.exp((-delta_E)/t)
            randomFloat = random.random()
            if randomFloat <= p:
                startState = randomNeighbor
                startStateCost = randomNeighborCost
                counter += 1
            continue
        


def problemGenerator(nCities):
    tsp = []
    for i in range(nCities):
        distances = []
        for j in range(nCities):
            if j == i:
                distances.append(0)
            elif j < i:
                distances.append(tsp[j][i])
            else:
                distances.append(random.randint(10, 1000))
        tsp.append(distances)
    return tsp



hilltime = []
hillgere = []
hillcount = 0
simulecount = 0
for i in range(20):
    starthill = time.time()
    citiesMatrix = problemGenerator(20)
    hill = hillAlgorithm(citiesMatrix)[0]
    simule = simulatedAnnealingAlgorithm(citiesMatrix)[0]
    if hill > simule :
        hillcount += 1
    elif simule > hill :
        simulecount += 1
   # hilltime.append(time.time() - starthill)
   # hillgere.append(simulatedAnnealingAlgorithm(citiesMatrix)[2])
#meantimehill = sum(hilltime)/len(hilltime)
#meangerehill = sum(hillgere)/len(hillgere)
#print(meangerehill , meantimehill*1000)
print(hillcount , simulecount)

