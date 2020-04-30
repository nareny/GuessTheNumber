import random

def practice():
    num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print("Please enter a number between 1 and 20:")
    user = int(input())
    valg = random.choice(num)

    if user == valg:
        print("User Value:", user)
        print("Random Value:", valg)
        print("You have guessed right!")
    elif user <= valg:
        print("Your guess is lower than the random number:",user)
        print("Random Value:",valg)
    elif user >= valg:
        print("You guess is higher than the random number:", user)
        print("Random Value:", valg)
    
practice()


