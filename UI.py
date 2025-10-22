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
        self.ui.grid_rowconfigure(0, weight=1)
        self.ui.grid_rowconfigure(1, weight=1)
        self.ui.grid_columnconfigure(0, weight=1)
        self.ui.grid_columnconfigure(1, weight=1)

        # Frames con scroll
        topRightContainer, topRightFrame = self.makeScrollable(self.ui)
        topRightContainer.grid(column=1, row=0, sticky=tk.NSEW, padx=5, pady=5)

        bottomLeftContainer, bottomLeftFrame = self.makeScrollable(self.ui)
        bottomLeftContainer.grid(column=0, row=1, sticky=tk.NSEW, padx=5, pady=5)

        # Frames comunes
        topLeftFrame = tk.Frame(self.ui)
        topLeftFrame.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        bottomRightFrame = tk.Frame(self.ui)
        bottomRightFrame.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        self.nameFrame = tk.Frame(topRightFrame)
        self.nameFrame.grid(column=0, row=0, sticky=tk.E)

        #Etiquetas y entradas
        tk.Label(topLeftFrame, text="Cantidad de entradas:").grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        self.quantity = tk.Entry(topLeftFrame)
        self.quantity.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        tk.Label(topLeftFrame, text="Cantidad de rolls:").grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
        self.rolls = tk.Entry(topLeftFrame)
        self.rolls.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        tk.Label(bottomLeftFrame, text="Resultados:").grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
        tk.Label(bottomLeftFrame, textvariable=self.results).grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        #Botones
        tk.Button(topLeftFrame, text="Roll", command=self.sort).grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)
        tk.Button(topLeftFrame, text="Generar slots", command=self.genFields).grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)
        tk.Button(bottomLeftFrame, text="Guardar resultados", command=self.logic.saveResults).grid(column=2, row=3, sticky=tk.W, padx=5, pady=5)

    def genFields(self):
        for widget in self.nameFrame.winfo_children():
            widget.destroy()

        quantity = int(self.quantity.get())
        self.names = []
        for i in range(quantity):
            tk.Label(self.nameFrame, text=f"Nombre {i+1}:").grid(column=0, row=i, sticky=tk.E, padx=5, pady=5)
            entry = tk.Entry(self.nameFrame)
            entry.grid(column=1, row=i, sticky=tk.E, padx=5, pady=2)
            self.names.append(entry)

    def sort(self):
        names = [entry.get() for entry in self.names]
        self.logic.loadActors(names)

        rolls = int(self.rolls.get())
        self.logic.roll(rolls)

        resultText = "\n".join(f"{k}: {v}" for k, v in self.logic.stage.items())
        self.results.set(resultText)

    def makeScrollable(self, parent):
        container = tk.Frame(parent)
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, command=canvas.yview, orient="vertical")
        scrollable = tk.Frame(canvas)

        scrollable.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NSEW)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Mousewheel fix
        def onMouseWheel(event):
            canvas.yview_scroll(int(-1 * (event.delta/120)), "units")
        scrollable.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", onMouseWheel))
        scrollable.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        return container, scrollable