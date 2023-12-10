class EngineSchematicAnalyzer:
    DIRECTIONS = [
        (-1, -1),  
        (-1, 0),   
        (-1, 1),  
        (0, -1),   
        (0, 1),   
        (1, -1),   
        (1, 0),   
        (1, 1)     
    ]

    def __init__(self, schematic):
        self.schematic = [list(line) for line in schematic.split('\n')]
        self.processed_locations = set()

    def calculate_part_number_sum(self):
        total_sum = 0
        for i, row in enumerate(self.schematic):
            j = 0
            while j < len(row):
                if row[j].isdigit() and (i, j) not in self.processed_locations:
                    part_number = self._get_full_part_number(i, j)
                    self.processed_locations.update(
                        (i, col_index) for col_index in range(j, j + len(str(part_number)))
                    )

                    if any(self._is_adjacent_to_symbol(i, col_index) for col_index in range(j, j + len(str(part_number)))):
                        total_sum += part_number
                    j += len(str(part_number)) - 1
                j += 1
            
        return total_sum
    
    def calculate_gear_ratio_sum(self):
        total_sum = 0
        for i, row in enumerate(self.schematic):
            for j, char in enumerate(row):
                if char == '*':
                    total_sum += self._calculate_gear_ratio(i, j)
        
        return total_sum

    def _calculate_gear_ratio(self, row, col):
        adjacent_numbers = []
        for dx, dy in self.DIRECTIONS:
            adjacent_row, adjacent_col = row + dx, col + dy
            if 0 <= adjacent_row < len(self.schematic) and 0 <= adjacent_col < len(self.schematic[adjacent_row]):
                if self.schematic[adjacent_row][adjacent_col].isdigit():
                    part_number = self._get_full_part_number(adjacent_row, adjacent_col)
                    if part_number not in adjacent_numbers:
                        adjacent_numbers.append(part_number)

        if len(adjacent_numbers) == 2:
            return adjacent_numbers[0] * adjacent_numbers[1]
        return 0

    def _get_full_part_number(self, row, col):
        number_str = self.schematic[row][col]

        left_col = col - 1
        while left_col >= 0 and self.schematic[row][left_col].isdigit():
            number_str = self.schematic[row][left_col] + number_str
            left_col -= 1

        right_col = col + 1
        while right_col < len(self.schematic[row]) and self.schematic[row][right_col].isdigit():
            number_str += self.schematic[row][right_col]
            right_col += 1

        return int(number_str)

    def _is_valid_symbol(self, char):
        return not (char.isdigit() or char == '.')

    def _is_adjacent_to_symbol(self, row, col):
        for dx, dy in self.DIRECTIONS:
            if 0 <= row + dx < len(self.schematic) and 0 <= col + dy < len(self.schematic[row + dx]):
                if self._is_valid_symbol(self.schematic[row + dx][col + dy]):
                    return True
        return False


def calculate_gear_ratios():
    with open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (2).txt') as file:
        engine_schematic = file.read()
    
    analyzer = EngineSchematicAnalyzer(engine_schematic)
    total_sum = analyzer.calculate_gear_ratio_sum()
    print(f"Sum of all gear ratios is {total_sum}")


if __name__ == "__main__":
    calculate_gear_ratios()

    
