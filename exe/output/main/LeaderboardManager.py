from tkinter import *

from penduxml.players.PlayersXML import PlayersXML


class LeaderboardManager:

    def __init__(self):
        self.window = Tk()

    def openWindow(self):
        self.window.title("Classement des joueurs • PenduPython")
        #self.window.geometry("1280x720")
        self.window.attributes('-fullscreen', True)
        self.window.config(background='midnightblue')

        # Récuparations des joueurs dans le fichier XML
        playersXML = PlayersXML()
        players = playersXML.getPlayers("penduxml/players/")

        label_title = Label(self.window, text="Classement TOP 10", font=("Courrier", 40), bg='royalblue', fg='white')
        label_title.pack()

        #Déclaration de variable pour les différentes boucles
        Lb = Listbox(self.window)
        i = -1
        y = 1
        joueur =[]

        # Classement des joueurs dans l'ordre croissant par rapport à son score
        for player in players: #
            joueur.append(("Name:",player.getName(), "Difficulty:",player.getDifficulty(),"Mot:",player.getWord(),"Score",int(player.getScore())))
        joueur = sorted(joueur, key=lambda joueur:joueur[7]) #range la liste joueur par ordre croissant en fonction du score

        #On range la liste joueur par ordre décroissant dans un nouveau tableau
        classement = []
        for k in range(len(joueur)):
            classement.append((str(k+1), joueur[i]))
            i -= 1

        #On insère dans la Liste box les 10 premières valeurs de classement + le Rang
        for j in range(10):
            Lb.insert(str(y), classement[j])
            y += 1 #Rang classement

        #Liste box pour afficher les joueurs
        Lb.pack()
        Lb.config(font=("Courrier", 20), width=70, heigh=14)
        Lb.place(relx=0.5, rely=0.50, anchor=CENTER)

        #Bouton de "retour" au menu
        exit_button = Button(self.window, text="Retour", font=("Courrier", 25), width=15, command=self.closeWindow)
        exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    #ferme la fenetre actuel
    def closeWindow(self):
        self.window.destroy()