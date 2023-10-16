
from tkinter import *
import math
import pandas
import random
from tkinter.scrolledtext import ScrolledText



# --------------------------------- Generating A list property   ---------------------------------------------# 


class List: 
    
    def __init__ (self):     
        self.given_word_list=[]


# --------------------------------- Constants ---------------------------------------------# 

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

timer=None
item_num = -1 
data=pandas.read_csv("english_words.csv")
list = List()


 
# # ---------------------------- TIMER & COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- TIMER countdown ------------------------------- # 



def count_down(count,given_word_list):
    
    
    count_min = math.floor(count/60)
    count_sec = count%60

    #when the reamining is less then 10 seconds 
    if count_sec<10:
      count_sec=f"0{count_sec}"


    #when the timer is at the begining 
    if count_sec ==0 :
       count_sec="00"
      #  check()
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    #here we are calling the function we maked above , where every 1 second , the count is decremented by 1 ,
    #  and according to what the count is , we will display it on the canvas ,
    #  or every one second , we are providing a new status for the count and how the time will be displayed . 
    if count > 0 :

      global timer
      timer=window.after(1000,count_down,count-1,given_word_list)
      give_new_statement



# ---------------------------- Checking mechanism  ------------------------------- #  


    # when the time is 0 , give the user a score , depending on how many wors are similar or correct to the words that we give him .  
    if count==0:
          
          user_input_list=(input.get()).split()
          score_count=0
          for word in user_input_list:
              if word in given_word_list:
                  score_count+=1
          canvas.itemconfig(score_text,text=f"Score(Words/minute):{score_count}")
         
              
          
        
      
      


    
      
 
    
    
 

# ---------------------------- TIMER Start ------------------------------- #  



def start_timer():

  #when the start button is clicked , we empty the old list , and make the new list for one time uniquely , and also the input field!
  input.delete(0, END)
  statement_label.delete('1.0', END)
  global data
  list.given_word_list=[]

  for n in range(0,400):
      list.given_word_list.append(data["word"][random.randint(0,4200)])

  random_num=random.randint(0,400)    
  statement_label.insert(END,f" {list.given_word_list[random_num]} ")    
       
  Time = 60
  count_down(Time,list.given_word_list)


  global startbuttonClicked
  startbuttonClicked = not startbuttonClicked 

  



startbuttonClicked  = False # Bfore first click



# ---------------------------- Listening To The Keyboard  ------------------------------- #  



def give_new_statement(event):
     
    #  only listen to keyboard when the start button is clicked  , we cannot just rely on the count starts ,
    #bcz the function is called outside the countdown !
    #every time the user press space , we increment the item number to print a new item on the screen 
    if startbuttonClicked==True:
        if  event.char == " ":
            global item_num
            item_num+=1
            statement_label.insert(END,f" {list.given_word_list[item_num]} ")   
            

 


 # # ----------------------------      Future improvements  ----------------------------------------------------------------------------------------------# 

 # # ----------------------------      TIMER RESET -------------------------------------------# 
# def reset_timer():
#   window.after_cancel(timer)
  
#   input.delete(0, END)
#   statement_label.delete('1.0', END)
  
#   canvas.itemconfig(timer_text,text="00:00")

#   global startbuttonClicked
#   startbuttonClicked = not startbuttonClicked 

#   start_timer()
     
    # # -------------------------------------------------------------------------------------------------------------------------------------------#          

  











# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Typing Speed Test")
window.config(bg=YELLOW)
window.minsize(width=1000, height=700)





canvas=Canvas(width=900,height=100,bg=YELLOW,highlightthickness=0)

timer_label=canvas.create_text(100,90,text="Time Left:",fill="red",font=(FONT_NAME,12,"bold"))

timer_text=canvas.create_text(190 ,90,text="00:00",fill="black",font=(FONT_NAME,12,"bold"))

score_text=canvas.create_text(700 ,90,text="Score(Words/minute): ",fill="black",font=(FONT_NAME,12,"bold"))

welcome_text=canvas.create_text(700 ,30,text="Typing Speed Test!",fill="black",font=(FONT_NAME,15,"bold"))

canvas.place(x=0,y=5)





statement_label = ScrolledText(height=5, width=57,font=("Courier",18,"bold"),fg="green",bg="grey" )
statement_label.place(x=250,y=200)
statement_label.configure(wrap='word')





input=Entry(width=57,border=3,font=("Courier",18,"bold"),fg="Black",bg=YELLOW)
input.place(x=250,y=330)   

   

button_start=Button(width=90,border=3,text="Start",command=start_timer)
button_start.place(x=350,y=430)   






window.bind('<Key>', give_new_statement)
window.mainloop()