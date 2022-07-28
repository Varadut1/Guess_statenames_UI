import turtle
import pandas
screen = turtle.Screen()
x=0
screen.title(f"Score:0/50")
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')
data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer = (screen.textinput(f"Score:{x}/50", prompt='Give a state name: ')).title()
    if answer==(None or 'Exit'):
        break

    if answer in state_list:
        x+=1
        xcor=int(data[data.state==answer].x)
        ycor = int(data[data.state == answer].y)
        tim=turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(xcor,ycor)
        tim.write(answer, align='center')
        print(answer)
        guessed_state.append(answer)
    else:
        pass
screen.exitonclick()

pandas.DataFrame([i for i in state_list if i not in guessed_state]).to_csv('States to learn.csv')


