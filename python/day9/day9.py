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
    RELATIVE_OFFSET = 9
    EXIT = 99

class MODE:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class STATE:
    RUNNING = 'running'
    WAITING = 'waiting'
    HALTED = 'halted'

class Memory(dict):
    def __missing__(self, key):
        return 0

class Computer:
    def __init__(self, mem, inputs):
        self.setup_mem(mem)
        self.pc = 0
        self.inputs = inputs.copy()
        self.outputs = []
        self.state = STATE.RUNNING
        self.relative_base = 0
    
    def setup_mem(self, mem):
        self.mem = Memory()
        for i in range(len(mem)):
            self.mem[i] = mem[i]

    def get_instruction(self):
        return self.mem[self.pc] % 100

    def get_parameter_mode(self, relative_position):
        return self.mem[self.pc] // (10**(2 + relative_position - 1)) % 10 

    def get_immediate_at(self, relative_position):
        return self.mem[self.pc + relative_position]

    def get_position_at(self, relative_position, is_relative=False):
        rel_offset = self.relative_base if is_relative else 0
        return self.mem[rel_offset + self.mem[self.pc + relative_position]]

    def get_value_for(self, relative_position):
        mode = self.get_parameter_mode(relative_position)
        if mode == MODE.POSITION:
            return self.get_position_at(relative_position)
        elif mode == MODE.IMMEDIATE:
            return self.get_immediate_at(relative_position)
        elif mode == MODE.RELATIVE:
            return self.get_position_at(relative_position, True)
        else:
            raise ValueError("Invalid mode")
    
    def set_value_for(self, relative_position, value):
        mode = self.get_parameter_mode(relative_position)
        if mode == MODE.POSITION:
            self.mem[self.get_immediate_at(relative_position)] = value
        elif mode == MODE.RELATIVE:
            self.mem[self.relative_base 
                + self.get_immediate_at(relative_position)] = value
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
                self.set_value_for(3, param1 + param2)
                self.pc += 4

            elif instruction == OP.MUL:
                param1 = self.get_value_for(1)
                param2 = self.get_value_for(2)
                self.set_value_for(3, param1 * param2)
                self.pc += 4

            elif instruction == OP.INPUT:
                # self.mem[self.get_immediate_at(1)] = int(input())
                if len(self.inputs) == 0:
                    self.state = STATE.WAITING
                    break
                self.set_value_for(1, self.inputs.pop(0))
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
                    self.set_value_for(3, 1)
                else:
                    self.set_value_for(3, 0)
                self.pc += 4

            elif instruction == OP.EQUALS:
                if self.get_value_for(1) == self.get_value_for(2):
                    self.set_value_for(3, 1)
                else:
                    self.set_value_for(3, 0)
                self.pc += 4

            elif instruction == OP.RELATIVE_OFFSET:
                self.relative_base += self.get_value_for(1)
                self.pc += 2

            elif instruction == OP.EXIT:
                self.state = STATE.HALTED
                break

            else:
                raise ValueError("Invalid Instruction: " + str(instruction))
        return self.outputs

def part1_test():
    test1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert Computer(test1, []).run() == test1

    test2 = [1102,34915192,34915192,7,4,7,99,0]
    assert Computer(test2, []).run() == [1219070632396864]

    test3 = [104,1125899906842624,99]
    assert Computer(test3, []).run() == [1125899906842624]

def part1():
    with open('input.in') as input_file:
        mem = [int(num.strip()) for num in input_file.read().split(',')]
        print(Computer(mem, [1]).run())

def part2():
    with open('input.in') as input_file:
        mem = [int(num.strip()) for num in input_file.read().split(',')]
        print(Computer(mem, [2]).run())

def main():
    part1_test()
    part1()
    part2()

main()
        
