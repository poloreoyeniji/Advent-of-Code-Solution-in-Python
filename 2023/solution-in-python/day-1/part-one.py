with open('C:/Users/HP/Desktop/advent-of-code-2023/day-1/puzzle-input.txt', 'r', encoding='utf-8') as f:
    list_of_calibration_values = []

    for line in f:
        list_of_calibration_values_for_each_line = []

        for i in line:
            if i.isdigit():
                list_of_calibration_values_for_each_line.append(i)

        calibration_value = list_of_calibration_values_for_each_line[0] + list_of_calibration_values_for_each_line[-1]
        int_calibration_value = int(calibration_value)

        list_of_calibration_values.append(int_calibration_value)

total_calibration_value = sum(list_of_calibration_values)

print(f"The sum of all of the calibration values is {total_calibration_value}")
            
        