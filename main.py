from EloCalculations import *
from SaveData import *

players = data('players')

done = False

def find_player(player):
    global players
    for i in players.data:
        if i.name.lower() == player.lower():
            break
    else:
        print("Player doesn't exist")
        i = None
    return i
        

while not done:  
    command = str(input("cmd: "))
    try:
        if command == "input new player":
            name = str(input("name: "))
            age = str(input("age: "))
            players.data.append(player(name,0,0,age))
        elif command == "input match":
            winner = str(input("winner: "))
            loser = str(input("loser: "))
            winner_score = int(input("winner score: "))
            loser_score = int(input("loser score: "))
            winner = find_player(winner)
            loser = find_player(loser)
            winner.wins += 1
            loser.losses += 1
            new_elos = calc(winner,loser,[winner_score,loser_score])
            winner.elo = new_elos[0]
            loser.elo = new_elos[1]
        elif command == "output player":
            player = str(input("player: "))
            player = find_player(player)
            print("")
            print("---")
            print("Name: ",player.name)
            print("Age: ",player.age)
            print("Wins: ",player.wins)
            print("Loses: ",player.losses)
            print("Elo: ",round(player.elo))
            print("---")
            print("")
        elif command == "reset players":
            players.data = []
            players.save()
            print("players reset")
        elif command == "output rankings":
            print("")
            print("---")
            sorted_players = sorted(players.data, key=lambda x: x.elo, reverse = True)
            for i in sorted_players:
                print((sorted_players.index(i) + 1),"- ",i.name,": ",round(i.elo))
            print("---")
            print("")
        elif command == "matchmaking":
            player = str(input("player: "))
            player = find_player(player)
            sorted_players = sorted(players.data, key=lambda x: x.elo, reverse = True)
            if sorted_players.index(player) == 0:
                print("Suggested matchup: ",player.name," vs ",sorted_players[1].name)
            elif player == sorted_players[-1]:
                print("Suggested matchup: ",player.name, " vs ", sorted_players[-2].name)
            else:
                player_above = sorted_players[(sorted_players.index(player) + 1)]
                player_below = sorted_players[(sorted_players.index(player) - 1)]
                print("Suggested matchup: ",player.name," vs ",player_above.name)
                print("Suggested matchup: ",player.name," vs ",player_below.name)
            
        elif command == "end":
            done = True
    except:
        print("an error occurred, please try again")
        print("make sure there are no spaces at the end when typing in names")
    print("")
    

players.save()
