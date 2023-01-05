from utilities.Windows import StartWindow
from utilities.game import Game
from utilities.player import Player
from os.path import abspath,join,dirname


dirPath = dirname(abspath(__file__))
iconPath = join(dirPath,'images/icon.ico')
boardPath = join(dirPath,'images/Board.png')

class Main:
    def __init__(self, name1, name2):
        app = Game(name1[:10], name2[:10],iconPath,boardPath)
        self.player1 = Player(app, name1, app.player_label, "X", startapp)
        self.player2 = Player(app, name2, app.player_label, "O", startapp)
        app.board.bind("<Button-1>", lambda e: self.player1.draw(e, self.player1, self.player2,iconPath))
        app.mainloop()


def startapp(start=False):
    app = StartWindow(Main,iconPath)

    if start:
        app.startAnimationConfig()
    else:
        app.commands()

    app.mainloop()
    return app.des


if __name__ == '__main__':
    isStart = True
    while startapp(isStart):
        isStart = False
