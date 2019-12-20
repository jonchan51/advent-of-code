def getDirection(instruction):
    direction = instruction[0:1]
    if (direction == 'L'):
        return (1, 0)
    elif (direction == 'R'):
        return (-1, 0)
    elif (direction == 'U'):
        return (0, 1)
    elif (direction == 'D'):
        return (0, -1)
    raise ValueError()

def getDistance(instruction):
    return int(instruction[1:])

def getTouched(path):
    prev = (0, 0)
    touched = set()
    steps = {}
    numSteps = 0
    for instruction in path:
        direction = getDirection(instruction)
        distance = getDistance(instruction)
        for i in range(0, distance):
            prev = (prev[0] + direction[0], prev[1] + direction[1])
            numSteps += 1
            if (prev not in touched):
                steps[prev] = numSteps
                touched.add(prev)
    return touched, steps

def part1(data):
    set1, _ = getTouched(data[0])
    set2, _ = getTouched(data[1])
    intersections = map(lambda intersect: abs(intersect[0]) + abs(intersect[1]), set1 & set2)
    return min(intersections)

def part2(data):
    set1, steps1 = getTouched(data[0])
    set2, steps2 = getTouched(data[1])
    distances = map(lambda intersect: steps1[intersect] + steps2[intersect], set1 & set2)
    return min(distances)
    
def main():
    data = [line.split(',') for line in open('input.in').readlines()]
    print(part1(data))
    print(part2(data))

main()
