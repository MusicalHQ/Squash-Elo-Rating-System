import math

class player:
    def __init__(self,name,wins,losses,age,elo=1500):
        self.elo = elo
        self.wins = wins
        self.losses = losses
        self.age = age
        self.name = name

def match(winner,loser,score,k=32):
    new_elo = calc(winner.elo,loser.elo,score)
    winner.elo = new_elo[0]
    loser.elo = new_elo[1]

def expected(A, B):
    return 1/(1+ 10 ** ((B - A)/400))

def elo(old, exp, result, k_multiplier, k=32):
    return old + (k*k_multiplier) * (result - exp)

def calc(winner,loser,score,k=32,use_multiplier = True):
    k_multiplier = math.log(abs(score[0]-score[1])+1) * (2.2/((winner.elo-loser.elo)*0.001+2.2))
    exp_winner = expected(winner.elo,loser.elo)
    exp_loser = expected(loser.elo,winner.elo)
    elo_winner = elo(winner.elo,exp_winner,1,k_multiplier,k)
    elo_loser = elo(loser.elo,exp_loser,0,k_multiplier,k)
    return [elo_winner,elo_loser]
