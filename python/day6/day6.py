import queue

def getOrbiting(orbitData):
    return orbitData[0]

def getOrbitedBy(orbitData):
    return orbitData[1]

def addToOrbiting(orbitData, planet):
    getOrbiting(orbitData).append(planet)

def addToOrbitedBy(orbitData, planet):
    getOrbitedBy(orbitData).append(planet)

def addOrbitConnection(orbitMap, orbitedPlanet, orbitingPlanet):
    if (orbitedPlanet not in orbitMap):
        orbitMap[orbitedPlanet] = [[], []]
    if (orbitingPlanet not in orbitMap):
        orbitMap[orbitingPlanet] = [[], []]
    addToOrbiting(orbitMap[orbitingPlanet], orbitedPlanet)
    addToOrbitedBy(orbitMap[orbitedPlanet], orbitingPlanet)

def parseData(data):
    orbitMap = {}
    for orbit in data:
        orbited, orbiter = orbit.split(')')
        addOrbitConnection(orbitMap, orbited, orbiter)
    return orbitMap

def computeOrbits(orbitMap, planet, memo):
    if (planet in memo):
        return memo[planet]
    if (planet not in orbitMap):
        return 0
    numOrbits = len(getOrbiting(orbitMap[planet]))
    for other in getOrbiting(orbitMap[planet]):
        numOrbits += computeOrbits(orbitMap, other, memo)
    return numOrbits

def part1(orbitMap):
    memo = {}
    totalOrbits = 0
    for planet in orbitMap:
        totalOrbits += computeOrbits(orbitMap, planet, memo)
    return totalOrbits

def part2(orbitMap):
    q = queue.Queue()
    q.put(('YOU', -1))
    visited = set()
    visited.add('YOU')
    while (not q.empty()):
        currPlanet, currDist = q.get()
        for planet in getOrbiting(orbitMap[currPlanet]):
            if (planet in visited):
                continue
            q.put((planet, currDist + 1))
            visited.add(planet)
        for planet in getOrbitedBy(orbitMap[currPlanet]):
            if (planet in visited):
                continue
            if (planet == 'SAN'):
                return currDist
            q.put((planet, currDist + 1))
            visited.add(planet)

def main():
    data = [line.strip() for line in open('input.in').readlines()]
    parsedData = parseData(data)
    print(part1(parsedData))
    print(part2(parsedData))

main()
