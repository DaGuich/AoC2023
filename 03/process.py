# namedtuple to construct a game description
from collections import namedtuple
# just used to read the input file
from pathlib import Path
# just sume typing stuff
from typing import Callable, Iterable

Game = namedtuple('Game', ['number', 'rounds'])
Round = namedtuple('Round', ['red', 'green', 'blue'])


def make_is_possible(red: int, green: int, blue: int) -> Callable:
    def round_possible(round: Round) -> bool:
        return all((
            round.red <= red,
            round.green <= green,
            round.blue <= blue
        ))

    def inner(game: Game) -> bool:
        return all(map(round_possible, game.rounds))

    return inner


def line_to_game(line: str) -> Game:
    def format_rounds(round: Iterable[str]) -> Round:
        round = map(str.strip, round)
        round = {
            **{
                'red': 0,
                'green': 0,
                'blue': 0,
            },
            **{
                p.split()[1]: int(p.split()[0].strip())
                for p in round
            }
        }
        return Round(**round)

    beginning, end = tuple(line.split(':'))
    rounds = list(end.split(';'))
    beginning = beginning.split()
    rounds = map(str.strip, rounds)
    rounds = map(lambda r: r.split(','), rounds)
    rounds = map(format_rounds, rounds)
    return Game(number=int(beginning[1]), rounds=list(rounds))


def process(lines: list[str]) -> int:
    is_possible = make_is_possible(12, 13, 14)
    lines = map(str.strip, lines)
    lines = filter(lambda line: len(line) > 0, lines)
    games = map(line_to_game, lines)
    games = filter(is_possible, games)
    games = list(games)
    return sum(map(lambda g: g.number, games))


if __name__ == '__main__':
    input_file = Path(__file__).parent / 'input.txt'

    # first test with test input
    example = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    result = process(example.split('\n'))
    print(result)
    assert result == 8

    with input_file.open() as f:
        result = process(f.readlines())
        print(result)
