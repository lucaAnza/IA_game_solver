matrice = [
    [1, 2, 3, 3, 5],
    [2, 3, 1, 5, 5],
    [5, 5, 3, 2, 1],
    [1, 3, 3, 4, 2],
    [1, 2, 2, 3, 3],
    [5, 5, 3, 1, 5]
]

matrice2 = [
    [0, 1, 3, 4, 5],
    [4, 3, 2, 1, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 1],
    [1, 2, 2, 4, 5],
    [1, 2, 4, 4, 5]
]


def check_adj_row(l):
    for i in range(len(l)):  # range 0-4
        '''print(
            f'check index {i} -> is M[{i}]-> {l[i]} == M[{i+1}]-> {l[i+1]}')'''
        if (i == 4):
            return -1
        else:
            if l[i] == l[i+1]:
                return i


r = 0
c = 0
for i in range(6):  # controllo per righe
    c = check_adj_row(matrice2[i])
    if c != -1:  # condizione di adiacenza
        print("Trovati due elementi simili nella riga ", i)
        print("Indici = [", c, ",", c+1, "] -> ",
              matrice[i][c], " ", matrice[i][c+1])
    else:
        print("Nessun elemento adiacente nella riga: ", i, "\n")
