import random
gate = True

while gate:
    print("--- Ultimate Randomizer ---")
    entries = input("Ingrese la cantidad de entradas: ")
    if entries == "exit":
        gate = False
        print("Goodbye")
        break
    entries = int(entries)

    actors = [""] * entries
    for i in range(0, entries):
        #print(i)
        actors[i] = input("Ingrese el nombre del actor: ")
    stage = {name : 0 for name in actors}

    rolls = int(input("Ingrese la cantidad de rolls: "))
    for i in range(rolls):
        rWinner = random.choice(actors)
        stage[rWinner] += 1

    print("Resultados: ")
    for i in stage:
        print(i, stage[i])