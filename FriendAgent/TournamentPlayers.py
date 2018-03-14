########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2018, Swarthmore College
########################################
# full name(s):
# username(s):
########################################

from Heuristics import breakthroughBetterEval
from MinMaxPlayers import PruningPlayer

class BreakthroughTournamentPlayer:
    """This is your submission to the Breakthrough tournament.

    The Breakthrough tournament focuses on designing board evaluation
    heuristics. All agents submitted to this tournament must run min/max search
    with alpha/beta pruning and a depth limit of 4. Your goal for this
    tournament is to design the best possible static evaluation function to
    help your agent make good decisions with a limited search depth. Static
    evaluation functions must be deterministic and must not perform additional
    search.

    The tournament will use a 7-row, 5-column board. A time limit of 15 seconds
    will be enforced on each move; if the time limit is exceeded a random move
    will be played. Each pair of teams will play two games, alternating which
    agent moves first. If needed, other board sizes may be used to break ties.

    The Breakthrough tournament is opt-out. If you do not want to participate,
    please see Piazza for instructions on opting out."""

    def __init__(self):
        """The current implementation of the BreakthroughTournamentPlayer
        creates a PruningPlayer instance with depth limit 4 and the
        breakthroughBetterEval heuristic. You are welcome to re-implement this
        (for example, calling an additional heuristic), subject to the rules
        outlined above.
        """
        self.name = "username1-username2" #TODO: put your username(s) here
        self.player = PruningPlayer(breakthroughBetterEval, 4)

    def getMove(self, game):
        return self.player.getMove()


class MancalaTournamentPlayer:
    """This is your submission to the Mancala tournament.

    For the Mancala tournament, you may implement any heuristic and any variety
    of game tree search you like, including iterative deepening. It is up to you
    how to trade off between computation time spent on evaluating heuristics and
    computation time spent searching. Your agent MAY NOT use Monte Carlo tree
    search or other randomized algorithms.

    The tournament will use 6 houses per player and 4 seeds per house. A time
    limit of 15 seconds will be enforced on each move; if the time limit is
    exceeded a random move will be played. Each pair of teams will play an
    even two games, alternating which agent moves first. If needed, games
    of other sizes may be used to break ties.

    The Mancala tournament is opt-in. If you want to participate, please see
    Piazza for instructions on opting in."""
    def __init__(self):
        self.name = "username1-username2" #TODO: put your username(s) here
        raise NotImplementedError("Optional")

    def getMove(self, game):
        raise NotImplementedError("Optional")
