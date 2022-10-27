import os
import sys

sys.path.append(f"..{os.sep}..{os.sep}01_strategy{os.sep}")

from lib.context_factory import ContextFactory
from utils import logger, Const

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = ContextFactory(Const.StrategyEnum.CONCRETE_STRATEGY_A)
    logger("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic(["a", "b", "c", "d", "e"])

    logger("Client: Strategy is set to reverse sorting.")
    context = ContextFactory(Const.StrategyEnum.CONCRETE_STRATEGY_B)
    context.do_some_business_logic(["a", "b", "c", "d", "e"])
