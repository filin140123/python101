import json

with open("task7-file.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
    splitted_lines = [i.split(" ") for i in lines]

    for s in splitted_lines:
        for ind, elem in enumerate(s):
            if elem.isdigit():
                s[ind] = int(elem)

        s[1] = s[2] - s[3]

    for i, s in enumerate(splitted_lines):
        splitted_lines[i] = splitted_lines[i][:2]

    first_dict = dict(splitted_lines)
    second_dict = {"average_profit": int(sum(first_dict.values()) / len(first_dict))}
    result_list = [first_dict, second_dict]

    print(result_list)

    result_list_json = json.dumps(result_list, indent=4)
    with open("task7-result.json", "w") as outf:
        outf.write(result_list_json)
