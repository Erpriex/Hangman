from tkinter import *

from Difficulty import Difficulty
from HelpManager import HelpManager
from LeaderboardManager import LeaderboardManager
from NotifyUtils import NotifyUtils
from Player import Player
from WordsManager import WordsManager
from game import Game


class PenduPython:

    def __init__(self):
        self.window = Tk()

    def openWindow(self):
        # Personnaliser fenetre
        self.window.title("Accueil • PenduPython")
        #self.window.geometry("1280x720")
        self.window.attributes('-fullscreen', True)
        self.window.config(background='midnightblue')



        # Texte
        label_title = Label(self.window, text="Bienvenue sur PenduPython", font=("Courrier", 40), bg='royalblue', fg='white')
        label_title.pack()
        label_title = Label(self.window, text="it's ugly but it works ", font=("Courrier", 17, "italic"), bg='royalblue', fg='white')
        label_title.pack()



        # Difficulté
        frame = Frame(self.window, padx=100, pady=50, bg='royalblue')
        frame.pack(fill="both", expand="yes")
        frame.place(relx=0.5, rely=0.3, anchor=CENTER)

        Pseudo_Text = Label(frame,text="Entrez Votre Pseudo : ", bd=0, width=20, font="Courrier 15", bg='royalblue')
        Pseudo_Text.place(relx=0.2, rely=-1, anchor=N)

        self.pseudoEntry = Entry(frame, bd=0, width=12, font="Courrier 15")
        self.pseudoEntry.place(relx=0.75, rely=-1, anchor=N)

        # Value par défaut des radio de difficultées
        self.radioDifficultyValue = IntVar()
        self.radioDifficultyValue.set(1)

        easy_radio = Radiobutton(frame, text="Facile", font="Courrier 18", variable=self.radioDifficultyValue, value=1)
        easy_radio.pack(anchor=W, side=LEFT)
        #easy_radio.select()

        normal_radio = Radiobutton(frame, text="Normal", font="Courrier 18", variable=self.radioDifficultyValue, value=2)
        normal_radio.pack(anchor=W, side=LEFT)
        #normal_radio.deselect()

        hard_radio = Radiobutton(frame, text="Difficile", font="Courrier 18", variable=self.radioDifficultyValue, value=3)
        hard_radio.pack(anchor=W, side=LEFT)
        #hard_radio.deselect()

        #Bouton
        play_button = Button(self.window, text="JOUER !", font=("Courrier", 25), width = 15, command=self.openGameWindow)
        play_button.place(relx = 0.5, rely=0.5, anchor=CENTER)

        ranking_button = Button(self.window, text="Classement", font=("Courrier", 25), width = 15, command=self.openLeaderboardManager)
        ranking_button.place(relx = 0.5, rely=0.6, anchor=CENTER)

        manageWords_button = Button(self.window, text="Gérer les mots", font=("Courrier", 25), width = 15, command=self.openWordsManagerWindow)
        manageWords_button.place(relx = 0.5, rely=0.7, anchor=CENTER)

        help_button = Button(self.window, text="Aide", font=("Courrier", 25), width = 15, command=self.openHelpWindow)
        help_button.place(relx = 0.5, rely=0.8, anchor=CENTER)

        exit_button = Button(self.window, text="Quitter le jeu", font=("Courrier", 25), width = 15, command=self.closeWindow)
        exit_button.place(relx = 0.5, rely=0.9, anchor=CENTER)



        # Afficher fenetre
        self.window.mainloop()


    def closeWindow(self):
        self.window.destroy()

    def openGameWindow(self):
        if self.pseudoEntry.get() == "": # Si le joueur n'a pas entré de pseudo
            notifyUtils = NotifyUtils()
            notifyUtils.sendNotify("Merci de saisir votre pseudo")
            return
        name = self.pseudoEntry.get().replace(" ", "_") # Remplacement des espaces dans le nom
        difficulty = Difficulty.EASY
        if self.radioDifficultyValue.get() == 1: # Conversion value des radios à l'enum Difficuly
            difficulty = Difficulty.EASY
        elif self.radioDifficultyValue.get() == 2:
            difficulty = Difficulty.NORMAL
        elif self.radioDifficultyValue.get() == 3:
            difficulty = Difficulty.HARD
        self.window.destroy()
        game = Game(name, difficulty)
        game.openWindow()

    def openWordsManagerWindow(self):
        wordsManager = WordsManager()
        wordsManager.openWindow()

    def openLeaderboardManager(self):
        leaderbordManager = LeaderboardManager()
        leaderbordManager.openWindow()

    def openHelpWindow(self):
        helpManager = HelpManager()
        helpManager.openWindow()

    def hideWindow(self, cache):
        if(cache == True):
            self.window.withdraw()
        else:
            self.window.deiconify()


main = PenduPython()
main.openWindow()