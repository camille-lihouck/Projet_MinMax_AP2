

# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``twoplayergame``

   :author: Camille Lihouck, Agayer Meryem, Farah Bouchahdane 
   
   :date:  2015, november
   
   This module is used to play games based on the :mod:`abstractgame` for two player games.

"""

import othello as Game
import player as Player

def register_player():
    """
    """
    name= input ('Player name :')
    coins = input ('Player coins:')
    return Player.create(name,coins)

def play(game):
    """
    """
    game['player1']=register_player()
    game['player2']=register_player()
    situation= Game.initSituation(game)
    turn_passed=0
    current_player=game['player1']
    print(situation)
    Game.displaySituation(situation)
    while not Game.isFinished(situation) and turn_passed<2:
        if Game.playerCanPlay(game, situation, current_player):
            turn_passed=0
            Game.displaySituation(situation)
            situation = Game.humanPlayerPlays(game,current_player,situation)
        else:
            turn_passed +=1
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
