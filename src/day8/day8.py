def solve(data: str) -> tuple[int, int]:
    forest = [[int(x) for x in y] for y in data.split("\n")]

    w = len(forest[0])
    h = len(forest)

    def scenic(y: int, x: int) -> int:
        t = forest[y][x]
        col = [r[x] for r in forest]

        left, right, up, down = 0, 0, 0, 0

        for i in reversed(range(0, x)):
            left += 1
            if forest[y][i] >= t:
                break

        for i in range(x + 1, w):
            right += 1
            if forest[y][i] >= t:
                break

        for i in reversed(range(0, y)):
            up += 1
            if col[i] >= t:
                break

        for i in range(y + 1, h):
            down += 1
            if col[i] >= t:
                break

        return left * right * up * down

    visible = 0
    scenic_score = 0

    for y in range(0, h):
        for x in range(0, w):
            scenic_score = max(scenic_score, scenic(y, x))

            # edges are always visible
            if any([y == 0, y == h - 1, x == 0, x == w - 1]):
                visible += 1
                continue

            col = [r[x] for r in forest]

            # check line of sight to edges
            if any(
                [
                    forest[y][x] > max(forest[y][:x]),  # left
                    forest[y][x] > max(forest[y][x + 1 :]),  # right
                    forest[y][x] > max(col[:y]),  # up
                    forest[y][x] > max(col[y + 1 :]),  # down
                ]
            ):
                visible += 1

    return visible, scenic_score
