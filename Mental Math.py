from tkinter import *                  # importing tkinter for GUI 
import pygame                          # importing pygame for music
from tkinter import messagebox         # importing massagebox form tkinter to show pop-up




pygame.init()                          # defining(installing) pygame
root = Tk()                            # defining window name
root.config(bg = "black")              # setting bg colour 
root.title(" Mental Math ")            # seetting title name
root.iconbitmap("logo_game.ico")       # adding icon to tital bar
pygame.mixer.music.load("hello.mp3")   # loading music 
pygame.mixer.music.play(loops=-1)      # playing music




def game_level_1():                    # defining function to open easy_ file
   import easy_
   
        
def game_level_2():                    # defining function to open easy_ file
    import medium_
    
        
def game_level_3():                    # defining function to open easy_ file
    import hard_
    

def exit_game():                       # defining function to exit game(python file)
    messagebox.showinfo("SCORE BOARD ",u"\u263A" + "  THANKS FOR PLAYING  "+ u"\u263A")   # defining pop-up box and content 
    exit()



Game_mode = Label(root, text=(f"Chose Your Game Mode :- "),font=("Bajigur Brush Font",30),fg = "white",bg = "black")  # defining label

Game_mode.pack(padx=50,pady=(70,10))   # placing lable in window


# making all buttons and commanding to run their respective defined functions ::--
button_easy = Button(root, text = "! PAINLESS !",padx=50,font=("Bajigur Brush Font",30),bg = "#9BFF76",pady=10,command = game_level_1)      
button_medium = Button(root, text = "  !! HITLER !!  ",padx=45,font=("Bajigur Brush Font",30),bg = "#FF693B",pady=10,command = game_level_2)
button_hard = Button(root, text = ("!"+u"\u2620"+"!  HARDCORE  !"+ u"\u2620"+"!"),padx=50,font=("Bajigur Brush Font",30),bg = "#FF1D1D", pady=10 , command =game_level_3)
button_exit = Button(root, text = ("!"+u"\u263A"+" EXIT "+ u"\u263A"+"!"),padx=0,font=("Bajigur Brush Font",30),bg = "#ff6600", pady=10 , command =exit_game)



# placing all buttons in window ::--
button_easy.pack(pady=10)
button_medium.pack(pady=10)
button_hard.pack(pady=(10,10))
button_exit.pack(pady=(10,70))




# exiting window loop
root.update()
root.mainloop()







