from abc import ABC, abstractmethod
from singleton_decorator import singleton
from random import randint
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
        self.data = []
        self.number_players = 0
        super().__init__()
    
    def notify(self, data) -> bool:
        for _, subscriber in self.subscribers.items():
            if subscriber.update(data):
                return True

        return False

    def subscribe(self, strategy, subscriber: Player) -> None:
        if strategy not in self.subscribers:
            self.subscribers[strategy] = subscriber
        else:
            print(f'There is a Player with the same strategy, choose another.')
        
        self.number_players += 1
        if self.number_players == 5:
            print(f'Game starts.')
            self.start_game()

    def unsubscribe(self, strategy) -> None:
        self.subscribers.pop(strategy)

    def start_game(self) -> None:
        winner_flag = False

        while not winner_flag:
            current_number = randint(1, 100)
            while current_number in self.data:
                current_number = randint(1, 100)
            self.data.append(current_number)
            
            winner_flag = self.notify(self.data)

        print(f'Game Over.')
