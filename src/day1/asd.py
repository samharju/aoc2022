from functools import reduce


def cumu(a: int, b: str) -> int:
    return int(a) + sum([int(bb) for bb in b.split("\n")])


def main() -> None:
    with open("input.txt") as f:
        d = f.read()

    asd = [elf.split("\n") for elf in d.split("\n\n")]

    elf_payloads = [int(reduce(cumu, e)) for e in asd]  # type: ignore

    print(max(elf_payloads))

    print(sum(sorted(elf_payloads)[-3:]))


if __name__ == "__main__":
    main()
