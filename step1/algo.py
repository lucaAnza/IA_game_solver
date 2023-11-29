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
    [2, 2, 3, 1, 1],
    [1, 2, 2, 4, 4],
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


def check_adj_column(M, j):
    for i in range(6):
        if (i == 5):
            return -1
        else:
            if M[i][j] == M[i+1][j]:
                return i


# controlla che il range sia valido per controllo orizzontale
def valid_bound(i, j):
    if ((i >= 0 and i <= 5) and (j >= 0 and j <= 4)):
        return True
    print("(((Elemento out of bounds)))")
    return False


# controlla che il range sia valido per controllo verticale
def valid_col_bound(i):
    if (i >= 0 and i <= 5):
        return True
    print("(((Elemento out of bounds)))")
    return False


def check_column_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i+1][j]
    if ((valid_col_bound(i+3)) and (matrice[i+3][j] == el2)):
        print(f">>OUTPUT>> Mossa -> Sposta M[{i+3}][{j}] verso nord")
        return True
    elif ((valid_col_bound(i-2)) and (matrice[i-2][j] == el1)):
        print(f">>OUTPUT>> Mossa -> Sposta M[{i-2}][{j}] verso sud")
        return True

    # nessuna possibile mossa trovata
    print(
        f">>OUTPUT>> Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")


# da eliminare i return true con gli indici dell'elemento da tradurre
def check_row_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i][j+1]
    # controllo elementi di sinistra:
    if (valid_bound(i-1, j-1) and (matrice[i-1][j-1] == el1)):
        print(f">>OUTPUT>> Mossa ->   Sposta M[{i-1}][{j-1}] verso sud")
        return True
    elif (valid_bound(i+1, j-1) and (matrice[i-1][j-1] == el1)):
        print(f">>OUTPUT>> Mossa ->   Sposta M[{i-1}][{j-1}] verso nord")
        return True
    # controllo elementi di destra:
    elif (valid_bound(i-1, j+2) and (matrice[i-1][j+2] == el2)):
        print(f">>OUTPUT>> Mossa ->   Sposta M[{i-1}][{j+2}] verso sud")
        return True
    elif (valid_bound(i+1, j+2) and (matrice[i+1][j+2] == el2)):
        print(f">>OUTPUT>> Mossa ->   Sposta M[{i+1}][{j+2}] verso nord")
        return True

    # nessuna possibile mossa trovata
    print(
        f">>OUTPUT>> Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")
    return False


r = 0
c = 0


def controllo_righe():
    for i in range(6):  # controllo per righe
        c = check_adj_row(matrice2[i])
        if c != -1:  # condizione di adiacenza
            print("Trovati due elementi simili nella riga ", i)
            print("Indici = [", c, ",", c+1, "] -> ",
                  matrice2[i][c], " ", matrice2[i][c+1], "\tinizio controllo feasibility")
            check_row_feasibility(i, c, matrice2)
            print()
            # [1, 2, 4, 4, 5]
        else:
            print("Nessun elemento adiacente nella riga: ", i, "\n")


for j in range(5):  # controllo per colonne
    riga_index = check_adj_column(matrice2, j)
    if riga_index != -1:  # condizione di adiacenza
        print("Trovati due elementi simili nella colonna ", j)
        print(
            f"Indici = [{riga_index},{riga_index+1}] -> {matrice2[riga_index][j]} {matrice2[riga_index][j]}")
        check_column_feasibility(riga_index, j, matrice2)
        print()
    else:
        print("Nessun elemento adiacente nella colonna: ", j, "\n")
