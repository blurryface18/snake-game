from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
with open("data.txt") as highest_score:
    content = highest_score.read()
HIGH_SCORE = int(content)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def resett(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as update_highest:
                update_highest.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",
    #                align=ALIGNMENT,
    #                font=FONT)
