# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``twoplayergame``

   :author: Camille Lihouck, Agayer Meryem, Farah Bouchahdane 
   
   :date:  2015, november
   
   This module is used to play games based on the :mod:`abstractgame` for two player games.

"""


import player as Player
import tictactoe 
import minmax
import othello as Game
import nim_game

LIST_GAME=['othello','nim_game','tic_tac_toe']

def play(g):
    """
    """
    game = init_game(g)
    situation= Game.initSituation(game)
    turn_passed=0
    current_player=game['player1']
    Game.displaySituation(situation)
    while not Game.isFinished(situation) and turn_passed<2:
        if Game.playerCanPlay(game, situation, current_player):
            turn_passed=0
            situation = Game.humanPlayerPlays(game,current_player,situation)
        else:
            turn_passed +=1
        Game.displaySituation(situation)
        current_player = next_player(current_player,game)
    winner=Game.getWinner(game,situation,current_player)
    return winner

def next_player(current_player, game):
    """
    """
    if current_player==game['player1']:
        next_player= game['player2']
    else:
        next_player = game['player1']
    return next_player


def init_game(game):
    """
    Initialize the game
    """
    assert game in LIST_GAME, 'game must be in list game'
    g={}
    list_coin=None
    if game =='othello':
        list_coin=['black','white']
    elif game =='tic_tac_toe':
        list_coin=['X','O']
    g['player1']=register_player(list_coin)
    player2= two_players()
    if player2:
        g['player2']=register_player(list_coin)
    else:
        g['player2']=Player.create('computer',list_coin[0])
    # allow the player to choose wether he play on terminal on with graphical board
    return g
    
        
        
def two_players():
    """
    allow a human player to choose if he wants to play against an other player or against the computer
    """
    option= input('Do you want to play versus an other human player?(Yes/No)')
    if option == 'Yes':
        return True
    elif option == 'No':
        return False
    else:
        print('Uncorrect answer')
        return two_players()
    
def register_player(list_coin):
    """
    register a human player
    :param list_coin: the list of allowed coins
    :type list_coin: list
    :returns: a new player
    :rtype: player
    """
    name= input ('Player name :')
    if list_coin == None:
        coins = None
    elif len(list_coin)==1:
        coins=list_coin[0]
    else:
        coins=choose_coins(list_coin)
    return Player.create(name,coins)


def choose_coins(list_coin):
    """
    allow a human player to choose the coins he want to used in the list given
    :param list_coin: the list of allowed coins
    :type list_coin: list
    :return: the chosen coins
    :rtype: str
    :Side Effect: list_coin is modified (the chosen coins are removed from list_coin)
    """
    t=''
    for i in list_coin:
        t+= i + ' '
    coins = input ('Which coins do you want to play ? ({:s})'.format(t))
    if coins in list_coin:
        list_coin.remove(coins)
        return coins
    else:
        print('This coins are not allowed')
        return choose_coins(list_coin)
