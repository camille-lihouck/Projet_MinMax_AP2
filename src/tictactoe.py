

# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``tictactoe``

   :author: Camille Lihouck, Agayer Meryem, Farah Bouchahdane 
   
   :date:  2015, october
   
   This module is an implementation of the :mod:`abstractgame` for a tic tac toe for two player games.

"""

_DEFAULT_HEIGHT = 3
_DEFAULT_WIDTH = 3
import player as Player

def initSituation(game):#gestion des pions pour graphique
    """builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
    sit = [[' ' for x in range(3)] for y in range(3)]
    return sit

def isFinished(situation):#trés lourd et faux
    """
    tells if the game is finished when in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    booleen = True
    for i in range(3):
        if situation[i][0] == situation[i][1] == situation[i][2] != ' ' :
            return True
        for j in range(3):
            if i == 0:
                if situation[i][j] == situation[i+1][j] == situation[i+2][j] != ' ' :
                    return True
                if j == 0 or j == 2 :
                    if situation[i][j] == situation[i+1][abs(j-1)] == situation[i+2][abs(j-2)] != ' ':
                        return True
            if situation[i][j] == ' ':
                booleen = False
    return booleen


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
    spec = Player.coins(player)
    sits = []
    for i in range(3):
        for j in range(3):
            if situation[i][j] == '':
                sit = initSituation([])
                for x in range(3):
                    for y in range(3):
                        sit[x][y]= situation[x][y]
                sit[i][j] = spec
                sits.append((sit,(i,j)))
    return sits
    
    




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
    spec = Player.coins(player)
    for i in range(len(situation)):
        if situation[i][0] == situation[i][1] == situation[i][2] == spec :
            return player
        if i == 0:
            for j in range(3):
                if situation[i][j] == situation[i+1][j] == situation[i+2][j] == spec :
                    return player
                if j == 0 or j == 2 :
                    if situation[i][j] == situation[i+1][abs(j-1)] == situation[i+2][abs(j-2)] == spec :
                        return player
    return None
            


def displaySituation(situation):
    """
    displays the situation, here the grid with 9 boxs of the game.

    :param situation: the situation to display
    :type situation: a game situation
    """
    for i in range(3):
        print('|', end ='')
        for j in range(3):
            if situation[i][j] == ' ':
                print('_', end ='')
            else:
                print(situation[i][j], end= '')
            print('|', end ='')
        print()
            


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
    x, y = inputcoords(situation, player)
    coin = Player.coins(player)
    situation[x][y] = coin
    return situation


def inputcoords(situation, player):
    """
    """
    coords = input ('Coords? x,y ')
    coords = coords.split(',')
    try :
        x = int(coords[0])
        y = int(coords[1])
        if onboard(x, y) and situation[x][y] == " ":
            return (x, y)
    except:
        pass#inputcoords(situation, player)#inutile est traité par le retour final et manque le return
    return inputcoords(situation, player)




def onboard(x, y):
    """
    """
    return 0 <= x <= 3 and 0 <= y <= 3

        
    

