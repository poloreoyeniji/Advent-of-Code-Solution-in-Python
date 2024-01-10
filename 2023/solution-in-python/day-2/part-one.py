import re

file_path = file_path = r'C:\Users\HP\Desktop\advent-of-code-solution\2023\puzzle-input\day2.txt'

max_red = 12
max_green = 13
max_blue = 14
games_possibiity_dict = {}

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        sample_string = line

        cGame = re.compile(r'Game \d+')

        mGame = cGame.search(sample_string)
        Game = mGame.group().split()
        game_number = int(Game[1])



        rsample_string = re.sub(r'Game \d+:', '', sample_string)
        # print('here', rsample_string[0])
        sets_string = rsample_string.split(';')
        game_possible = True


        for string_iter in sets_string:
            z_dict = {}

            for color in ['red', 'green', 'blue']:
                cColor = re.compile(r'\d+ ' + color)
                moColor = cColor.finditer(string_iter)

                for i in moColor:
                    z = i.group()
                    z = z.split()
                    if z[1] in z_dict:
                        z_dict[z[1]] += int(z[0])
                    else:
                        z_dict[z[1]] = int(z[0])        

            red = z_dict.get('red', 0)
            green = z_dict.get('green', 0)
            blue = z_dict.get('blue', 0)

            if (red > max_red) or (green > max_green) or (blue > max_blue):
                game_possible = False
                break
        
        games_possibiity_dict[game_number] = game_possible

    print(games_possibiity_dict)
    um_v = sum(key for key, values in games_possibiity_dict.items() if values == True)
    print(um_v)


