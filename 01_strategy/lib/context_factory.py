from typing import List

from strategy import Strategy
from utils import Const, logger
from concrete_strategy_a import ConcreteStrategyA
from concrete_strategy_b import ConcreteStrategyB


class ContextFactory(object):
    """
    The Context defines the interface of interest to clients.
    """

    strategy_dict = {
        Const.StrategyEnum.CONCRETE_STRATEGY_A: ConcreteStrategyA,
        Const.StrategyEnum.CONCRETE_STRATEGY_B: ConcreteStrategyB
    }

    def __init__(self, strategy_name: str) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        strategy_class = ContextFactory.strategy_dict.get(strategy_name)
        if not strategy_class:
            raise AttributeError(f"Invalid strategy_name: {strategy_name}")
        else:
            self._strategy = strategy_class()

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def do_some_business_logic(self, data: List) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        logger("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(data)
        logger(",".join(result))

        # ...
