

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
    if not 'coins' in game:
        game['coins']=DEFAULT_COINS
    situation={}
    situation['board']=[]                
    for i in range (8):
        situation['board'].append([])
        for j in range (8):
            situation['board'][i].append (None)
    situation ['board'][4][3]= game['coins']['black']
    situation ['board'][3][4]= game['coins']['black']
    situation ['board'][3][3]= game['coins']['white']
    situation ['board'][4][4]= game['coins']['white']
    return situation

            
        
def isFinished(situation): #OK
    """
    tells if the game is finished in given situation

    :param situation: the tested situation
    :type situation: a game situation
    :returns: *(boolean)* -- True if the given situation ends the game
    """
    for column in range (8):
        for line in range(8):
            if situation['board'][column][line] == None:
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
    situation['next_situation']=nextSituations(game,situation,player)
    return situation['next_situation'] !=[]

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
    next_situation=[]
    coins= game['coins'][Player.coins(player)]
    for column in range (8):
        for line in range(8):
            if situation['board'][column][line]==None:
                new_situation={}
                new_situation['board']=[]
                for i in range (8):
                    new_situation['board'].append([])
                    new_situation['board'][i]= situation['board'][i].copy()
                for direction in DIRECTIONS:
                    _possible_action(column,line,DIRECTIONS[direction],player,new_situation,game)
                if new_situation['board']!=situation['board']:
                    new_situation['square']=(column,line)
                    next_situation.append(new_situation)
    return next_situation

def _next_square(column,line,direction): #Should be ok
    """
    get the coordinate of the next square in the given direction
    :type column: int
    :type line: int
    :type direction: tuple (a,b) a,b in {-1,0,1}
    """
    new_column= column +direction[0]
    new_line= line + direction[1]
    return (new_column,new_line)

def _possible_action(colum,line,direction,player,situation,game): #OK
    """
    give the coordinate of the square in which you can play in the given direction is this square exist, otherwise, returns None
    """
    coins = game['coins'][Player.coins(player)]
    try :
        next_colum1,next_line1=_next_square(colum,line,direction)
        if (situation['board'][next_colum1][next_line1] != coins) and (situation['board'][next_colum1][next_line1] != None):
            next_colum2,next_line2=_next_square(next_colum1,next_line1,direction)
            if situation['board'][next_colum2][next_line2] == coins:
                situation['board'][next_colum1][next_line1]=coins
                situation['board'][colum][line]=coins
                return (colum,line)
            elif situation['board'][next_colum2][next_line2]!=coins:
                res=_possible_action(next_colum1,next_line1,direction,player,situation,game)
                if res!=None:
                    situation['board'][colum][line]=coins
                return res
    except IndexError:
        pass
    return None


def getWinner(game, situation, player):#should be ok
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
    for column in range(8):
        for line in range (8):
            if situation['board'][column][line]==game['coins']['white']:
                white+=1
            elif situation['board'][column][line]==game['coins']['black']:
                black+=1
    if white>black:
        if Player.coins(player)=='white':
            winner=player
        elif player==game['player1']:
            winner=game['player2']
        else:
            winner=game['player1']
    elif black>white:
        if Player.coins(player)=='black':
            winner=player
        elif player==game['player1']:
            winner=game['player2']
        else:
            winner=game['player1']
    return winner



def displaySituation(situation):#OK work well
    """
    displays the situation

    :param situation: the situation to display
    :type situation: a game situation
    """
    print(situation)
    print('   a   b   c   d   e   f   g   h  ')
    print(separator1)
    for line in range (8):
        print(separator2)
        print('{:s}|'.format(str(line+1)),end="" )
        for column in range (8):
            content=situation['board'][column][line]
            if content== None:
                content=' '
            print(' {:s} |'.format(content),end='')
        print()
        print (separator3)

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
    situation_number=_input_action(game,situation,player)
    situation['board']=[]
    for i in range(8):
        situation['board'].append([])
        situation['board'][i]=situation['next_situation'][situation_number]['board'][i].copy()
    situation['next_situation']=[]
    return situation

def _input_action(game, situation, player) :# on a good way
    """
    """
    print(Player.name(player)+" it's your turn to play")
    print('Enter a letter between a and h followed by a number between 1 and 8')
    action=input('Where do you want to play? ')
    try:
        assert len(action)==2
        column= ord(action[0])-ord('a')
        line = int(action[1])-1
        possible= False
        for i in range (len(situation['next_situation'])):
            if (column,line)==situation['next_situation'][i]['square']:
                possible=True
                situation_number=i
        if possible:
            return situation_number
    except AssertionError:
        pass
    print('unauthorised action')
    return _input_action(game, situation, player)
