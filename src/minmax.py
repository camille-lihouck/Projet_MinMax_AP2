import nim_game as Game 
import tictactoe 
import player as Player
 
def Mini(situation,comp ,player):
    """
    """
    mini = 1000
    if Game.isFinished(situation):
        return Game.evalFunction(situation,comp)
    else:
        situations = Game.nextSituations({"":0},situation, player)
        for sit in situations:
            tmp = Maxi (sit[0] ,comp, player)
            if tmp <= mini :
                mini = tmp
    return mini

def Maxi (situation, comp ,player):
    """
    """
    maxi = -1000
    if Game.isFinished(situation):
        return Game.evalFunction(situation,player)
    else:
        situations = Game.nextSituations({"":0},situation, comp)
        for sit in situations:
            tmp = Mini(sit[0] ,comp, player)
            
            if tmp >= maxi:
                maxi = tmp
    return maxi

def IA(situation, comp, player):
    """
    """
    n = -1000
    situations = Game.nextSituations({"":0},situation, comp)
    for sit in situations:
        tmp = Mini(sit[0], comp, player)
        if tmp >= n :
            n = tmp
            valueToPlay = sit[1]
    situation = Game.changeValue(situation , valueToPlay, comp)  
    return situation

