def is_symbol(char):
    return not char.isalnum() and char != '.'

def valid_numbers(grid):
    number_of_columns = len(grid[0])
    number_of_rows = len(grid)
    valid_nums = []

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            working_char = grid[i][j]
            if working_char.isdigit():
                # Collect surrounding characters considering boundaries
                surrounding_chars = []

                for x in range(max(0, i - 1), min(i + 2, number_of_rows)):
                    for y in range(max(0, j - 1), min(j + 2, number_of_columns)):
                        if x != i or y != j:  # Exclude the current digit itself
                            surrounding_chars.append(grid[x][y])

                if any(map(is_symbol, surrounding_chars)):
                    valid_nums.append(int(working_char))
    return valid_nums

def get_lines_in_groups_of_three(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_groups = num_lines // 3
    list_of_lines = []

    for i in range(num_groups):
        group = lines[i * 3: i * 3 + 3]
        list_of_lines.append(group)

    remaining_lines = num_lines % 3
    if remaining_lines > 0:
        last_group = lines[num_groups * 3:]
        list_of_lines.append(last_group)
    
    for group in list_of_lines:
        for i in range(len(group)):
            group[i] = group[i].strip()
    
    return(list_of_lines)



file_path = r'C:\Users\HP\Desktop\advent-of-code-2023\day-3\puzzle-input.txt'
grids = get_lines_in_groups_of_three(file_path)

result = []
for i in grids:
    i = valid_numbers(i)
    result.append(i)


sum_result = 0
for i in result:
    sumx = sum(i)
    sum_result += sumx
print(sum_result)
