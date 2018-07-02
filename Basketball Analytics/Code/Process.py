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
# row[11]: Person 2

def processGames():
    for filename in os.listdir("../Games/"):
        game = gdt.Game(filename[:-4]) #Initialize game object with gameid.
        createTeams(game)
        print(game)
        print("")
        with open("../Games/" + filename) as file: #Opens a gameid.csv file
            reader = csv.reader(file, delimiter=',')
            team1Playing = []
            team2Playing = []
            period = "0"
            for row in reader:
                if(row[0] != ""):
                    if(period != row[4]): #checks if a new period is starting
                        print("Starting roster for period %s:" % (row[4]))
                        team1Playing = getPlaying(game, game.teams[0])
                        print(game.teams[0])
                        team2Playing = getPlaying(game, game.teams[1])
                        print(game.teams[1])
                        period = row[4]
                    #process event type
        return


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

def getPlaying(game, team):
    team.players = []
    with open("../NBA Hackathon - Game Lineup Data Sample (50 Games).txt") as file:
        reader = csv.reader(file, delimiter='\t')
        playersAdded = 0 #counter variable for adding new teams to the game
        for row in reader:
            if(row[0] != '' and row[0] == game.id and row[3] == team.id):
                if(playersAdded < 5):
                    if(row[2] not in [player.id for player in team.players]):
                        team.players.append(gdt.Player(row[2]))
                        playersAdded += 1
                else:
                    return
            
if __name__ == "__main__":
    processGames()