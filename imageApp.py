
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image App')
root.iconbitmap('')

myImage = ImageTk.PhotoImage(Image.open("images/bazmtn.jpg"))  # Image definition
myLab = Label(image=myImage)
myLab.grid(row=0, column=1, columnspan=1)

myImage2 = ImageTk.PhotoImage(Image.open("images/baz.png"))
myImage3 = ImageTk.PhotoImage(Image.open("images/Desert.jpg"))
myImage4 = ImageTk.PhotoImage(Image.open("images/Hydrangeas.jpg"))
myImage5 = ImageTk.PhotoImage(Image.open("images/passport.png"))
myImage6 = ImageTk.PhotoImage(Image.open("images/Penguins.jpg"))
myImage7 = ImageTk.PhotoImage(Image.open("images/ney.JPG"))

bigList = [myImage, myImage2, myImage3, myImage4, myImage5, myImage6, myImage7]

# Adding status bar
status = Label(root, text=f'Image 1 of {len(bigList)}', bd=1, relief=SUNKEN, anchor=E)
# anchor changes the direction; north, south, east, west
status.grid(row=2, column=1, sticky=W+E)


num = 1


def forward():

    global num, myLab, status
    myLab.grid_forget()  # remove a picture from the screen
    buttonBackward.config(state=ACTIVE)

    status = Label(root, text=f'Image {num+1} of {len(bigList)}', bd=1, relief=SUNKEN, anchor=E)
    myLab = Label(image=bigList[num])

    if num == len(bigList) - 1:
        buttonForward.config(state=DISABLED)
    num += 1

    myLab.grid(row=0, column=1)
    status.grid(row=2, column=1, sticky=W+E)
    return


def back():
    global num, myLab, status
    myLab.grid_forget()
    buttonForward.config(state=ACTIVE)

    status = Label(root, text=f'Image {num - 1} of {len(bigList)}', bd=1, relief=SUNKEN, anchor=E)
    # bd, relief gives a border and changes the label somehow
    myLab = Label(image=bigList[num-2])

    num -= 1
    if num == 1:
        buttonBackward.config(state=DISABLED)

    myLab.grid(row=0, column=1)
    status.grid(row=2, column=1, sticky=W+E)
    return


buttonForward = Button(root, text='>>>', command=forward)
buttonForward.grid(row=1, column=2)

buttonBackward = Button(root, text='<<<', command=back, state=DISABLED)
buttonBackward.grid(row=1, column=0, pady=10)  # pady gives it an extra space vertically

buttonQuit = Button(root, text='EXIT', padx=30, command=root.quit)
buttonQuit.grid(row=1, column=1)

root.mainloop()
