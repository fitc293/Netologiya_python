# 1. Даны 2 строки long_phrase и short_phrase. 
# Напишите код, который проверяет действительно ли длинная фраза long_phrase длиннее короткой short_phrase. 
# И выводит True или False в зависимости от результата сравнения.

long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(long_phrase) > len(short_phrase):
    print(True)
else:
    print(False)
