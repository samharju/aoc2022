from pathlib import Path

from day4 import solve, solve2

puzzle = (Path(__file__).parent / "input1.txt").read_text()


def test_part1() -> None:

    data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    assert solve(data) == 2


def test_solution_1() -> None:
    assert solve(puzzle) == 550


def test_part2() -> None:

    data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    assert solve2(data) == 4


def test_solution_2() -> None:
    assert solve2(puzzle) == 931
