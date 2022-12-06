from pathlib import Path

from day3 import solve, solve2


def test_part1() -> None:

    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    assert solve(data) == 157


def test_solution_1() -> None:
    puzzle = (Path(__file__).parent / "input1.txt").read_text()
    assert solve(puzzle) == 7716


def test_part2() -> None:

    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert solve2(data) == 70


def test_solution_2() -> None:
    puzzle = (Path(__file__).parent / "input1.txt").read_text()
    assert solve2(puzzle) == 2973
