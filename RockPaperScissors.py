import threading
import time
import random

rps=(" Камень "," Ножницы "," Бумага ")
score=[0,0]
def player1(i):
    global p1
    p1=0
    for i in range(i):
        p1=random.randint(0,2)
        print("1:  ",rps[p1])
        time.sleep(2)
def player2(i):
    global p2
    p2=0
    for i in range(i):
        p2=random.randint(0,2)
        print("2:  ",rps[p2],"\n")
        time.sleep(2)
def game(t):
    for i in range(t):
        if p1<p2:
            if p1==0 and p2==2:
                score[1]+=1
            else:
                score[0]+=1
        if p1>p2:
            if p1==2 and p2==0:
                score[0]+=1
            else:
                score[1]+=1
        print(score)
        time.sleep(2.01)
def main(i):
    myThread1=threading.Thread(target=player1,args=(i,))
    myThread2=threading.Thread(target=player2,args=(i,))
    myThread3=threading.Thread(target=game,args=(i,))
    myThread1.start()
    time.sleep(0.02)
    myThread2.start()
    time.sleep(0.02)
    myThread3.start()
main(10)
