from tkinter import Tk, Label, Button, Entry, Toplevel, Frame, Checkbutton, StringVar, Canvas
from tkinter.messagebox import showwarning

WINDOWBG = "#39AEA9"


class StartWindow(Tk):
    def __init__(self, functionName,iconPath):
        super().__init__()
        self.loop = None
        self.focus_force()
        self.minsize(width=300, height=300)
        self.resizable(False, False)
        self.x = 0
        self.iconPath = iconPath
        self.functionName = functionName
        self.title('Tic Tac Toe')
        self.iconbitmap(self.iconPath)
        self.des = False

        self.config(pady=2, padx=2, bg=WINDOWBG)
        self.mainText = 'Tic Tac Toe'
        self.mainTextVar = StringVar(self, value=self.mainText)
        self.i = 1

        self.main_label = Label(self, textvariable=self.mainTextVar,
                                font=('sacramento', 28, 'underline'), bg=WINDOWBG)
        self.main_label.pack(fill='x', expand=True, anchor='n')

        self.play_btn = Button(self, text='Play', width=7, bg='#A2D5AB', border=.5, font=('arial', 15, 'normal'),
                          cursor='hand2')
        self.play_btn.place(x=40, y=150)

        self.quit_btn = Button(self, text='Quit', width=7, bg='#A2D5AB', border=.5, font=('arial', 15, 'normal'), cursor='hand2')
        self.quit_btn.place(x=180, y=150)

        self.checkBtnVar = StringVar(self)
        noNameNeed = Checkbutton(self, text="Custom Name", bg=WINDOWBG, activebackground=WINDOWBG,
                                 variable=self.checkBtnVar,onvalue="ON",offvalue="")
        noNameNeed.place(x=80, y=110)

    def startAnimationConfig(self):
        self.canvas1 = Canvas(self, bg="#F5EDDC", width=150, height=300, highlightthickness=0)
        self.canvas1.create_text(113, 130, text="Welc", font="arial, 20")
        self.canvas1.place(x=-1, y=-2)

        self.canvas2 = Canvas(self, bg="#F5EDDC", width=150, height=300, highlightthickness=0)
        self.canvas2.create_text(37, 130, text="ome!", font="arial, 20")
        self.canvas2.place(x=149, y=-2)

        self.startBtn = Button(self, text=" Enter ", bg="#A2D5AB", cursor='hand2', command=self.startAnimation)
        self.startBtn.place(x=120, y=170)

    def isNameWindow(self):
        if not self.checkBtnVar.get():
            self.destroy()
            self.functionName("Player1", "Player2")
        else:
            self.Name()

    def Name(self):
        self.nameWin = Toplevel(master=self)
        self.title("Names")
        self.iconbitmap(self.iconPath)
        self.nameWin.config(padx=50, pady=50)
        self.nameWin.minsize(width=270, height=100)
        self.nameWin.resizable(False, False)

        back = Label(self.nameWin, text="<back",cursor="hand2",font=("arial",10,"bold"))
        back.place(x=0,y=-30)
        Label(self.nameWin, text='Player 1 Name: ', ).grid(row=0, column=0)
        Label(self.nameWin, text='Player 2 Name: ').grid(row=1, column=0)

        self.entry1 = Entry(self.nameWin, )
        self.entry1.focus_force()
        self.entry1.grid(row=0, column=1)

        self.entry2 = Entry(self.nameWin, )
        self.entry2.grid(row=1, column=1)

        Button(self.nameWin, text='Ok', bg='#A2D5AB', border=.5, padx=10,
               pady=2, cursor='hand2', command=self.btn).place(x=100, y=50)

        self.nameWin.bind('<Return>', self.btn)
        self.wm_attributes('-alpha', 0)
        self.nameWin.wm_attributes("-topmost", True)
        self.bind("<Button-1>", lambda e: self.nameWin.focus_force())
        self.nameWin.protocol("WM_DELETE_WINDOW", self.destroy)
        back.bind("<Button-1>",self.onClosing)

        self.nameWin.mainloop()

    def btn(self, e=None):
        self.name1 = self.entry1.get()
        self.name2 = self.entry2.get()

        if all((self.name1, self.name2)) and self.name1 != self.name2:
            self.nameWin.destroy()
            self.destroy()
            self.functionName(self.name1, self.name2)
        else:
            en = self.nameWin.focus_get()
            showwarning("Field Error.", "The name shouldn't be the same. Also, both fields have to fill.")
            en.focus_force()

    def commands(self):
        self.play_btn["command"] = self.isNameWindow
        self.quit_btn["command"] = quit
        self.main_label.bind("<Enter>",self.startTextAnimation)
        self.main_label.bind("<Leave>",self.endTextAnimation)
    def startAnimation(self):
        self.startBtn.place_forget()
        self.x -= 3
        self.canvas1.place(x=self.x, y=-2)
        self.canvas2.place(x=150 - self.x, y=-2)

        if self.x > -151:
            self.after(10, self.startAnimation)
            return

        self.commands()
        

    def startTextAnimation(self, e=None):
        try:
            self.mainTextVar.set(self.mainText[:self.i])
        except IndexError:
            self.endTextAnimation()
        else:
            self.i += 1
            self.loop = self.after(100, self.startTextAnimation)

    def endTextAnimation(self, e=None):
        self.mainTextVar.set('Tic Tac Toe')
        self.i = 1
        try:
            self.after_cancel(self.loop)
        except ValueError:
            pass

    def onClosing(self,e=None):
        self.des = True
        self.destroy()


class WinningWindow(Tk):

    def __init__(self, symbol, name, iconPath):
        super().__init__()
        self.title("Tic Tac Toe")
        self.iconbitmap(iconPath)
        self.focus_force()
        self.minsize(width=300, height=280)
        self.resizable(False, False)
        self.re = False

        frame = Frame(self, padx=50, pady=50, bg='#66bfbf')
        frame.place(x=0, y=0)

        text = f"{name}({symbol}) win." if symbol else "Draw"
        Label(frame, text=text, font=('arial', 20, 'normal'), width=10, bg='#66bfbf').grid(
            column=0, row=0, ipadx=20, ipady=50, columnspan=2)

        Button(frame, text='Main Menu',
               cursor='hand2', bg='Light Cyan', activebackground='#6f6f3f',
               activeforeground='White', border=0.5, command=self.restart).grid(column=0, row=1)

        Button(frame, text='Quit',
               cursor='hand2', bg='Light Cyan', activebackground='#6f6f3f',
               activeforeground='White', border=0.5, command=quit).grid(column=1, row=1)
    
    def restart(self):
        self.re = True
        self.destroy()
