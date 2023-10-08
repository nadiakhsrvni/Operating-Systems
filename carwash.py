from threading import Semaphore, Thread
from time import sleep

n = int(input())

sem_enter = Semaphore(8)
sem_wash = Semaphore(2)
sem_dry = Semaphore(1)
sem_pay = Semaphore(1)

booth_A = True  # booth A is free
booth_B = True  # booth B is free


def enter_car_wash(car_number):
    sem_enter.acquire()
    print(f'Car {car_number} enters car wash')
    wash(car_number)
    sem_enter.release()


def wash(car_number):
    sem_wash.acquire()
    global booth_A
    global booth_B
    if  booth_A:
        print(f'Car {car_number} enters booth A')
        booth_A = False
        sleep(0.5)
        booth_A = True
    elif booth_B:
        print(f'Car {car_number} enters booth B')
        booth_B = False
        sleep(0.5)
        booth_B = True
    sem_wash.release()
    dry(car_number)


def dry(car_number):
    sem_dry.acquire()
    sleep(0.25)
    print(f'Car {car_number} dries')
    sem_dry.release()
    pay(car_number)


def pay(car_number):
    sem_pay.acquire()
    sleep(0.1)
    print(f'Car {car_number} pays and leaves')
    sem_pay.release()


if __name__ == '__main__':
    for i in range(1, n+1):
        t = Thread(target=enter_car_wash, args=(i,))
        t.start()
