def length_str(str):
    if str == '':
        return 0
    return 1 + length_str(str[:-1])

print(length_str('rahulji'))