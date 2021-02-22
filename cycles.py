
import os
from pprint import pprint
import json
import numpy as np
from cycleutil import simple_cycles


# This script checks for cycles in the graph P[i,j]>threshold, where P[i,j] is the average number of
# points won when a game is completed between algorithms i and j.
#
# I was curious to see if there were any cycles, as this might indicate that the Elo system might
# need to be replaced with something slightly fancier, perhaps https://arxiv.org/pdf/1806.02643.pdf
# However, this doesn't seem to be a big issue, yet.
#
# So for now this serves as an example of extracting the game results and doing something with them.


OPTIMIZER_ELO_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'results'
GAME_LOG_PATH = OPTIMIZER_ELO_PATH + os.path.sep + 'games'


def load_games(n_games):
    games = list()
    i = 0
    for subdir, dirs, files in os.walk(GAME_LOG_PATH):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".json"):
                with open(GAME_LOG_PATH+os.path.sep+filename,'rt') as fp:
                   games.append(json.load(fp))
                   i+=1
            if i>=n_games:
                break
    return games


def head_to_head(n_games):
    games = load_games(n_games=n_games)
    players = set()
    for game in games:
        players.add(game['white'])
        players.add(game['black'])
    ordered_players = sorted(list(players))
    n_players = len(ordered_players)
    A = np.zeros(shape=[n_players,n_players])
    C = np.zeros(shape=[n_players, n_players])
    for game in games:
        if all(game['passing']) and game['points'] is not None:
            w = ordered_players.index(game['white'])
            b = ordered_players.index(game['black'])
            A[w,b] = A[w,b] + game['points']
            C[w,b] = C[w,b] + 1
            A[b, w] = A[b, w] + (1.0- game['points'])
            C[b, w] = C[b, w] + 1
    P = np.divide(A,C)
    return P, ordered_players


def domination_graph(threshold:float, n_games:int):
    P, players = head_to_head(n_games=n_games)
    n = P.shape[0]
    G = dict()
    for j, player in enumerate(players):
        G[player] = [ players[k] for k in range(n) if k!=j and 1>P[j,k]>threshold ]
    return G, players, P


def domination_cycles(threshold,n_games):
    G, players, P = domination_graph(threshold=threshold,n_games=n_games)
    C = simple_cycles(G)
    return C, players, P, G


def annotated_cycles(max_cycle_len=8):
    C, players, P, G = domination_cycles(n_games=100000, threshold=0.55)
    annotated_cycles = list()
    for c in C:
        if len(c)<=max_cycle_len:
            pprint(c)
            ac = list()
            for j, player in enumerate(c):
                next_player = c[ (j+1) % len(c) ]
                i1 = players.index(player)
                i2 = players.index(next_player)
                Pij = P[i1,i2]
                ac.append( (player,next_player,Pij) )
            annotated_cycles.append(ac)
            pprint(ac)
            print(' ')
    return annotated_cycles, C, players, P, G

if __name__=='__main__':
    ac = annotated_cycles()
    print('_______DONE_______ ')
    print('There were '+str(len(ac))+' cycles ')

