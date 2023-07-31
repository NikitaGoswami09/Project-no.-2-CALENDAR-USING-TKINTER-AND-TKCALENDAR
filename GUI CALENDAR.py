from tkinter import*
from tkcalendar import Calendar

# creating an object of tkinter

tkobj = Tk()

#setting up the dimensions

tkobj.geometry("400*400")
tkobj.title("Calendar date picker")

#creating a calendar object

tkc=Calendar(tkobj,selectmode="day",year=2022,month=1,date=1)

#display on main window
tkc.pack(pady=40)

# getting the date from the calendar

def fetch_date():
    date.config(text="The date you selected is:"+tkc.get_date())

# add button to load the date clicked on the calendar date picker
but=Button(tkobj,text="Select Date",command=fetch_date,bg="black",fg='white')

#displaying button on the main display

but.pack()

#label for showing date on main display

date=Label(tkobj,text="",bg='black',fg='white')
date.pack(pady=20)

#starting the object

tkobj.mainloop()