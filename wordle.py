import time
from termcolor import colored
import getpass

wordle = getpass.getpass("Enter Wordle Word: ").lower()

if len(wordle) >= 6:
    print("Not a 5 letter word.")
    quit()
if len(wordle) <= 4:
    print("Not a 5 letter word.")
    quit()


def wait(sec):
    time.sleep(sec)

def wordcheck(var):
    global in1
    global in2
    global in3
    global in4 
    global in5
    global in6
    
    if var == "exit":
        quit()

    if len(var) >= 6:
        print("Not a 5 letter word.")
        quit()
    if len(var) <= 4:
        print("Not a 5 letter word.")
        quit()
    
    if var[0] == wordle[0]:
        print(colored(var[0], 'green'),end = ' ')
    elif var[0] in wordle:
        print(colored(var[0], 'yellow'),end = ' ')
    else:
        print(var[0], end = ' ')

    if var[1] == wordle[1]:
        print(colored(var[1], 'green'), end = ' ')
    elif var[1] in wordle:
        print(colored(var[1], 'yellow'), end = ' ')
    else:
        print(var[1], end = ' ')

    if var[2] == wordle[2]:
        print(colored(var[2], 'green'), end = ' ')
    elif var[2] in wordle:
        print(colored(var[2], 'yellow'), end = ' ')
    else:
        print(var[2], end = ' ')

    if var[3] == wordle[3]:
        print(colored(var[3], 'green'), end = ' ')
    elif var[3] in wordle:
        print(colored(var[3], 'yellow'), end = ' ')
    else:
        print(var[3], end = ' ')

    if var[4] == wordle[4]:
        print(colored(var[4], 'green'))
    elif var[4] in wordle:
        print(colored(var[4], 'yellow'))
    else:
        print(var[4])
    
    if var == wordle:
        wait(0.5)
        print("You Won!")
        quit()
    
in1 = input("First Guess: ").lower()
wait(0.5)
wordcheck(in1)
in2 = input("Second Guess: ").lower()
wait(0.5)
wordcheck(in2)
in3 = input("Third Guess: ").lower()
wait(0.5)
wordcheck(in3)
in4 = input("Forth Guess: ").lower()
wait(0.5)
wordcheck(in4)
in5 = input("Fifth Guess: ").lower()
wait(0.5)
wordcheck(in5)
in6 = input("Sixth Guess: ").lower()
wait(0.5)
wordcheck(in6)
print("It Was: "+colored(wordle, 'green'))
print("You Lost.")
quit()
