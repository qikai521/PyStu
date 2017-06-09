import random
print('*****cai  shu  zi********')
secrt = random.randint(1,10)
count = 0
temp = input("write point from 0 to 10 :")
guess = int(temp)
isFirst = True
if count >= 3:
    print('no moqi');
elif guess == secrt:
    print('you are right')
else:
    while count < 3 and guess != secrt:
        if isFirst == False:
            temp = input("write point from 0 to 10:")
            guess = int(temp)
        else :
            isFirst = False
        count += 1
        if guess > secrt:
            change = 3 - count
            print("is big more you have ")
        elif guess < secrt:
            print("is small more you have ")
    if count >= 3:
        print('no moqi');
    elif guess == secrt:
        print('you are right')
    else :
        print("game over")


