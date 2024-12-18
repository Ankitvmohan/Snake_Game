from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")



class score_board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align = ALIGNMENT, font =FONT)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}",align = ALIGNMENT, font =FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align = ALIGNMENT, font =FONT)
        
        