from itertools import permutations

# DEBUG = True
DEBUG = False

class OP:
    ADD = 1
    MUL = 2
    INPUT = 3
    PRINT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    EXIT = 99

class MODE:
    POSITION = 0
    IMMEDIATE = 1

class STATE:
    RUNNING = 'running'
    WAITING = 'waiting'
    HALTED = 'halted'

class Computer:
    def __init__(self, mem, inputs):
        self.mem = mem.copy()
        self.pc = 0
        self.inputs = inputs.copy()
        self.outputs = []
        self.state = STATE.RUNNING

    def get_instruction(self):
        return self.mem[self.pc] % 100

    def get_parameter_mode(self, relative_position):
        return self.mem[self.pc] // (10**(2 + relative_position - 1)) % 10 

    def get_immediate_at(self, relative_position):
        return self.mem[self.pc + relative_position]

    def get_position_at(self, relative_position):
        return self.mem[self.mem[self.pc + relative_position]]

    def get_value_for(self, relative_position):
        mode = self.get_parameter_mode(relative_position)
        if (mode == MODE.POSITION):
            return self.get_position_at(relative_position)
        elif (mode == MODE.IMMEDIATE):
            return self.get_immediate_at(relative_position)
        else:
            raise ValueError("Invalid mode")

    def input_signal(self, signal):
        self.inputs.append(signal)

    def debug(self, info):
        if DEBUG:
            print(info)

    def run(self):
        self.state = STATE.RUNNING
        while True:
            instruction = self.get_instruction()
            if instruction == OP.ADD:
                param1 = self.get_value_for(1)
                param2 = self.get_value_for(2)
                self.mem[self.get_immediate_at(3)] = param1 + param2
                self.pc += 4

            elif instruction == OP.MUL:
                param1 = self.get_value_for(1)
                param2 = self.get_value_for(2)
                self.mem[self.get_immediate_at(3)] = param1 * param2
                self.pc += 4

            elif instruction == OP.INPUT:
                # self.mem[self.get_immediate_at(1)] = int(input())
                if len(self.inputs) == 0:
                    self.state = STATE.WAITING
                    break
                self.mem[self.get_immediate_at(1)] = self.inputs.pop(0)
                self.pc += 2

            elif instruction == OP.PRINT:
                # print(self.get_value_for(1))
                self.debug(f"Print: {self.get_value_for(1)}")
                self.outputs.append(self.get_value_for(1))
                self.pc += 2

            elif instruction == OP.JUMP_IF_TRUE:
                if self.get_value_for(1) != 0:
                    self.pc = self.get_value_for(2)
                else:
                    self.pc += 3

            elif instruction == OP.JUMP_IF_FALSE:
                if self.get_value_for(1) == 0:
                    self.pc = self.get_value_for(2)
                else:
                    self.pc += 3
                
            elif instruction == OP.LESS_THAN:
                if self.get_value_for(1) < self.get_value_for(2):
                    self.mem[self.get_immediate_at(3)] = 1
                else:
                    self.mem[self.get_immediate_at(3)] = 0
                self.pc += 4

            elif instruction == OP.EQUALS:
                if self.get_value_for(1) == self.get_value_for(2):
                    self.mem[self.get_immediate_at(3)] = 1
                else:
                    self.mem[self.get_immediate_at(3)] = 0
                self.pc += 4

            elif instruction == OP.EXIT:
                self.state = STATE.HALTED
                break

            else:
                raise ValueError("Invalid Instruction: " + str(instruction))
        return self.outputs

def amplify(mem, settings):
    input_signal = 0
    for setting in settings:
        outputs = Computer(mem, [setting, input_signal]).run().copy()
        input_signal = outputs[0]
    return outputs[0]

def part1():
    mem = [int(num.strip()) for num in open('input.in').read().split(',')]
    res = 0
    for perm in permutations([0,1,2,3,4]):
        res = max(res,amplify(mem, perm))
    return res

def part1_test(file_name, settings):
    mem = [int(num.strip()) for num in open(file_name).read().split(',')]
    return amplify(mem, settings)

def feedback_loop(mem, settings):
    computers = []
    for setting in settings:
        computers.append(Computer(mem, [setting]))
    signal = 0
    while computers[-1].state != STATE.HALTED:
        for com in computers:
            com.input_signal(signal)
            outputs = com.run()
            signal = outputs[-1]
    return signal

def part2_test(file_name, settings):
    mem = [int(num.strip()) for num in open(file_name).read().split(',')]
    return feedback_loop(mem, settings)

def part2():
    mem = [int(num.strip()) for num in open('input.in').read().split(',')]
    res = 0
    for setting in permutations([5,6,7,8,9]):
        res = max(res, feedback_loop(mem, setting))
    return res


def main():
    assert part1_test('test1.in', [4,3,2,1,0]) == 43210
    assert part1_test('test2.in', [0,1,2,3,4]) == 54321
    assert part1_test('test3.in', [1,0,4,3,2]) == 65210

    print(part1())

    assert part2_test('test4.in', [9,8,7,6,5]) == 139629729
    assert part2_test('test5.in', [9,7,8,5,6]) == 18216
    
    print(part2())
    

main()
        
