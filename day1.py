def extract_calibration_values_from_file(file_path):
    total_sum = 0

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            first_digit = None
            last_digit = None

            # Find the first digit in the line
            for char in line:
                if char.isdigit():
                    first_digit = int(char)
                    break
            
            # Find the last digit in the line
            for char in reversed(line):
                if char.isdigit():
                    last_digit = int(char)
                    break
            
            if first_digit is not None and last_digit is not None:
                combined_value = int(str(first_digit) + str(last_digit))
                total_sum += combined_value

    return total_sum

file_path = '/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input.txt'

#Calculates the sum of calibration values from the file
result = extract_calibration_values_from_file(file_path)
print("The sum of all calibration values is:", result)
