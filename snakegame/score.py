
from turtle import Turtle

class Score(Turtle):
   def __init__(self):
       super().__init__()
       self.color("white")
       self.penup()
       self.goto(0,270)
       self.hideturtle()
       self.escore=0
       with open("python/snakegame/data.txt") as data:
           self.highscore=int(data.read())
        
      
       self.increase_score()
   


   def increase_score(self):
       self.clear()
       self.escore+=1
       self.write(arg=f"score: {self.escore} High Score: {self.highscore}",move=True,align="center",font=("arial",20,"normal"))
       self.teleport(0,270)


   def reset(self):
       if self.escore>self.highscore:
           self.highscore=self.escore
           with open("python/snakegame/data.txt", mode="w") as data: 
                data.write(f"{self.highscore}")
      
       self.escore=0
       self.increase_score()


        
    
        
        




    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center",font=("arial",20,"normal"))
        


        

