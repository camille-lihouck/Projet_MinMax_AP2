

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
    situation=[]                
    for i in range (8):
        situation.append([])
        for j in range (8):
            situation[i].append (None)
    situation[4][3]= game['coins']['black']
    situation[3][4]= game['coins']['black']
    situation[3][3]= game['coins']['white']
    situation[4][4]= game['coins']['white']
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
            if situation[column][line] == None:
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
    next_situation=nextSituations(game,situation,player)
    return next_situation !=[]

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
            if situation[column][line]==None:
                new_situation=[]
                for i in range (8):
                    new_situation.append([])
                    new_situation[i]= situation[i].copy()
                for direction in DIRECTIONS:
                    _possible_action(column,line,DIRECTIONS[direction],player,new_situation,game)
                if new_situation!=situation:
                    new_situation[column][line]=coins
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
        assert colum>=0 and colum<=7
        assert line>=0 and line<=7
        next_colum1,next_line1=_next_square(colum,line,direction)
        assert next_colum1>=0 and next_colum1<=7
        assert next_line1>=0 and next_colum1<=7
        if (situation[next_colum1][next_line1] != coins) and (situation[next_colum1][next_line1] != None):
            next_colum2,next_line2=_next_square(next_colum1,next_line1,direction)
            assert next_colum2>=0 and next_colum2<=7
            assert next_line2>=0 and next_line2<=7
            if situation[next_colum2][next_line2] == coins:
                situation[next_colum1][next_line1]=coins
                situation[colum][line]=coins
                return (colum,line)
            elif situation[next_colum2][next_line2]!=coins:
                res=_possible_action(next_colum1,next_line1,direction,player,situation,game)
                if res!=None:
                    situation[next_colum1][next_line1]=coins
                    situation[colum][line]=coins
                return res
    except IndexError:
        pass
    except AssertionError:
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
            if situation[column][line]==game['coins']['white']:
                white+=1
            elif situation[column][line]==game['coins']['black']:
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
    print('   a   b   c   d   e   f   g   h  ')
    print(separator1)
    for line in range (8):
        print(separator2)
        print('{:s}|'.format(str(line+1)),end="" )
        for column in range (8):
            content=situation[column][line]
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
    next_situation=_input_action(game,situation,player)
    situation=[]
    for i in range(8):
        situation.append([])
        situation[i]=next_situation[i].copy()
    return situation

def _input_action(game, situation, player) :# on a good way
    """
    """
    print(Player.name(player)+" it's your turn to play")
    print('Enter a letter between a and h followed by a number between 1 and 8')
    action=input('Where do you want to play? ')
    try:
        coins=game['coins'][Player.coins(player)]
        assert len(action)==2
        column= ord(action[0])-ord('a')
        line = int(action[1])-1
        new_situation=[]
        for i in range (8):
            new_situation.append([])
            new_situation[i]= situation[i].copy()
            for direction in DIRECTIONS:
                _possible_action(column,line,DIRECTIONS[direction],player,new_situation,game)
        if new_situation!=situation:
            new_situation[column][line]=coins
            situation = new_situation
            return situation
    except AssertionError:
        pass
    except ValueError:
        pass
    print('unauthorised action')
    return _input_action(game, situation, player)


def evalFunction(situation, player,game):
    """
    the evaluation function for the min-max algorithm. It evaluates the given situation, the evaluation function increases with the quality of the situation for the player
         
    :param situation: the current situation
    :type situation: a game situation
    :param player: the current player
    :type player: player
    :returns: *(number)* -- the score of the given situation for the given player.
        The better the situation for the minmax player, the higher the score. The opposite for human player.
    """
    win= 1000
    loose = -1000
    turn_pass=-200
    coins=game['coins'][Player.coins(player)]
    coeff= _square_coeff()
    value = 0
    if isFinished(situation):
        if getWinner(game,situation,player)== player:
            value=win
        else:
            value=loose
    elif not playerCanPlay(game,situation,player):
        value= turn_pass
    else:
        for column in range(8):
            for line in range(8):
                if situation[column][line]==coins:
                    value+=coeff[column][line]
                elif situation[column][line]!=None:
                    value-=coeff[column][line]
    return value

def _square_coeff():#OK
    """
    attribute a weight to each square according to its strategic weight
    """
    coeff=[]
    for column in range(8):
        coeff.append([])
        for line in range(8):
            coeff[column].append(1)
            if column==0 or column==7:
                coeff[column][line]*=4
            if line==0 or line ==7:
                coeff[column][line]*=4
    return coeff
