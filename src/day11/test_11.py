from pathlib import Path

from day11 import solve


def test_example_1() -> None:

    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    assert solve(data, 20) == 10605


puzzle = (Path(__file__).parent / "input.txt").read_text()


def test_solution_1() -> None:
    assert solve(puzzle, 20) == 90882


def test_solution_2() -> None:
    assert solve(puzzle, 10000, True) == 30893109657
