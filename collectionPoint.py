#2021
#Tyler Tobin (Tysco Software)
#Car Park System - Ticket collection point

'''
Press button
display spaces
take picture of numberplate
send numberplate to backend
and time and date
give ticket
open barrier

'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
from time import time, sleep
import time
from cv2 import *
import cv2 as cv2


class ticketCollection(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        
        self.master = master
        self.master.title("TPS ANPR")
        self.master.geometry("700x500+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(background = 'white')
        self.frame.configure(background = 'white')


        self.image1 = Image.open("pSign.png")
        self.resize_image = self.image1.resize((50, 50))
        self.parkingSign = ImageTk.PhotoImage(self.resize_image)

        self.label1 = Label(self.frame, image = self.parkingSign, bg = "white")
        self.label1.image = self.parkingSign
        self.label1.grid(row = 0, column = 0)

        self.headerTitle = Label(self.frame, text = "Tysco Parking Services", bg = "white", fg = "black", font = ("helvetica new", 25))
        self.headerTitle.grid(row = 0, column = 1, columnspan = 2, ipadx = 10, ipady = 16, padx = 20)
        
        self.label2 = Label(self.frame, image = self.parkingSign, bg = "white")
        self.label2.image = self.parkingSign
        self.label2.grid(row = 0, column = 3)

        self.currentTime = datetime.now()
        self.timeFormatted = self.currentTime.strftime("%H:%M")
        

        self.timeLabel = Label(self.frame, text = self.timeFormatted, font = ("helvetica new", 30), bg = "white", fg = "black")
        self.timeLabel.grid(row = 1, column = 1, pady = 20, columnspan = 2)


        self.spacesLabel = Label(self.frame, text = "0 Spaces", font = ("helvetica new", 30), bg = "white", fg = "black")
        self.spacesLabel.grid(row = 4, column = 1, columnspan = 2, pady = 20)

        self.ticketFree = Label(self.frame, text = "TICKET-FREE PARKING, PAY AFTER STAY", bg = "white", fg = "#00589c")
        self.ticketFree.grid(row = 2, column = 0, columnspan = 4)


        self.ticketButton = Button(self.frame, text = "Enter", command = self.takePicture, font = ("helvetica new", 50), bg = "blue", fg = "#00589c", width = 6)
        self.ticketButton.grid(row = 3, column = 1, columnspan = 2, pady = 20, padx = 5)


    def updateTime(self):
        self.now = time.strftime("%H:%M:%S")
        self.timeLabel.configure(text = self.now)
        self.after(1, self.updateTime)

    def takePicture(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if s: 
            namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
            imshow("cam-test",img)
            waitKey(0)
            destroyWindow("cam-test")
            imwrite("filename.jpg",img)
            



root = Tk()
app = ticketCollection(root)

root.after(1000, app.updateTime)
root.mainloop()




