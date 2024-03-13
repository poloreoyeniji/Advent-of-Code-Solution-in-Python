import re
filepath = r"C:\Users\HP\Desktop\advent-of-code-2023\day-4\sample-input.txt"

def length_of_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return(len(lines))

final_wins = []

with open(filepath, 'r', encoding='utf-8') as f:
    length_of_filex = length_of_file(filepath)
    i = 0
    for line in f:
        sample_string = line

        cleaned = re.sub(r'Card\s*\d+\:', '', sample_string)

        numbers = cleaned.split('|')
        winning_numbers = numbers[0]
        winning_numbers_list = winning_numbers.split()

        numbers_possessed = numbers[1]
        numbers_possessed_list = numbers_possessed.split()

        wins = [i for i in numbers_possessed_list if i in winning_numbers_list]
        finall = len(wins) * (length_of_filex - i)

        i += 1
        if i == len(filepath):
            break
        
print(sum(final_wins))