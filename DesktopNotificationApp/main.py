import customtkinter
import time
from tkinter import *
from plyer import notification
from tkinter import messagebox

app = customtkinter.CTk()

app.title("Notification")
app.geometry("45x180")
app.config(bg="#1702f5") #000000

font1 = ('Arial',15,'bold')

def notify_me():
    if(notify_entry.get()=='' or After_entry.get()==''):
        messagebox.showerror(title='Error',message='Please, enter a notification and a time.')
    else:
        time.sleep(int(After_entry.get()))
        notification.notify(title='Alert',message=notify_entry.get(),timeout=60)

notify_label=customtkinter.CTkLabel(app,text="Notification",text_font=font1,text_color="#ff0000")
notify_label.place(x=13,y=20)

notify_entry = customtkinter.CTkEntry(app,text_font=font1,text_color="#000000",fg_color="#FFFFFF",border_color="#eeff00",width=200)  #FFFFFF
notify_entry.place(x=20,y=50)


After_label=customtkinter.CTkLabel(app,text="Enter duration(sec)",text_font=font1,text_color="#ff0000")
After_label.place(x=290,y=20)

After_entry = customtkinter.CTkEntry(app,text_font=font1,text_color="#000000",fg_color="#FFFFFF",
border_color="#eeff00",width=50)
After_entry.place(x=310,y=50)

notify_button = customtkinter.CTkButton(app,command=notify_me,text="Notify Me",text_font=font1,text_color="#FFFFFF",fg_color="#127a16",hover_color="#4000ff",width=50) #127a16
notify_button.place(x=190,y=110)

app.mainloop()