import re
from math import prod

with open(r"C:\Users\HP\Desktop\advent-of-code-2023\day-6\puzzle-input.txt", "r", encoding="utf-8") as f:
    line_time = f.readline()
    line_distance = f.readline()

time_cleaned = re.sub(r"Time:\s*", '', line_time)
time_list = time_cleaned.split()
time = int(''.join(map(str, time_list)))

distance_cleaned = re.sub(r"Distance:\s*", '', line_distance)
distance_list = distance_cleaned.split()
distance = int(''.join(map(str, distance_list)))

number_of_wins = 0

for i in range(time + 1):
    current_time = i
    value = current_time * time
    # wins = 0
    if value > distance:
        number_of_wins += 1
    current_time += 1
    time -=1
    
print(number_of_wins)
