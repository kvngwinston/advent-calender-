class CubeGameAnalyzer:
    def __init__(self, max_cubes):
        self.max_cubes = max_cubes

    def sum_of_possible_game_ids(self, games):
        sum_ids = 0
        for game in games:
            try:
                game_id, sequences = game.split(": ")
                if self._is_game_possible(sequences):
                    sum_ids += int(game_id.split()[1])
            except ValueError as e:
                print(f"Error processing game data: {e}")
        return sum_ids

    def _is_game_possible(self, game_sequence):
        sequences = game_sequence.split(";")
        for sequence in sequences:
            sequence = sequence.strip()
            if not self._is_sequence_possible(sequence):
                return False
        return True

    def _is_sequence_possible(self, sequence):
        cubes = sequence.split(", ")
        for cube in cubes:
            count, color = cube.split()
            if int(count) > self.max_cubes[color]:
                return False
        return True


def main():
    # read games from the input file
    file_path = '/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (1).txt'
    with open(file_path) as f:
        games = f.readlines()

    # calculate and display the sum of possible game IDs
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    analyzer = CubeGameAnalyzer(max_cubes)
    print(analyzer.sum_of_possible_game_ids(games))



if __name__ == "__main__":
    # run the test function
    test_cube_game_analyzer()

    # execute the main function
    main()
