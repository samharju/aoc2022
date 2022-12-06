from pathlib import Path

from day5 import solve

puzzle = (Path(__file__).parent / "input1.txt").read_text()


def test_part1() -> None:
    data = (
        "    [D]    \n"
        "[N] [C]    \n"
        "[Z] [M] [P]\n"
        " 1   2   3 \n\n"
        "move 1 from 2 to 1\n"
        "move 3 from 1 to 3\n"
        "move 2 from 2 to 1\n"
        "move 1 from 1 to 2\n"
    )
    assert solve(data, "CrateMover 9000") == "CMZ"


def test_solution_1() -> None:
    assert solve(puzzle, "CrateMover 9000") == "TLNGFGMFN"


def test_solution_2() -> None:
    assert solve(puzzle, "CrateMover 9001") == "FGLQJCMBD"
