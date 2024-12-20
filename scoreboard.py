from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")



class score_board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/python_programs/Udemy_bootcamp/PROJECTS/SnakeGame/data.txt") as data:
            self.highscore = int(data.read())
            
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align = ALIGNMENT, font =FONT)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align = ALIGNMENT, font =FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/../../../../data.txt", mode = 'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
        
        
    def increase_score(self):
        self.score += 1
        self.update_score()       
        