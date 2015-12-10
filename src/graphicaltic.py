import tictactoe, os
import player as Player
import tkinter as tk
from functools import partial

def create():
    global img
    win = tk.Tk()
    win.title ('tictactoe')
    sit = tictactoe.initSituation({})
    playerone = Player.create('meryem','O')
    playertwo = Player.create('farah','X')
    global current
    current = playerone
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons")
    img = [
        tk.PhotoImage(file=os.path.join(iconpath,"c.gif")),
        tk.PhotoImage(file=os.path.join(iconpath,"x.gif")),
        tk.PhotoImage(file=os.path.join(iconpath,"o.gif"))
        ]
    b = []
    for i in range(3):
        b.insert(i,[])
        for j in range(3):
            if sit[i][j] == 'X':
                ig = img[1]
            if sit [i][j] == 'O':
                ig = img[2]
            if sit[i][j] == ' ':
                ig = img[0]
            button = tk.Button(win,padx=0,pady=0, width=120, height=120, image=img[0])
            button.grid(column = i, row = j)
            b[i].insert(j,button)
            button.bind("<Button-1>",partial(onClick, button.grid_info()['row'], button.grid_info()['column'], b, sit, playerone, playertwo))
    win.mainloop()


def onClick(x, y, b, sit, pone, ptwo, event):
    """
    """
    global current
    coin = Player.coins(current)
    if tictactoe.onboard(x, y) and sit[x][y] == " ":
        sit[x][y] = coin
    if current == pone:
        current = ptwo
    else:
        current = pone
    __redraw(sit, b)


def __redraw(sit, b):
    """
    """
    for i in range(3):
        for j in range(3):
            if sit[i][j] == 'X':
                ig = img[1]
            if sit [i][j] == 'O':
                ig = img[2]
            if sit[i][j] == ' ':
                ig = img[0]
            button = b[j][i]
            button.config(image = ig)
