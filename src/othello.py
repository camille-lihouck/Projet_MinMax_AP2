

# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``othello``

   :author: Camille Lihouck, Agayer Meryem, Farah Bouchahdane 
   
   :date:  2015, november
   
   This module is an implementation of the :mod:`abstractgame` for a othello two player games.

"""
# coins authorised for a player are 'black' and 'white'
import player as Player

DEFAULT_COINS={'black':'X','white':'O'}

DIRECTIONS={'NO':(-1,-1),
            'N':(-1,0),
            'NE':(-1,1),
            'O':(0,-1),
            'E':(0,1),
            'SO':(1,-1),
            'S':(1,0),
            'SE':(1,1)}


separator1='  ___ ___ ___ ___ ___ ___ ___ ___ '
separator2=' |   |   |   |   |   |   |   |   |'
separator3=' |___|___|___|___|___|___|___|___|'


def initSituation(game): # OK
    """
    builds the initial situation for the game. 

    :param game: the game for which the initial situation is created
    :type game: game
    :returns: *(situation)* the siutation at the beginning of the game
    """
    if 'coins' in game:
        coins=game['coins']
    else:
        coins=DEFAULT_COINS
    situation={}
    situation['board']={}                 
    for i in range (8):
        situation['board'][chr(i+ord('a'))]={}
        for j in range (8):
            situation['board'][chr(i+ord('a'))][str(j+1)]= None
    situation ['board']['e']['4']= coins['black']
    situation ['board']['d']['5']= coins['black']
    situation ['board']['d']['4']= coins['white']
    situation ['board']['e']['5']= coins['white']
    return situation

            
        
def isFinished(situation): # Should be ok
    """
    tells if the game is finished in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    for column in situation['board']:
        for line in situation['board'][column]:
            if situation['board'][column][line] == None:
                print('game finished') # to be errease
                displaySituation(situation) # to be errease
                return False
    return True

def playerCanPlay(game, situation, player): # Should be ok
    """
    tells whether player can play in given situation

    :param game: the game 
    :type game: game
    :param situation: the situation to display
    :type situation: a game situation
    :param player: the player
    :type player: player
    :returns: *(boolean)* -- True if player can play in situation
    """
    situation ['nextSituations']= nextSituations(game,situation,player)
    print (situation['nextSituations'])
    return nextSituations(game, situation, player) !=[]

def nextSituations(game, situation, player): # Could be ok
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
    nextSituation=[]
    coins = Player.coins(player)
    for column in situation['board']:
        for line in situation['board'][column]:
            if situation['board'][column][line]==coins:
                for direction in DIRECTIONS:
                    action = _action(column,line,DIRECTIONS[direction],player,situation)
                    if action!=None:
                        newSituation= situation.copy
                        _play_action(action[0],action[1],(-1*DIRECTIONS[direction][0],-1*DIRECTIONS[direction][1]),player,newSituation)
                        nextSituation.append(newSituation)
    return nextSituation

def _next_square(column,line,direction): #Should be ok
    """
    get the coordinate of the next square in the given direction
    """
    new_column= chr(ord(column)+direction[0])
    new_line= str(int(line)+direction[1])
    return (new_column,new_line)

def _action(colum,line,direction,player,situation): #Should be ok
    """
    give the coordinate of the square in whitch you can play in the given direction is this square exist, otherwise, returns None
    """
    coins = Player.coins(player)
    try :
        next_colum1,next_line1=_next_square(colum,line,direction)
        next_colum2,next_line2=_next_square(next_colum1,next_line1,direction)
        if situation['board'][next_colum1][next_line1] != coins and situation['board'][next_colum1][next_line1] != None:
            if situation['board'][next_colum2][next_line2] == None:
                return (next_colum2,next_line2)
            elif situation['board'][next_colum2][next_line2]!=coins:
                return _next_square(next_colum1,next_colum2,direction,player,situation)
    except KeyError:
        pass
    return None

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
    white=0
    black=0
    winner=None
    for column in situation['board']:
        for line in situation['board'][column]:
            if situation['board'][column][line]=='O':
                white+=1
            elif situation['board'][column][line]=='X':
                black+=1
    if white>black:
        if Player.coins(player)=='O':
            winner=player
        else:
            winner= 'other player' #Check how to get it , perhaps situation should be a dict with a key board and a key winner
    elif black>white:
        if Player.coins(player)=='X':
            winner=player
        else:
            winner= 'other player' #Check how to get it
    return winner



def displaySituation(situation):#OK work well
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    print('   a   b   c   d   e   f   g   h  ')
    print(separator1)
    for line in range (8):
        print(separator2)
        print('{:s}|'.format(str(line+1)),end="" )
        for colum in range (8):
            content=situation['board'][chr(ord('a')+colum)][str(line+1)]
            if content== None:
                content=' '
            print(' {:s} |'.format(content),end='')
        print()
        print (separator3)

def _play_action(column, line, direction,player,situation): #Should be ok , may miss exception traitement for being used in HumanPlayerPlay
    """
    returns all coins from a started position given to the next coin of the same color in the given direction
    :Side effect: situation is modify
    """
    coins = Player.coins(player)
    new_column,new_line=_next_square(column,line,direction)
    if situation['board'][new_column][new_line] != coins and situation[new_column][new_line] != None:
        situation['board'][new_column][new_line]= coins
        _play_action(new_column,new_line,direction,player,situation)


def humanPlayerPlays(game, player, situation): #Don't work
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
    action = _input_action(game, situation, player)    
    for direction in DIRECTIONS:
        action = _action(column,line,direction,player,situation)
        if action!=None:
             _play_action(action[0],action[1],(-1*DIRECTIONS[direction][0],-1*DIRECTIONS[direction][1]),player,situation)
        

def _input_action(game, situation, player) :# on a good way
    """
    """
    print(Player.name(player)+"it's your turn to play")
    print('Enter a letter between a and h followed by a number between 1 and 8')
    action=input('Where do you want to put a coin?')
    try:
        if action in nextSituations(game, situation, player):
            return action
    except:
        pass
    print('unauthorised action')
    return _input_action(game, situation, player)
