# Making Tournament
class T2Cup:
    allTeams = []
    def entry_team(self,teamObj):
        self.allTeams.append(teamObj)


# Making Team Class
class Team(T2Cup):
    def __init__(self,name) -> None:
        self.teamName = name
        self.playersListOfObject = []
        super().entry_team(self)

    def entry_player(self,player): ## Player is a type of object
        self.playersListOfObject.append(player)

    def __repr__(self) -> str:
        return f"Team Name: {self.teamName}"

# Making class Player
class Player:
    def __init__(self,name,teamObj) -> None:
        self.playerName = name
        self.strikeRate = 0.0
        self.runBat = 0
        self.ballUsed = 0
        self.fours = 0
        self.sixes = 0
        self.runBowl = 0
        self.wicketsTaken = 0
        self.ballsBowled = 0
        teamObj.playersListOfObject.append(self)

    def __repr__(self) -> str:
        return f"Name: {self.playerName}"



# Making Innings Class
class Innings:
    def __init__(self,teamOne,teamTwo,battingTeam,bowlingTeam) -> None:
        self.teamOneObj = teamOne
        self.teamTwoObj = teamTwo
        self.battingTeam = battingTeam
        self.bowlingTeam = bowlingTeam
        self.totalRun = 0
        self.totalWickets = 0
        self.totalOver = 0
        self.currentBall = 0
        self.currentBattingList = [battingTeam.playersListOfObject[0],battingTeam.playersListOfObject[1]]
        self.striker = battingTeam.playersListOfObject[0]
        self.currentBowler = None
        self.currentOverStatus = []
        self.allOversStatus = []

cup = T2Cup()
bangladesh = Team("Bangladesh")
india = Team("India")

tamim = Player("Tamim Iqbal",bangladesh)
sakib = Player("Sakib Al Hasan",bangladesh)
mustafiz = Player("Mustafizur Rahman",bangladesh)
kohli = Player("Virat Kohli",india)
rohit = Player("Rohit Sharma",india)
bumra = Player("Bumrah",india)

while True:
    print(cup.allTeams)


    break

