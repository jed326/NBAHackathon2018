import os, csv
import GameDataType as gdt

#Processes a line of data in the gameid.csv file
def processLine(line):
    pass

#################################
# Row definitions:
# row[1]: Game_id
# row[2]: Event_Num
# row[3]: Event_Msg_Type
# row[4]: Period
# row[5]: WC_Time
# row[6]: PC_Time
# row[7]: Action_Type
# row[8]: Option1 - point value of a shot
# row[9]: Team_id
# row[10]: Person1
# row[11]: Person2

def processGames():
    with open("../Tilted_Towers_Q1_BBALL.csv", "w") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(['Game_ID', 'Player_ID', 'Player_Plus/Minus'])
        file.close()

    for filename in os.listdir("../Games/"):
        game = gdt.Game(filename[:-4]) #Initialize game object with gameid.
        createTeams(game)
        print(game, '\n')
        with open("../Games/" + filename) as file: #Opens a gameid.csv file
            reader = csv.reader(file, delimiter=',')
            getRoster(game, game.teams[0])
            getRoster(game, game.teams[1])
            print("Team 1 roster:")
            game.teams[0].printRoster()
            print("")
            print("Team 2 roster:")
            game.teams[1].printRoster()
            print("")
            period = "0"
            for row in reader:
                if(row[0] != ""):
                    if(period != row[4]): #if a new period is starting
                        period = row[4]
                        print("Starting rosters for period %s:" % (row[4]))
                        getStarters(game, game.teams[0], period)
                        getStarters(game, game.teams[1], period)
                        print("Team 1:")
                        print(game.teams[0])
                        print("Team 2:")
                        print(game.teams[1])
                    else:
                        #Scoring Event_Msg_Types: 1,3, 
                        if(row[3] == "1" or row[3] == "3"):
                            addPoints(getTeam(game, row[9]), row[8])
                            subtractPoints(getOtherTeam(game, row[9]), row[8])
                        elif(row[3] == "8"):
                            changePlayer(getTeam(game, row[9]), row[10], row[11])
                            #print("PLAYER CHANGE")    
            #process event type
            print("TEAM 1: ")
            game.teams[0].printRoster()
            print("TEAM 2: ")
            game.teams[1].printRoster()
            writeToCSV(game)
        #return

def writeToCSV(game):
    with open("../Tilted_Towers_Q1_BBALL.csv", "a") as file:
        writer = csv.writer(file, delimiter=",")
        for team in game.teams:
            for player, pm in team.roster.items():
                writer.writerow([game.id, player.id, pm])
        file.close()

def getTeam(game, team_id):
    if(game.teams[0].id == team_id):
        return game.teams[0]
    elif(game.teams[1].id == team_id):
        return game.teams[1]

def getOtherTeam(game, team_id):
    if(game.teams[0].id == team_id):
        return game.teams[1]
    elif(game.teams[1].id == team_id):
        return game.teams[0]

def subtractPoints(team, points):
    #print(points, team.id)
    players = team.onCourt
    for player in team.roster.keys():
        if player.id in [x.id for x in players]:
            team.roster[player] -= int(points)

def addPoints(team, points):
    #print(points, team.id)
    players = team.onCourt
    for player in team.roster.keys():
        if player.id in [x.id for x in players]:
            team.roster[player] += int(points)

def changePlayer(team, player1, player2):
    #print(team.id, player1, player2)
    if( player2 not in [player.id for player in team.roster.keys()]):
        team.roster.update({gdt.Player(player2): 0})
    for spot in range(len(team.onCourt)):
        if(team.onCourt[spot].id == player1):
            team.onCourt[spot] = gdt.Player(player1)

def createTeams(game):
    with open("../NBA Hackathon - Game Lineup Data Sample (50 Games).txt") as file:
        reader = csv.reader(file, delimiter='\t')
        teamsAdded = 0 #counter variable for adding new teams to the game
        for row in reader:
            if(row[0] != '' and row[0] == game.id):
                if(teamsAdded < 2):
                    if(row[3] not in [team.id for team in game.teams]):
                        game.teams.append(gdt.Team(row[3]))
                        teamsAdded += 1
                else:
                    return

def getStarters(game, team, period):
    team.onCourt = []
    with open("../NBA Hackathon - Game Lineup Data Sample (50 Games).txt") as file:
        reader = csv.reader(file, delimiter='\t')
        playersAdded = 0 #counter variable for adding new teams to the game
        for row in reader:
            if(row[0] != '' and row[0] == game.id and row[3] == team.id and row[1] == period):
                if(playersAdded < 5 and (row[2] not in [player.id for player in team.onCourt])):
                    team.onCourt.append(gdt.Player(row[2]))
                    playersAdded += 1
                else:
                    return

def getRoster(game, team):
    with open("../NBA Hackathon - Game Lineup Data Sample (50 Games).txt") as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if(row[0] != '' and row[0] == game.id and row[3] == team.id):
                if((row[2] not in [player.id for player in team.roster.keys()])):
                    team.roster.update({gdt.Player(row[2]): 0})
                else:
                    return
            
if __name__ == "__main__":
    processGames()