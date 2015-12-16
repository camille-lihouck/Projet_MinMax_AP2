# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``min_max``

   :author: Camille Lihouck
   
   :date:  2015, november
   
   This module is an implementation of the min max algorithm

"""
import player as Player

COMPUTER_NAME='minMAX'

def main(game,player,situation):
    if game['IA_level']!=None:
        val,situation=minMax(situation,player,game,game['IA_level'])
    else:
        val,situation=minMaxFinal(situation,player,game)
    return situation

    

def changePlayer(player,game):
    """
    """
    if player==game['player1']:
        return game['player2']
    else:
        return game['player1']

def minMaxFinal(situation,player,game):
    name=game['name']
    if name == 'othello':
        import othello as Game
    elif name == 'tic_tac_toe':
        import tictactoe as Game
    elif name =='nim_game':
        import nim_game as Game
    next_player=changePlayer(player,game)
    if Game.isFinished(situation):
        return (Game.evalFunction(situation,player),situation)
    else:
        next_situation=Game.nextSituations(game, situation, player)
        res=None
        if Player.name(player)==COMPUTER_NAME:
            for sit in next_situation:
                temp =minMaxFinal(sit,next_player,game)
                if res==None or temp!=None and res[0]<temp[0]:
                   res=temp
        else:
            for sit in next_situation:
                temp =minMaxFinal(sit,next_player,game)
                if res==None or temp!=None and res[0]>temp[0]:
                    res=temp
        try:
            return res[0],sit
        except:
            pass

def minMax(situation,player,game,depth):
    name=game['name']
    if name == 'othello':
        import othello as Game
    elif name == 'tic_tac_toe':
        import tictactoe as Game
    elif name =='nim_game':
        import nim_game as Game
    if Player.name(player)==COMPUTER_NAME:
        coeff=1
    else:
        coeff=-1
    next_player=changePlayer(player,game)
    if Game.isFinished(situation) or depth==0:
        #décomenter pour vérifier le résultat de la fonction d'évaluation
        #print(Game.evalFunction(situation,player,game)*coeff) 
        return Game.evalFunction(situation,player,game)*coeff,situation
    else:
        next_situation=Game.nextSituations(game, situation, player)
        res=None
        if Player.name(player)==COMPUTER_NAME:
            for sit in next_situation:
                temp =minMax(sit,next_player,game,depth-1)
                if res==None or temp!=None and res[0]<temp[0]:
                   res=temp
        else:
            for sit in next_situation:
                temp =minMax(sit,next_player,game,depth-1)
                if res==None or temp!=None and res[0]>temp[0]:
                    res=temp
        try:
            return res[0],sit
        except:
            print (res)
