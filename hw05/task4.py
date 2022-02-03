from translate import Translator


def translate_to_russian(word):
    return Translator(from_lang="english", to_lang="russian").translate(word).title()


with open("task4-file.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

with open("task4-file-result.txt", "w", encoding="utf-8") as r:
    for line in lines:
        splitted_line = line.split(" ")
        splitted_line[0] = translate_to_russian(splitted_line[0])
        correct_line = " ".join(splitted_line)
        print(correct_line, file=r)
