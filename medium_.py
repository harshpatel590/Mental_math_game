from tkinter import *
import time 
import random as rdm
from tkinter import messagebox
import pyttsx3

medium_gui = Tk()
medium_gui.config(bg="black")
medium_gui.title("Mental Math Medium Mode")
medium_gui.iconbitmap("logo_game.ico")

def change_ques(event = None):
    num_1 = rdm.randrange(0,20)
    num_2 = rdm.randrange(0,20)
    add_ = num_1 + num_2
    sub_ = num_1 - num_2
    multi_ = num_1 * num_2
    

    global ques
    ques = rdm.choice([add_,sub_,multi_])
    
    if ques == add_:
        show_ques = f"   {num_1} + {num_2}    "
    elif ques == sub_:
        show_ques = f"   {num_1} - {num_2}    "
    else:
        show_ques = f"   {num_1} " +u"\u2717" + f" {num_2}    "

    ques_label = Label(medium_gui,text = (show_ques),font=("Bellattrix",30),fg = "white",bg = "black")
    ques_label.grid(row =1,column=0,columnspan = 2,padx=(70,10))


score_list = []
def score_adder():
    ans_ = input_ans.get()
    
    ans_spaced_removed = ans_.replace(" ", "")

    if ans_spaced_removed == str(ques):
        score_list.append('3')
    else :
        score_list.append('-1')
    
    
def clear_value(event = None):

    score_adder()

    input_ans.delete(0,END)
    





time_left = Label(medium_gui, text="Time Left :-",font=("Bajigur Brush Font",30),fg = "white",bg = "black")
time_left.grid(row=0,column=0,columnspan =2,padx = (0,0))

score_scheme = Label(medium_gui, text=(f"Score Scheme :- "),font=("Bajigur Brush Font",30),fg = "white",bg = "black")
score_scheme.grid(row=3,column=0,columnspan =2,padx = (0,0))

correct_scheme = Label(medium_gui, text=(u"\u2713"+" :- + 3 "),font=("Bajigur Brush Font",40),fg = "#6CFF6C",bg = "black")
correct_scheme.grid(row=3,column=2,columnspan =2,padx = (0,0))

wrong_scheme = Label(medium_gui, text=(u"\u2717"+" :- - 1 "),font=("Bajigur Brush Font",40),fg = "#FF3E3E",bg = "black")
wrong_scheme.grid(row=4,column=2,columnspan =2,padx = (0,0))

change_button = Button(medium_gui, text = "click or \n press Enter \n for next ques",padx=0,font=("BlackChancery",15),bg = "#25C1A3",pady=0,command = change_ques)
change_button.grid(row = 3 ,column = 4)

clear_button = Button(medium_gui, text = "click or \n press Spacebar \n to clear box",padx=0,font=("BlackChancery",15),bg = "#56ADE8",pady=1,command = change_ques)
clear_button.grid(row = 4 ,column = 4,pady=10)

medium_gui.bind("<space>",change_ques)

medium_gui.bind("<Return>",clear_value)  






input_ans= Entry(medium_gui,font=("Bajigur Brush Font",40),fg="#0036A3",bg ="#161616",width = 5)
input_ans.grid(row =1,column=4,pady = (15,20))






for i in range(120,-1,-1):
    min_ = i // 60
    sec_ = i % 60
    
    if sec_ <= 10 and min_ == 0:
        time_ = Label(medium_gui, text=(f" {min_}:{sec_} "),font=("Advanced Sans Serif 7",40),fg = "red",bg = "black")
    elif sec_ <= 30 and min_ == 0:
        time_ = Label(medium_gui, text=(f" {min_}:{sec_} "),font=("Advanced Sans Serif 7",40),fg = "#DD944B",bg = "black")
    else:
        time_ = Label(medium_gui, text=(f" {min_}:{sec_} "),font=("Advanced Sans Serif 7",40),fg = "#7FEA7F",bg = "black")

    
    time_left.grid(row=0,column=0,columnspan =2,padx = (70,0),pady=(50,20)) 
    time_.grid(row =0,column=4,padx = (0,70),pady=(50,20))
    time_.place_forget()
    medium_gui.update()
    time.sleep(1)

speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
speaker.setProperty("rate" ,100)  

if  min_ == 0 and sec_ == 0 :
    total_score = 0
    for i in score_list:
        num = int(i)
        total_score += num
    if total_score < 0:
        total_score = 0
    
    speaker.say(f"your score is {total_score}")
    speaker.runAndWait()
    
    messagebox.showinfo("score board ",f"YOUR SCORE IS : {total_score} \n THANKS FOR PLAYING")
    medium_gui.withdraw()
    
    




medium_gui.mainloop()
