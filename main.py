# # 1. Користувач вводить рядок з клавіатури.
# # Порахуйте кількість літер, цифр у рядку.
# # Виведіть обидві кількості на екран. (використовувати цикл)
# line = input("Write some symbols and digits ")
# ii = 0
# dd = 0
# for i in line:
#     if i.isalpha():
#         ii += 1
#
# print("words", ii)
# for d in line:
#     if d.isdigit():
#         dd += 1
# print("digits", dd)

# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.

# line = input("Enter some symbols ")
# search = input("Enter symbol what you need to find ")
# id = 0
# for i in line:
#     if i == search:
#         id += 1
# print("symbols ", id)

#3. Користувач вводить з клавіатури рядок,
# слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше.
# Отриманий рядок на екрані.

# line = input("Enter some text ")
# search = input("Enter search word ")
# replace = input("Enter word for replace ")
#
# line = line.replace(search, replace)
# print(line)

# 4. Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами
#   (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто,
#   починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у
#   зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.

# text = "Some random text here"
# print(text)
# print(text[2:3])
# print(text[-2:-1])
# print(text[:5])
# print(text[:-2])
# print(text[::2])
# print(text[1::2])
# print(text[::-1])
# print(text[::-2])
# print(len(text))
#!!!


