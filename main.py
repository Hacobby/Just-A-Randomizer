import random
import os
import time
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

gate = True
count = 0

while gate:
    print("--- Just A Randomizer ---")
    entries = input("Cantidad de entradas: ")
    if entries == "exit":
        gate = False
        print("Goodbye")
        break
    entries = int(entries)

    actors = [""] * entries
    for i in range(0, entries):
        actors[i] = input("Nombre del actor [" + str(i+1) +"]: ")
    stage = {name : 0 for name in actors} #Adjust to new logic

    rolls = int(input("Cantidad de rolls: "))
    for i in range(rolls):
        rWinner = random.choice(actors)
        stage[rWinner] += 1

    print("Resultados: ")
    for i in stage:
        time.sleep(1)
        print(i, stage[i])

    time.sleep(2)

    entries = input("Enter para continuar\n")
    if entries == "exit":
        gate = False
        print("Goodbye")
        time.sleep(1)
        break
    if entries == "save":
        print("Guardando...")
        with open("resultados " +str(count) +".json", "w") as archivo:
            json.dump(stage, archivo, indent=4)

    count += 1
    clear()