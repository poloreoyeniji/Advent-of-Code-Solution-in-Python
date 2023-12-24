import re

sample_string = 'Game 123: 1 blue, 2 green, 3 red; 7 red, 8 green; 1 green, 2 red, 1 blue; 2 green, 3 red, 1 blue; 8 green, 1 blue'

cGame = re.compile(r'Game \d+')

mGame = cGame.search(sample_string)
Game = mGame.group()
Game = Game.split()
print(Game[0], Game[1])


rsample_string = re.sub(r'Game \d+:', '', sample_string)
print('here', rsample_string[0])
sets_string = rsample_string.split(';')
for string_iter in sets_string:

    cBlue = re.compile(r'\d+ blue')
    moBlue = cBlue.finditer(string_iter)
    z_dict = {}
    for i in moBlue:
        z = i.group()
        z = z.split()
        if z[1] in z_dict:
            z_dict[z[1]] += int(z[0])
        else:
            z_dict[z[1]] = int(z[0])
    
    cRed = re.compile(r'\d+ red')
    moRed = cRed.finditer(string_iter)

    for i in moRed:
        z = i.group()
        z = z.split()
        if z[1] in z_dict:
            z_dict[z[1]] += int(z[0])
        else:
            z_dict[z[1]] = int(z[0])

    cGreen = re.compile(r'\d+ green')
    moGreen= cGreen.finditer(string_iter)

    for i in moGreen:
        z = i.group()
        z = z.split()
        if z[1] in z_dict:
            z_dict[z[1]] += int(z[0])
        else:
            z_dict[z[1]] = int(z[0])
    print(z_dict)