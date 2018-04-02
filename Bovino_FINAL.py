#Connor Bovino
#Connor.Bovino@gmail.com
#December 13
#Flight Reservation System

from tkinter import *
import pymysql


class Main:

#__init__ with login Menu
    def __init__(self, Master):

        #master window and closing tk()
        self.master = Master
        self.master.withdraw()

        # database Connector
        self.connector = pymysql.connect(
            host='localhost',
            port=3306, user='me',
            passwd='me',
            db="FlightReservation",
            autocommit=True
        )
        #database cursors used throughout program
        self.db1 = self.connector.cursor()
        self.db2 = self.connector.cursor()
        self.db3 = self.connector.cursor()
        self.db4 = self.connector.cursor()
        self.db5 = self.connector.cursor()
        self.db6 = self.connector.cursor()
        self.db7 = self.connector.cursor()
        self.db8 = self.connector.cursor()
        self.db9 = self.connector.cursor()
        self.db10 = self.connector.cursor()
        self.db11 = self.connector.cursor()
        self.db12 = self.connector.cursor()
        self.db13 = self.connector.cursor()
        self.db14 = self.connector.cursor()
        self.db15 = self.connector.cursor()
        self.db16 = self.connector.cursor()

        #open the login window
        self.login()
#login window
    def login(self):
        self.login1 = Toplevel()

        #labels and entrys for username and password
        self.username  = Label(self.login1, text="User Name:")
        self.username.pack()
        self.unentry = Entry(self.login1)
        self.unentry.pack()

        self.password = Label(self.login1, text="Password:")
        self.password.pack()
        self.passentry = Entry(self.login1)
        self.passentry.pack()

        #Button to click login and open create a user page
        self.loginbutton = Button(self.login1, text="Login", command=self.loginattempt)
        self.loginbutton.pack()

        self.createaccountbutton = Button(self.login1, text="Create Airline Account", command=self.createaccountwindow)
        self.createaccountbutton.pack()

#opens up form to create account, connects to database as well
    def createaccountwindow(self):
        self.ca = Toplevel()

        #full name label and entry
        fullnamelabel = Label(self.ca, text="Full name: ex (Connor Bovino):")
        fullnamelabel.pack()
        self.fn = Entry(self.ca)
        self.fn.pack()

        # Birthday label and entry
        BirthdayLabel = Label(self.ca, text="Birthday: use hypen ex(03-14-1997")
        BirthdayLabel.pack()
        self.bd = Entry(self.ca)
        self.bd.pack()

        #Creditcard label and entry
        creditcardlabel = Label(self.ca, text="Credit Card:")
        creditcardlabel.pack()
        self.cc = Entry(self.ca)
        self.cc.pack()

        #username label and entry
        username1 = Label(self.ca, text="User Name:")
        username1.pack()
        self.un = Entry(self.ca)
        self.un.pack()

        #password label and entry
        password1 = Label(self.ca, text="Password:")
        password1.pack()
        self.pw = Entry(self.ca)
        self.pw.pack()

        #submit form button
        submit = Button(self.ca, text="Submit", command=self.submitform)
        submit.pack()

#submit form button, connected to database
    def submitform(self):
        #gettting all the entry info
        name = self.fn.get()
        uncheck = self.un.get()
        birth1 = self.bd.get()
        cc1 = self.cc.get()
        pw1 = self.pw.get()

        #checking if Username in data/ else add to data
        self.db1.execute('SELECT Full_Name, Birthday, Credit_Card, User_Name, Password From Airline_Account')
        all = self.db1.fetchall()



        for tuple in all:
            if tuple[1] == name and tuple[4] == uncheck:
                print("Unable to create account")
        else:
            self.db1.execute("""
            insert into Airline_Account (Full_Name, Birthday, Credit_Card, User_Name, Password)\
            values
            (%s, %s, %s, %s, %s)

            """, (name, birth1, cc1, uncheck, pw1))
            self.ca.destroy()

    def loginattempt(self):
        #getting entry info for login screen
        self.username = self.unentry.get()
        self.password = self.passentry.get()

        # check if username and password is in the database
        self.db1.execute('SELECT Full_Name, Birthday, Credit_Card, User_Name, Password From Airline_Account')
        all = self.db1.fetchall()

        for tuple in all:
            if tuple[3] == self.username and tuple[4] == self.password:
                    self.mainwindow()
                    self.login1.destroy()

            if tuple[3] == self.username and tuple[4] == self.password not in all:
                print("Failed Attempt")

    def mainwindow(self):
        self.mw = Toplevel()

        #Make a Reservation Button
        self.MARbutton = Button(self.mw, text="Make a Reservation", command=self.MAR)
        self.MARbutton.pack()

        #Tickets Button
        self.Ticketsbutton = Button(self.mw, text="Tickets", command=self.Tickets)
        self.Ticketsbutton.pack()

        #Flight Button
        self.Flightsbutton = Button(self.mw, text="Flights", command=self.Flights)
        self.Flightsbutton.pack()

        #Planes Button
        self.Planesbutton = Button(self.mw, text="Planes", command=self.Planes)
        self.Planesbutton.pack()

        #Changes account info
        self.CAinfobutton = Button(self.mw, text= "Change Account Information", command=self.CAinfo)
        self.CAinfobutton.pack()

