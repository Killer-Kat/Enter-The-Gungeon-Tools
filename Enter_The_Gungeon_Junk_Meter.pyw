#A small little app that shows some sats related to junk in enter the gungeon
#Why? Becuase I enjoy making things, I have ideas and I want to put them to life. Someday I might include this in a larger program for ETG.
#Written by KillerKat on 11/22/2020, version 1.0 finished on 12/30/2020
#Robot damage boost works under the assumption that you will not drop a piece of junk and pick it back up again (I have no idea why you would do that)
from tkinter import *
import tkinter.messagebox

junk = 0
gold_junk = 0
lies = 0
total = 0
junkan = False
junkan_rank = "N/A"
robot_DMG_boost = 0

def reset():
    global junk, gold_junk, lies, junkan, junkan_rank, robot_DMG_boost
    junk = 0
    gold_junk = 0
    lies = 0
    total = 0
    junkan = False
    junkan_rank = "N/A"
    robot_DMG_boost = 0
    junk_output.set(str(junk))
    gold_junk_output.set(str(gold_junk))
    lies_output.set(str(lies))
    total_output.set(str(total))
    junkan_rank_output.set(junkan_rank)
    robot_DMG_boost_output.set(str(robot_DMG_boost))

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
    global robot_DMG_boost
    robot_DMG_boost = (robot_DMG_boost + 0.5)
    robot_DMG_boost_output.set(str(robot_DMG_boost))
    Rank_Check()

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
    Rank_Check()

def Rank_Check():
    global junkan, gold_junk, total
    if junkan == False:
        junkan_rank = "N/A"
    elif gold_junk > 0:
        junkan_rank = "Mecha Junkan"
    elif total >= 7:
        junkan_rank = "Angelic Knight"
    elif total == 0:
        junkan_rank = "Peasant"
    elif total == 1:
        junkan_rank = "Squire"
    elif total == 2:
        junkan_rank = "Knight"
    elif total == 3:
        junkan_rank = "Knight Lieutenant"
    elif total == 4:
        junkan_rank = "Knight Commander"
    elif total == 5:
        junkan_rank = "Holy Knight"
    elif total == 6:
        junkan_rank = "Hedge Knight"
    else:
        junkan_rank = "Internal ERROR"
    junkan_rank_output.set(junkan_rank)
def Junkan_Toggle():
    global junkan
    if junkan == False:
        junkan = True
    else:
       junkan = False
    Rank_Check()
#Gui
root = Tk()
root.title("Junk O Meeter")
root.geometry("500x275")
root.resizable(0,0)
root.configure(background="saddle brown")

junk_output = StringVar() #Sets a variable that can be used as the text in the label
junk_output.set(str(junk))
gold_junk_output = StringVar()
gold_junk_output.set(str(gold_junk))
lies_output = StringVar() 
lies_output.set(str(lies))
total_output = StringVar()
total_output.set(str(total))
junkan_rank_output = StringVar()
junkan_rank_output.set(junkan_rank)
robot_DMG_boost_output = StringVar()
robot_DMG_boost_output.set(str(robot_DMG_boost))

title_label = Label(root, text="The Junk O Meeter!", bg="sandy brown", fg="brown4")
title_label.grid(row=0, column=0,  sticky=N)
reset_button = Button(root, text="RESET", command=reset, bg="sandy brown", fg="brown4")
reset_button.grid(row=0, column=1)
junkan_toggle_button = Button(root, text="Toggle Junkan", command=Junkan_Toggle, bg="sandy brown", fg="brown4")
junkan_toggle_button.grid(row=0, column=2, columnspan=2)

junk_label = Label(root, text="Junk", bg="sandy brown", fg="brown4")
junk_label.grid(row=1,)
junk_output_label = Label(root, textvariable=junk_output, bg="sandy brown", fg="brown4")
junk_output_label.grid(row=1, column=1)
junk_plus_button = Button(root, text="+", command= lambda: plus_button(1), bg="sandy brown", fg="brown4")
junk_plus_button.grid(row=1, column=2)
junk_minus_button = Button(root, text="-", command= lambda: minus_button(1), bg="sandy brown", fg="brown4")
junk_minus_button.grid(row=1, column=3)

gold_junk_label = Label(root, text="Gold Junk", bg="Darkorange2", fg="gold")
gold_junk_label.grid(row=2, sticky=N)
gold_junk_output_label = Label(root, textvariable=gold_junk_output, bg="Darkorange2", fg="gold")
gold_junk_output_label.grid(row=2, column=1)
gold_junk_plus_button = Button(root, text="+", command= lambda: plus_button(2), bg="Darkorange2", fg="gold")
gold_junk_plus_button.grid(row=2, column=2)
gold_junk_minus_button = Button(root, text="-", command= lambda: minus_button(2), bg="Darkorange2", fg="gold")
gold_junk_minus_button.grid(row=2, column=3)

lies_label = Label(root, text="Lies", bg="sandy brown", fg="brown4")
lies_label.grid(row=3, sticky=N)
lies_output_label = Label(root, textvariable=lies_output,  bg="sandy brown", fg="brown4")
lies_output_label.grid(row=3, column=1)
lies_plus_button = Button(root, text="+", command= lambda: plus_button(3), bg="sandy brown", fg="brown4")
lies_plus_button.grid(row=3, column=2)
lies_minus_button = Button(root, text="-", command= lambda: minus_button(3), bg="sandy brown", fg="brown4")
lies_minus_button.grid(row=3, column=3)

total_label = Label(root, text="Total", bg="sandy brown", fg="brown4")
total_label.grid(row=4, sticky=N)
total_output_label = Label(root, textvariable=total_output, bg="sandy brown", fg="brown4")
total_output_label.grid(row=4, column=1)

junkan_rank_label = Label(root, text="Junkan Rank: ", bg="sandy brown", fg="brown4")
junkan_rank_label.grid(row=5, sticky=N)
junkan_rank_output_label = Label(root, textvariable=junkan_rank_output, bg="sandy brown", fg="brown4")
junkan_rank_output_label.grid(row=5, column=1, columnspan=3)

robot_DMG_boost_label = Label(root, text="Robot DMG boost : %", bg="grey60", fg="LightSteelBlue1")
robot_DMG_boost_label.grid(row=6)
robot_DMG_boost_output_label = Label(root, textvariable=robot_DMG_boost_output, bg="grey60", fg="LightSteelBlue1")
robot_DMG_boost_output_label.grid(row=6, column=1)

root.mainloop() #Keeps the window open and running