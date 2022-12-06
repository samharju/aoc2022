from pathlib import Path

from day1 import solve1, solve2

input = (Path(__file__).parent / "input.txt").read_text()


def test_solution_1() -> None:
    assert solve1(input) == 66616


def test_solution_2() -> None:
    assert solve2(input) == 199172
