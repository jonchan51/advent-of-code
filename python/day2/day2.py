def extractIndices(data, index):
    return data[index + 1], data[index + 2], data[index + 3]

def compute(data, index):
    if (data[index] == 1):
        index1, index2, index3 = extractIndices(data, index)
        data[index3] = data[index1] + data[index2]
    elif (data[index] == 2):
        index1, index2, index3 = extractIndices(data, index)
        data[index3] = data[index1] * data[index2]

def runIntCode(data, i, j):
    data[1] = i
    data[2] = j
    index = 0
    while (data[index] != 99):
        compute(data, index)
        index += 4
    return data

def part1(data):
    return runIntCode(data, 12, 2)

def part2(data):
    for i in range(0, 100):
        for j in range(0, 100):
            if (runIntCode(data.copy(), i, j)[0] == 19690720):
                return i * 100 + j

def main():
    data = [int(num.strip()) for num in open('input.in').read().split(',')]
    print(part1(data.copy())[0])
    print(part2(data.copy()))

main()
