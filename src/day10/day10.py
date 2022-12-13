def solve(data: str) -> tuple[int, str]:
    cmds = data.split("\n")
    cycles = []
    for cmd in cmds:
        asd = cmd.split(" ")
        cycles.append(0)
        if asd[0] == "addx":
            value = int(asd[1])
            cycles.append(0)
            cycles.append(value)
    x = 1
    signals = []
    crt = ""
    idx = 0
    for i, c in enumerate(cycles):
        cn = i + 1

        if cn == 20:
            signals.append(cn * x)
        elif (cn - 20) % 40 == 0:
            signals.append(cn * x)
        x += c

        if x in [idx - 1, idx, idx + 1]:
            crt += "#"
        else:
            crt += "."
        idx += 1
        if cn % 40 == 0:
            crt += "\n"
            idx = 0

    return sum(signals), crt
