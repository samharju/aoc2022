from pathlib import Path

from day9 import solve


def test_example() -> None:
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    assert solve(data, 2) == 13


def test_example_2() -> None:
    data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    assert solve(data, 10) == 36


puzzle = (Path(__file__).parent / "input.txt").read_text()


def test_solution_1() -> None:
    assert solve(puzzle) == 6266


def test_solution_2() -> None:
    assert solve(puzzle, 10) == 2369
