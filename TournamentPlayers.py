########################################
# CS63: Artificial Intelligence, Lab 4
# Spring 2018, Swarthmore College
########################################
# NOTE: You should replace this with your TournamentPlayers.py
########################################

# from Heuristics import breakthroughBetterEval, mancalaBetterEval
# from MinMaxPlayers import PruningPlayer

class BreakthroughTournamentPlayer:
    """Default implementation for the Breakthrough tournament."""

    def __init__(self):
        self.name = "username1-username2" #TODO: put your username(s) here
        self.player = PruningPlayer(breakthroughBetterEval, 4)

    def getMove(self, game):
        return self.player.getMove()


class MancalaTournamentPlayer:
    """Default implementation for the Mancala tournament."""
    def __init__(self):
        self.name = "username1-username2" #TODO: put your username(s) here
        self.player = PruningPlayer(mancalaBetterEval, 4)

    def getMove(self, game):
        return self.player.getMove()
