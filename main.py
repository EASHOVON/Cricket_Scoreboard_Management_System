
# Making Team Class
class Team:
    def __init__(self,name) -> None:
        self.teamName = name
        self.playersListOfObject = []

    def entry_player(self,player): ## Player is a type of object
        self.playersListOfObject.append(player)


bangladesh = Team("Bangladesh")
india = Team("India")

