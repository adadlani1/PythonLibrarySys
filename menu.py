from tkinter import*
'''import search2'''
import sys
import os

root = Tk()

def checkout():
    os.system('checkout.py') #defined the functions that are links to the buttons

def search():
    os.system('search2.py')
    '''searchWindow = Toplevel()
    outputlistBox = Listbox(searchWindow, width = 80).pack()
    inputTextbox = Entry(searchWindow).pack()
    searchWindow.geometry("800x200")
    label_1 = Label(searchWindow, text= "Please enter the name of the book")
    label_1.place(x=0,y=164)
    searchButton2 = Button(searchWindow, text = "Search")
    searchButton2.place(x=480, y=164)
    data = []
    with open('Database.txt') as f:
        for line in f:
            data += line.split()
    print(data)
    #Create your listbox here. 
    for i in range(len(data)):
        outputlistBox.insert(i+1, data[i])'''

    
def returnBook():
    os.system('bookreturn.py')

def weeding():
    os.system('weeding.py')

root.title("Anmol's Library System")
root.configure(background='red')

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

root.geometry("510x150")
root.mainloop()

