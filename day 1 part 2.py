lines = open('/Users/winstonewoof/Desktop/Desktop - MacBook Air/my school stuff/fourth year f sem/comp 371/input.txt').read().splitlines()
p = 0
for line in lines:
    digits = []
    for i,c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    p += int(digits[0]+digits[-1])
print(p)
