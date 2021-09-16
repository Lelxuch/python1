def all_possible_strings(symbols):
    if len(symbols) == 0:
        return []
    elif len(symbols) == 1:
        return [symbols]
    else:
        first = symbols[0]
        rest = symbols[1:]
        rest_strings = all_possible_strings(rest)
        result = []
        for string in rest_strings:
            for i in range(len(string) + 1):
                result.append(string[:i] + first + string[i:])
        return result

given = ['a', 'b', 'c', 'd', 'e']
toProcess = ""
for i in given:
    toProcess = toProcess + i

print(all_possible_strings(toProcess))