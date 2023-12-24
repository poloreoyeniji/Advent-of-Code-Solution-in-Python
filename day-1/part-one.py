with open('C:/Users/HP/Desktop/advent-of-code-2023/day-1/puzzle-input.txt', 'r', encoding='utf-8') as f:
    list_of_calibration_values = []
    for line in f:
        inner_values = []
        for i in line:
            if i.isdigit():
                inner_values.append(i)
        value = inner_values[0] + inner_values[-1]
        int_value = int(value)
        list_of_calibration_values.append(int_value)
calibration_values = sum(list_of_calibration_values)
print(calibration_values)
            
        