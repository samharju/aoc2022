from pathlib import Path

from day10 import solve

example = (Path(__file__).parent / "example.txt").read_text()


def test_example() -> None:
    assert solve(example)[0] == 13140


puzzle = (Path(__file__).parent / "input.txt").read_text()


def test_solution_1() -> None:
    assert solve(puzzle)[0] == 15020


def test_example_2() -> None:
    print()
    assert (
        solve(example)[1]
        == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
    )


def test_solution_2() -> None:
    assert (
        solve(puzzle)[1]
        == """####.####.#..#..##..#....###...##..###..
#....#....#..#.#..#.#....#..#.#..#.#..#.
###..###..#..#.#....#....#..#.#..#.#..#.
#....#....#..#.#.##.#....###..####.###..
#....#....#..#.#..#.#....#....#..#.#....
####.#.....##...###.####.#....#..#.#....
"""
    )
