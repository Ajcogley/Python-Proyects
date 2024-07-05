import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S Stastes Game")
image="python/UsStatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on=True
guessed=[]


while len(guessed)<50:
    answer_state=screen.textinput(title=f"Guess the State   {len(guessed)}/50",prompt=" Whatas another state name?")

    data=pandas.read_csv("python/UsStatesGame/50_states.csv")

    states=data["state"].to_list()

    if answer_state=="exit":
        for n in states:
            no_guessed=[n for n in guessed if  n not in guessed]
            newdata=pandas.DataFrame(no_guessed)
            newdata.to_csv("python/UsStatesGame/ToLearn")
        break


   
    if answer_state in states:
        guessed.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        column=data[data["state"]==answer_state]
        t.teleport(int(column.x),int(column.y))
        t.write(answer_state)





screen.exitonclick()