#Make a Reservation
    def MAR(self):
        self.mar = Toplevel()

        #database selecting departure airport
        self.db1.execute('SELECT Departure_Airport FROM Flight')
        DAall = self.db1.fetchall()
        DAlist = []
        for tuple in DAall:
            if tuple not in DAlist:
                DAlist.append(tuple)

        #database selecting Destination
        self.db1.execute('SELECT Destination FROM Flight')
        Dall = self.db1.fetchall()
        Dlist = []
        for tuple in Dall:
            if tuple not in Dlist:
                Dlist.append(tuple)

        #database selecting time
        self.db1.execute('SELECT Departure_time FROM Flight')
        Tall = self.db1.fetchall()
        Tlist = []
        for tuple in Tall:
            if tuple not in Tlist:
                Tlist.append(tuple)


        self.makesure = Label(self.mar, text="Make Sure Flight is Available through SQL or Create New Flight:")
        self.makesure.pack()
        #labels and popupmenu for Departing
        self.MARLabel = Label(self.mar, text="Choose a Departing Airport")
        self.MARLabel.pack()
        self.MARVALUE = StringVar(self.mar)
        self.MARMENU = OptionMenu(self.mar, self.MARVALUE, *DAlist)
        self.MARMENU.pack()

        #labels and popupmenu for Destination
        self.DallLabel = Label(self.mar, text="Choose a Destination Airport")
        self.DallLabel.pack()
        self.DallVALUE = StringVar(self.mar)
        self.DallMENU = OptionMenu(self.mar, self.DallVALUE, *Dlist)
        self.DallMENU.pack()

        # labels and popupmenu for Time
        self.TallLabel = Label(self.mar, text="What Time?")
        self.TallLabel.pack()
        self.TallVALUE = StringVar(self.mar)
        self.TallMENU = OptionMenu(self.mar, self.TallVALUE, *Tlist)
        self.TallMENU.pack()

        #button to Make Reservation
        self.MARbutton2 = Button(self.mar, text="Submit Reservation", command=self.submitreservation)
        self.MARbutton2.pack()

#Takes the users selections then searches through flight database
    def submitreservation(self):
        #gets all the string variables
        MARVALUE1 = self.MARVALUE.get()
        DallVALUE1 = self.DallVALUE.get()
        TallVALUE1 = self.TallVALUE.get()

        #selects flight number with users values
        self.db2.execute("""
        Select Flight_Number FROM FLIGHT
        Where Departure_Airport = %s AND Destination = %s AND Departure_time = %s
        """, (MARVALUE1[1:6], DallVALUE1[1:6], TallVALUE1[1:11]))

        #Flight number
        self.all2 = self.db2.fetchone()

        #Gets Airline Account Number
        self.db3.execute("""
        Select Account_Number FROM Airline_Account
        Where User_Name = %s
        """, (self.username))

        #account number
        self.unaccount = self.db3.fetchone()

        #inserts into reservation
        self.db2.execute("""
        insert into Reservation(Account_Number)
        values (%s)
        """, (self.unaccount))

        #destroys page
        self.mar.destroy()

#gets reservations from usernames
    def Tickets(self):
        self.tix = Toplevel()

        #gets airline account number and saves it to aanumber
        self.db6.execute("""
        Select Account_Number FROM Airline_Account
        Where User_Name = %s
        """, (self.username))
        self.aanumber = self.db6.fetchone()

        self.db15.execute("""Select Flight_Number FROM Flight""")
        self.flnumlist = self.db15.fetchall()

        self.flnumlist1 = []
        for item in self.flnumlist:
            self.flnumlist1.append(item)


        #gets all from users reservations
        self.db4.execute("""
        Select Reservation_ID From Reservation
        Where Account_Number = %s
        """, (self.aanumber))

        self.dbreservations = self.db4.fetchall()

        self.reservationumbers = []
        for item in self.dbreservations:
            self.reservationumbers.append(item)

        self.rezlabel = Label(self.tix, text="Select a Reservation ID to Delete Ticket")
        self.rezlabel.pack()

        self.reservationoptionmenuvalue = StringVar()
        self.reservationoptionmenu = OptionMenu(self.tix, self.reservationoptionmenuvalue, *self.reservationumbers)
        self.reservationoptionmenu.pack()
        self.deleteticketbutton = Button(self.tix, text="Delete Ticket", command= self.removeticketandreservation)
        self.deleteticketbutton.pack()

        self.displaytick = Label(self.tix, text="Select Flight Number to show ticket")
        self.displaytick.pack()

        self.flnumtick1 = StringVar()
        self.flnumtick = OptionMenu(self.tix, self.flnumtick1, *self.flnumlist1)
        self.flnumtick.pack()


        self.ticketdisplaybutton = Button(self.tix, text="Click to Display Ticket", command=self.tickets2)
        self.ticketdisplaybutton.pack()


        #gets all flight from users reservations

