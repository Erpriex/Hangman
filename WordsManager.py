from tkinter import *

from NotifyUtils import NotifyUtils
from penduxml.words.WordsXML import WordsXML

class WordsManager:

    def __init__(self):
        self.window = Tk()

    def removeWord(self):
        targetIndex = self.Lb.curselection()
        targetWord = self.Lb.get(targetIndex)
        self.words.remove(targetWord) # Suppression en cache
        self.refreshListbox()

    def addWord(self):
        target = self.wordEntry.get()
        if target == "":
            notifyUtils = NotifyUtils()
            notifyUtils.sendNotify("Vous devez saisir un mot")
            return
        targetUpper = target.upper() # Convertion des lettres du mot en majuscule
        if targetUpper in self.words:
            notifyUtils = NotifyUtils()
            notifyUtils.sendNotify("Ce mot existe déjà dans la liste")
            return
        self.words.append(targetUpper) # Ajout du mot en cache
        self.refreshListbox()

    def saveWords(self):
        wordsxml = WordsXML()
        wordsxml.writeWords(self.words) # Enregistrement des mots en cache dans le XML
        self.closeWindow()



    def refreshListbox(self): # Actualisation de la listbox avec les mots en cache
        self.Lb.delete(0, 'end') # Clear de la listebox
        i = 1
        for word in self.words:
            self.Lb.insert(i, word)
            i = i + 1
        self.Lb.select_set(0) # Selection par défaut pour éviter les erreurs


    def openWindow(self):
        self.window.title("Gestion des mots • PenduPython")
        #self.window.geometry("1280x720")
        self.window.attributes('-fullscreen', True)
        self.window.config(background='midnightblue')

        wordsXML = WordsXML()
        self.words = wordsXML.getWords("penduxml/words/") # On récupère tous les mots dans le XML sous forme d'array

        label_title = Label(self.window, text="Gestion des mots", font=("Courrier", 40), bg='royalblue', fg='white')
        label_title.pack()

        # En haut
        self.Lb = Listbox(self.window)
        i = 1
        for word in self.words:
            self.Lb.insert(i, word)
            i = i + 1
        self.Lb.pack()
        self.Lb.config(font=("Courrier", 20), width=20, heigh=8)
        self.Lb.place(relx=0.5, rely=0.30, anchor=CENTER)
        self.Lb.select_set(0)


        remove_button = Button(self.window, text="Supprimer", font=("Courrier", 20), width=15, command=self.removeWord)
        remove_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Au milieu
        self.wordEntry = Entry(self.window, bd=0, font="Courrier 20", width=15)
        self.wordEntry.place(relx=0.5, rely=0.58, anchor=CENTER)

        add_button = Button(self.window, text="Ajouter", font=("Courrier", 20), width=15, command=self.addWord)
        add_button.place(relx=0.5, rely=0.63, anchor=CENTER)

        # Tout en bas
        save_button = Button(self.window, text="Enregistrer", font=("Courrier", 25), width=15, command=self.saveWords)
        save_button.place(relx = 0.5, rely=0.8, anchor=CENTER)

        exit_button = Button(self.window, text="Annuler", font=("Courrier", 25), width=15, command=self.closeWindow)
        exit_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def closeWindow(self):
        self.window.destroy()

