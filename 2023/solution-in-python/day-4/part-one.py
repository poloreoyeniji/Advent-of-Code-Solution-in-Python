import re



final_wins = []
with open(r"C:\Users\HP\Desktop\advent-of-code-2023\day-4\puzzle-input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        sample_string = line

        cleaned = re.sub(r'Card\s*\d+\:', '', sample_string)
        # print(cleaned)
        numbers = cleaned.split('|')
        winning_numbers = numbers[0]
        winning_numbers_list = winning_numbers.split()


        numbers_possessed = numbers[1]
        numbers_possessed_list = numbers_possessed.split()

        wins = [i for i in numbers_possessed_list if i in winning_numbers_list]

        winss = 0
        if len(wins) == 1:
            winss = 1
        elif len(wins) > 1:
            root = len(wins) - 1
            winss = 2 ** root
        final_wins.append(winss)

print(sum(final_wins))