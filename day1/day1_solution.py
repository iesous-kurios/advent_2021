# read in txt file and convert into a list

import pandas as pd

day1_data = pd.read_csv('day1.txt', header=None)

numbers = day1_data[0]

# count number of times the number increases from the previous number
# and add to a list
counting = 0

# print each number in the list
for i in day1_data[0]:
    print(i)

print(type(numbers))

print(len(numbers))

print(day1_data.shape)

for i in range(0, len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        counting += 1

print(counting)