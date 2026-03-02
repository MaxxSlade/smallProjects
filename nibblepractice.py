import random
import os
import time 
import sys


nums = ["0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]


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
    print(f"{number}")
    curguess = input("Answer in decimal?: ")

    exit(curguess)

    try:
        curguess = int(curguess)
    except ValueError:
        print("Invalid input!")
        return

    if (int(number, 2)) == curguess:
        correct += 1
        os.system("clear")
    else:
        incorrect += 1
        os.system("clear")
        print(f"Incorrect! Correct answer: {int(number, 2)}")
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


    
