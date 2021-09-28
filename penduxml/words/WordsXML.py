from xml.dom import minidom
import random

from Difficulty import Difficulty


class WordsXML:

    def getWords(self, path):
        finalPath = path + "words.xml"
        doc = minidom.parse(finalPath) # Parse contenu 'words.xml' depuis son path
        words = doc.getElementsByTagName("word") # Récupérations des noeuds
        wordsList = []
        for word in words:
            name = word.getAttribute("name")
            wordsList.append(name)
        return wordsList

    def getRandomWord(self, path):
        words = self.getWords(path)
        wordRandom = random.choice(words)
        return wordRandom

    def getRandomWordWithDifficulty(self, difficulty, path):
        # nb lettres en fonction de la difficulté
        # Facile : <=4
        # Normal : >4 && <= 8
        # Difficile : >8
        words = self.getWords(path)
        wordsTarget = []
        finded = False
        for word in words:
            if difficulty == Difficulty.EASY:
                if len(word) <= 4:
                    wordsTarget.append(word)
                    finded = True
            if difficulty == Difficulty.NORMAL:
                if len(word) > 4 and len(word) <= 8:
                    wordsTarget.append(word)
                    finded = True
            if difficulty == Difficulty.HARD:
                if len(word) > 8:
                    wordsTarget.append(word)
                    finded = True
        wordFinal = ""
        if finded == True:
            wordFinal = random.choice(wordsTarget)
        else:  # Si aucun mot trouvé (nb lettre suffisant n'existe pas), on récupère un mot aléatoire
            wordFinal = self.getRandomWord(path)
        return wordFinal


    def writeWords(self, wordsToWrite):
        document = minidom.Document() # Création document
        words = document.createElement('words')
        for word in wordsToWrite:
            entry = document.createElement('word') # Création noeud
            entry.setAttribute('name', word)
            words.appendChild(entry)
        document.appendChild(words)
        with open('./penduxml/words/words.xml', 'w') as out:
            document.writexml(out, encoding='utf-8') # Ecriture dans XML
        print("Fichier 'words.xml' mis a jour")