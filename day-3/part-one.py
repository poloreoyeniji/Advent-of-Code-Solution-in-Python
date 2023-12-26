# regex to get digits

def is_symbol(char):
    if not char.isalnum() and char != '.':
        return True
    return False

print(is_symbol('a'))