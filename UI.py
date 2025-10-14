import tkinter as tk

class UI:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic

        self.names = []
        self.results = tk.StringVar()

        # UI Setup

        self.ui.title("Just A Randomizer")
        self.ui.geometry("800x600")

        self.quantity = tk.Entry(self.ui)
        self.quantity.pack()

        self.genButton = tk.Button(self.ui, text="Crear campos", command=self.genFields)
        self.genButton.pack()

        self.nameFrame = tk.Frame(self.ui)
        self.nameFrame.pack()

        self.rolls = tk.Entry(self.ui)
        self.rolls.pack()

        self.sortButton = tk.Button(self.ui, text="Sortear", command=self.sort)
        self.sortButton.pack()

        self.resultLabel = tk.Label(self.ui, textvariable=self.results)
        self.resultLabel.pack()

    def genFields(self):
        quantity = int(self.quantity.get())
        self.names = []
        for i in range(quantity):
            entry = tk.Entry(self.nameFrame)
            entry.pack()
            self.names.append(entry)

    def sort(self):
        names = [entry.get() for entry in self.names]
        self.logic.loadActors(names)

        rolls = int(self.rolls.get())
        self.logic.roll(rolls)

        resultText = "\n".join(f"{k}: {v}" for k, v in self.logic.stage.items())
        self.results.set(resultText)