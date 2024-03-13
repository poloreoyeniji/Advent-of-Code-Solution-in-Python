import re 

file_path = r'2023\puzzle-input\day1.txt'

umber_values = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    11: '1',
    12: '2',
    13: '3',
    14: '4',
    15: '5',
    16: '6',
    17: '7',
    18: '8',
    19: '9'
}

number_values ={
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def regexxing(umber_values, line):
    listss = []
    for key, values in umber_values.items():
        string_text = values
        
        mo1 = re.finditer(rf'{string_text}', line)
        
        for match in mo1:
            listss.append([match.group(), match.start(), match.end()])

    return listss
    
def minx(z):
    li = []
    for i in z:
        li.append(i[1])
    return(min(li))

def stt_min(lists):
    mz = minx(lists)
    for i in lists:
        if i[1] == mz:
            return i[0] 

def ed_max(lists):
    end_ = 0
    parts = None
    for i in lists:
        if i[2] >= end_:
            end_ = i[2]
            parts = i[0]
    return parts

def digitise(x):
    if x.isdigit():
        return x
    else:
        return number_values[x]

with open(file_path, 'r', encoding='utf-8') as f:
    final_values = []
    for line in f:
        lines_list = regexxing(umber_values, line=line)
        minii = digitise(stt_min(lists=lines_list))
        maxii = digitise(ed_max(lines_list))

        final_values.append(int(str(minii) + str(maxii)))
    print(f"The sum of all calibration values is {sum(final_values)}")
