
file_path = '/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input (3).txt'
with open(file_path) as file:
    lines = file.read().splitlines()

data = [line.split('|') for line in lines]


winning_numbers = [x[0][10:].strip().split() for x in data]
player_numbers = [x[1].strip().split() for x in data]


duplicates = [1 for _ in player_numbers]

for i, card in enumerate(player_numbers):
    hit_count = 0
    for num in card:
        if num in winning_numbers[i]:
            hit_count += 1
            duplicates[i + hit_count] += duplicates[i]

total_duplicates = sum(duplicates)
print(total_duplicates)