#displays ticket
    def tickets2(self):

        self.po = self.flnumtick1.get()

        self.db16.execute("""
        Select Departure_Airport, Destination, Departure_Time From Flight
        Where Flight_Number = %s
        """, (self.po[1]))

        self.p1 = self.db16.fetchall()

        self.defeat = Label(self.tix, text="Check the IDE for Your printed Ticket!")
        self.defeat.pack()

        print(self.p1)



#deleting reservation and ticket
    def removeticketandreservation(self):
        self.deleteit1 = self.reservationoptionmenuvalue.get()

        self.db13.execute("""
        DELETE FROM RESERVATION
        WHERE Reservation_ID = %s
        """, (self.deleteit1[1]))

        self.tix.destroy()

#starts add and change flight pages
    def Flights(self):
        self.flightchoice = Toplevel()

        self.addflightbutton = Button(self.flightchoice, text="Add a Flight", command=self.addflight)
        self.addflightbutton.pack()

        self.editflightbutton = Button(self.flightchoice, text="Edit a Flight", command=self.editflight)
        self.editflightbutton.pack()


# add a flight
    def addflight(self):
        self.addflight = Toplevel()

        self.departurelabel = Label(self.addflight, text="Type a Departure Airport: Must Use Three letter Airport Code")
        self.departurelabel.pack()
        self.departureentry = Entry(self.addflight)
        self.departureentry.pack()

        self.destinationlabel = Label(self.addflight, text="Type a Destination: Must Use Three letter Airport Code")
        self.destinationlabel.pack()
        self.destinationentry = Entry(self.addflight)
        self.destinationentry.pack()

        self.timing = Label(self.addflight, text='Type a time: Follow Example 07:00AM')
        self.timing.pack()
        self.timingentry = Entry(self.addflight)
        self.timingentry.pack()

        self.selectplanelabel = Label(self.addflight, text= "Select a Plane: Their Must be a Plane Available."
                                                            "If No planes available make another one under planes"
                                                            "Flight_ID Plane_Type")
        self.selectplanelabel.pack()

        self.db10.execute("""SELECT Plane_ID FROM Planes""")

        self.planeid= self.db10.fetchall()
        listforplanes = []
        for i in self.planeid:
            listforplanes.append(i)

        print(listforplanes)

        self.planesmenu = StringVar()
        self.planemenu1 = OptionMenu(self.addflight, self.planesmenu, *listforplanes)
        self.planemenu1.pack()

        self.submitaddplane = Button(self.addflight, text="Add Flight", command=self.addflightdatabase)
        self.submitaddplane.pack()

    def addflightdatabase(self):
        entrydf = self.departureentry.get()
        entryd = self.destinationentry.get()
        entrytime = self.timingentry.get()
        planeid = self.planesmenu.get()

        self.db11.execute("""
        insert into Flight(Departure_Airport, Destination, Departure_Time, Plane_ID)
        values
        (%s, %s, %s, %s)

        """, (entrydf, entryd, entrytime, planeid[1:4]))

        self.addflight.destroy()


