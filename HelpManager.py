from tkinter import *

class HelpManager:

    def __init__(self):
        self.window = Tk()

    def openWindow(self):
        self.window.title("Aide • PenduPython")
        #self.window.geometry("1280x720")
        self.window.attributes('-fullscreen', True)
        self.window.config(background='midnightblue')


        # Contruction fenêtre
        label_title = Label(self.window, text="Aide • PenduPython", font=("Courrier", 40), bg='royalblue', fg='white')
        label_title.pack()


        #1er Paragraphe Difficulté Explication
        label_Diff = Label(self.window, text="Explication de la difficulté :", font=("Courrier", 20,"underline"),
                           bg='midnightblue', fg='white')
        label_Diff.place(relx=0.5, rely=0.15, anchor=CENTER)

        label_Diff1 = Label(self.window, text="• La difficulté facile lorsqu'elle est choisie "
                                "prend un mot avec 4 lettres ou moins. ", font=("Courrier", 15), bg='midnightblue',
                                fg='white')
        label_Diff1.place(relx=0.5, rely=0.2, anchor=CENTER)

        label_Diff2 = Label(self.window, text="• La difficulté normal lorsqu'elle est choisie "
                                "prend un mot dans un intervalle de 5 lettres et 8 lettres.", font=("Courrier", 15),
                                bg='midnightblue',fg='white')
        label_Diff2.place(relx=0.5, rely=0.25, anchor=CENTER)


        label_Diff3 = Label(self.window, text="• La difficulté difficile lorsqu'elle est choisie "
                                "prend un mot de 9 lettres et plus.", font=("Courrier", 15),
                                bg='midnightblue',fg='white')
        label_Diff3.place(relx=0.5, rely=0.3, anchor=CENTER)


        #2eme Paragraphe Sur le Score+explication
        label_Score = Label(self.window, text="Explication du Score :", font=("Courrier", 20,"underline"),
                           bg='midnightblue', fg='white')
        label_Score.place(relx=0.5, rely=0.4, anchor=CENTER)

        label_Score1 = Label(self.window, text="• Pour chaque lettre trouvé le joueur gagne plus 1.",
                             font=("Courrier", 15), bg='midnightblue', fg='white')
        label_Score1.place(relx=0.5, rely=0.45, anchor=CENTER)

        label_Score2 = Label(self.window, text="• Lorsque le joueur trouve un mot il va gagner des points "
                                               "en fonction de la difficulté choisi :",
                             font=("Courrier", 15), bg='midnightblue', fg='white')
        label_Score2.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_Score3 = Label(self.window, text="- Facile : 5 points     - Normal : 10 points      "
                                               "- Difficile : 20 points",
                             font=("Courrier", 15), bg='midnightblue', fg='white')
        label_Score3.place(relx=0.5, rely=0.54, anchor=CENTER)

        label_Score4 = Label(self.window, text="• Le nombre d'essais restants a la fin de la partie vont s'ajouter au "
                                               "score du joueur.",
                             font=("Courrier", 15), bg='midnightblue', fg='white')
        label_Score4.place(relx=0.5, rely=0.6, anchor=CENTER)


        #Bouton de retour au menu (en bas)
        exit_button = Button(self.window, text="Retour", font=("Courrier", 25), width=15, command=self.closeWindow)
        exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)


    def closeWindow(self):
        self.window.destroy()