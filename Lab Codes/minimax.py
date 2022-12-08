# Tic-Tac-Toe MiniMax Bot
# CS420 - Assignment 2
# Name: Nathan Ayele
import random
from tttlib import *

def minimaxBot(mySpaces,opponentSpaces,emptySpaces):
    '''Returns an integer 1-9 to indicate current move, based on this board layout:
                1 | 2 | 3
                ---+---+---
                4 | 5 | 6
                ---+---+---
                7 | 8 | 9
       Each argument (mySpaces, opponentSpaces, and emptySpaces)
         is a set of integers, indicating the spaces taken by me,
         by my opponent, and untaken spaces on the board.
       Uses minimax algorithm to find optimal move at each turn.
    '''
    bestSpace = None
    bestValue = -2

    for space in emptySpaces:
        value = minimax(mySpaces|{space}, opponentSpaces, emptySpaces-{space}, maximizingPlayer=False)
        if (value > bestValue):
            bestValue = value
            bestSpace = space

    return bestSpace

def minimax(mySpaces,opponentSpaces, emptySpaces, maximizingPlayer=True):
    if playerWins( mySpaces ):
        return 1
    if playerWins (opponentSpaces):
        return -1
    if len(emptySpaces) == 0:
        return 0
    
    if maximizingPlayer:
        value = -20
        for space in emptySpaces:
            value = max(value, minimax(mySpaces|{space},opponentSpaces, emptySpaces-{space}, False))
        

    else:
        value = 2
        for space in emptySpaces:
            value = min(value, minimax(mySpaces, opponentSpaces|{space}, emptySpaces-{space}, True))
    
    return value
    
    