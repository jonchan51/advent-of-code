def extractValues(data, index):
    return data[index + 1], data[index + 2], data[index + 3]

def parseMode(instruction):
    opcode = instruction % 100
    mode1 = (instruction // 100) % 10
    mode2 = (instruction // 1000) % 10
    mode3 = (instruction // 10000) % 10
    return opcode, mode1, mode2, mode3

def getValue(data, mode, value):
    return value if mode else data[value]

def compute(data, index):
    opcode, mode1, mode2, mode3 = parseMode(data[index])
    value1, value2, value3 = extractValues(data, index)

    if (opcode == 1):
        data[value3] = getValue(data, mode1, value1) + getValue(data, mode2, value2)
        index += 4
    elif (opcode == 2):
        data[value3] = getValue(data, mode1, value1) * getValue(data, mode2, value2)
        index += 4
    elif (opcode == 3):
        data[value1] = int(input())
        index += 2
    elif (opcode == 4):
        print(getValue(data, mode1, value1))
        index += 2
    elif (opcode == 5):
        if (getValue(data, mode1, value1) != 0):
            index = getValue(data, mode2, value2)
        else:
            index += 3
        # jump if first is non-zero
    elif (opcode == 6):
        if (getValue(data, mode1, value1) == 0):
            index = getValue(data, mode2, value2)
        else:
            index += 3
        # jump if first is zero
    elif (opcode == 7):
        if (getValue(data, mode1, value1) < getValue(data, mode2, value2)):
            data[value3] = 1
        else:
            data[value3] = 0
        index += 4
        # store 1 in third param if first < second
    elif (opcode == 8):
        if (getValue(data, mode1, value1) == getValue(data, mode2, value2)):
            data[value3] = 1
        else:
            data[value3] = 0
        index += 4
        # store 1 in third param if first == second
    return opcode, index

def runIntCode(data):
    index = 0
    while (data[index] != 99):
        opcode, index = compute(data, index)
    return data

def part1(data):
    return runIntCode(data)

def main():
    data = [int(num.strip()) for num in open('input.in').read().split(',')]
    part1(data)

main()
