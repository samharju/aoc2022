"""now this is some ugly shit

I wanted to try handling input data as lists and fiddle with
indices and handling it in batches. Seems to work."""


def solve(data: str, crane: str) -> str:

    # separate initial stacks and instructions
    stackstr, cmdstr = data.split("\n\n")
    # parse values from string representation
    vals = [stackstr[i] for i in range(1, len(stackstr), 4)]

    # as data is parsed as rows, convert it to columns
    stackss = list(
        zip(
            *[
                vals[i : i + int(stackstr[-2])]
                for i in range(0, len(vals), int(stackstr[-2]))
            ]
        )
    )

    # drop column numbers and empty cells
    stacks = [[y for y in x if y.isalpha()] for x in stackss]

    # parse commands into a single list of numbers
    cmds = [int(y) for x in cmdstr.split("\n") for y in x.split(" ") if y.isdigit()]

    # step through commands in chunks of three
    for i in range(0, len(cmds), 3):
        count, from_, to_ = cmds[i : i + 3]
        if crane == "CrateMover 9000":
            # just pop required number of crates
            for j in range(count):
                asba = stacks[from_ - 1].pop(0)
                stacks[to_ - 1].insert(0, asba)
        elif crane == "CrateMover 9001":
            # slice required number of crates and prepend to target stack
            stacks[to_ - 1] = stacks[from_ - 1][:count] + stacks[to_ - 1]
            del stacks[from_ - 1][:count]

    # dump topmost crates
    return "".join([x[0] for x in stacks])


if __name__ == "__main__":
    with open("input1.txt") as f:
        data = f.read()
        print(solve(data, "CrateMover 9000"))
        print(solve(data, "CrateMover 9001"))
