from abc import ABC, abstractmethod
from strategy import Strategy

class Observer(ABC):
    def __init__(self) -> None:
        # Init
        pass

    @abstractmethod
    def update(self, data) -> bool:
        pass

class Player():
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy
        super().__init__()

    def update(self, data) -> bool:
        if self.strategy.execute(data):
            print(f'I win the game.')
            return True
        else:
            return False
