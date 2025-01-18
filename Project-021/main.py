import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")

image = r"C:\Users\sodiu\OneDrive\Documents\Coding\Python Projects\Project-021\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(r"C:\Users\sodiu\OneDrive\Documents\Coding\Python Projects\Project-021\50_states.csv")
all_state = data.state.to_list()
no_of_states = 0
correct_guess = []

while no_of_states < 51 :
    answer_input = screen.textinput(title= f"{no_of_states}/50 states", prompt="What's other state name?").title()
    correct_guess.append(answer_input)
    if answer_input in all_state :
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        state_data = data[data.state == answer_input]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_input)
        no_of_states += 1
        all_state.remove(answer_input)



screen.exitonclick()  