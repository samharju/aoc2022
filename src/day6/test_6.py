from collections import namedtuple
from pathlib import Path

import pytest

from day6 import solve

testcase = namedtuple("testcase", ["input", "seqlen", "expected"])

tcs = [
    testcase("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
    testcase("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
    testcase("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
    testcase("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
    testcase("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
    testcase("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
    testcase("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
    testcase("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
    testcase("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
    testcase("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
]


@pytest.mark.parametrize("tc", tcs)
def test_examples(tc: testcase) -> None:
    assert solve(tc.input, tc.seqlen) == tc.expected


puzzle = (Path(__file__).parent / "input1.txt").read_text()


def test_solution_1() -> None:
    assert solve(puzzle, 4) == 1034


def test_solution_2() -> None:
    assert solve(puzzle, 14) == 2472
