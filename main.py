"""
Задание 1:
Дан список из строк, в каждой строке содержится по предложению
для дальнейшей обработки текста необходимо в каждой строке
убрать символы пунктуации и разделить слова по пробелам.
Показать результат обработки.
Для получения символов пунктуации можно воспользоваться следующим
кодом:
import string
print(string.punctuation)
"""

import string
import datetime

some_text_1 = ["Python - высокоуровневый язык программирования общего назначения с динамической строгой типизацией и "
               "автоматическим управлением памятью, ориентированный на повышение производительности разработчика, "
               "читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.",
               "Язык является полностью объектно-ориентированным — всё является объектами.",
               "Необычной особенностью языка является выделение блоков кода пробельными отступами.",
               "Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться "
               "к документации.",
               "Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов.",
               "Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти "
               "написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких "
               "как Си или C++."]

some_text_2 = ["Это первое предложение!",
               "Это второе предложение с символами пунктуации ,!-_?."]


def delete_special_str(text: str):
    special_str = string.punctuation

    for x in text:
        if x in special_str:
            text = text.replace(x, "")
    return text


result_1 = list(map(lambda x: delete_special_str(x).split(), some_text_1))
result_2 = list(map(lambda x: delete_special_str(x).split(), some_text_2))
print(result_1)
print(result_2)


"""
Задание 2:
Дана последовательность дат рождения пользователей записанная в строках:
['1/5/2012', '14/10/1973', '6/10/1999', '7/5/2000', '6/9/1966', '24/12/2002', '3/3/1964', '30/9/1984', '29/5/1956',
'15/9/1952', '1/4/1960', '3/4/1992', '8/8/1968', '19/12/1994', '2/12/1982', '29/10/1991', '20/11/1991', '31/6/1979',
'10/1/2009', '1/2/2001']
Необходимо из этих дат определить количество полных лет пользователей,
записать их в новый список и отобразить.
"""

birthdays = ['1/5/2012', '14/10/1973', '6/10/1999', '7/5/2000', '6/9/1966', '24/12/2002', '3/3/1964', '30/9/1984',
             '29/5/1956', '15/9/1952', '1/4/1960', '3/4/1992', '8/8/1968', '19/12/1994', '2/12/1982', '29/10/1991',
             '20/11/1991', '30/6/1979', '10/1/2009', '1/2/2001'
             ]


def calc_age(birthday: str):
    date_of_birth = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
    current_date = datetime.datetime.today().date()

    age = current_date.year - date_of_birth.year
    month_verification = current_date.month - date_of_birth.month
    date_verification = current_date.day - date_of_birth.day

    if month_verification < 0:
        age = age - 1
    elif date_verification < 0 and month_verification == 0:
        age = age - 1

    return str(age)


# Была ошибка в задании (17 элемент списка), в июне 30 дней, а не 31.

result_ages = list(map(lambda x: calc_age(x), birthdays))
print(birthdays)
print(result_ages)
