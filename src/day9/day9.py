from __future__ import annotations


class Knot:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def trail(self, lead: Knot) -> None:

        dx = lead.x - self.x
        dy = lead.y - self.y

        if abs(dx) > 1:
            self.x += dx // 2
            if abs(dy) > 1:
                self.y += dy // 2
            elif dy != 0:
                self.y += dy

        elif abs(dy) > 1:
            self.y += dy // 2
            if abs(dx) > 1:
                self.x += dx // 2
            elif dx != 0:
                self.x += dx


def solve(data: str, length: int = 2) -> int:

    moves = [y.split() for y in data.splitlines()]
    rope = [Knot() for _ in range(length)]

    hits = set()

    for dir, c in moves:
        for _ in range(int(c)):
            match dir:
                case "U":
                    rope[0].y += 1
                case "D":
                    rope[0].y -= 1
                case "R":
                    rope[0].x += 1
                case "L":
                    rope[0].x -= 1

            for i in range(1, len(rope)):
                rope[i].trail(rope[i - 1])

            hits.add((rope[-1].x, rope[-1].y))

    return len(hits)
