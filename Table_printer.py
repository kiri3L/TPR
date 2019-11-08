def append_to_str(s1, s2, length, filer=' '):
    length -= len(s1)
    s1 += filer*length
    s1 += ' | ' + str(s2)
    return s1


def resize_list(count):
    l = []
    for i in range(count):
        l.append('')
    return l


def print_table(table, line_count, colon_count):
    if type(table) is not list:
        print('ERROR 1')
        return
    if len(table) == 0:
        print('ERROR 2')
        return
    print()
    lines = resize_list(line_count)
    length1 = 0
    length2 = 0
    for colon in range(colon_count):
        for line in range(line_count):
            if type(table[line]) is not list:
                lines[line] = append_to_str(lines[line],'',length1,'-')
            else:
                lines[line] = append_to_str(lines[line], table[line][colon], length1)
                length2 = max(len(lines[line]), length2)
        length1 = length2
    for line in lines:
        print(line)
