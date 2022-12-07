def build_fs(data: str) -> dict[str, int]:
    """parse commands and outputs to generate filesystem"""
    fs = {"/": 0}
    cursor = "/"

    cmd_output = data.split("$ ")[1:]
    for k in cmd_output:
        cmd, output = k.split("\n", 1)
        cmd_tokens = cmd.split(" ")

        if cmd_tokens[0] == "cd":
            if cmd_tokens[1] == "..":
                # /asd/pasd/ => cd .. => /asd/
                cursor = cursor.rsplit("/", 2)[0] + "/"
            elif cmd_tokens[1] == "/":
                # jump to root
                cursor = "/"
            else:
                # /asd/ => cd pasd => /asd/pasd/
                cursor = cursor + cmd_tokens[1] + "/"

        elif cmd_tokens[0] == "ls":
            files = output.strip("\n").split("\n")
            for f in files:
                info, basename = f.split(" ")
                fname = cursor + basename
                if info == "dir":
                    # append slash to detect dir roots
                    fs[fname + "/"] = 0
                else:
                    fs[fname] = int(info)

    # add folder sizes by summing files in subpaths
    for k, v in fs.items():
        if v == 0:
            fs[k] = sum([y for x, y in fs.items() if x.startswith(k)])
    return fs


def solve(data: str) -> int:
    fs = build_fs(data)
    return sum([v for k, v in fs.items() if k.endswith("/") and v < 100000])


def solve2(data: str) -> int:
    fs = build_fs(data)
    missing = fs["/"] + 30000000 - 70000000  # used + required - available
    return min([v for k, v in fs.items() if k.endswith("/") and v > missing])
