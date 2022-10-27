from typing import List

from strategy import Strategy


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return list(reversed(sorted(data)))
