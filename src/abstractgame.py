

# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``abstractgame``

   :author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_
   
   :date:  2015, october
   
   This module defines an abstraction for two player games.
   This abstraction is used by :mod:`twoplayersgame` module.
   
   To define a particular game you have to chose how to design a game
   situation and then to create a module that implements the functions in
   this module.  Then, you can replace the ``import abstractgame as
   Game`` in :mod:`twoplayersgame` with ``import
   <your_implementation_module> as Game``.

"""


def initSituation(game):
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
    raise NotImplementedError( "initSituation must be defined to return the initial game configuration" )


def isFinished(situation):
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    raise NotImplementedError( "isFinished must be defined as a function to test end of game" )



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
    raise NotImplementedError( "playerCanPlay must be defined to determine whether player can play")


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
    raise NotImplementedError( "nextSituations must be defined as a function that provides successor situations" )



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
    raise NotImplementedError( "getWinner function must be defined to tell who win the game" )    




def displaySituation(situation):
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    raise NotImplementedError( "displaySituation must be defined to display the situation on the screen" )


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
    raise NotImplementedError( "humanPlayerPlays must be defined to make the human player plays one round, the reached new situation must be returned" )

