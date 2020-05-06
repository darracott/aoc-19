# /usr/bin/python3
import os
import sys
sys.path.append("C:\\Users\\joe-p\\aoc_19")

from day1.puzzle_day1 import load_input

INPUT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,2,27,13,31,1,10,31,35,1,10,35,39,2,39,6,43,1,43,5,47,2,10,47,51,1,5,51,55,1,55,13,59,1,59,9,63,2,9,63,67,1,6,67,71,1,71,13,75,1,75,10,79,1,5,79,83,1,10,83,87,1,5,87,91,1,91,9,95,2,13,95,99,1,5,99,103,2,103,9,107,1,5,107,111,2,111,9,115,1,115,6,119,2,13,119,123,1,123,5,127,1,127,9,131,1,131,10,135,1,13,135,139,2,9,139,143,1,5,143,147,1,13,147,151,1,151,2,155,1,10,155,0,99,2,14,0,0]  # noqa
KNOWN_OPCODES = [1, 2, 3, 4, 5, 6, 7, 8, 99]
KNOWN_MODES = [0, 1]

TEST = [3,225,1,225,6,6,1100,1,238,225,104,0,1002,148,28,224,1001,224,-672,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,8,21,225,1102,13,10,225,1102,21,10,225,1102,6,14,225,1102,94,17,225,1,40,173,224,1001,224,-90,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,2,35,44,224,101,-80,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,26,94,224,101,-120,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1001,52,70,224,101,-87,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,16,92,225,1101,59,24,225,102,83,48,224,101,-1162,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,80,10,225,101,5,143,224,1001,224,-21,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1102,94,67,224,101,-6298,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,102,2,223,223,1005,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,359,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,374,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,419,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,449,1001,223,1,223,8,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,479,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,554,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,614,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

# TODO: sort out loading inputs
# TODO: make debug mode
# TODO: add tests
# TODO: sort out directory structure;
# add a comm folder and ship this class into it
# along with other helpful functions.
# google about good python package structures because this 
# sibling directory stuff is BS.




def intcode(noun, verb):
    _input = list(INPUT)
    _input[1] = noun
    _input[2] = verb
    return _input


class IntCodeComputer(object):
    """
    Computes IntCode programs.
    """
    def __init__(self, intcode):
        self.memory = intcode
        self.instruction_pointer = 0
        self.running = False
        self.known_opcodes = KNOWN_OPCODES
        self.known_modes = KNOWN_MODES
    
    def retrieve_value(self, parameter, mode):
        """
        Get the value from 
        """
        if mode == 0:
            # Position mode.
            return self.memory[parameter]
        elif mode == 1:
            # Immediate mode.
            return parameter
        else:
            print(f"Unknown parameter mode: {mode}")

    def step_forward(self):
        opcode = self.memory[self.instruction_pointer]
        # print(f"input opcode: {opcode}")

        # Parse opcode and parameter modes.
        digits = [digit for digit in str(opcode)]
        # print(f"digits: {digits}")

        opcode = int("".join(digits[-2:]))
        # print(f"actual opcode: {opcode}")

        parameter_modes = [ int(mode) for mode in digits[-3::-1] ]
        # print(f"parameter_modes: {parameter_modes}")

        # Check we've got a good Opcode.
        if opcode not in self.known_opcodes:
            print(f"Unknown opcode: {opcode}")
            self.running = False

        # Run the instruction.
        if parameter_modes:
            self.__getattribute__(f"opcode{opcode}")(*parameter_modes)
        else:
            self.__getattribute__(f"opcode{opcode}")()


    def run(self):
        self.running = True
        while self.running:
            # print(self.memory[:12])
            self.step_forward()

    def opcode1(self, mode_a=0, mode_b=0, mode_c=0):
        """
        Adds the values from addresses a and b.
        Writes this sum to address c.
        """
        # print(f"running 1 with {[mode_a, mode_b,mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.memory[c] = self.retrieve_value(a, mode_a) + self.retrieve_value(b, mode_b)
        self.instruction_pointer += 4

    def opcode2(self, mode_a=0, mode_b=0, mode_c=0):
        """
        Multiplies the values from addresses a and b.
        Writes this sum to address c.
        """
        # print(f"running 2 with {[mode_a, mode_b,mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.memory[c] = self.retrieve_value(a, mode_a) * self.retrieve_value(b, mode_b)
        self.instruction_pointer += 4
    
    def opcode3(self, mode_a=0):
        """
        Takes a single integer as input and
        saves it to the address x.

        :param input: An integer
        """
        _input = input("Input required: ")
        try:
            _input = int(_input) 
        except ValueError as e:
            print("ERROR: Opcode 3 only takes an integer as input.")
            raise(e)

        a = self.memory[self.instruction_pointer + 1]
        self.memory[a] = _input
        self.instruction_pointer += 2

    def opcode4(self, mode_a=0):
        """
        Takes a single integer as input and
        saves it to the address a.
        """
        a = self.memory[self.instruction_pointer + 1]
        output = self.retrieve_value(a, mode_a) 
        self.instruction_pointer += 2
        print(f"Opcode4 output: {output}")
        # look up a Dqueue
        return output
    
    def opcode5(self, mode_a=0, mode_b=0):
        """
        If the first parameter is non-zero, set the instruction pointer
        to the value from the second parameter. 
        Otherwise, do nothing.
        """
        # print(f"running 5 with {[mode_a, mode_b]}")
        a = self.memory[self.instruction_pointer + 1]
        if self.retrieve_value(a, mode_a):
            b = self.memory[self.instruction_pointer + 2]
            self.instruction_pointer = self.retrieve_value(b, mode_b)
        else:
            self.instruction_pointer += 3
    
    def opcode6(self, mode_a=0, mode_b=0):
        """
        If the first parameter is zero, set the instruction pointer
        to the value from the second parameter. 
        Otherwise, do nothing.
        """
        # print(f"running 6 with {[mode_a, mode_b]}")
        a = self.memory[self.instruction_pointer + 1]
        if self.retrieve_value(a, mode_a) == 0:
            b = self.memory[self.instruction_pointer + 2]
            self.instruction_pointer = self.retrieve_value(b, mode_b)
        else:
            self.instruction_pointer += 3
    
    def opcode7(self, mode_a=0, mode_b=0, mode_c=0):
        """
        If the first parameter is less than the second parameter,
        store 1 in the position given by the third parameter. 
        Otherwise, store 0.
        """
        # print(f"running 7 with {[mode_a, mode_b, mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        if self.retrieve_value(a, mode_a) < self.retrieve_value(b, mode_b):
            self.memory[c] = 1
        else:
            self.memory[c] = 0
        self.instruction_pointer += 4
    
    def opcode8(self, mode_a=0, mode_b=0, mode_c=0):
        """
        If the first parameter is equal to the second parameter,
        store 1 in the position given by the third parameter. 
        Otherwise, store 0.
        """
        # print(f"running 8 with {[mode_a, mode_b, mode_c]}")
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        if self.retrieve_value(a, mode_a) == self.retrieve_value(b, mode_b):
            self.memory[c] = 1
        else:
            self.memory[c] = 0
        self.instruction_pointer += 4

    def opcode99(self):
        """
        Stop running.
        """
        self.running = False


def day2_part1():
    """
    What value is left at position 0 after the program halts?
    """
    my_intcode_computer = IntCodeComputer(intcode(12, 2))
    my_intcode_computer.run()
    return my_intcode_computer.memory[0]


def day2_part2(target=None):
    """
    Find the input noun and verb that cause the program to
    produce the output target 19690720. 
    What is 100 * noun + verb?
    """
    if not target:
        target = 19690720
    for noun in range(99):
        for verb in range(99):
            my_intcode_computer = IntCodeComputer(intcode(noun, verb))
            my_intcode_computer.run()
            if my_intcode_computer.memory[0] == target:
                return 100 * noun + verb


if __name__ == "__main__":
    # my_intcode = load_input(2)
    # print(my_intcode)
    # print(day2_part1())
    # print(day2_part2())

    day5computer = IntCodeComputer(TEST)
    day5computer.run()
