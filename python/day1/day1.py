def computeFuel(mass):
    return mass // 3 - 2

def totalFuel(mass):
    fuel = computeFuel(mass)
    if (fuel > 0):
        return fuel + totalFuel(fuel)
    else:
        return 0

def part1(data):
    return sum([computeFuel(mass) for mass in data])

def part2(data):
    return sum([totalFuel(mass) for mass in data])

def main():
    data = [int(line.strip()) for line in open('input.in').readlines()]
    print(part1(data))
    print(part2(data))

main()
