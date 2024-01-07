import re
from math import prod

with open(r"C:\Users\HP\Desktop\advent-of-code-2023\day-6\puzzle-input.txt", "r", encoding="utf-8") as f:
    line_time = f.readline()
    line_distance = f.readline()

time_cleaned = re.sub(r"Time:\s*", '', line_time)
time_list = time_cleaned.split()

distance_cleaned = re.sub(r"Distance:\s*", '', line_distance)
distance_list = distance_cleaned.split()

wins_list = []

for i in range(len(time_list)):
    time = int(time_list[i])
    distance = int(distance_list[i])

    number_of_wins = 0

    for i in range(time + 1):
        current_time = i
        value = current_time * time
        if value > distance:
            number_of_wins += 1
        current_time += 1
        time -=1
    wins_list.append(number_of_wins)

answer = prod(wins_list)
print(answer)
