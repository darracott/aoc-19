#! /usr/bin/python3


# def test_module_fuel():
#     """
#     Get the fuel required for a module of given weight.
#     :param weight: int
#     """
#     from puzzle_day1 import module_fuel
#     assert module_fuel(1969) == 654
#     assert module_fuel(100756) == 33583


# def test_recursive_fuel():
#     """
#     Get the fuel required for the this fuel.
#     :param fuel: int: fuel weight, not a module weight.
#     """
#     from puzzle_day1 import recursive_fuel
#     assert recursive_fuel(2) == 2
#     assert recursive_fuel(654) == 966
#     assert recursive_fuel(33583) == 50346


def test_day2_part1():
    """
    The sum of the fuel requirements for all of the modules
    """
    from puzzle_day2 import day2_part1
    assert day2_part1() == 4462686


def test_day2_part2():
    """
    Modules require fuel, that fuel requires fuel,
    which requires fuel...

    We can ignore mass which requires negative fuel.

    Return all the fuel required.
    """
    from puzzle_day2 import day2_part2
    assert day2_part2() == 5936

if __name__ == "__main__":
    # test_module_fuel()
    # test_recursive_fuel()
    test_day2_part1()
    test_day2_part2()