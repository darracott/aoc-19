# /usr/bin/python3
import os
import sys
sys.path.append("C:\\Users\\joe-p\\aoc_19")
print(sys.path)

from ..day1.puzzle_day1 import load_input

INPUT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,2,27,13,31,1,10,31,35,1,10,35,39,2,39,6,43,1,43,5,47,2,10,47,51,1,5,51,55,1,55,13,59,1,59,9,63,2,9,63,67,1,6,67,71,1,71,13,75,1,75,10,79,1,5,79,83,1,10,83,87,1,5,87,91,1,91,9,95,2,13,95,99,1,5,99,103,2,103,9,107,1,5,107,111,2,111,9,115,1,115,6,119,2,13,119,123,1,123,5,127,1,127,9,131,1,131,10,135,1,13,135,139,2,9,139,143,1,5,143,147,1,13,147,151,1,151,2,155,1,10,155,0,99,2,14,0,0]  # noqa
KNOWN_OPCODES = [1, 2, 99]


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

    def step_forward(self):
        opcode = self.memory[self.instruction_pointer]

        # Check we've got a good Opcode.
        if opcode not in self.known_opcodes:
            print(f"Unknown opcode {opcode}")
            self.running = False

        # Run the instruction.
        self.__getattribute__(f"opcode{opcode}")()

    def run(self):
        self.running = True
        while self.running:
            self.step_forward()

    def opcode1(self):
        """
        Adds the values from addresses a and b.
        Writes this sum to address c.
        """
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.memory[c] = self.memory[a] + self.memory[b]
        self.instruction_pointer += 4

    def opcode2(self):
        """
        Multiplies the values from addresses a and b.
        Writes this sum to address c.
        """
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.memory[c] = self.memory[a] * self.memory[b] 
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
    my_intcode = load_input(2)
    print(my_intcode)
    print(day2_part1())
    print(day2_part2())
