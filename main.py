import random
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

    def show_score_board(self):
        print(f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat}({self.currentBattingList[0].ballUsed})",end="\t")
        print(f"{self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat}({self.currentBattingList[1].ballUsed})")
        print(f"{battingTeamObj.teamName[:3].upper()} | {self.totalRun}-{self.totalWickets}")
        print(f"Overs: {self.totalOver}.{self.currentBall}")
        if self.currentBowler is not None:
            print(f"{self.currentBowler.playerName} - {self.currentBowler.runBowl}/{self.currentBowler.wicketsTaken}")

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
    print("Select teams to be played")
    for i,val in enumerate(cup.allTeams):
        print(f"{i+1}. {val.teamName}")
    teamOneIndex,teamTwoIndex = map(int,input("Enter two team indexes: ").split(" "))
    teamOneIndex = -1
    teamTwoIndex = -1
    teamOneObj = cup.allTeams[teamOneIndex]
    teamTwoObj = cup.allTeams[teamTwoIndex]
    tossWin = random.choice([teamOneIndex,teamTwoIndex])
    print(f"{cup.allTeams[tossWin].teamName} wins toss")
    if tossWin == teamOneIndex:
        tossLose = teamTwoIndex
    else:
        tossLose = teamOneIndex
    rand = random.choice([0,1])
    if rand == 0:
        # Winner Team Choose Bowling
        print(f"{cup.allTeams[tossWin].teamName} choose bowling")
        battingTeamObj = cup.allTeams[tossLose]
        bowlingTeamObj = cup.allTeams[tossWin]
    else:
        # Winner Team Choose Batting
        print(f"{cup.allTeams[tossWin].teamName} choose batting")
        battingTeamObj = cup.allTeams[tossWin]
        bowlingTeamObj = cup.allTeams[tossLose]
    firstInnings = Innings(teamOneObj,teamTwoObj,battingTeamObj,bowlingTeamObj)
    firstInnings.show_score_board()


    break

