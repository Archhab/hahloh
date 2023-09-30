import random
randNum = random.randint(1,10)
for i in range(5):
    num = int(input('Угадай число от 0 до 10 '))
    print(num)
    if num == randNum:
        print('Ты победил')
        break
        
if i == 4:
    print('Ты проиграл')
