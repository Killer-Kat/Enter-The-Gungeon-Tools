#A small little app that shows some sats related to junk in enter the gungeon
#Written by KillerKat on 11/22/2020

from tkinter import *
import tkinter.messagebox

junk = 0
gold_junk = 0
lies = 0
total = 0
junkan = False

def reset():
    global junk, gold_junk, lies, junkan
    junk = 0
    gold_junk = 0
    lies = 0
    total = 0
    junkan = False
    junk_output.set(str(junk))
    gold_junk_output.set(str(gold_junk))
    lies_output.set(str(lies))
    total_output.set(str(total))

def plus_button( type ): #Yes I know this isnt the most efficent way but python doesnt have switches, if I could I would just use the varible as the argument.
    if type == 1:
        global junk
        junk += 1
        junk_output.set(str(junk))
    elif type == 2:
        global gold_junk
        gold_junk += 1
        gold_junk_output.set(str(gold_junk))
    elif type == 3:
        global lies
        lies += 1
        lies_output.set(str(lies))
    else:
        tkinter.messagebox.showinfo("Unexpected error", "Impossible Error has occured")
    global total
    total = (junk + gold_junk + lies)
    total_output.set(str(total))

def minus_button( type ): #Like why cant I just give it a global varible as an argument and then refrence that variable in the function as an argument?
    if type == 1:
        global junk
        junk -= 1
        junk_output.set(str(junk))
    elif type == 2:
        global gold_junk
        gold_junk -= 1
        gold_junk_output.set(str(gold_junk))
    elif type == 3:
        global lies
        lies -= 1
        lies_output.set(str(lies))
    else:
        tkinter.messagebox.showinfo("Unexpected error", "Impossible Error has occured")
    global total
    total = (junk + gold_junk + lies)
    total_output.set(str(total))



#Gui
root = Tk()
root.title("Junk O Meeter")
root.geometry("750x500")
root.resizable(0,0)

junk_output = StringVar() #Sets a variable that can be used as the text in the label
junk_output.set(str(junk))
gold_junk_output = StringVar()
gold_junk_output.set(str(gold_junk))
lies_output = StringVar() 
lies_output.set(str(lies))
total_output = StringVar() 
total_output.set(str(total))

title_label = Label(root, text="The Junk O Meeter!",)
title_label.grid(row=0, column=0,  sticky=N)
reset_button = Button(root, text="RESET", command=reset)
reset_button.grid(row=0, column=1)

junk_label = Label(root, text="Junk",)
junk_label.grid(row=1,)
junk_output_label = Label(root, textvariable=junk_output, bg="Darkorange2", fg="gold")
junk_output_label.grid(row=1, column=1)
junk_plus_button = Button(root, text="+", command= lambda: plus_button(1), bg="Darkorange2", fg="gold")
junk_plus_button.grid(row=1, column=2)
junk_minus_button = Button(root, text="-", command= lambda: minus_button(1), bg="Darkorange2", fg="gold")
junk_minus_button.grid(row=1, column=3)

gold_junk_label = Label(root, text="Gold Junk",)
gold_junk_label.grid(row=2, sticky=N)
gold_junk_output_label = Label(root, textvariable=gold_junk_output, bg="Darkorange2", fg="gold")
gold_junk_output_label.grid(row=2, column=1)
gold_junk_plus_button = Button(root, text="+", command= lambda: plus_button(2), bg="Darkorange2", fg="gold")
gold_junk_plus_button.grid(row=2, column=2)
gold_junk_minus_button = Button(root, text="-", command= lambda: minus_button(2), bg="Darkorange2", fg="gold")
gold_junk_minus_button.grid(row=2, column=3)

lies_label = Label(root, text="Lies",)
lies_label.grid(row=3, sticky=N)
lies_output_label = Label(root, textvariable=lies_output, bg="Darkorange2", fg="gold")
lies_output_label.grid(row=3, column=1)
lies_plus_button = Button(root, text="+", command= lambda: plus_button(3), bg="Darkorange2", fg="gold")
lies_plus_button.grid(row=3, column=2)
lies_minus_button = Button(root, text="-", command= lambda: minus_button(3), bg="Darkorange2", fg="gold")
lies_minus_button.grid(row=3, column=3)

total_label = Label(root, text="Total",)
total_label.grid(row=4, sticky=N)
total_output_label = Label(root, textvariable=total_output, bg="Darkorange2", fg="gold")
total_output_label.grid(row=4, column=1)



root.mainloop() #Keeps the window open and running