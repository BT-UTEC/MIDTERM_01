from game import Game
from player import Player
from strategy import StrategyFiveEven, StrategyFiveOdd, StrategyPrime, StrategyTenMultiple, StrategyTwoTwentyFive

def main():
    game = Game()

    # NOTE: Test for Singleton
    game_singleton = Game()
    if(id(game) == id(game_singleton)):
        print(f'Singleton works.')
    
    print('Game subscribers.')
    game.subscribe('FiveEven', Player(StrategyFiveEven()))
    game.subscribe('FiveOdd', Player(StrategyFiveOdd()))
    game.subscribe('Prime', Player(StrategyPrime()))
    game.subscribe('TenMultiple', Player(StrategyTenMultiple()))
    game.subscribe('TwoTwentyFive', Player(StrategyTwoTwentyFive()))

main()
