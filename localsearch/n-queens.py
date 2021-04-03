import random
import math


def firstState(n):
    queensLoc = []
    for i in range(n):
        row = random.randint(0 , n-1)
        queensLoc.append(row)
    return queensLoc

def findNeighbors(queensLoc):
    neighbors = []
    for i in range(len(queensLoc)):
        for j in range(len(queensLoc)):
            temp = queensLoc.copy()
            temp[i] = j
            neighbors.append(temp)
    return neighbors

def stateCost(queensLoc):
    stateCost = 0
    for curColumn in range(len(queensLoc)):
        curRow = queensLoc[curColumn]
        for nextColumn in range(curColumn+1 , len(queensLoc)):
            nextRow = queensLoc[nextColumn]
            if nextRow == curRow :
                stateCost += 1
                continue
            if abs(nextColumn - curColumn) == abs(nextRow - curRow):
                stateCost += 1
                continue
        return stateCost

def findBestNeighbor(neighbors):
    bestNeighborCost = stateCost(neighbors[0])
    bestNeighbor = neighbors[0]
    for i in range(len(neighbors[0])):
        tempCost = stateCost(neighbors[i])
        if tempCost < bestNeighborCost:
            bestNeighborCost = tempCost
            bestNeighbor = neighbors[i]
    return bestNeighborCost , bestNeighbor

def hillAlgorithm(n):
    counter = 0
    startState = firstState(n)
    startStateCost = stateCost(startState)
    neighbors = findNeighbors(startState)
    bestNeighborCost , bestNeighbor = findBestNeighbor(neighbors)

    while bestNeighborCost < startStateCost:
        counter += 1
        startState = bestNeighbor
        startStateCost = bestNeighborCost
        neighbors = findNeighbors(startState)
        bestNeighborCost , bestNeighbor = findBestNeighbor(neighbors)
    return startStateCost , startState , counter

def scheduleFunc(temp = 100, scale = 1.01):
    # iter = 1
    new_temp = temp
    while True:
        new_temp = new_temp/scale
        # iter += 1
        yield new_temp

def simulatedAnnealingAlgorithm(n  , temp = 100):
    startState = firstState(n)
    startStateCost = stateCost( startState)
    iteration = 0
    for t in scheduleFunc(100 , 1.01):
        if iteration >= 1000 or t < 1e-6 :
            return startStateCost , startState
        iteration += 1
        neighbors = findNeighbors(startState)
        randomNeighbor = neighbors[random.randint(0 , len(neighbors) - 1)]
        randomNeighborCost = stateCost(randomNeighbor)

        delta_E = randomNeighborCost - startStateCost
        if delta_E < 0:
            startState = randomNeighbor
            startStateCost = randomNeighborCost
            continue
        else :
            p = math.exp((-delta_E)/t)
            randomFloat = random.random()
            if randomFloat <= p:
                startState = randomNeighbor
                startStateCost = randomNeighborCost
            continue

print(simulatedAnnealingAlgorithm(8))









