from functools import reduce

class Decoder:
    def parse(image, width, height):
        """ single line image, the width and height in px, splits layers """
        layers = []
        for i in range(0, len(image), width * height):
            layer = image[i : i + width * height]
            layers.append(layer)

        for i in range(len(layers)):
            currentLayer = layers[i]
            rows = []
            for h in range(height):
                row = []
                for w in range(width):
                    row.append(int(currentLayer[h * width + w]))
                rows.append(row)
            layers[i] = rows
        return layers

    def decode(layers):
        height = len(layers[0])
        width = len(layers[0][0])
        output = []
        for h in range(height):
            row = []
            for w in range(width):
                for layer in layers:
                    if layer[h][w] != 2:
                        row.append(layer[h][w])
                        break
            output.append(row)
        return output

    def to_string(layer):
        res = ''
        for row in layer:
            str_row = reduce(lambda a, b: str(a) + str(b), row)
            res += str_row + '\n'
        return res

def get_fewest_zero(layers):
    count = 150
    res = []
    for layer in layers:
        cur_count = count_in_layer(layer, 0)
        if cur_count <= count:
            res = layer
            count = cur_count
    return res

def count_in_layer(layer, num):
    count = 0
    for row in layer:
        count += row.count(num)
    return count
    
def part1():
    with open('input.in') as data:
        image = data.read().strip()
        layers = Decoder.parse(image, 25, 6)
        fewestLayer = get_fewest_zero(layers)
        return count_in_layer(fewestLayer, 1) * count_in_layer(fewestLayer, 2)

def part1_test(image, width, height):
    return Decoder.parse(image, width, height)

def part2_test(image, width, height):
    layers = Decoder.parse(image, width, height)
    return Decoder.to_string(Decoder.decode(layers))

def part2():
    with open('input.in') as data:
        image = data.read().strip()
        layers = Decoder.parse(image, 25, 6)
        return Decoder.to_string(Decoder.decode(layers))

def main():
    assert part1_test('123456789012', 3, 2) == [[[1,2,3],[4,5,6]], [[7,8,9], [0,1,2]]]

    print(part1())

    assert part2_test('0222112222120000', 2, 2) == '01\n10\n'

    print(part2())

main()
