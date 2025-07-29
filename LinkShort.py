import pyshorteners
from tkinter import *
from tkinter.messagebox import showinfo,showerror
def generate():
    link=urlinput.get()
    Shortener = pyshorteners.Shortener()
    shorted_link = Shortener.tinyurl.short(link)
    showinfo(title="Shorten Any Link",message="Link Shorted")
    generatedinput.set(shorted_link)
     
page=Tk()
page.title("Shorten Any Link ..")
page.iconbitmap("link.ico")
page.geometry("1500x750+10+10")
page.resizable(False,False)
urlinput=StringVar()
generatedinput=StringVar()
TitleLabel=Label(page,text="Shorten Any URL",font=("Calibri",30,"bold"),bg="black",relief=SUNKEN,fg="white")
TitleLabel.place(x=150,y=50,height=70,width=1200)
LinkLabel=Label(page,text="Url Link: ",font=("Calibri",20))
LinkLabel.place(x=280,y=200,height=60,width=150)
ShortenLabel=Label(page,text="Shorten: ",font=("Calibri",20),fg="red")
ShortenLabel.place(x=280,y=300,height=60,width=150)
LinkInput=Entry(page,textvariable=urlinput,font=("Calibri",20))
LinkInput.place(x=450,y=200,height=60,width=700)
ShortenInput=Entry(page,textvariable=generatedinput,font=("Calibri",20))
ShortenInput.place(x=450,y=300,height=60,width=700)
SaveButton=Button(page,text="Generate",bg="black",fg="white",font=("Arial Black",20,"bold"),command=generate)
SaveButton.place(x=700,y=500,height=70,width=200)
page.mainloop()

