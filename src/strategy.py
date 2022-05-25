from abc import ABC, abstractmethod
from sympy import isprime
from __future__ import annotations

class Strategy(ABC):
    def init(self) -> None:
        pass

    @abstractmethod
    def execute(self, data) -> bool:
        pass

class StrategyFiveEven(Strategy):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, data) -> bool:
        quantity = 0
        for number in data:
            # NOTE: Even number
            if number % 2 == 0:
                quantity += 1
            if quantity == 5:
                return True

        return False

class StrategyFiveOdd(Strategy):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, data) -> bool:
        quantity = 0
        for number in data:
            # NOTE: Even number
            if number % 2 != 0:
                quantity += 1
            if quantity == 5:
                return True

        return False

class StrategyPrime(Strategy):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, data) -> bool:
        for number in data:
            # NOTE: Prime number
            if isprime(number):
                return True

        return False

class StrategyTenMultiple(Strategy):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, data) -> bool:
        quantity = 0
        for number in data:
            # NOTE: Prime number
            if number % 10 == 0:
                quantity += 1
            if quantity == 3:
                return True

        return False

class StrategyTwoTwentyFive(Strategy):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, data) -> bool:
        quantity = 0
        for number in data:
            # NOTE: Prime number
            if number % 25 == 0:
                quantity += 1
            if quantity == 2:
                return True

        return False
