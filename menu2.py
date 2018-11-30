import sys
import os
# first step is to greet the user and ask them what they would like to do
first_step = input("Hello and welcome to the Library System.\nWhat would you like to do?\nType 'search' to find a book\nType 'checkout' to take a book out\nType 'return' to return a book\n").strip() 

#now writing an if statement which loads different .py files that corresponds to the input from first_step

def search():
    os.system('search2.py')

def checkout():
    os.system('checkout.py')

def return():
    os.system('return.py')

if first_step == "search":
    search()
    
elif first_step == "checkout":
    checkout()
    
elif first_step == "return":
    return()

    
