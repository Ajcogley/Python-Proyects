from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("PYTHON/FlashCardProyect/data/words_to_learn.csv")


except:
    data=pandas.read_csv("PYTHON/FlashCardProyect/data/french_words.csv")



dict=data.to_dict(orient="records")

    
choice={}
flip_timer=None
words_to_learn=[]







def update_word():
    global choice
    canvas1.delete("word")
    choice=random.choice(dict)
    france_word=choice["French"]
    english_word=choice["English"]
    canvas1.create_text(400, 150, text="French", font=("Arial", 40, "italic"),tag="lenguaje")
    canvas1.create_text(400, 263, text=france_word, font=("Arial", 60, "bold"),tag="word")
    flip_timer=window.after(3000,flip_card)



def flip_card():
    canvas1.itemconfig(canvas_image,image=new_image)
    canvas1.delete("word")
    canvas1.delete("lenguaje")
    canvas1.create_text(400, 150, text="English", font=("Arial", 40, "italic"),fill="white")
    canvas1.create_text(400, 263, text=choice["English"], font=("Arial", 60, "bold"),tag="word",fill="white")
    

def change_word_yes():
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    canvas1.itemconfig(canvas_image, image=old_image)
    update_word()
    dict.remove(choice)
    df=pandas.DataFrame(dict)
    df.to_csv("PYTHON/FlashCardProyect/data/words_to_learn.csv")
    

    


def change_word():
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    canvas1.itemconfig(canvas_image, image=old_image)
    update_word()
    








    

   
    
        
   











window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("card game")

old_image=PhotoImage(file="PYTHON\FlashCardProyect\images\card_front.png")
new_image=PhotoImage(file="PYTHON/FlashCardProyect/images/card_back.png")

canvas1=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,borderwidth=0,highlightthickness=0)
canvas_image=canvas1.create_image(400,263,image=old_image)
canvas1.grid(column=0,row=0,columnspan=2)

canvas1.create_text(400, 150, text="French", font=("Arial", 40, "italic"),tag="lenguaje")
canvas1.create_text(400, 263, text="Word", font=("Arial", 60, "bold"),tag="word")



wrong_image=PhotoImage(file="PYTHON\FlashCardProyect\images\wrong.png")
wrong_button=Button(image=wrong_image,borderwidth=0,highlightthickness=0,background=BACKGROUND_COLOR,command=change_word)
wrong_button.grid(column=0,row=1)




rigt_image=PhotoImage(file="PYTHON/FlashCardProyect/images/right.png")
right_button=Button(image=rigt_image,highlightthickness=0,background=BACKGROUND_COLOR,borderwidth=0,highlightcolor=BACKGROUND_COLOR,command=change_word_yes)
right_button.grid(column=1,row=1)






window.mainloop()

