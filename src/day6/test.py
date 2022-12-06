from collections import namedtuple

import pytest

from .asd import solve

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
def test_all(tc: testcase) -> None:
    assert solve(tc.input, tc.seqlen) == tc.expected
