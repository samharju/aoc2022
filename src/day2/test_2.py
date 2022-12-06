from pathlib import Path

from day2 import solve, solve2


def test_part1() -> None:

    data = """A Y
B X
C Z"""
    assert solve(data) == 15


def test_solution_1() -> None:
    puzzle = (Path(__file__).parent / "input1.txt").read_text()
    assert solve(puzzle) == 13009


def test_part2() -> None:

    data = """A Y
B X
C Z"""
    assert solve2(data) == 12


def test_solution_2() -> None:
    puzzle = (Path(__file__).parent / "input2.txt").read_text()
    assert solve2(puzzle) == 10398
