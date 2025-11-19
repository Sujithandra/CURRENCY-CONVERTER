import tkinter as tkinter
from tkinter import *
from tkinter import tkinter
from datatime import datetime
import requests
from PIL import ImageTK, Image
from tkinter import messagebox

root=tk.Tk()
root.geometry("700*270")
root.title("currency converter")
root.iconbitmap('icon.ico')
root.minsize(600,270)

image=Image.open('currency.png')
zoom=0.5

pixels_x, pixels_y, =tuple([int(zoom * x) for x in image.size])

img=ImageTK.photo.PhotoImage(image.resize((pixels_x, pixels_y)))
panel= Label(root, image=img)
panel.place(x=190,y=35)

def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url= 'https://api.exchangerate-api.com/v4/latest/USD'

    if amount == " ":
        messagebox.showerror("currency converter","please fill the amount")
    elif to_currency == " ":
        messagebox.showerror("currency converter","pleasse fill the currency")
    else:
        data= request.get(url).json()
        currency=from_currency.strip()+to_currency.strip()
        amount=int(amount)
        cc=data['quotes'][currency]
        cur_conv=cc*amount
        E2.insert(0,cur_conv)
        total.insert('end',f'{amount}united state Dollar Equals{cur_conv} {to_currency} \n\n last time update --- \t {datetime.now()}')

def clear():
    E1.delete(0,'end')
    E2.delete(0,'end')
    text.delete(1.0,'end')

l1=label(root,text="USD currency converter", font=('Timesnewroman', '10', 'bold'))
l1.place(x=150,y=15)

amt=label(root,text="Amount",font=('roboto',10,'bold'))
amt.place(x=20,y=15)
E1= Enter(root, width=20, borderwidth=1, font=('robot'10,'bold'))
E1.place(x=20,y=40)

c1=tk.Stringvar()
c2=tk.Stringvar()
currencychoose1 =ttk.Combobox(root, width=20, textvarible= c1, state='readonly', font=('roboto',10,'bold'))

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

B= Button(root,text="search",command=show+date, font=('Timesnewe=roman', '10','bold'))
B.place(x=20,y=120)

clear =Button (root,text="clear", command=clear, font=('Timesnewe=roman', '10','bold'))
clear.place(x=20,y=120)

root.mainloop()


# < ================ code end ================>


