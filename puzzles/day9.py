from common.functions import load_input
from common.classes import IntCodeComputer


def day9_part1():
    """
    Run test intcode.
    """
    data = load_input(9)[0].strip()
    intcode = [int(x) for x in data.split(",")]
    boost_computer = IntCodeComputer(intcode=intcode, additional_memory=10**2)
    # Run in Test mode by providing input 1.
    boost_computer.queue_input(1)
    boost_computer.run()
    return boost_computer.outputs[0]


def day9_part2():
    """
    Run test intcode.
    """
    data = load_input(9)[0].strip()
    intcode = [int(x) for x in data.split(",")]
    boost_computer = IntCodeComputer(intcode=intcode, additional_memory=10**3)
    # Run in some mode by providing input 2.
    boost_computer.queue_input(2)
    boost_computer.run()
    return boost_computer.outputs[0]


if __name__ == "__main__":
    print(f"9 part 1: {day9_part1()}")
    print(f"9 part 2: {day9_part2()}")