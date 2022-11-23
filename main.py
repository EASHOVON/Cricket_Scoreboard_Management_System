
# Making Team Class
class Team:
    def __init__(self,name) -> None:
        self.teamName = name
        self.playersListOfObject = []

    def entry_player(self,player): ## Player is a type of object
        self.playersListOfObject.append(player)


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

bangladesh = Team("Bangladesh")
india = Team("India")

tamim = Player("Tamim Iqbal",bangladesh)
sakib = Player("Sakib Al Hasan",bangladesh)
mustafiz = Player("Mustafizur Rahman",bangladesh)

print(bangladesh.playersListOfObject)

