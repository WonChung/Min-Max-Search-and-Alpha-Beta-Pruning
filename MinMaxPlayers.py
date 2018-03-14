########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2018, Swarthmore College
########################################
# full name(s):
# username(s):
########################################
from math import inf
class MinMaxPlayer:
    """Gets moves by depth-limited min-max search."""
    def __init__(self, boardEval, depthBound):
        self.name = "MinMax"
        self.boardEval = boardEval
        self.depthBound = depthBound

    def getMove(self, game_state):
        best_value, best_move = self.bounded_min_max(game_state, 0)
        return best_move


    def bounded_min_max(self, state, depth):
        if(state.isTerminal or self.depthBound == depth):
            return self.boardEval(state), None
        # best_value = self.boardEval(state)
        if(state.turn==1):
            best_value = -1*inf
        else:
            best_value = inf
        best_move = None
        for move in state.availableMoves:
            next_state = state.makeMove(move)
            value, boundedMove = self.bounded_min_max(next_state, depth+1)
            # if(value == None):
            #     continue
            if(state.turn==1):
                if(value > best_value):
                    best_value = value
                    best_move = move
            else:
                if(value < best_value):
                    best_value = value
                    best_move = move
        return best_value, best_move



class PruningPlayer:
    """Gets moves by depth-limited min-max search with alpha-beta pruning."""
    def __init__(self, boardEval, depthBound):
        self.name = "Pruning"
        self.boardEval = boardEval
        self.depthBound = depthBound

    def getMove(self, game_state):
        best_value, best_move = self.alpha_beta(game_state, inf, -1*inf, 0)
        return best_move

    def alpha_beta(self, state, UB, LB, depth):
        if(state.isTerminal or self.depthBound == depth):
            return self.boardEval(state), None
        if(state.turn==1):
            best_value = -1*inf
        else:
            best_value = inf
        best_move = None
        for move in state.availableMoves:
            next_state = state.makeMove(move)
            value, boundedMove = self.alpha_beta(next_state, UB, LB, depth+1)
            if(state.turn==1):
                if(value >= UB):
                    return value, boundedMove
                if(value > LB):
                    LB = value
                if(value > best_value):
                    best_value = value
                    best_move = move
            else:
                if(value <= LB):
                    return value, boundedMove
                if(value < UB):
                    UB = value
                if(value < best_value):
                    best_value = value
                    best_move = move
        return best_value, best_move
