import tkinter as tk # Alies name
from tkinter import *  # importing all functions from tkinter
from datatime import datetime # used to import time & date
import requests  # used to send the request to server
from PIL import ImageTK, Image # used to import images
from tkinter import messagebox # give the message when no data is entered

root=tk.Tk()    # work space is root , before using tkinter module we have create work space
root.geometry("700*270")   # application size
root.title("currency converter")
root.iconbitmap('icon.ico')  # displaying icon, icon.ico is file name
root.minsize(600,270)

image=Image.open('currency.png')
zoom=0.5

# Environment is set or foxed


pixels_x, pixels_y, =tuple([int(zoom * x) for x in image.size])  #we take tuple, because of pillow expert tuple value (width,height)
                                                                 #This loops over each value in image.size , → first x = width, second x = height
                                                                # Multiplies each by zoom (a scaling factor) , Converts the result to int

img=ImageTK.photo.PhotoImage(image.resize((pixels_x, pixels_y))) #Takes a tuple (new_width, new_height), Returns a resized image
                                                                 # ImageTk.PhotoImage does (Converts the PIL image into a Tkinter-compatible image object
panel= Label(root, image=img)  # label font, because of to adjust the size of the image
panel.place(x=190,y=35)  # address, to place the image


def show_data():  # function for getting values
    amount = E1.get()  # get function used to get the data
    from_currency = c1.get()
    to_currency = c2.get()
    url= 'https://api.currencylayer.com/live?access_key=473d2c37f738367f08780b934ce7dda&format=1'

    if amount == " ":
        messagebox.showerror("currency converter","please fill the amount")
    elif to_currency == " ":
        messagebox.showerror("currency converter","pleasse fill the currency")
    else:
        data= request.get(url).json() # data in that url in json formate, passing request to that url
        currency=from_currency.strip()+to_currency.strip()
        amount=int(amount)
        cc=data['quotes'][currency]  # is used to mension particular currency
        cur_conv=cc*amount
        E2.insert(0,cur_conv)
        total.insert('end',f'{amount}united state Dollar Equals{cur_conv} {to_currency} \n\n last time update --- \t {datetime.now()}')  # it displays in show boxs

def clear():
    E1.delete(0,'end')
    E2.delete(0,'end')
    text.delete(1.0,'end')

l1=label(root,text="USD currency converter", font=('Timesnewroman', '10', 'bold'))  # Tkinter uses a parent–child structure
l1.place(x=150,y=15)

amt=label(root,text="Amount",font=('roboto',10,'bold'))
amt.place(x=20,y=15)
E1= Enter(root, width=20, borderwidth=1, font=('robot'10,'bold'))
E1.place(x=20,y=40)

c1=tk.Stringvar()
c2=tk.Stringvar()
currencychoose1 =ttk.Combobox(root, width=20, textvarible= c1, state='readonly', font=('roboto',10,'bold'))  # dropdown menu

# Adding combox drop down list

currencychoose1['values']=(
                            'USD',
                            'INR',
                            'EUR',
                            'GBP',
                            'AED',
                            'CAD',
                            'AUD',
                            'JPY',

)

currencychoose2.place(x=300,y=80)
currencychoose2.current()

text=Text(root,heigth=7,widht=54,font=('Timesnewroman','10','bold'))
text.place(x=100,y=120)

B= Button(root,text="search",command=show+date, font=('Timesnewe=roman', '10','bold'))  # search button
B.place(x=20,y=120)

clear =Button (root,text="clear", command=clear, font=('Timesnewe=roman', '10','bold'))  # clear button
clear.place(x=20,y=120)

root.mainloop()


# < ================ code end ================>


