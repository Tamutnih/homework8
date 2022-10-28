# 1. Напишите программу, удаляющую из
# текста все слова содержащие "абв".


txt = input(f"Enter text:\n")


def del_some_words(some_txt):
    some_txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return " ".join(my_text)


my_text = del_some_words(txt)
print(txt)

