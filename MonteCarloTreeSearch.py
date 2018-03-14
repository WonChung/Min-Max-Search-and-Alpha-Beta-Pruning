########################################
# CS63: Artificial Intelligence, Lab 4
# Spring 2018, Swarthmore College
########################################
# full name(s): Won Chung and David Chang
# username(s): wchung3 and dchang2
########################################

#NOTE: You will probably want to make use of these imports.
#      Feel free to add more.
from math import log, sqrt
from numpy.random import choice
import random

class Node(object):
    """Node used in MCTS"""
    def __init__(self, state, parent_node):
        self.state = state
        self.children = {} # maps moves to Nodes
        self.visits = 0
        self.value = 0
        #NOTE: you may add additional fields if needed

    def updateValue(self, outcome):
        """Updates the value estimate for the node's state.
        outcome: a game object, where the winner field will store +1 for a
                1st player win, -1 for a 2nd player win, or 0 for a draw."""
        #2 is player 1 win
        #1 is draw
        #0 is player 2 win
        self.value = (self.value*self.visits + outcome + 1)/(self.visits + 1)
        self.visits += 1

    def UCBWeight(self, parent_visits, UCB_const, player):
        """Weight from the UCB formula used by parent to select a child.
        This node will be selected by the parent with probability
        proportional to its weight."""
        if(player==1):
            weight = self.value + UCB_const * sqrt(log(parent_visits)/self.visits)
        else:
            weight = (2 - self.value) + UCB_const * sqrt(log(parent_visits)/self.visits)
        return weight

class MCTSPlayer(object):
    """Selects moves using Monte Carlo tree search."""
    def __init__(self, rollouts=10000, UCB_const=0.9):
        self.name = "MCTS"
        self.rollouts = rollouts
        self.UCB_const = UCB_const
        self.nodes = {} #maps states to their nodes

    def getMove(self, game):
        #TODO: find the node for game if it exists, otherwise create one
        #TODO: call MCTS to perform rollouts
        #TODO: return the best move
        if(game in self.nodes):
            currentNode = self.nodes[game]
        else:
            currentNode = Node(game, None)
            self.nodes[game] = currentNode
        self.MCTS(currentNode)
        maxValue = 0
        minValue = 2
        maxMove = None
        minMove = None
        for move, node in currentNode.children.items():
            if (node.value >= maxValue):
                maxValue = node.value
                maxMove = move
            if (node.value <= minValue):
                minValue = node.value
                minMove = move
        if(currentNode.state.turn == 1):
            return maxMove
        else:
            return minMove

    def MCTS(self, root_node):
        """Plays random games from the root node to a terminal state.
        Each rollout consists of four phases:
            Selection: nodes are selected according to UCB as long as all
                    children have been expanded.
            Expansion: a new node is created for a random unexpanded child.
            Simulation: uniform random moves are played until the end of
                    the game.
            Backpropagation: values and visits are updated for each node
                    visited during selection and expansion."""
        for i in range(self.rollouts):
            node = root_node
            node.visits+=1
            path = []
            while(len(node.state.availableMoves)==len(node.children) and not node.state.isTerminal):
                weights = []
                childrenList = []
                for move, child in node.children.items():
                    weight = child.UCBWeight(node.visits, self.UCB_const, child.state.turn)
                    weights.append(weight)
                    childrenList.append(child)
                total = sum(weights)
                distribution = [i/total for i in weights]
                # print(childrenList)
                # print(distribution)
                node = choice(childrenList, 1, p=distribution)
                node = node[0]
                path.append(node)
            if(not node.state.isTerminal):
                move = random.choice(node.state.availableMoves)
                randomState = node.state.makeMove(move)
                new_node = Node(randomState, node)
                node.children[move]=new_node
                path.append(new_node)
                outcome = self.random_playout(new_node.state)
            else:
                outcome = node.state.winner
            for j in range(len(path)):
                path[j].updateValue(outcome)

    def random_playout(self, state):
        while(not state.isTerminal):
            state = state.makeMove(random.choice(state.availableMoves))
        return state.winner
