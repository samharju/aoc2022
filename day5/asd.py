"""now this is some ugly shit"""


def solve(data, crane):

    stackstr, cmdstr = data.split("\n\n")
    vals = [stackstr[i] for i in range(1, len(stackstr), 4)]

    stackss = list(
        zip(
            *[
                vals[i : i + int(stackstr[-2])]
                for i in range(0, len(vals), int(stackstr[-2]))
            ]
        )
    )
    stacks = [[y for y in x if y.isalpha()] for x in stackss]

    cmds = [int(y) for x in cmdstr.split("\n") for y in x.split(" ") if y.isdigit()]

    for i in range(0, len(cmds), 3):
        count, from_, to_ = cmds[i : i + 3]
        if crane == "CrateMover 9000":
            for j in range(count):
                asba = stacks[from_ - 1].pop(0)
                stacks[to_ - 1].insert(0, asba)
        elif crane == "CrateMover 9001":
            stacks[to_ - 1] = stacks[from_ - 1][:count] + stacks[to_ - 1]
            del stacks[from_ - 1][:count]

    return "".join([x[0] for x in stacks])


if __name__ == "__main__":
    with open("input1.txt") as f:
        data = f.read()
        print(solve(data, "CrateMover 9000"))
        print(solve(data, "CrateMover 9001"))
