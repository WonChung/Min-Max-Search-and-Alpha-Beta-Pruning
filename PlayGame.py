#! /usr/bin/env python3
########################################
# CS63: Artificial Intelligence, Lab 3
# Spring 2017, Swarthmore College
########################################
# NOTE: you should not need to modify this file.
########################################

from argparse import ArgumentParser

from Breakthrough import Breakthrough
from Mancala import Mancala
from BasicPlayers import HumanPlayer, RandomPlayer
from MinMaxPlayers import MinMaxPlayer, PruningPlayer
from TournamentPlayers import BreakthroughTournamentPlayer, \
                              MancalaTournamentPlayer
from Heuristics import mancalaBasicEval, breakthroughBasicEval, \
                       mancalaBetterEval, breakthroughBetterEval
from FriendAgent import TournamentPlayers as Friend

games = {"mancala":Mancala,
         "breakthrough":Breakthrough}

eval_options = ["basic", "better"]
eval_functions = {"mancala":{"basic":mancalaBasicEval,
                             "better":mancalaBetterEval},
             "breakthrough":{"basic":breakthroughBasicEval,
                             "better":breakthroughBetterEval}}


players = {"random":RandomPlayer,
           "human":HumanPlayer,
           "minmax":MinMaxPlayer,
           "pruning":PruningPlayer,
           "tournament":"tournament",
           "friend":"friend"}

tournament_players = {"mancala":MancalaTournamentPlayer,
                     "breakthrough":BreakthroughTournamentPlayer}

friend_players = {"mancala":Friend.MancalaTournamentPlayer,
                  "breakthrough":Friend.BreakthroughTournamentPlayer}

def main():
    args = parse_args()
    if args.p1 == "tournament":
        p1 = tournament_players[args.game]()
    elif args.p1 == "friend":
        p1 = friend_players[args.game]()
    elif args.p1 == "minmax" or args.p1 == "pruning":
        e1 = eval_functions[args.game][args.e1]
        p1 = players[args.p1](e1, args.d1)
    else:
        p1 = players[args.p1]()
    if args.p2 == "tournament":
        p2 = tournament_players[args.game]()
    elif args.p2 == "friend":
        p2 = friend_players[args.game]()
    elif args.p2 == "minmax" or args.p2 == "pruning":
        e2 = eval_functions[args.game][args.e2]
        p2 = players[args.p2](e2, args.d2)
    else:
        p2 = players[args.p2]()
    game = games[args.game](*args.game_args)

    if args.games == 1:
        play_game(game, p1, p2, args.show)
    else:
        p1_wins = 0
        p2_wins = 0
        draws = 0
        for i in range(args.games):
            if i % 2:
                result = play_game(game, p1, p2, args.show)
                if result.winner == 1:
                    p1_wins += 1
                elif result.winner == -1:
                    p2_wins += 1
                else:
                    draws += 1
            else:
                result = play_game(game, p2, p1, args.show)
                if result.winner == -1:
                    p1_wins += 1
                elif result.winner == 1:
                    p2_wins += 1
                else:
                    draws += 1
        print("results after", args.games, "games:")
        print(p1_wins, "wins for player 1 (" + p1.name + ")")
        print(p2_wins, "wins for player 2 (" + p2.name + ")")
        if draws > 0:
            print(draws, "draws")

def parse_args():
    p = ArgumentParser()
    p.add_argument("game", type=str, choices=list(games.keys()),
                   help="Game to be played.")
    p.add_argument("p1", type=str, choices=list(players.keys()),
                   help="Player 1 type.")
    p.add_argument("p2", type=str, choices=list(players.keys()),
                   help="Player 2 type.")
    p.add_argument("-games", type=int, default=1,
                   help="Number of games to play.")
    p.add_argument("--show", action="store_true", help=
                   "Set this flag to print the board every round.")
    p.add_argument("-game_args", type=int, nargs="*", default=[],
                   help="Optional arguments to pass to the game constructor, "+
                   "such as board dimensions. Must be listed in order.")
    p.add_argument("-e1", type=str, choices=eval_options, default="basic",
                   help="Board eval function for player 1.")
    p.add_argument("-e2", type=str, choices=eval_options, default="basic",
                   help="Board eval function for player 2.")
    p.add_argument("-d1", type=int, default=4,
                   help="Search depth for player 1.")
    p.add_argument("-d2", type=int, default=4,
                   help="Search depth for player 2.")
    return p.parse_args()

def play_game(game, player1, player2, show=False):
    """Plays a game then returns the final state."""
    while not game.isTerminal:
        if show:
            print(game)
        if game.turn == 1:
            m = player1.getMove(game)
        else:
            m = player2.getMove(game)
        if m not in game.availableMoves:
            raise Exception("invalid move: " + str(m))
        game = game.makeMove(m)
    if show:
        print(game, "\n")
        if game.winner != 0:
            print("player", game._print_char(game.winner), "wins")
        else:
            print("it's a draw")
    return game

if __name__ == "__main__":
    main()
