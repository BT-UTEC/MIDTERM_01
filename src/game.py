from abc import ABC, abstractmethod
from singleton_decorator import singleton
from player import Player

class Publisher(ABC):
    def __init__(self):
        self.subscribers = {}
    
    @abstractmethod
    def notify(self, data) -> None:
        pass

    @abstractmethod
    def subscribe(self, strategy, subscriber) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, strategy) -> None:
        pass

@singleton
class Game(Publisher):
    def __init__(self) -> None:
        self.number_players = 0
        super().__init__()
    
    def notify(self, data) -> None:
        for _, subscriber in self.subscribers:
            subscriber.update(data)

    def subscribe(self, strategy, subscriber: Player) -> None:
        if strategy not in self.subscribers:
            self.subscribers[strategy] = subscriber
        else:
            print(f'There is a Player with the same strategy, choose another.')

        if self.number_players == 5:
            self.start_game()

    def unsubscribe(self, strategy) -> None:
        self.subscribers.pop(strategy)

    def start_game(self):
        pass
