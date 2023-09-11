#Tyler Tobin (Tysco Software)
#Car Park System - Backend
'''
Recognise letters/numbers
save number plate in database with metadata
Store new number of available spaces
'''

#open database
#text recognise image number plate
#store plate and time in db


import sqlite3
from datetime import datetime


class carManagement:
    def __init__(self):

        self.connection = sqlite3.connect("cars.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cars (Plate TEXT, Time TEXT, Paid TEXT)")
        
        #will be made to be got from database, if entries in database == 0 set noofcars to 0
        self.noOfCars = 0

    def addCar(self, numberPlate):
        
        self.time = datetime.now()
        self.numberPlateTxt = numberPlate
        self.paidInit = "0"

        self.connection.execute("INSERT INTO cars (Plate, Time, Paid) VALUES(?, ?, ?)", (self.numberPlateTxt, self.time, self.paidInit))
        
        self.connection.commit()
        self.connection.close()

    def removeCar(self, numberPlate):
        pass

    def paymentRecieved(self):
        pass
        
obj = carManagement()
obj.addCar("LB71 OEN")
