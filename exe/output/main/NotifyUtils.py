from tkinter import *

class NotifyUtils:
    def __init__(self):
        self.window = Tk()

    def center_window(self, w=300, h=200): # Affichage de la fenêtre au centre de l'ecran
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def sendNotify(self, message):
        self.window.title("Notification • PenduPython")
        #self.window.geometry("650x250")
        self.window.config(background='midnightblue')

        self.center_window(650,250)

        # On récupère le message de notification dans le parametre de la methode
        label_message = Label(self.window, text=message, font=("Courrier", 25), bg='royalblue', fg='white')
        label_message.pack()

        exit_button = Button(self.window, text="OK !", font=("Courrier", 20), width=5, command=self.closeWindow)
        exit_button.pack()

    def closeWindow(self):
        self.window.destroy()