with open("task6-file.txt", "r", encoding="utf-8") as f:
    cut_list = ["(пр)", "(л)", "(лаб)", ":"]
    lines = f.read().splitlines()
    splitted_lines = [i.split(" ") for i in lines]

    for s in splitted_lines:
        for i, elem in enumerate(s):
            if elem == '—':
                s[i] = "0"

            for useless_symbols in cut_list:
                if elem.endswith(useless_symbols):
                    s[i] = s[i][:-len(useless_symbols)]

        for i, elem in enumerate(s):
            if elem.isdigit():
                s[i] = int(s[i])

        s[1] = sum(s[1:])

    for i, s in enumerate(splitted_lines):
        splitted_lines[i] = splitted_lines[i][:2]

    result = dict(splitted_lines)
    print(result)
