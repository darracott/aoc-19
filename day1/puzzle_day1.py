#! /usr/bin/python3
import os


def load_input(day):
    """
    Loads the input file for the given day.
    :param day: int:
    """
    path = os.path.join(
        "./",
        f"day{day}",
        f"input_day{day}.txt"
    )
    with open(path) as _input:
        data = _input.readlines()
    return data


def module_fuel(weight):
    """
    Get the fuel required for a module of given weight.
    :param weight: int
    """
    return weight//3 - 2


def recursive_fuel(fuel):
    """
    Get the fuel required for the this fuel.
    :param fuel: int: fuel weight, not a module weight.
    """
    extra_fuel = max(0, module_fuel(fuel))
    if extra_fuel:
        extra_fuel = recursive_fuel(extra_fuel)
    # print(f"fuel: {fuel}, extra_fuel {extra_fuel}")
    return fuel + extra_fuel


def day1_part1():
    """
    The sum of the fuel requirements for all of the modules
    """
    data = load_input(1)
    modules = [int(line) for line in data]
    return sum([module_fuel(module) for module in modules])


def day1_part2():
    """
    Modules require fuel, that fuel requires fuel,
    which requires fuel...

    We can ignore mass which requires negative fuel.

    Return all the fuel required.
    """
    data = load_input(1)
    modules = [int(line) for line in data]
    module_fuels = [module_fuel(module) for module in modules]
    return sum([recursive_fuel(module_fuel) for module_fuel in module_fuels])


if __name__ == "__main__":
    print(f"Part 1: {day1_part1()}")
    print(f"Part 2: {day1_part2()}")
