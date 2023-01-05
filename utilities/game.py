from tkinter import Tk, PhotoImage, Label


class Game(Tk):
    def __init__(self, name1, name2,iconPath,boardPath):
        super().__init__()
        self.focus_force()
        self.player1 = name1
        self.player2 = name2
        self.minsize(width=300, height=300)
        self.resizable(False, False)
        self.title('Play Game')
        self.iconbitmap(iconPath)
        self.config(bg='Light Blue')

        board_img = PhotoImage(master=self, file=boardPath)
        self.board = Label(master=self, image=board_img, bg='#66bfbf')
        self.board.image = board_img
        self.board.pack(fill='both', anchor='center', expand=True)

        self.player_label = Label(self, text=f'{self.player1} (X) Chance.',
                                  font=('arial', 12, 'bold'), bg='#66bfbf')
        self.player_label.place(x=50, y=10)
        self.lst = []

    def valueofX(self, x):
        if 53 < x < 109:
            return 75
        elif 120 < x < 178:
            return 135
        elif 187 < x < 247:
            return 205

    def findXandY(self, e):
        x_cor = e.x
        y_cor = e.y
        y = None

        if 187 < y_cor < 248:
            y = 200
        elif 127 < y_cor < 178:
            y = 135
        elif 51 < y_cor < 117:
            y = 70

        x = self.valueofX(x_cor)
        tup = (x, y)

        if all(tup) and tup not in self.lst:
            self.lst.append(tup)
            return tup, True, self.lst

        return tup, False, self.lst
