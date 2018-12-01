ffrom tkinter import*
import sys
import os

root = Tk()

def checkout():
    os.system('checkout.py') #defined the functions that are links to the buttons

def search():
    os.system('search2.py')

def returnBook():
    os.system('bookreturn.py')

def weeding():
    os.system('weeding.py')

root.title("Anmol's Library System")

searchButton = Button(root, text = "Search", command = search)
searchButton.place(x = 100, y = 75)

checkoutButton = Button(root, text = "Checkout", command = checkout)
checkoutButton.place(x = 175, y = 75)

introMsg = Label(root, text = "Hello\nWelcome to Anmol's Library System. Please chose from the following what you would like to do\nwith your book.")
introMsg.place(x = 0, y = 0)

returnButton = Button(root, text = "Return", command = returnBook)
returnButton.place(x = 275, y = 75)

weedingButton = Button(root, text = "Weeding", command = weeding)
weedingButton.place(x = 350, y = 75)

root.geometry("525x150")
root.mainloop()
