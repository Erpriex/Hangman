from xml.dom import minidom

from Difficulty import Difficulty
from Player import Player


class PlayersXML:

    def getPlayers(self, path):
        finalPath = path + "players.xml"
        doc = minidom.parse(finalPath) # Parse du XML avec son path
        players = doc.getElementsByTagName("player") # Récupération de tous les noeuds 'player'
        playersList = []
        for player in players: # Conversion des value en objet Player
            name = player.getAttribute("name")
            score = int(player.getAttribute("score"))
            difficulty = ""
            if player.getAttribute("difficulty") == "Facile": # Conversion difficultée d'affichage en Enum
                difficulty = Difficulty.EASY
            elif player.getAttribute("difficulty") == "Normal":
                difficulty = Difficulty.NORMAL
            elif player.getAttribute("difficulty") == "Difficile":
                difficulty = Difficulty.HARD
            word = player.getAttribute("word")
            playerInstance = Player(name, score, difficulty, word) # Création de l'objet Player avec les valeurs récupérées
            playersList.append(playerInstance)
        return playersList

    def addPlayer(self, player):
        players = self.getPlayers("penduxml/players/")
        players.append(player)
        self.writePlayers(players)

    def writePlayers(self, playersToWrite):
        document = minidom.Document()
        players = document.createElement('players') # Création arbre XML
        for player in playersToWrite:
            entry = document.createElement('player') # Création noeud player
            entry.setAttribute('name', player.getName())
            entry.setAttribute('score', str(player.getScore()))
            if player.getDifficulty() == Difficulty.EASY: # Conversion Enum Difficulty en String
                entry.setAttribute('difficulty', 'Facile')
            elif player.getDifficulty() == Difficulty.NORMAL:
                entry.setAttribute('difficulty', 'Normal')
            elif player.getDifficulty() == Difficulty.HARD:
                entry.setAttribute('difficulty', 'Difficile')
            else:
                entry.setAttribute('difficulty', 'Non definie') # par defaut si difficultée inconnue
            entry.setAttribute('word', player.getWord())
            players.appendChild(entry)
        document.appendChild(players) # Ajout noeuds au document
        with open('./penduxml/players/players.xml', 'w') as out:
            document.writexml(out, encoding='UTF-8') # Ecriture XML
        print("Fichier 'players.xml' mis a jour")