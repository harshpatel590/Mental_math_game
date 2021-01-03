from tkinter import *               # importing tkinter for GUI 
import time                         # importing time for timer
import random as rdm                
from tkinter import messagebox      # importing massagebox form tkinter 
import pyttsx3                      # importing pyttsx3 for reading score


easy_gui = Tk()                     # defining window name
easy_gui.config(bg="black")         # setting bg colour 
easy_gui.title("Mental Math Easy Mode")     # seetting title name
easy_gui.iconbitmap("logo_game.ico")        # adding icon to tital bar




def change_ques(event = None):              # defining function to make a new ques when every time runs
    num_1 = rdm.randrange(0,20)
    num_2 = rdm.randrange(0,20)
    add_ = num_1 + num_2
    sub_ = num_1 - num_2

    global ques
    ques = rdm.choice([add_,sub_])
    
    if ques == add_:
        show_ques = f"   {num_1} + {num_2}    "
    else :
        show_ques = f"   {num_1} - {num_2}    "
    

    ques_label = Label(easy_gui,text = (show_ques),font=("Bellattrix",30),fg = "white",bg = "black")       # adding lable to show ques on window
    ques_label.grid(row =1,column=0,columnspan = 2,padx=(70,10))



score_list = []
def score_adder():                      # defining function to get input of ques and add score in list 
    ans_ = input_ans.get()
    
    ans_spaced_removed = ans_.replace(" ", "")

    if ans_spaced_removed == str(ques):
        score_list.append('3')
    else :
        score_list.append('-1')
    
    
def clear_value(event = None):         # defining function to clear the value of input box

    score_adder()

    input_ans.delete(0,END)
    



# defining all label and buttons:-

time_left = Label(easy_gui, text="Time Left :-",font=("Bajigur Brush Font",30),fg = "white",bg = "black")

score_scheme = Label(easy_gui, text=(f"Score Scheme :- "),font=("Bajigur Brush Font",30),fg = "white",bg = "black")

correct_scheme = Label(easy_gui, text=(u"\u2713"+" :- + 3 "),font=("Bajigur Brush Font",40),fg = "#6CFF6C",bg = "black")

wrong_scheme = Label(easy_gui, text=(u"\u2717"+" :- - 1 "),font=("Bajigur Brush Font",40),fg = "#FF3E3E",bg = "black")

change_button = Button(easy_gui, text = "click or \n press Enter \n for next ques",padx=0,font=("BlackChancery",15),bg = "#25C1A3",pady=0,command = change_ques)

clear_button = Button(easy_gui, text = "click or \n press Spacebar \n to clear box",padx=0,font=("BlackChancery",15),bg = "#56ADE8",pady=1,command = change_ques)

# placing all buttons and lable in window :-

time_left.grid(row=0,column=0,columnspan =2,padx = (0,0))
score_scheme.grid(row=3,column=0,columnspan =2,padx = (0,0))
correct_scheme.grid(row=3,column=2,columnspan =2,padx = (0,0))
wrong_scheme.grid(row=4,column=2,columnspan =2,padx = (0,0))
change_button.grid(row = 3 ,column = 4)
clear_button.grid(row = 4 ,column = 4,pady=10)

# binding button to function :-

easy_gui.bind("<space>",change_ques)                     
easy_gui.bind("<Return>",clear_value)  

# making an input box :-

input_ans= Entry(easy_gui,font=("Bajigur Brush Font",40),fg="#0036A3",bg ="#161616",width = 5)
input_ans.grid(row =1,column=4,pady = (15,20))




# making a timer :-

for i in range(120,-1,-1):
    min_ = i // 60
    sec_ = i % 60
    
    if sec_ <= 10 and min_ == 0:
        time_ = Label(easy_gui, text=(f" {min_}:{sec_} "),font=("Advanced Sans Serif 7",40),fg = "red",bg = "black")
    elif sec_ <= 30 and min_ == 0:
        time_ = Label(easy_gui, text=(f" {min_}:{sec_} "),font=("Advanced Sans Serif 7",40),fg = "#DD944B",bg = "black")
    else:
        time_ = Label(easy_gui, text=(f" {min_}:{sec_} "),font=("Advanced Sans Serif 7",40),fg = "#7FEA7F",bg = "black")

    # showing a timer in window :-
    time_left.grid(row=0,column=0,columnspan =2,padx = (70,0),pady=(50,20)) 
    time_.grid(row =0,column=4,padx = (0,70),pady=(50,20))
    time_.place_forget()
    easy_gui.update()
    time.sleep(1)


# defining properties  of speaker :-

speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
speaker.setProperty("rate" ,100)

# making a  score couter and pop-up window when game overs :-
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
    

    easy_gui.withdraw()
    




easy_gui.mainloop()     # closing window loop
