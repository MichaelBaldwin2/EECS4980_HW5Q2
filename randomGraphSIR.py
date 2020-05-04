from random import randrange
import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnp_random_graph(10000, 0.0005)
initialCarrier = randrange(10000)
infectedNodes = [initialCarrier]
recoveredNodes = []
healthyCountList = [10000]
infectedCountList = [1]
recoveredCountList = [0]

while len(infectedNodes) > 0:
    newInfected = []
    for n in infectedNodes:
        neighbors = nx.neighbors(G, n)
        for a in neighbors:
            if a not in recoveredNodes and a not in newInfected:
                prob = randrange(100)
                if prob < 40:
                    newInfected.append(a)
    print("new infections: " + str(len(newInfected)))
    infectedCountList.append(len(newInfected))
    recoveredCountList.append(recoveredCountList[-1] + len(infectedNodes))
    healthyCountList.append(10000 - infectedCountList[-1] - recoveredCountList[-1])
    recoveredNodes.extend(infectedNodes)
    infectedNodes.clear()
    infectedNodes.extend(newInfected)

plt.plot(infectedCountList, 'go')
plt.plot(recoveredCountList, 'bo')
plt.plot(healthyCountList, 'yo')
plt.show()
