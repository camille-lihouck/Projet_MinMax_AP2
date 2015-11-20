

# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``tictactoe``

   :author: Camille Lihouck, Agayer Meryem, Farah Bouchahdane 
   
   :date:  2015, october
   
   This module is an implementation of the :mod:`abstractgame` for a tic tac toe for two player games.

"""

_DEFAULT_HEIGHT = 3
_DEFAULT_WIDTH = 3


def initSituation(game):
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
    board=[]
    if ('width' in game):
        w=game['width']
    else :
        w=_DEFAULT_WIDTH
    if ('height' in game):
        h=game[height]
    else :
        h=_DEFAULT_HEIGHT
    for i in range(w):
        board.append([])
        for j in range(h):
            board.append('')
    return board


def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    return situation == board



def playerCanPlay(game, situation, player):
    """
    tells whether player can play in given situation

    :param game: the game 
    :type game: game
    :param situation: the situation to display
    :type situation: a game situation
    :param player: the player
    :type player: player
    :returns: *(boolean)* -- True iff player can play in situation
    """
    return True


def nextSituations(game, situation, player):
    """
    returns the list of situations that can be reached from given situation by the player in the game

    :param game: the game
    :type game: a two players game
    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(list<situtation>)* -- the list of situations that can be reached from given situation when player plays one round in the game
    """
    next = []
    




def getWinner(game, situation, player):
    """
    Gives the winner of the game that end in situation

    :param game: the game 
    :type game: game
    :param situation: the situation which is a final game situation
    :type situation: a game situation
    :param player: the player who should have played if situation was not final (then other player plays previous turn)
    :type player: player
    :returns: *(player)* -- the winner player or None in case of tie game

    :CU: situation is a final situation
    """
      





def displaySituation(situation):
    """
    displays the situation, here the grid with 9 boxs of the game.

    :param situation: the situation to display
    :type situation: a game situation
    """
    for i in range(3):
        print('|_|_|_|')


def humanPlayerPlays(game, player, situation):
    """
    makes the human player plays for given situation in the game

    :param game: the game 
    :type game: game
    :param player: the human player
    :type player: player
    :param situation: the current situation
    :type situation: a game situation
    :returns: *(game situtation)* -- the game situation reached afte the human player play
    """
    

