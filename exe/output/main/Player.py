class Player:

    def __init__(self, name, score, difficulty, word):
        self.name = name
        self.score = score
        self.difficulty = difficulty
        self.word = word

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def addScore(self, amount):
        self.score = self.score + amount

    def getDifficulty(self):
        return self.difficulty

    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word