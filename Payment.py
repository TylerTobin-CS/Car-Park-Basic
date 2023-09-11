#2021
#Tyler Tobin (Tysco Software)
#Car Park System - Payment Selection

'''
Enter Number plate
check how long they have stayed
pay then grant access to leave

'''
from tkinter import *
import tkinter
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
from time import time, sleep
import time

from tkinter import ttk

class paymentScreen:

    
                
    def __init__(self, master):
        self.master = master
        self.master.title("TPS Payment")
        self.master.geometry("900x500")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(background = "white")
        self.frame.configure(background = "white")

        self.image1 = Image.open("pSign.png")
        self.resize_image = self.image1.resize((50, 50))
        self.parkingSign = ImageTk.PhotoImage(self.resize_image)

        self.headerTitle = Label(self.frame, text = "Tysco Parking Service", bg = "white", fg = "black", font = ("helvetica new", 25))
        self.headerTitle.grid(row = 0, column = 2, columnspan = 2, ipadx = 10, ipady = 30)
        
        self.label2 = Label(self.frame, image = self.parkingSign, bg = "white")
        self.label2.image = self.parkingSign
        self.label2.grid(row = 0, column = 1)
        

        self.label1 = Label(self.frame, image = self.parkingSign, bg = "white")
        self.label1.image = self.parkingSign
        self.label1.grid(row = 0, column = 4)


        self.entryFrame = Frame(self.frame, bg = "white")
        self.entryFrame.grid(row = 1, column = 0, columnspan = 6, pady = 25)

        self.textEntered = "Enter Plate"


        self.plateEntry = Entry(self.entryFrame, text = self.textEntered, bg = "grey", fg = "#d9d9d9", width = 20, font = ("helvetica new", 15))
        self.plateEntry.grid(row = 0, column = 0, padx = 5, ipady = 10)

        self.checkPlate = Button(self.entryFrame, text = "Proceed", fg = "black", command = self.checkTicket, width = 10, height = 2, font = ("helvetica new", 15))
        self.checkPlate.grid(row = 0, column = 1, padx = 5)


        self.keyFrame = Frame(self.frame, bg = "white")
        self.keyFrame.grid(row = 2, column = 0, pady = 25, columnspan = 6)

 

        

        self.buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                   "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                   "T", "U", "V", "W", "Y", "X", "Z", "CLEAR"]


        varRow = 2
        varColumn = 0

        for button in self.buttons:
            command = lambda x = button: self.select(x)
            if button != "space":
                tkinter.Button(self.keyFrame, text = button, command = command, width = 5).grid(row = varRow, column = varColumn)






            varColumn += 1
            if varColumn > 10:
                varColumn = 0
                varRow += 1
            if varColumn >10:
                varColumn = 0
                varRow += 1
            if varColumn >9:
                varColumn = 0
                varRow += 1

    def select(self, value):
        if value == "CLEAR":
            entry2 = self.plateEntry.get()
            pos = entry2.find("")
            pos2 = entry2[pos:]
            self.plateEntry.delete(0, END)
        else:
            self.plateEntry.insert(tkinter.END, value)

    def carValid(self):
        pass
        #if numberplate in database:
            #proceed to payment screen
        #put this function in backend in future

    def checkTicket(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = ticketPayment(self.newWindow, str(self.plateEntry.get()))


#===========================================================================

class ticketPayment:
    def __init__(self, master, plate):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.title("TPS Payment")
        self.master.geometry("900x500")
        self.master.configure(background = "white")
        self.frame.configure(background = "white")

        
        self.image1 = Image.open("pSign.png")
        self.resize_image = self.image1.resize((50, 50))
        self.parkingSign = ImageTk.PhotoImage(self.resize_image)

        self.headerTitle = Label(self.frame, text = "Tysco Parking Service", bg = "white", fg = "black", font = ("helvetica new", 25))
        self.headerTitle.grid(row = 0, column = 2, columnspan = 2, ipadx = 10, ipady = 30)

                
        self.label2 = Label(self.frame, image = self.parkingSign, bg = "white")
        self.label2.image = self.parkingSign
        self.label2.grid(row = 0, column = 1)
        

        self.label1 = Label(self.frame, image = self.parkingSign, bg = "white")
        self.label1.image = self.parkingSign
        self.label1.grid(row = 0, column = 4)

        self.carLabel = Label(self.frame, text = "CAR:")
        self.entryTimeLabel = Label(self.frame, text = "ENTRY:")
        self.priceLabel = Label(self.frame, text = "PRICE:")
        self.helpButton = Button(self.frame, text = "HELP")
        self.payButton = Button(self.frame, text = "PAY", command = self.tapScreen)

        self.carEntered = Label(self.frame, text = plate)
        

        self.carLabel.grid(row = 1, column = 1)
        self.entryTimeLabel.grid(row = 2, column = 1)
        self.priceLabel.grid(row = 3, column = 1)
        self.helpButton.grid(row = 4, column = 1)
        self.payButton.grid(row = 4, column = 2)

        self.carEntered.grid(row = 1, column = 2)
        


    def tapScreen(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = tapPayment(self.newWindow)


class tapPayment(tk.Tk):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.title("TPS Payment (external)")
        self.master.geometry("900x500")
        self.master.configure(background = "white")
        self.frame.configure(background = "white")

        self.image1 = Image.open("contactless.png")
        self.resize_image = self.image1.resize((250, 150))
        self.contactlessSign = ImageTk.PhotoImage(self.resize_image)


        self.pdqFrame = Frame(self.frame, bg = "black")
        self.pdqFrame.grid(row = 0, column = 0)

        self.tysPayLabel = Label(self.pdqFrame, text = "TYSPAY", bg = "black", fg = "grey")
        self.tysPayLabel.grid(row = 0, column = 0, columnspan = 4)

        self.tapButton = Button(self.pdqFrame, image = self.contactlessSign, command = self.contactTapped)
        self.tapButton.grid(row = 1, column = 0, padx = 20, pady = 20, columnspan = 4)

        self.payDot1 = Label(self.pdqFrame, text = " ", bg = "grey")
        self.payDot1.grid(row = 2, column = 0)

        self.payDot2 = Label(self.pdqFrame, text = " ", bg = "grey")
        self.payDot2.grid(row = 2, column = 1)

        self.payDot3 = Label(self.pdqFrame, text = " ", bg = "grey")
        self.payDot3.grid(row = 2, column = 2)

        self.payDot4 = Label(self.pdqFrame, text = " ", bg = "grey")
        self.payDot4.grid(row = 2, column = 3)

    def contactTapped(self):
        self.payDot1.configure(bg = "green")
                
        self.payDot2.configure(bg = "green")
        self.payDot3.configure(bg = "green")
        self.payDot4.configure(bg = "green")
        self.exitLabel = Label(self.frame, text = "PAYMENT SUCCESSFUL, YOU MAY NOW EXIT", bg = "white", fg = "green")
        self.exitLabel.grid(row = 1, column = 0, pady = 10)
        self.nextButton = Button(self.frame, text = "Next Customer", command = self.goHome, bg = "white", width = 15, height = 3)
        self.nextButton.grid(row = 2, column = 0, pady = 10)


    def goHome(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = paymentScreen(self.newWindow)





root = Tk()
app = paymentScreen(root)
