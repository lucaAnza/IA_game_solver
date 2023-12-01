print("Test matrice 6x5")

# inizializzazione
matrice = [
    [],
    [],
    [],
    [],
    [],
    []
]

cont = 1

'''matrice[0].append(1)
matrice[1].append([1, 2, 3, 4, 5])
print(matrice[0][0])
print(matrice[1])'''

for i in range(6):
    for j in range(5):
        matrice[i].append(cont)
        cont += 1

for i in range(6):
    print()
    for j in range(5):
        print(matrice[i][j], end=' ')
