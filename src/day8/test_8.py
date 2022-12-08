from pathlib import Path

from day8 import solve


def test_example() -> None:

    data = """30373
25512
65332
33549
35390"""
    assert solve(data) == (21, 8)


puzzle = (Path(__file__).parent / "input.txt").read_text()


def test_solution() -> None:
    assert solve(puzzle) == (1684, 486540)
