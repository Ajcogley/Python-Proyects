from turtle import Turtle,Screen
positions=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.serpiente=[]

    def create_square(self):
        for position in positions:
            self.add_segment(position)
            

    def move(self):
        
        for n in range(len(self.serpiente)-1,0,-1):
            new_x=self.serpiente[n-1].xcor()
            new_y=self.serpiente[n-1].ycor()
            self.serpiente[n].goto(new_x,new_y)
        self.serpiente[0].forward(20)


    def add_segment(self,position):
        new_segment=Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.serpiente.append(new_segment)

    def extend(self):
        self.add_segment(self.serpiente[-1].position())

    def reset(self):
        for n in self.serpiente:
            n.goto(1000,10000)
        self.serpiente.clear()
        self.create_square()
        



    
    def up(self):
        if self.serpiente[0].heading()!=270:
            self.serpiente[0].setheading(90)
        
        
    def down(self):
        if self.serpiente[0].heading()!=90:
            self.serpiente[0].setheading(270)


    def left(self):
        if self.serpiente[0].heading()!=0:
            self.serpiente[0].setheading(180)

    def right(self):
        if self.serpiente[0].heading()!=180:
            self.serpiente[0].setheading(0)

 


       
        

        




        
