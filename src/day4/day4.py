def vals(a: str) -> set[int]:
    b = a.split("-")
    return set(range(int(b[0]), int(b[1]) + 1))


def solve(data: str) -> int:
    pairs = [d.split(",") for d in data.split("\n")]
    return sum([vals(x) >= vals(y) or vals(x) <= vals(y) for x, y in pairs])


def solve2(data: str) -> int:
    pairs = [d.split(",") for d in data.split("\n")]
    return sum([bool(vals(x) & vals(y)) for x, y in pairs])