# edit a flight
    def editflight(self):
        self.editflight = Toplevel()

        self.editflightlabel = Label(self.editflight, text="Type the Flight Number in which is going to be edited:")
        self.editflightlabel.pack()

        self.flightnumberentry = Entry(self.editflight)
        self.flightnumberentry.pack()

        self.departurelabel2 = Label(self.editflight, text="Edit a Departure Airport: Must Use Three letter Airport Code")
        self.departurelabel2.pack()
        self.departureentry2 = Entry(self.editflight)
        self.departureentry2.pack()

        self.destinationlabel2 = Label(self.editflight, text="Edit a Destination: Must Use Three letter Airport Code")
        self.destinationlabel2.pack()
        self.destinationentry2 = Entry(self.editflight)
        self.destinationentry2.pack()

        self.timing2 = Label(self.editflight, text='Edit a time: Follow Example 07:00AM')
        self.timing2.pack()
        self.timingentry2 = Entry(self.editflight)
        self.timingentry2.pack()

        self.submitchangefl = Button(self.editflight, text="Submit Flight Change", command= self.editflightdatabase)
        self.submitchangefl.pack()


    def editflightdatabase(self):
        self.flightnumberentry1 = int(self.flightnumberentry.get())
        self.departureentry3 = self.departureentry2.get()
        self.destinationentry3 =self.destinationentry2.get()
        self.timing3 = self.timingentry2.get()

        print(self.flightnumberentry1)

        self.db12.execute("""
        Update Flight
            SET Departure_Airport = %s, Destination = %s, Departure_Time = %s
            WHERE Flight_Number = %s;
        """, (self.departureentry3, self.destinationentry3, self.timing3, self.flightnumberentry1))

        self.editflight.destroy()


#method to add planes for more flights
    def Planes(self):
        self.plane =Toplevel()

        # list and dictionary with drop down menu info
        self.listofplanebrands = ["Airbus", "Boeing", "Bombardier", "Cessna Aircraft", "Hawker", "Gulfstream"]
        self.dictofmodelandoccupancy = {"747": "350", "767": "400", "777": "450", "787" : "500"}

        #plane brand option menu
        planebrandlabel = Label(self.plane, text = "Select the Brand of Aircraft")
        planebrandlabel.pack()
        self.planebrand = StringVar(self.plane)
        self.planebrandmenu = OptionMenu(self.plane, self.planebrand, *self.listofplanebrands)
        self.planebrandmenu.pack()

        #model option menu
        modellabel = Label(self.plane, text = "Select the Model")
        modellabel.pack()
        self.model = StringVar(self.plane)
        self.modelmenu = OptionMenu(self.plane, self.model, *list(self.dictofmodelandoccupancy.keys()))
        self.modelmenu.pack()

        #add plane button
        planebutton = Button(self.plane, text="Click to add plane", command =self.addplane)
        planebutton.pack()

    def addplane(self):
        #gets user choices
        planebrand=self.planebrand.get()
        model=self.model.get()
        occupancy = self.dictofmodelandoccupancy.get(model)


        #adds info to database
        self.db9.execute("""
        Insert into Planes (Plane_type, Occupancy)
        Values (%s, %s)
        """, (planebrand + " " + model, occupancy))
        print("Plane Added")
        self.plane.destroy()


    def CAinfo(self):
        self.CAchange = Toplevel()

        # confirm previous password label and entry
        confirmpass = Label(self.CAchange, text="Confirm Previous Password:")
        confirmpass.pack()
        self.confirmpass1 = Entry(self.CAchange)
        self.confirmpass1.pack()

        #change Creditcard label and entry
        creditcardlabel2 = Label(self.CAchange, text="New Credit Card:")
        creditcardlabel2.pack()
        self.ccchange = Entry(self.CAchange)
        self.ccchange.pack()

        #username label and entry
        username2 = Label(self.CAchange, text="New UserName:")
        username2.pack()
        self.unchange = Entry(self.CAchange)
        self.unchange.pack()

        #new pass
        password2 = Label(self.CAchange, text="New Password")
        password2.pack()
        self.pwchange = Entry(self.CAchange)
        self.pwchange.pack()

        #must fill all fields and then click submit button
        must = Label(self.CAchange, text="All Fields Required, then Click Submit")
        must.pack()
        must1 = Button(self.CAchange, text= "Submit Changes", command=self.changeaccount)
        must1.pack()

#Method to submit changes to account
    def changeaccount(self):

        #gets all the entries from CAinfo
        self.unchange1 = self.unchange.get()
        self.pwchange1 = self.pwchange.get()
        self.ccchange1 = self.ccchange.get()
        self.oldpass = self.confirmpass1.get()

        #gets account number
        self.db8.execute("""
        Select Account_Number From Airline_Account
        Where User_Name = %s""", (self.username))
        aanumber2 = self.db8.fetchone()


        #Comparing passwords, label for incorrect password
        if self.password != self.oldpass:
            w = Label(self.CAchange, text="Incorrect Password, Please try again!")
            w.pack()
        #else, updates if password correct and labels updated
        else:
            self.db7.execute("""
            UPDATE Airline_Account
            SET Credit_Card = %s, User_Name = %s, Password = %s
            WHERE Account_Number = %s
            """, (self.ccchange1, self.unchange1, self.pwchange1, aanumber2))

            w = Label(self.CAchange, text= "Updated")
            w.pack()


root = Tk()
my_gui = Main(root)
root.mainloop()

