from tkinter import *



from Difficulty import Difficulty
from HelpManager import HelpManager
from LeaderboardManager import LeaderboardManager
from NotifyUtils import NotifyUtils
from Player import Player
from penduxml.players.PlayersXML import PlayersXML
from penduxml.words.WordsXML import WordsXML


class Game:

    #region Constructeur de Game
    def __init__(self, name, difficulty):
        self.window = Tk()
        self.player = Player(name, 0, difficulty, "")
        self.score = str(self.player.getScore())
        self.scoreSaved = False
        self.enableTask = True
    #endregion

    #region Fonction qui permet de rajouter des points au joueur qui rentre dans le jeu
    def addPlayerScore(self, amount):
        self.player.addScore(amount)
        self.score = str(self.player.getScore())
        self.lbScore["text"] = "Score : "+self.score
    #endregion

    #region Fonction qui permet d'ouvrir la fenêtre Classement
    def openLeaderboardManager(self):
        leaderbordManager = LeaderboardManager()
        leaderbordManager.openWindow()
    #endregion

    #region Focntion de pour sauvegarder le joueur dans le classement
    def savePlayerToXML(self):
        if self.scoreSaved == False:
            playersXML = PlayersXML()
            playersXML.addPlayer(self.player)
            self.scoreSaved = True
    #endregion

    #region Notification lorsque le joueur perd
    def losePlayer(self):
        self.enableTask = False
        self.savePlayerToXML()
        notify = NotifyUtils()
        notify.sendNotify("Vous avez perdu !\nAller voir votre Score dans classement")
    #endregion

    #region Notification lorsque le joueur gagne
    def WonPlayer(self):
        self.enableTask = False
        self.savePlayerToXML()
        notify = NotifyUtils()
        notify.sendNotify("Bravo, vous avez gagné !\nAller voir votre Score dans classement")
        #self.window.destroy()
    #endregion

    #region Fonction qui permet d'ouvrir la fenetre Aide
    def openHelpWindow(self):
        helpManager = HelpManager()
        helpManager.openWindow()
    #endregion

    #region BUG Fonction qui permet d'ouvrir le Menu principal (ne marche pas donc on affiche un message d'erreur)
    def openMainMenu(self):
        self.enableTask = False
        self.savePlayerToXML()
        notifyUtils = NotifyUtils()
        notifyUtils.sendNotify("Une erreur liée au développement,\nNous contraint de vous faire relancer le jeu\n \nMais rassurez-vous\nVos données ont été sauvegardées ;)")
        self.window.destroy()
        #exec(open("main.py").read())
    #endregion

    # region La fenêtre principal qui contient le jeu du pendu
    def openWindow(self):
        # Personnaliser fenetre
        self.window.title("Jeu • PenduPython")                                                                          #self.window.geometry("1280x720")
        self.window.attributes('-fullscreen', True)
        self.window.config(background='midnightblue')
    #endregion

        #region Variables globals qui sont utilisé a travers plusieurs fonctions
        global essai
        global end
        global img
        global compteur
        #endregion

        #region Fonction du timer qui a un pas de 1 seconde
        def incremente():
            global compteur
            if self.enableTask == True:
                compteur += 1
                compteur_lbl['text'] = "Timer : " + str(compteur)
                self.window.after(1000, incremente)
        #endregion

        #region Fonction qui parcours le mot et trouve la lettre du joueur dans le mot ou non et l'actualiser sur le mot caché
        def majMot(cache, lettre, word):
            n = len(word)
            for i in range(n):
                if word[i] == lettre:
                    cache[i] = lettre
                    self.addPlayerScore(1) #va ajouter +1 au score du joueur lorsqu'il trouve une lettre
        #endregion

        #region Fonction qui actualise l'image du pendu et le nombre d'essai, ajout des points au score du joueur lorsque le jeu est fini +message
        def score(lettre):
            global essai, end, img
            if lettre not in word:
                essai = essai - 1
                if essai == 7:
                    img = PhotoImage(file="img/1.png")
                    imageP.configure(image=img)
                if essai == 6:
                    img = PhotoImage(file="img/2.png")
                    imageP.configure(image=img)
                if essai == 5:
                    img = PhotoImage(file="img/3.png")
                    imageP.configure(image=img)
                if essai == 4:
                    img = PhotoImage(file="img/4.png")
                    imageP.configure(image=img)
                if essai == 3:
                    img = PhotoImage(file="img/5.png")
                    imageP.configure(image=img)
                if essai == 2:
                    img = PhotoImage(file="img/6.png")
                    imageP.configure(image=img)
                if essai == 1:
                    img = PhotoImage(file="img/7.png")
                    imageP.configure(image=img)
                if essai == 0:
                    img = PhotoImage(file="img/8.png")
                    imageP.configure(image=img)
                if essai <= limite:
                    annonce["text"] = "Perdu !"
                    end = True
                    self.losePlayer()
                else:
                    annonce["text"] = "Il vous reste " + str(essai) + " essais"
            elif cache == list(word):
                annonce["text"] = "Gagné !"
                if (self.player.getDifficulty() == Difficulty.EASY) :
                        self.addPlayerScore(5+essai)
                elif (self.player.getDifficulty() == Difficulty.NORMAL) :
                        self.addPlayerScore(10+essai)
                else:
                        self.addPlayerScore(20+essai)
                end = True
                self.WonPlayer()
        #endregion

        #region Fonction Event qui va être utilisé sur chaque Boutons Lettre et qui appelle plusieurs fonctions
        def clicklettre(event):
            global essai, end, img
            print(end)
            if end == False:
                btn = event.widget
                lettre = btn["text"]
                majMot(cache, lettre, word)
                lbCache["text"] = " ".join(cache)
                score(lettre)
                btn.destroy()
        #endregion

        #region Initialisation des variables
        wordsXML = WordsXML()
        word = wordsXML.getRandomWordWithDifficulty(self.player.getDifficulty(), "penduxml/words/")
        self.player.setWord(word)
        print(word)
        compteur = -1
        cache = list("_"* len(word))
        stars = " ".join(cache)
        limite = 0
        essai = 8
        end = False
        img = PhotoImage(file="./img/0.png")
        #endregion

        #region fonction Affichage de la Difficulté choisi dans Menu
        difficultyString = ""
        if self.player.getDifficulty() == Difficulty.EASY:
            difficultyString = "Facile"
        elif self.player.getDifficulty() == Difficulty.NORMAL:
            difficultyString = "Normal"
        elif self.player.getDifficulty() == Difficulty.HARD:
            difficultyString = "Difficile"
        #endregion

        #label Titre "Jeu du Pendu"
        label_title = Label(self.window, text="Jeu Python", font=("Courrier", 40), bg='royal blue', fg='white')
        label_title.place(relx=0.09, rely=0.09, anchor=CENTER)

        #label pseudo et Difficulté
        displayPseudo = Label(self.window, text="Pseudo : " + self.player.getName(), font=("Courrier", 20), bg='royalblue', fg='white')
        displayPseudo.place(relx=0.25, rely=0.09, anchor=CENTER)

        displayDifficulty = Label(self.window, text="Difficulté : " + difficultyString, font=("Courrier", 20), bg='royalblue', fg='white')
        displayDifficulty.place(relx=0.25, rely=0.14, anchor=CENTER)

        #Timer Label
        compteur_lbl = Label(self.window, text=str(compteur), font=("Courrier", 30), bg='royal blue', fg='white')
        compteur_lbl.place(relx=0.50, rely=0.12, anchor=CENTER)
        self.window.after(1000, incremente())

        #menu jeu en haut a droite
        menu_button = Button(self.window, text="Revenir au menu", font=("Courrier", 15), width=18, command=self.openMainMenu)
        menu_button.place(relx=0.9, rely=0.1, anchor=CENTER)

        abandon_button = Button(self.window, text="Abandonner la partie", font=("Courrier", 15), width=18, command=self.openMainMenu)
        abandon_button.place(relx=0.75, rely=0.1, anchor=CENTER)

        leaderboard_button = Button(self.window, text="Afficher le TOP 10", font=("Courrier", 15), width=18, command=self.openLeaderboardManager)
        leaderboard_button.place(relx=0.9, rely=0.15, anchor=CENTER)

        help_button = Button(self.window, text="Afficher l'aide", font=("Courrier", 15), width=18, command=self.openHelpWindow)
        help_button.place(relx=0.75, rely=0.15, anchor=CENTER)


        #Frame contenant mot caché + essais
        f = Frame(self.window, padx=200, pady=100,bg='royalblue')
        f.pack(fill="both", expand="yes")
        f.place(relx=0.70, rely=0.4, anchor=CENTER)

        lbCache = Label(f, text=stars, font="Courrier 30 bold")
        lbCache.pack(padx=20, pady=20)

        annonce = Label(f, width=22, font=("Courrier", 25), bg='royalblue', fg='white')
        annonce.place(relx=0.5, rely=-1,anchor=N)

        imageP = Label(self.window, image=img)
        imageP.place(relx=0.25, rely=0.4, anchor=CENTER)


        #Label Score
        self.lbScore = Label(self.window, text="Score : " + self.score, font="Courrier 30 ", bg='royal blue', fg='white')
        self.lbScore.place(relx=0.5, rely=0.70, anchor=CENTER)


        #region BOUTONS 1ERE LIGNE ALPHABET
        lettreA = Button(self.window, text="A", font=("Courier", 15), width=5)
        lettreA.place(relx = 0.20, rely=0.8, anchor=CENTER)
        lettreA.bind("<Button-1>", clicklettre)

        lettreB = Button(self.window, text="B", font=("Courier", 15), width=5)
        lettreB.place(relx=0.25, rely=0.8, anchor=CENTER)
        lettreB.bind("<Button-1>", clicklettre)

        lettreC = Button(self.window, text="C", font=("Courier", 15), width=5)
        lettreC.place(relx=0.30, rely=0.8, anchor=CENTER)
        lettreC.bind("<Button-1>", clicklettre)

        lettreD= Button(self.window, text="D", font=("Courier", 15), width=5)
        lettreD.place(relx=0.35, rely=0.8, anchor=CENTER)
        lettreD.bind("<Button-1>", clicklettre)

        lettreE = Button(self.window, text="E", font=("Courier", 15), width=5)
        lettreE.place(relx=0.40, rely=0.8, anchor=CENTER)
        lettreE.bind("<Button-1>", clicklettre)

        lettreF = Button(self.window, text="F", font=("Courier", 15), width=5)
        lettreF.place(relx=0.45, rely=0.8, anchor=CENTER)
        lettreF.bind("<Button-1>", clicklettre)

        lettreG = Button(self.window, text="G", font=("Courier", 15), width=5)
        lettreG.place(relx=0.50, rely=0.8, anchor=CENTER)
        lettreG.bind("<Button-1>", clicklettre)

        lettreH = Button(self.window, text="H", font=("Courier", 15), width=5)
        lettreH.place(relx=0.55, rely=0.8, anchor=CENTER)
        lettreH.bind("<Button-1>", clicklettre)

        lettreI = Button(self.window, text="I", font=("Courier", 15), width=5)
        lettreI.place(relx=0.60, rely=0.8, anchor=CENTER)
        lettreI.bind("<Button-1>", clicklettre)

        lettreJ = Button(self.window, text="J", font=("Courier", 15), width=5)
        lettreJ.place(relx=0.65, rely=0.8, anchor=CENTER)
        lettreJ.bind("<Button-1>", clicklettre)

        lettreK = Button(self.window, text="K", font=("Courier", 15), width=5)
        lettreK.place(relx=0.70, rely=0.8, anchor=CENTER)
        lettreK.bind("<Button-1>", clicklettre)

        lettreL = Button(self.window, text="L", font=("Courier", 15), width=5)
        lettreL.place(relx=0.75, rely=0.8, anchor=CENTER)
        lettreL.bind("<Button-1>", clicklettre)

        lettreM = Button(self.window, text="M", font=("Courier", 15), width=5)
        lettreM.place(relx=0.80, rely=0.8, anchor=CENTER)
        lettreM.bind("<Button-1>", clicklettre)
        #endregion

        #region BOUTONS 2EME LIGNE ALPHABET
        lettreN = Button(self.window, text="N", font=("Courier", 15), width=5)
        lettreN.place(relx=0.20, rely=0.9, anchor=CENTER)
        lettreN.bind("<Button-1>", clicklettre)

        lettreO = Button(self.window, text="O", font=("Courier", 15), width=5)
        lettreO.place(relx=0.25, rely=0.9, anchor=CENTER)
        lettreO.bind("<Button-1>", clicklettre)

        lettreP = Button(self.window, text="P", font=("Courier", 15), width=5)
        lettreP.place(relx=0.30, rely=0.9, anchor=CENTER)
        lettreP.bind("<Button-1>", clicklettre)

        lettreQ = Button(self.window, text="Q", font=("Courier", 15), width=5)
        lettreQ.place(relx=0.35, rely=0.9, anchor=CENTER)
        lettreQ.bind("<Button-1>", clicklettre)

        lettreR = Button(self.window, text="R", font=("Courier", 15), width=5)
        lettreR.place(relx=0.40, rely=0.9, anchor=CENTER)
        lettreR.bind("<Button-1>", clicklettre)

        lettreS = Button(self.window, text="S", font=("Courier", 15), width=5)
        lettreS.place(relx=0.45, rely=0.9, anchor=CENTER)
        lettreS.bind("<Button-1>", clicklettre)

        lettreT = Button(self.window, text="T", font=("Courier", 15), width=5)
        lettreT.place(relx=0.50, rely=0.9, anchor=CENTER)
        lettreT.bind("<Button-1>", clicklettre)

        lettreU = Button(self.window, text="U", font=("Courier", 15), width=5)
        lettreU.place(relx=0.55, rely=0.9, anchor=CENTER)
        lettreU.bind("<Button-1>", clicklettre)

        lettreV = Button(self.window, text="V", font=("Courier", 15), width=5)
        lettreV.place(relx=0.60, rely=0.9, anchor=CENTER)
        lettreV.bind("<Button-1>", clicklettre)

        lettreW = Button(self.window, text="W", font=("Courier", 15), width=5)
        lettreW.place(relx=0.65, rely=0.9, anchor=CENTER)
        lettreW.bind("<Button-1>", clicklettre)

        lettreX = Button(self.window, text="X", font=("Courier", 15), width=5)
        lettreX.place(relx=0.70, rely=0.9, anchor=CENTER)
        lettreX.bind("<Button-1>", clicklettre)

        lettreY = Button(self.window, text="Y", font=("Courier", 15), width=5)
        lettreY.place(relx=0.75, rely=0.9, anchor=CENTER)
        lettreY.bind("<Button-1>", clicklettre)

        lettreZ = Button(self.window, text="Z", font=("Courier", 15), width=5)
        lettreZ.place(relx=0.80, rely=0.9, anchor=CENTER)
        lettreZ.bind("<Button-1>", clicklettre)
        #endregion