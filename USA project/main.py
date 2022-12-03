import pandas as pd
import turtle

data = pd.read_csv("50_states.csv")
states = data["state"].tolist()

screen = turtle.Screen()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

t = turtle.Turtle()
t.penup()
t.hideturtle()

while len(guessed_states) < 50:
    ans_state = (screen.textinput(title=f"{len(guessed_states)}/50 states guessed:",
                                  prompt=f"What's another state's name: ")).title()
    if ans_state == "Exit":
        missing_states = [stat for stat in states if stat not in guessed_states]
        dat = pd.DataFrame(guessed_states)
        dat.to_csv("guessed states.csv")
        break
    if ans_state in states:
        ans = data[data.state == ans_state]
        x = int(ans.x)
        y = int(ans.y)
        t.goto(x, y)
        t.write(ans_state)
        guessed_states.append(ans_state)

