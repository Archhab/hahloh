import random
from time import sleep

side = random.randint(0,2)

hp=100
speed=0
dist=400

yatti=3
tree=2
rock=1
 
while True:

    chance = random.randint(0,3)
    if chance == rock:
         print("вы столкнулись c панк рокерами")
         a =int(input("куда вы повернёте \n ghfdj = 1 \n лево = 2  "))
         if side = a
         print(ЛОХ нитуда повернуд)
         hp -= 10
         

         hp-= 5
    elif chance == tree:
         print("вы столкнулись с бумагой")
         a =int(input("куда вы повернёте \n ghfdj = 1 \n лево = 2  "))
         if side = a
         print(ЛОХ нитуда повернуд)
         hp -= 10
         
    elif chance == yatti:
         print("вы столкнулись с  ети")
          a =int(input("куда вы повернёте \n ghfdj = 1 \n лево = 2  "))
         if side = a
         print(ЛОХ нитуда повернуд)
         hp -= 10

     


    speed+=1
    dist-=speed
    print("\nвы едите во скоросьтью",(speed), "m/s")
    print("вам осталось ехать",(dist))
    print('у вас',(hp),"жызний")
