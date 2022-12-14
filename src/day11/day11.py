from typing import Any, Generator


class Monke:

    supermod: int = 0

    def __init__(
        self,
        items: list[int],
        op: str,
        test: int,
        ttarget: int,
        ftarget: int,
    ) -> None:
        self._items = items
        self._op = self._parse_op(op)
        self._test = test
        self._ttarget = ttarget
        self._ftarget = ftarget
        self._business_count = 0

    def _parse_op(self, a: str) -> Any:
        match a[0], a[1:]:
            case ["*", ""]:
                return eval("lambda x: x*x")
            case [op, val]:
                return eval(f"lambda x: x{op}{val}")
            case _:
                raise Exception("nada")

    def catch(self, item: int) -> None:
        self._items.append(item)

    def business(self) -> Generator[tuple[int, int], None, None]:
        for item in self._items:
            self._business_count += 1

            new_val = self._op(item)

            if self.supermod:
                new_val %= self.supermod
            else:
                new_val //= 3

            if new_val % self._test == 0:
                yield new_val, self._ttarget
            else:
                yield new_val, self._ftarget
        self._items = []


def solve(data: str, rounds: int, scale: bool = False) -> int:
    monkee_data = data.split("\n\n")
    tokens = "0123456789:,+-*"
    monkees: list[Monke] = []
    if scale:
        Monke.supermod = 1

    for monke in monkee_data:
        vals = "".join([x.strip() for x in monke if x in tokens]).split(":")
        monkees.append(
            Monke(
                [int(x) for x in vals[2].split(",")],
                vals[3],
                int(vals[4]),
                int(vals[5]),
                int(vals[6]),
            )
        )
        Monke.supermod *= int(vals[4])

    for i in range(rounds):
        for m in monkees:
            for item, target in m.business():
                monkees[target].catch(item)

    business_factors = [x._business_count for x in monkees]
    business_factors.sort(reverse=True)

    return business_factors[0] * business_factors[1]
