# import random
# import random
# attempts = 3
# print("Попробуй угадать число от 0 до 5!")
# number = random.randint(0, 5)
# while attempts != 0:
       
#     user_number = int(input("Введи число: "))
#     if user_number == number:
#         print("Это верно, я загадал число", number)
#         break
       
#     else:
#         print('Не угадал')
#         attempts -= 1
#     if attempts == 0:
#         print('Ты проиграл!')
#     if attempts == 1 and number >= 3:
#         print('Даю тебе подсказку - число больше или равно трем')
#     if attempts == 1 and number < 3:
#         print('Даю тебе подсказку - число меньше трех')
import random 
number = int(input('Впиши число от 0 до 10: '))
count = 0
quest = ''
while quest != 'да':
    count = random.randint(0,10)
    print('Я думаю это число -', count)
    quest = input('Это верно?: ').lower()
print('Я угадал число!')