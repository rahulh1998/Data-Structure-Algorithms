def reverse_string(string):
    if len(string) == 0:
        return ''
    return str(string[-1]) + reverse_string(string[:-1])

print(reverse_string('memo'))
