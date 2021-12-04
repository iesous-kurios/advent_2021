# read in txt file and convert into a list of ints
with open('day2.txt') as f:
    rows = f.readlines()

lines = []

for item in rows:
    # strip the newline character
    item = item.strip('\n')
    lines.append(item)
    # split the string into a list of ints

h = 0
d = 0

for item in lines:
    print(h, d)

    # check each line, if line contains the string 'forward', increment h by the following number
    # if the line contains the string 'down', increment d by the following number
    if 'forward' in item:
        h += int(item.split()[1])
        print('forward found, this is second part',int(item.split()[1]))
    if 'back' in item:
        h -= int(item.split()[1])
        print('back found, this is second part',int(item.split()[1]))
    if 'up' in item:
        d -= int(item.split()[1])
        print('up found, this is second part',int(item.split()[1]))
    if 'down' in item:
        d += int(item.split()[1])
        print('down found, this is second part',int(item.split()[1]))
    
print(h, d)
    
answer = h * d

print('answer to part 1 is', answer)

# part 2
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

aim = 0

h = 0
d = 0

for item in lines:
    print(h, d)

    if 'forward' in item:
        # increases horizontal position by x units and depth by aim * x
        h += int(item.split()[1])
        d += aim * int(item.split()[1])
        print('forward found, this is second part',int(item.split()[1]))
    if 'back' in item:
        # decreases horizontal position by x units and depth by aim * x
        h -= int(item.split()[1])
        d -= aim * int(item.split()[1])
        print('back found, this is second part',int(item.split()[1]))
    if 'up' in item:
        # increases aim by x units
        aim -= int(item.split()[1])
        print('up found, this is second part',int(item.split()[1]))
    if 'down' in item:
        # decreases aim by x units
        aim += int(item.split()[1])
        print('down found, this is second part',int(item.split()[1]))


    
print(h, d)
    
answer = h * d

print('answer to part 2 is', answer)