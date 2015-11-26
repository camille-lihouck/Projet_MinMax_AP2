# -*- coding: utf-8 -*-

"""
    :author: Camille LIHOUCK

    :date: 17 novembre 2015

    This module defines a type player in order to play games

    This module content:

    * create(name,coins): create a new player 
    * name(player): get the name of a given player
    * coins(player): get the coins of a given player
"""

def create(name,coins):
    """
    create a new player define by a name and a chosen type of coin

    :param name: the players name
    :type name: str
    :param coins: the chosen coins
    :type coins: str
    :returns: a new player
    :rtype: dict
    :Example:

    >>> toto=create('toto','rouge')
    >>> toto
    {'name': 'toto', 'coins': 'rouge'}
    """
    return {"name" : name , "coins" : coins}

def name(player):
    """
    get the name of a given player

    :param player: a player
    :type player: player
    :returns: the player name
    :rtype: str
    :Example:

    >>> toto=create('toto','rouge')
    >>> name(toto)
    'toto'
    """
    return player['name']

def coins(player):
    """
    get the coin used by given player

    :param player: a player
    :type player: player
    :returns: the coins 
    :rtype: str
    :Example:

    >>> toto=create('toto','rouge')
    >>> coins(toto)
    'rouge' 
    """
    return player['coins']
