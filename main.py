import random
import os
import json
from UI import UI
import tkinter as tk

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Logic:
    def __init__(self):
        self.count = 1
        self.actors = []
        self.stage = {}

    def loadActors(self, names):
        self.actors = names
        self.stage = {name: 0 for name in self.actors}

    def roll(self, quantity):
        for i in range(quantity):
            winner = random.choice(self.actors)
            self.stage[winner] += 1

    def saveResults(self):
        with open(f"resultados {self.count}.json", "w") as file:
            json.dump(self.stage, file, indent=4)
            self.count += 1

if __name__ == "__main__":
    root = tk.Tk()
    appLogic = Logic()
    ui = UI(root, appLogic)
    root.mainloop()