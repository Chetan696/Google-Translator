from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

def change(text="type",src="English",dest="hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d= comb_dest.get()
    msg= Sor_txt.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("Translator")
root.geometry("800x600")  # widthHeight
root.config(bg='Grey')

lab_txt = Label(root, text="Welcome to Translator", font=("Bell MT", 30, "bold"), bg='Yellow')
lab_txt.place(x=175, y=40, height=40, width=450)

frame = Frame(root).pack(side=BOTTOM)

lab_txt1 = Label(root, text="Input Text", font=("Bell MT", 13, "bold"), bg='Yellow')
lab_txt1.place(x=25, y=90, height=30, width=100)

lab_txt2 = Label(root, text="Translated Text", font=("Bell MT", 12, "bold"), bg='Yellow')
lab_txt2.place(x=25, y=350, height=30, width=120)

Sor_txt = Text(frame, font=("Bell MT", 15, "bold"), bg='Black', wrap=WORD,fg="White")
Sor_txt.place(x=25, y=120, height=175, width=750)

list_txt=list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_txt, font=30)
comb_sor.place(x=25, y=300, height=30, width=125)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, font=30,bg="Red",command=data)
button_change.place(x=325, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame,value=list_txt, font=30)
comb_dest.place(x=650, y=300, height=30, width=125)
comb_dest.set("hindi")

dest_txt = Text(frame, font=("Bell MT", 15, "bold"), bg='Black', wrap=WORD,fg="White")
dest_txt.place(x=25, y=375, height=175, width=750)


root.mainloop()