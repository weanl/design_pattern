import os
import sys

sys.path.append(f"..{os.sep}..{os.sep}01_strategy{os.sep}")

from utils import logger
from lib.context import Context
from lib.concrete_strategy_a import ConcreteStrategyA
from lib.concrete_strategy_b import ConcreteStrategyB

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(ConcreteStrategyA())
    logger("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()

    logger("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
