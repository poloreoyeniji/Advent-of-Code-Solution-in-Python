# Define a function to calculate the score of a hand
def score_hand(hand):
    values = sorted(hand)
    unique_values = len(set(values))

    if len(set(values)) == 1:  # Check for a flush
        return 7
    elif values.count(values[0]) == 4 or values.count(values[1]) == 4:  # Check for four of a kind
        return 6
    elif (values.count(values[0]) == 3 and values.count(values[3]) == 2) or (values.count(values[0]) == 2 and values.count(values[4]) == 3):  # Check for full house
        return 5
    elif len(set(values)) == 2:  # Check for three of a kind
        return 4
    elif len(set(values)) == 3 and (values.count(values[0]) == 2 or values.count(values[2]) == 2 or values.count(values[4]) == 2):  # Check for two pairs
        return 3
    elif len(set(values)) == 4:  # Check for one pair
        return 2
    else:  # High card
        return 1

# Read hands from the input file
with open(r'C:\Users\HP\Desktop\advent-of-code-2023\day-7\sample-input.txt', 'r') as file:
    data = file.read().strip().split('\n')

# Process each hand, calculate its score, and store in a list
hands = []
for line in data:
    cards = line.split()
    card_values = [ord(card[0]) - ord('A') + 1 for card in cards]  # Convert card values to numeric representation
    hand_score = score_hand(card_values)
    hands.append((card_values, hand_score))

# Sort the hands based on their scores and card values
hands.sort(key=lambda x: (x[1], x[0],), reverse=True)

# Calculate the total score by multiplying hand scores with their positions
total_score = sum((i + 1) * hand[1] for i, hand in enumerate(hands))

print('Day 07 Part 1:', total_score)
