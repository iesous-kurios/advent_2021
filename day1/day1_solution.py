# read in txt file and convert into a list of ints
with open('day1.txt') as f:
    numbers = f.readlines()

number_list = [int(i) for i in numbers]


# count number of times the number increases from the previous number
# and add to a list


def part1(numbers):
    counting = 0
    for i in range(0, len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            counting += 1
    return counting


print('Solution to part 1 is:', part1(number_list))

def part2(numbers):
    # count number of times the sum of three numbers is higher than the sum of previous three numbers
    # add to counter each time it happens
    counting = 0
    for i in range(1, len(numbers)-2):
        if numbers[i-1] + numbers[i] + numbers[i+1] < numbers[i] + numbers[i+1] + numbers[i+2]:
            counting += 1
    return counting

print('Solution to part 2 is:', part2(number_list))
