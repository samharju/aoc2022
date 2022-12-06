def solve(data: str, seqlen: int) -> int:
    for i in range(seqlen, len(data)):
        if len(set(data[i - seqlen : i])) == seqlen:
            return i
    return 0


if __name__ == "__main__":
    with open("input1.txt") as f:
        data = f.read()
        print(solve(data, 4))
        print(solve(data, 14))
