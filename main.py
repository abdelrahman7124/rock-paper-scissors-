import random

class Player:
    def __init__(self):
        self.score = []
        self.scoreInt = 0
    def scoreAppend(self, score):
        self.score.append(score)
    def scoreUpdate(self, score):
        self.scoreInt += score
    def generateRandomNumber(self):
        self.rand = random.randrange(1, 4)
    
def Win(Player):
    Player.scoreAppend(1)
    Player.scoreUpdate(1)

def lose(Player):
    Player.scoreAppend(0)
    Player.scoreUpdate(0)

p1 = Player()
p2 = Player()
condition ={
    1: 3,
    2: 1,
    3: 2
}
while True:
    p1.score=[]
    p2.score=[]
    p1.scoreInt=p2.scoreInt=0
    for i in range(4):
        p1.generateRandomNumber()
        p2.generateRandomNumber()
        print(f"p1={p1.rand}")
        print(f"p2={p2.rand}")
        if p1.rand == p2.rand:
            lose(p1)
            lose(p2)
        elif condition.get(p1.rand) == p2.rand:
            Win(p1)
            lose(p2)
        else:
            Win(p2)
            lose(p1)
    print(f"Player1 score per round = {p1.score}")
    print(f"Player2 score per round = {p2.score}")
    print(f"P1 score={p1.scoreInt}")
    print(f"P2 score={p2.scoreInt}")
    if p1.scoreInt > p2.scoreInt:
        print("Player1 Wins!")
    elif p1.scoreInt < p2.scoreInt:
        print("Player2 Wins!")
    else:
        print("Draw!")
    
    while True:
        choice = input("Do you want to play again (enter yes or no): ")
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            break
        else:
            print("Invalid input, enter another one")

    if choice.lower() == "no":
        break
        