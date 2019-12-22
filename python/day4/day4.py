
def twoAdjacent(number):
    num = number
    while (num > 0):
        firstDigit = num % 10
        secondDigit = (num // 10) % 10
        if (firstDigit == secondDigit):
            return True
        num //= 10
    return False

def twoAdjacentOnly(number):
    num = number
    freq = {}
    while (num > 0):
        firstDigit = num % 10
        secondDigit = (num // 10) % 10
        if (firstDigit == secondDigit):
            if (firstDigit in freq):
                freq[firstDigit] += 1
            else:
                freq[firstDigit] = 1
        num //= 10
    for digit in freq:
        if freq[digit] == 1:
            return True
    return False

def neverDecreasing(number):
    num = number
    last = 9
    while (num > 0):
        current = num % 10
        if (last < current):
            return False
        last = current
        num //= 10
    return True
    

def part1(lower, higher):
    count = 0
    for i in range(lower, higher + 1):
        if (twoAdjacent(i) and neverDecreasing(i)):
            count += 1
    return count

def part2(lower, higher):
    count = 0
    for i in range(lower, higher + 1):
        if (twoAdjacentOnly(i) and neverDecreasing(i)):
            count += 1
    return count

def main():
    lower = 245183
    higher = 790572
    print(part1(lower, higher))
    print(part2(lower, higher))

main()
