from tkinter import *


root = Tk()

# defined the functions that are links to the buttons


def checkout():
    import checkout
    checkout.main()


def search():
    import search2
    search2.search()


def returnBook():
    import bookreturn
    bookreturn.main()


def weeding():
    import weeding
    weeding.main()


def main():
    root.title("Anmol's Library System")
    root.configure(background='#808080')

    searchButton = Button(root, text = "Search", command = search)
    searchButton.place(x = 150, y = 75)

    canvas = Canvas(root, width=739, height=55, bg = "black")
    canvas.pack()


    line = canvas.create_line(0,0,0,0)

    checkoutButton = Button(root, text = "Checkout", command = checkout)
    checkoutButton.place(x=280, y=75)

    introMsg = Label(root, text="Hello,\n"
                            "Welcome to Anmol's Library System. "
                            "Please chose from the following what you would like to do"
                            "\nwith your book.", bg='#9932CC', font = ("FIXEDSYS", 12))
    introMsg.place(x = 0, y = 0)

    returnButton = Button(root, text = "Return", command = returnBook)
    returnButton.place(x = 425, y = 75)

    weedingButton = Button(root, text = "Weeding", command = weeding)
    weedingButton.place(x = 550, y = 75)

    root.geometry("739x110")
    root.mainloop()

main()