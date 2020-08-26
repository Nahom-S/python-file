import random

low = ["africa", "south america"]
good = ['europe', 'north america']
best = ["asia"]
while True:
    try:
        name = input("name: ")
        area = input("continent: ")
        age = input("age: ")
        if area.lower() in low:
            exc = random.randint(60, 77)
            time_Left = exc - int(age)
            print("hi " + name + " your time left is : " + str(time_Left) + " years!!!")
            print(exc)
        elif area.lower() in good:
            exc = random.randint(70, 87)
            time_Left = exc - int(age)
            print("hi " + name + " your time left is : " + str(time_Left) + " years!!!")
            print(exc)
        elif area.lower() in best:
            exc = random.randint(80, 95)
            time_Left = exc - int(age)
            print("hi " + name + " your time left is : " + str(time_Left) + " years!!!")
            print(exc)
        else:
            print("error")
    except ValueError:
        print("error")
