from itertools import permutations


def solve(data: str):
    return eval(
        data.replace(" ", "")
        .replace("AY", "8")
        .replace("BZ", "9")
        .replace("CX", "7")
        .replace("AZ", "3")
        .replace("BX", "1")
        .replace("CY", "2")
        .replace("AX", "4")
        .replace("BY", "5")
        .replace("CZ", "6")
        .replace("\n", "+")
    )


def solve2(data: str):

    return solve(
        data.replace("A X", "AZ")
        .replace("A Y", "AX")
        .replace("A Z", "AY")
        .replace("C X", "CY")
        .replace("C Y", "CZ")
        .replace("C Z", "CX")
    )


if __name__ == "__main__":
    with open("input1.txt") as f:
        print(solve(f.read()))

    with open("input2.txt") as f:
        print(solve2(f.read()))
