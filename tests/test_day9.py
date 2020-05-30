#! /usr/bin/python3


def test_day9_part1():
    """
    """
    from puzzles.day9 import day9_part1
    assert day9_part1() == 3507134798


def test_day9_part2():
    """
    """
    from puzzles.day9 import day9_part2
    assert day9_part2() == 84513


if __name__ == "__main__":
    test_day9_part1()
    test_day9_part2()