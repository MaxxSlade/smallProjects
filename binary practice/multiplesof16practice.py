import random
import os
import time 
import sys


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


start_time = time.time()


def exit(curguess):
    if str(curguess).lower() == "exit":
        os.system("clear")
        sys.exit()

def genran():
    return nums[random.randint(0,14)]


correct = 0
incorrect = 0
print("You can enter 'exit' to stop the program.")
quantity = int(input("How many to do?:  "))

def score():
    print(f'''
    ============================================
    Correct guesses = {correct}
    Incorrect guesses = {incorrect}
    Problems left = {quantity - correct}
    Current time = {int(current_time - start_time)} seconds
    ============================================
    ''')


def guess():
    global correct, incorrect
    number = genran()
    print(f"{number} * 16 ?")
    curguess = input("Answer?: ")

    exit(curguess)

    try:
        curguess = int(curguess)
    except ValueError:
        print("Invalid input!")
        return

    if (number * 16) == curguess:
        correct += 1
        os.system("clear")
    else:
        incorrect += 1
        os.system("clear")
        print(f"Incorrect! Correct answer: {number*16}")
        time.sleep(2)
        os.system("clear")
        


while correct < quantity:
    current_time = time.time()
    score()
    guess()

if correct == quantity:
    end_time = time.time()
    os.system("clear")
    print("=" * 30)
    print(f"""
Final score:
Percentage correct: {"{:.2f}".format(100*(correct/(correct+incorrect)))}%
Time for {quantity} problems: {int(end_time-start_time)} seconds
    """)
    print("=" * 30)


    
