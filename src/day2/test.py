from .asd import solve, solve2


def test_part1() -> None:

    data = """A Y
B X
C Z"""
    assert solve(data) == 15


def test_part2() -> None:

    data = """A Y
B X
C Z"""
    assert solve2(data) == 12
