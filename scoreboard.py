from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.create_level()

    def create_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.create_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=FONT)

