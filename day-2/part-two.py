import re
import pprint
values_list = []
with open('C:/Users/HP/Desktop/advent-of-code-2023/day-2/input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sample_string = line
        rsample_string = re.sub(r'Game \d+:', '', sample_string)

        list_of_sets = rsample_string.split(';')
        rlist_of_sets = []
        for set in list_of_sets:
            set = set.rstrip()
            rlist_of_sets.append(set)
        # print(rlist_of_sets)
        # print(len(rlist_of_sets))

        list_of_dicts = []
        for i in range(len(rlist_of_sets)):
            current_game = rlist_of_sets[i] 

            color_dict = {'red': 0, 'green': 0, 'blue': 0}


            for color in ['red', 'green', 'blue']:
                cColor = re.compile(r'\d+ ' + color)
                moColor = cColor.finditer(current_game)
                count = 0

                for match in moColor:
                    count += int(match.group().split()[0])
                
                color_dict[color] = count
            # print(color_dict)
            list_of_dicts.append(color_dict)
        # pprint.pprint(list_of_dicts)

        real_color_count = {}
        for i in list_of_dicts:
            for color, count in i.items():
                if color not in real_color_count:
                    real_color_count[color] = []
                real_color_count[color].append(count)
        # print(real_color_count)

        min_real_color_count = {'red': 0, 'green': 0, 'blue': 0}
        for color in real_color_count:
            least_needed_amount = max(real_color_count[color])
            min_real_color_count[color] = least_needed_amount
        # print(min_real_color_count)

        sum_count = 1
        for key, items in min_real_color_count.items():
            sum_count *= items
        # print(sum_count)
        values_list.append(sum_count)
print(sum(values_list))
                







