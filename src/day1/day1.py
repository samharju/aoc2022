from functools import reduce


def cumu(a: int, b: str) -> int:
    return int(a) + sum([int(bb) for bb in b.split("\n")])


def solve1(data: str) -> int:
    asd = [elf.split("\n") for elf in data.split("\n\n")]
    elf_payloads = [int(reduce(cumu, e)) for e in asd]  # type: ignore

    return max(elf_payloads)


def solve2(data: str) -> int:
    asd = [elf.split("\n") for elf in data.split("\n\n")]
    elf_payloads = [int(reduce(cumu, e)) for e in asd]  # type: ignore

    return sum(sorted(elf_payloads)[-3:])
