# -*- coding: utf-8 -*-


"""
 .. topic:: Module ``twoplayergame``

   :author: Camille Lihouck, Agayer Meryem, Farah Bouchahdane 
   
   :date:  2015, november
   
   This module is used to play games based on the :mod:`abstractgame` for two player games.

"""


import player as Player 
import min_max as minmax

LIST_GAME=['othello','nim_game','tic_tac_toe']

def play(name):
    """
    """
    assert name in LIST_GAME, 'g must be in LIST_GAME'
    if name=='othello':
        import othello as Game
    elif name=='tic_tac_toe':
        import tictactoe as Game
    elif name=='nim_game':
        import nim_game as Game
    game = init_game(name)
    situation= Game.initSituation(game)
    turn_passed=0
    current_player=first_player(game)
    Game.displaySituation(situation)
    while not Game.isFinished(situation) and turn_passed<2:
        if Game.playerCanPlay(game, situation, current_player):
            turn_passed=0
            if Player.name(current_player)!='minMAX':
                situation = Game.humanPlayerPlays(game,current_player,situation)
            else:
                print("computer's playing")
                situation = minmax.main(game,current_player,situation)
            Game.displaySituation(situation)
        else:
            turn_passed +=1
        current_player = next_player(current_player,game)
    winner=Game.getWinner(game,situation,current_player)
    if winner == None:
        print("It's a draw")
    elif Player.name(winner)!="minMAX":
        print("Well done {:s} you win".format(Player.name(winner)))
    else:
        print("Sorry, you loose")

def first_player(game):
    """
    get the first player to play
    """
    name=game['name']
    if name == 'othello':
        color= Player.coins(game['player1'])
        if color == 'black':
            return game['player1']
        else:
            return game['player2']
    else:
        return game['player1']

def next_player(current_player, game):
    """
    """
    if current_player==game['player1']:
        next_player= game['player2']
    else:
        next_player = game['player1']
    return next_player


def init_game(name):
    """
    Initialize the game

    :param game: the game you want to play
    :type game: str
    :returns: the games setup
    :rtype: dict
    """
    game={}
    game['name']=name
    list_coin=None
    if name =='othello':
        list_coin=['black','white']
    elif name =='tic_tac_toe':
        list_coin=['X','O']
    game['player1']=register_player(list_coin)
    player2= two_players()
    game['IA_level']= None
    if player2:
        game['player2']=register_player(list_coin)
    else:
        if list_coin==None:
            game['player2']=Player.create('minMAX',None)
        else:
            game['player2']=Player.create('minMAX',list_coin[0])
        if name == 'othello':
            game['IA_level']=set_difficulty()
        else:
            game['IA_level']=None
    # allow the player to choose wether he play on terminal on with graphical board
    return game
    
def set_difficulty():
    """
    """
    difficulty= input('What IA level do you want? (1 is for begineer)')
    try:
        return int(difficulty)
    except ValueError:
        return set_difficulty()
        
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
    name= choose_name()
    if list_coin == None:
        coins = None
    elif len(list_coin)==1:
        coins=list_coin[0]
    else:
        coins=choose_coins(list_coin)
    return Player.create(name,coins)

def choose_name():
    """
    allow player to choose their name
    :returns: the chosen name
    :rtype: str
    """
    name= input ('Player name :')
    #if name=='minMAX':
        #print('The name"minMAX" is not available')
        #return choose_name()
    return name
    
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
