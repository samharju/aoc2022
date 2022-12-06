from string import ascii_letters


def solve(data: str) -> int:
    sacks = [
        (set(s[: int(len(s) / 2)]), set(s[int(len(s) / 2) :])) for s in data.split("\n")
    ]
    return sum([ascii_letters.index(d) + 1 for s in sacks for d in s[0] & s[1]])


def solve2(data: str) -> int:
    elfss = data.split("\n")
    return sum(
        [
            ascii_letters.index(d) + 1
            for g in [elfss[i : i + 3] for i in range(0, len(elfss), 3)]
            for d in set(g[0]) & set(g[1]) & set(g[2])
        ]
    )


if __name__ == "__main__":
    with open("input1.txt") as f:
        d = f.read()
        print(solve(d))
        print(solve2(d))
