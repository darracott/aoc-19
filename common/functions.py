"""Useful functions for Advent of Code"""
import os


def load_input(day):
    """
    Loads the input file for the given day.
    :param day: int:
    """
    top_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(
        top_dir,
        "inputs",
        f"day{day}.txt"
    )
    with open(path) as _input:
        data = _input.readlines()
    return data