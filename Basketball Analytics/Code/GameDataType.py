class Player:
    def __init__(self, id):
        self.id = id
        self.PM = 0

class Team:
    def __init__(self, team_id):
        self.id = team_id
        self.onCourt = []
        self.roster = {}

    def printRoster(self):
        for player in self.roster.keys():
            print(player.id)

    def __str__(self):
        for player in self.onCourt:
            print(player.id)
        return ""

class Game:
    def __init__(self, game_id):
        self.id = game_id
        self.teams = []

    def __str__(self):
        print("Game ID:", self.id)
        return "Team 1: %s\nTeam 2: %s" % (self.teams[0].id, self.teams[1].id)