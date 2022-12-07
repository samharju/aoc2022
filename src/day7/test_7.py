from pathlib import Path

from day7 import solve, solve2

puzzle = (Path(__file__).parent / "input.txt").read_text()

test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_part_1() -> None:
    assert solve(test_data) == 95437


def test_part_2() -> None:
    assert solve2(test_data) == 24933642


def test_solution_1() -> None:
    assert solve(puzzle) == 1844187


def test_solution_2() -> None:
    assert solve2(puzzle) == 4978279
