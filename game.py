import random
from time import sleep

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
         hp-= 5
    elif chance == tree:
         print("вы столкнулись с бумагой")
         hp-= 5
    elif chance == yatti:
         print("вас сьел ети")
         hp-= 5

     


    speed+=1
    dist-=speed
    print("\nвы едите во скоросьтью",(speed), "m/s")
    print("вам осталось ехать",(dist))
    print('у вас',(hp),"жызний")


    if(dist<=0):
        print('Ура победа')
        break
    
    
    if(hp<=0):
            print("ты проиграл")
            break
    sleep(0.5)
