from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

def change(text="type",src="English",Translated="Hindi"):
    text1=text
    src1=src
    Translated1=Translated
    trans=Translator()
    trans1=trans.translate(text,src=src1,Translated1=Translated)

def data():
    s=comb_source.get()
    d=comb_dest.get()
    msg=Source_txt.get(1.0,END)
    textget = change(text=msg,src=s,Translated=d)
    Translated_txt.delete(1.0,END)
    Translated_txt.insert(END,textget)









root = Tk()
root.title("Translator")
root.geometry("800x600")  # widthHeight
root.config(bg='Grey')

lab_txt = Label(root, text="Welcome to Translator", font=("Bell MT", 30, "bold"), bg='Yellow')
lab_txt.place(x=175, y=40, height=40, width=450)

frame = Frame(root).pack(side=BOTTOM)

lab_txt1 = Label(root, text="Source Text", font=("Bell MT", 13, "bold"), bg='Yellow', fg='Red')
lab_txt1.place(x=25, y=100, height=20, width=100)

Source_txt = Text(frame, font=("Bell MT", 15, "bold"), bg='Black', wrap=WORD,fg="White")
Source_txt.place(x=25, y=120, height=175, width=750)

list_text=list(LANGUAGES.values())
comb_source = ttk.Combobox(frame,value=list_text, font=30)
comb_source.place(x=25, y=300, height=30, width=125)
comb_source.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, font=30,bg="Red",command=data)
button_change.place(x=350, y=300, height=30, width=125)


comb_dest = ttk.Combobox(frame,value=list_text, font=30)
comb_dest.place(x=650, y=300, height=30, width=125)
comb_dest.set(" French")

Translated_txt = Text(frame, font=("Bell MT", 15, "bold"), bg='Black', wrap=WORD,fg="White")
Translated_txt.place(x=25, y=375, height=175, width=750)

lab_txt2 = Label(root, text="Translated Text", font=("Bell MT", 13, "bold"), bg='Yellow', fg='Red')
lab_txt2.place(x=25, y=350, height=20, width=125)



root.mainloop()