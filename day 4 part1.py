class ScratchCardProcessor:
    def calculate_total_points(self, scratchcard_data):
        return sum(self._calculate_points(scratchcard) for scratchcard in scratchcard_data.splitlines())

    def _calculate_points(self, scratchcard):
        _, numbers = scratchcard.split(": ")
        winning_numbers, your_numbers = map(lambda ns: [int(n) for n in ns.split()], numbers.split(" | "))
        match_count = sum(1 for number in your_numbers if number in winning_numbers)

        return 0 if match_count == 0 else 2 ** (match_count - 1)

def process_scratchcards():
    processor = ScratchCardProcessor()
    with open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (3).txt') as file:
        scratchcard_data = file.read()
    total_points = processor.calculate_total_points(scratchcard_data)
    print(f"Total points: {total_points}")

if __name__ == "__main__":
    process_scratchcards()
