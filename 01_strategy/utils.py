from datetime import datetime


class Const(object):
    class StrategyEnum(object):
        CONCRETE_STRATEGY_A = "concrete_strategy_a"
        CONCRETE_STRATEGY_B = "concrete_strategy_b"


def logger(info):
    print(f'{datetime.now()}: {info}')
