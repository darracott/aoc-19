#! /usr/bin/python3

from common.classes import IntCodeComputer
from common.functions import load_input


def intcode(_input, noun, verb):
    _intcode = list(_input)
    _intcode[1] = noun
    _intcode[2] = verb
    return _intcode


def day2_part1(_input):
    """
    What value is left at position 0 after the program halts?
    """
    my_intcode_computer = IntCodeComputer(intcode(_input, 12, 2))
    my_intcode_computer.run()
    return my_intcode_computer.memory[0]


def day2_part2(_input, target=19690720):
    """
    Find the input noun and verb that cause the program to
    produce the output target 19690720.
    What is 100 * noun + verb?
    """
    for noun in range(99):
        for verb in range(99):
            my_intcode_computer = IntCodeComputer(intcode(_input, noun, verb))
            my_intcode_computer.run()
            if my_intcode_computer.memory[0] == target:
                return 100 * noun + verb


if __name__ == "__main__":
    _input = load_input(2)
    print(f"Day 2, Part 1: {day2_part1(_input)}")
    print(f"Day 2, Part 2: {day2_part2(_input)}")