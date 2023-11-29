import pyautogui
import time

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


def mangio():
    pass


dizionario_movimenti = {
    # R0
    'M[0][0] basso': 'a',
    'M[0][0] dx': 'b',
    'M[0][1] sx': 'c',
    'M[0][1] basso': 'd',
    'M[0][1] dx': 'e',
    'M[0][2] sx': 'f',
    'M[0][2] basso': 'g',
    'M[0][2] dx': 'h',
    'M[0][3] sx': 'i',
    'M[0][3] basso': 'j',
    'M[0][3] dx': 'k',
    'M[0][4] dx': 'l',
    'M[0][4] basso': 'm',
    # R1
    'M[1][0] basso': '',
    'M[1][0] dx': '',
    'M[1][0] alto': '',
    'M[1][1] sx': '',
    'M[1][1] basso': '',
    'M[1][1] dx': '',
    'M[1][1] alto': '',
    'M[1][2] sx': '',
    'M[1][2] basso': '',
    'M[1][2] dx': '',
    'M[1][2] alto': '',
    'M[1][3] sx': '',
    'M[1][3] basso': '',
    'M[1][3] dx': '',
    'M[1][3] alto': '',
    'M[1][4] sx': '',
    'M[1][4] basso': '',
    'M[1][4] alto': '',
    # R2
    'M[2][0] basso': '',
    'M[2][0] dx': '',
    'M[2][0] alto': '',
    'M[2][1] sx': '',
    'M[2][1] basso': '',
    'M[2][1] dx': '',
    'M[2][1] alto': '',
    'M[2][2] sx': '',
    'M[2][2] basso': '',
    'M[2][2] dx': '',
    'M[2][2] alto': '',
    'M[2][3] sx': '',
    'M[2][3] basso': '',
    'M[2][3] dx': '',
    'M[2][3] alto': '',
    'M[2][4] sx': '',
    'M[2][4] basso': '',
    'M[2][4] alto': '',
    # R3
    'M[3][0] basso': '',
    'M[3][0] dx': '',
    'M[3][0] alto': '',
    'M[3][1] sx': '',
    'M[3][1] basso': '',
    'M[3][1] dx': '',
    'M[3][1] alto': '',
    'M[3][2] sx': '',
    'M[3][2] basso': '',
    'M[3][2] dx': '',
    'M[3][2] alto': '',
    'M[3][3] sx': '',
    'M[3][3] basso': '',
    'M[3][3] dx': '',
    'M[3][3] alto': '',
    'M[3][4] sx': '',
    'M[3][4] basso': '',
    'M[3][4] alto': '',

    # R4
    'M[4][0] basso': '',
    'M[4][0] dx': '',
    'M[4][0] alto': '',
    'M[4][1] sx': '',
    'M[4][1] basso': '',
    'M[4][1] dx': '',
    'M[4][1] alto': '',
    'M[4][2] sx': '',
    'M[4][2] basso': '',
    'M[4][2] dx': '',
    'M[4][2] alto': '',
    'M[4][3] sx': '',
    'M[4][3] basso': '',
    'M[4][3] dx': '',
    'M[4][3] alto': '',
    'M[4][4] sx': '',
    'M[4][4] basso': '',
    'M[4][4] alto': '',
    # R5
    'M[5][0] dx': '',
    'M[5][0] alto': '',
    'M[5][1] sx': '',
    'M[5][1] dx': '',
    'M[5][1] alto': '',
    'M[5][2] sx': '',
    'M[5][2] dx': '',
    'M[5][2] alto': '',
    'M[5][3] sx': '',
    'M[5][3] dx': '',
    'M[5][3] alto': '',
    'M[5][4] sx': '',
    'M[5][4] alto': '',
}


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
    # controllo elementi di dx:
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


def scan_matrice(matrice2):
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


scan_matrice(matrice)
