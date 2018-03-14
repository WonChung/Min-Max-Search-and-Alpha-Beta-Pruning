########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2018, Swarthmore College
########################################
# full name(s): Won Chung and David Chang
# username(s): wchung3 and dchang2
########################################

import numpy as np

def mancalaBasicEval(mancala_game):
    """Difference between the scores for each player.
    Returns +(max possible score) if player +1 has won.
    Returns -(max possible score) if player -1 has won.

    Otherwise returns (player +1's score) - (player -1's score).

    Remember that the number of houses and seeds may vary."""
    if(mancala_game.isTerminal):
        if mancala_game.winner == 1:
            return mancala_game.scores.max()
        elif mancala_game.winner == -1:
            return -1*mancala_game.scores.max()
        else:
            return 0
    else:
        return mancala_game.scores[0] - mancala_game.scores[1]

def breakthroughBasicEval(breakthrough_game):
    """Measures how far each player's pieces have advanced
    and returns the difference.

    Returns +(max possible advancement) if player +1 has won.
    Returns -(max possible advancement) if player -1 has won.

    Otherwise finds the rank of each piece (number of rows onto the board it
    has advanced), sums these ranks for each player, and
    returns (player +1's sum of ranks) - (player -1's sum of ranks).

    An example on a 5x3 board:
    ------------
    |  0  1  1 |  <-- player +1 has two pieces on rank 1
    |  1 -1  1 |  <-- +1 has two pieces on rank 2; -1 has one piece on rank 4
    |  0  1 -1 |  <-- +1 has (1 piece * rank 3); -1 has (1 piece * rank 3)
    | -1  0  0 |  <-- -1 has (1*2)
    | -1 -1 -1 |  <-- -1 has (3*1)
    ------------
    sum of +1's piece ranks = 1 + 1 + 2 + 2 + 3 = 9
    sum of -1's piece ranks = 1 + 1 + 1 + 2 + 3 + 4 = 12
    state value = 9 - 12 = -3

    Remember that the height and width of the board may vary."""
    if(breakthrough_game.isTerminal):
        if(breakthrough_game.winner==1):
            return len(breakthrough_game.board)*len(breakthrough_game.board[0])
        elif(breakthrough_game.winner==-1):
            return -1*len(breakthrough_game.board)*len(breakthrough_game.board[0])
        else:
            return 0
    else:
        board = breakthrough_game.board
        player1 = 0
        player2 = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == 1):
                    player1 += (row+1)
                elif(board[row][col] ==-1):
                    player2 += (len(board)-row)
        return (player1 - player2)

def mancalaBetterEval(mancala_game):
    """A heuristic that generally wins agains mancalaBasicEval.
    This must be a static evaluation function (no search allowed).

    This heuristic takes into account the available moves that will
    capture the opponent's marbles. This would be 1 + the number of marbles
    on the other side and this is added to the player1 or player2. This
    heuristic also finds the number of marbles on each side of the board for
    the respective players.

    Returns +/-(max score + #marbles on side + #marbles from capturing moves)
    if player 1/2 wins.

    otherwise returns the difference between their scores + difference between
    number of marbles on their sides + difference between number of marbles
    from capturing moves + difference between moves that will grant an extra
    move
    """
    marblesSide1 = sum(mancala_game.houses[0])
    marblesSide2 = sum(mancala_game.houses[1])
    marblesDifference = marblesSide1 - marblesSide2

    player1 = 0
    player2 = 0
    for i in range(len(mancala_game.houses[0])):
        if(mancala_game.houses[0][i]%(len(mancala_game.houses[0])*2+2)<=i):
            if(mancala_game.houses[1][i]!=0 and mancala_game.houses[0][i]!=0):
                player1+=mancala_game.houses[1][i]+1
        if(mancala_game.houses[1][i]%(len(mancala_game.houses[0])*2+2)<len(mancala_game.houses[0])-i):
            if(mancala_game.houses[1][i]!=0 and mancala_game.houses[0][i]!=0):
                player2+=mancala_game.houses[0][i]+1
        if mancala_game.houses[0][i] == i+1:
            player1 += 2
        if mancala_game.houses[1][i] == len(mancala_game.houses[0]) -  i:
            player2 += 2
    if(mancala_game.isTerminal):
        if mancala_game.winner == 1:
            return mancala_game.scores.max() + marblesSide1 + player1
        elif mancala_game.winner == -1:
            return -1*(mancala_game.scores.max()+marblesSide2 + player2)
        else:
            return 0
    else:
        return (mancala_game.scores[0] - mancala_game.scores[1] + player1 - player2 + marblesDifference)

def breakthroughBetterEval(breakthrough_game):
    """A heuristic that generally wins agains breakthroughBasicEval.
    This must be a static evaluation function (no searchin allowed).

    Measures how far each player's pieces have advanced
    and returns the difference. However, more weight is given to
    pieces that are further towards the other side

    Returns +(max possible advancement)**3 if player +1 has won.
    Returns -(max possible advancement)**3 if player -1 has won.

    Otherwise finds the rank of each piece (number of rows onto the board it
    has advanced), sums these ranks for each player, subtracts if the move will
    result in the piece being capture, and returns
    (player+1's sum of ranks (rank is 0 if the move results in piece captured))**3
    - (player-1's sum of ranks (rank is 0 if the move results in piece captured))**3."""
    if(breakthrough_game.isTerminal):
        if(breakthrough_game.winner == 1):
            return (len(breakthrough_game.board)*len(breakthrough_game.board[0]))
        else:
            return -1*((len(breakthrough_game.board)*len(breakthrough_game.board[0])))
    else:
        board = breakthrough_game.board
        player1 = 0
        player2 = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == 1):
                    player1 += ((row+1)**3)
                    if((row < (len(board)-3)) and col > 0 and col < len(board[0])-1):
                        if((board[row+2][col+1] == -1) or (board[row+2][col-1] == -1) or (board[row+3][col+1] == -1) or (board[row+3][col-1] == -1)):
                            player1 -= (row+1)**3

                elif(board[row][col] == -1):
                    player2 += ((len(board)-row)**3)
                    if((row > 3) and col > 0 and col < len(board[0])-1):
                        if((board[row-2][col+1] == 1) or (board[row-2][col-1] == 1) or (board[row-3][col+1] == 1) or (board[row-3][col-1] == 1)):
                            player2 -= (len(board)-row)**3

        return (player1-player2)
