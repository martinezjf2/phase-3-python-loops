#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    i = 10
    while (i > 0):
        print(i)
        i = i -1
    print("Happy New Year!")
    

def reverse_string(string):
    # code goes here
    a = ''
    for i in string:
        a = i + a
    return a

def fizzbuzz():
    # code goes here
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0:
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
       
        print(str(i))
    # pass
