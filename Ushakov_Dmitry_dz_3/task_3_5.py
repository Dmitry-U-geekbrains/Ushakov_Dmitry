# 5.Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
from random import choice

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, no_doubles=True):
    res = []
    if no_doubles:
        res2 = []
    for _ in range(n):
        tmp = []
        if n > 5:
            no_doubles = False
        if no_doubles:
            new=choice(NOUNS)
            while new in res2:
                new=choice(NOUNS)
            tmp.append(new)

            new=choice(ADVERBS)
            while new in res2:
                new=choice(ADJECTIVES)
            tmp.append(new)
        else:
            tmp.append(choice(NOUNS))
            tmp.append(choice(ADVERBS))
            tmp.append(choice(ADJECTIVES))
        res.append("".join(tmp))
        if no_doubles:
            res2.extend(tmp)
    return res
print(get_jokes(n=5))
