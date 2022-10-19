from tkinter import*
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root= Tk()
root.geometry("600x500")
clock_image= ImageTk.PhotoImage(Image.open("clock.jpg"))

india_label= Label(root,text= "India")
india_label.place(relx= 0.2, rely= 0.05, anchor= CENTER)

india_clock= Label(root)
india_clock["image"]= clock_image
india_clock.place(rel= 0.2,rely=0.35,anchor=CENTER)

india_time= Label(root)
india_time.place(relx=0.2,rely=0.65,anchor=CENTER)

usa_label= Label(root,text= "USA")
usa_label.place(relx= 0.7, rely= 0.05, anchor= CENTER)

usa_clock= Label(root)
usa_clock["image"]= clock_image
usa_clock.place(rel= 0.7,rely=0.35,anchor=CENTER)

usa_time= Label(root)
usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)

japan_label= Label(root,text= "Japan")
japan_label.place(relx= 0.8, rely= 0.05, anchor= CENTER)

japan_clock= Label(root)
japan_clock["image"]= clock_image
japan_clock.place(rel= 0.8,rely=0.35,anchor=CENTER)

japan_time= Label(root)
japan_time.place(relx=0.8,rely=0.65,anchor=CENTER)

australia_label= Label(root,text= "Australia")
australia_label.place(relx= 0.9, rely= 0.05, anchor= CENTER)

australia_clock= Label(root)
australia_clock["image"]= clock_image
australia_clock.place(rel= 0.9,rely=0.35,anchor=CENTER)

australia_time= Label(root)
australia_time.place(relx=0.9,rely=0.65,anchor=CENTER)


class India():
    def times():
        home= pytz.timezone("Asia/Kolkata")
        local_time= datetime.now(home)
        current_time= localtime.strftime("%H:%M:%S")
        india_time["text"]= "Time:"+ current_time
        india_time.after(200,self.times)

class USA():
    def times():
        home= pytz.timezone("US/CEntral")
        local_time= datetime.now(home)
        current_time= localtime.strftime("%H:%M:%S")
        usa_time["text"]= "Time:"+ current_time
        usa_time.after(200,self.times)
        
class Japan():
    def times():
        home= pytz.timezone("Japan")
        local_time= datetime.now(home)
        current_time= localtime.strftime("%H:%M:%S")
        japan_time["text"]= "Time:"+ current_time
        japan_time.after(200,self.times)
        

class Australia():
    def times():
        home= pytz.timezone("Australia")
        local_time= datetime.now(home)
        current_time= localtime.strftime("%H:%M:%S")
        australia_time["text"]= "Time:"+ current_time
        australia_time.after(200,self.times)
        
obj_india= India()
obj_usa=USA()
obj_japan= Japan()
obj_australia= Australia()

india_button= Button(root,text= "showtime", command= obj_india.times)
india_button.place(relx= 0.2,rely= 0.8, anchor= CENTER)
usa_button= Button(root,text= "showtime", command= obj_usa.times)
usa_button.place(relx= 0.7,rely= 0.8, anchor= CENTER)
japan_button= Button(root,text= "showtime", command= obj_japan.times)
japan_button.place(relx= 0.8,rely= 0.8, anchor= CENTER)
australia_button= Button(root,text= "showtime", command= obj_australia.times)
australia_button.place(relx= 0.9,rely= 0.8, anchor= CENTER)


root.mainloop()
                
