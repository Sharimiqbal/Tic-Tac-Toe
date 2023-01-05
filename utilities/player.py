from time import sleep
from tkinter import Label
from utilities.Windows import WinningWindow

corDict = {}
indexLst = []


def updateData():
    corDict.update({
        '1': (75, 70), '2': (135, 70), '3': (205, 70),
        '4': (75, 135), '5': (135, 135), '6': (205, 135),
        '7': (75, 200), '8': (135, 200), '9': (205, 200)
    })
    indexLst.extend([('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), ('1', '4', '7'),
                     ('2', '5', '8'), ('3', '6', '9'), ('1', '5', '9'), ('3', '5', '7')])


updateData()


class Player:
    def __init__(self, win, name, player_label, symbol, additionalFunction):
        self.lst = None
        self.secondaryName = None
        self.startapp = additionalFunction
        self.root = win
        self.name = name
        self.player_label = player_label
        self.symbol = symbol

    def draw(self, e, mainPlayer, secondaryPlayer,iconPath):
        self.secondaryName = secondaryPlayer.name
        (x, y), T, self.lst = self.root.findXandY(e)

        if T:
            self.player_label.config(text=f"{secondaryPlayer.name} ({secondaryPlayer.symbol}) Chance")
            Label(self.root, text=self.symbol, bg='white', font=(
                'arial', 20, 'normal')).place(x=x, y=y)

            for key, value in corDict.items():
                if value == (x, y):
                    corDict[key] = self.symbol

            self.root.board.unbind("<Button-1>")
            self.root.board.bind("<Button-1>", lambda event: secondaryPlayer.draw(event, secondaryPlayer, mainPlayer,iconPath))
            self.check(iconPath)
            return True

    def check(self,iconPath):
        winnerSymbol = None
        isWin = False
        draw = len(self.lst) == 9

        for elms in indexLst:

            if len(set([corDict[e] for e in elms])) == 1:
                self.root.board.unbind('<Button-1>')
                winnerSymbol = corDict[elms[0]]
                break

        if winnerSymbol or draw:

            if winnerSymbol == self.symbol:
                name = self.name
            else:
                name = self.secondaryName
            
            isWin = True

            win = WinningWindow(winnerSymbol, name, iconPath=iconPath)
            win.after(500,lambda:[self.root.destroy(),win.deiconify(),win.deiconify()])
            win.withdraw()
            win.mainloop()

        if isWin and win.re:
            updateData()
            while self.startapp():
                pass
