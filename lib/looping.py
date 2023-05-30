#!/usr/bin/env python3
#using a while loop that outputs numbers starting at 10 and counting down to 1. 
#After reaching 1, print out "Happy New Year!
def happy_new_year():
    countdown = 10 
    while countdown in range (10, 0, -1):
        print(countdown)
        countdown -=1 
        print("Happy New Year!")

#takes one argument, a list of integers and returns the list of squared elements.
def square_integers(int_list):
    return [i ** 2 for i in int_list]


def fizzbuzz():
    for i in range(1,101): #prints number 1-100
        if not i % 15: 
            print("FizzBuzz") 
        elif not i % 5: # 
            print("Buzz")
        elif not i % 3: #mutiples of 3 print out fizz 
            print("Fizz")
        else:
            print(i)

