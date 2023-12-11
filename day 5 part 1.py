class AlmanacProcessor:
    def __init__(self, almanac_data):
        self.almanac_data = almanac_data
        self.seeds, self.mappings = self._parse_input(almanac_data)

    def find_lowest_location_number(self):
        """Finds the lowest location number using the rules specified in the almanac."""
        seed_locations = {}
        for seed in self.seeds:
            current_number = seed
            for mapping_data in self.mappings:
                current_number = self._find_mapped_number(current_number, mapping_data)
            seed_locations[seed] = current_number  # Location of seed in the last map
        return min(seed_locations.values())

    def _parse_input(self, input_data):
        """Parses the input data into seeds and mapping rules."""
        sections = input_data.strip().split('\n\n')
        seeds = list(map(int, sections[0].split(': ')[1].split()))
        mappings = [section.split(':\n')[1].split('\n') for section in sections[1:]]
        return seeds, mappings

    def _find_mapped_number(self, number, mapping_data):
        """Finds the corresponding mapped number based on the mapping rules."""
        for line in mapping_data:
            if line.strip():
                dest_start, src_start, length = map(int, line.split())
                if src_start <= number < src_start + length:
                    return dest_start + (number - src_start)
        return number

def process_almanac():
    with open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (4).txt') as file:
        almanac_data = file.read()

    processor = AlmanacProcessor(almanac_data)
    lowest_location = processor.find_lowest_location_number()
    print("The lowest location number is:", lowest_location)

    
    

if __name__ == "__main__":
   
    process_almanac()
