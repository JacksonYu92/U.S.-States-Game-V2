from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

def show_state(state, x, y):
    state_show = Turtle()
    state_show.hideturtle()
    state_show.penup()
    state_show.goto(x, y)
    state_show.write(state, align="center", font=("Arial", "8", "normal"))

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?")
    guess = str(answer_state.title())

    data = pandas.read_csv("50_states.csv")
    states = data.state

    if guess == "Exit":
        missing_state = [state for state in states if state not in correct_guesses]
        missing_state_x = [int(data[states == state].x) for state in states if state not in correct_guesses]
        missing_state_y = [int(data[states == state].y) for state in states if state not in correct_guesses]
        # for state in states:
        #     if state not in correct_guesses:
        #         missing_state.append(state)
        #         missing_state_x.append(int(data[states == state].x))
        #         missing_state_y.append(int(data[states == state].y))

        df = pandas.DataFrame({"state": missing_state,
                               "x": missing_state_x,
                               "y": missing_state_y})
        df.to_csv("states_to_learn.csv", index=False)
        break

    for state in states:
        if guess == state:
            state_row = data[states == guess]
            state_x = int(state_row.x)
            state_y = int(state_row.y)
            show_state(guess, state_x, state_y)
            correct_guesses.append(guess)









# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()


screen.exitonclick()