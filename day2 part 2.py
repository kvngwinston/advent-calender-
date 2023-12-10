from functools import reduce
from operator import mul


class CubeGameAnalyzer:
    def __init__(self, games, max_cubes=None):
        self.games = games
        self.max_cubes = max_cubes if max_cubes else {"red": 12, "green": 13, "blue": 14}

    def sum_of_possible_game_ids(self):
        return sum(int(game.split(": ")[0].split()[1]) for game in self.games if self._is_game_possible(game.split(": ")[1]))

    def sum_of_power_of_games(self):
        sum_power_of_games = 0

        for game in self.games:
            game_sets = game.split(": ")[1].split("; ")

            min_cubes_required = {"red": 0, "green": 0, "blue": 0}

            for cubes in game_sets:
                for count, color in map(str.split, cubes.split(", ")):
                    min_cubes_required[color] = max(int(count), min_cubes_required[color])

            game_power = reduce(mul, min_cubes_required.values(), 1)
            sum_power_of_games += game_power

        return sum_power_of_games

    def _is_game_possible(self, game_sequence):
        sequences = game_sequence.split(";")
        return all(self._is_sequence_possible(sequence.strip()) for sequence in sequences)

    def _is_sequence_possible(self, sequence):
        cubes = sequence.split(",")
        return all(int(count) <= self.max_cubes[color] for count, color in (cube.strip().split() for cube in cubes))


def main():
    with open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (1).txt') as f:
        games = f.readlines()

    analyzer = CubeGameAnalyzer(games)
    print(analyzer.sum_of_power_of_games())


if __name__ == "__main__":
    main()
