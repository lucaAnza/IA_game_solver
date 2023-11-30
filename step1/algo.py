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
    'M[0][4] sx': 'l',
    'M[0][4] basso': 'm',
    # R1
    'M[1][0] basso': 'n',
    'M[1][0] dx': 'o',
    'M[1][0] alto': 'p',
    'M[1][1] sx': 'q',
    'M[1][1] basso': 'r',
    'M[1][1] dx': 's',
    'M[1][1] alto': 't',
    'M[1][2] sx': 'u',
    'M[1][2] basso': 'v',
    'M[1][2] dx': 'x',
    'M[1][2] alto': 'y',
    'M[1][3] sx': 'z',
    'M[1][3] basso': 'w',
    'M[1][3] dx': '1',
    'M[1][3] alto': '2',
    'M[1][4] sx': '3',
    'M[1][4] basso': '4',
    'M[1][4] alto': '5',
    # R2
    'M[2][0] basso': '6',
    'M[2][0] dx': '7',
    'M[2][0] alto': '8',
    'M[2][1] sx': '9',
    'M[2][1] basso': 'ctrl+a',
    'M[2][1] dx': 'ctrl+b',
    'M[2][1] alto': 'ctrl+c',
    'M[2][2] sx': 'ctrl+d',
    'M[2][2] basso': 'ctrl+e',
    'M[2][2] dx': 'ctrl+f',
    'M[2][2] alto': 'ctrl+g',
    'M[2][3] sx': 'ctrl+h',
    'M[2][3] basso': 'ctrl+i',
    'M[2][3] dx': 'ctrl+j',
    'M[2][3] alto': 'ctrl+k',
    'M[2][4] sx': 'ctrl+l',
    'M[2][4] basso': 'ctrl+m',
    'M[2][4] alto': 'ctrl+n',
    # R3
    'M[3][0] basso': 'ctrl+o',
    'M[3][0] dx': 'ctrl+p',
    'M[3][0] alto': 'ctrl+q',
    'M[3][1] sx': 'ctrl+r',
    'M[3][1] basso': 'ctrl+s',
    'M[3][1] dx': 'ctrl+t',
    'M[3][1] alto': 'ctrl+u',
    'M[3][2] sx': 'ctrl+v',
    'M[3][2] basso': 'ctrl+x',
    'M[3][2] dx': 'ctrl+y',
    'M[3][2] alto': 'ctrl+z',
    'M[3][3] sx': 'ctrl+0',
    'M[3][3] basso': 'ctrl+1',
    'M[3][3] dx': 'ctrl+2',
    'M[3][3] alto': 'ctrl+3',
    'M[3][4] sx': 'ctrl+4',
    'M[3][4] basso': 'ctrl+5',
    'M[3][4] alto': 'ctrl+6',

    # R4
    'M[4][0] basso': 'ctrl+7',
    'M[4][0] dx': 'ctrl+8',
    'M[4][0] alto': 'ctrl+9',
    'M[4][1] sx': 'alt+a',
    'M[4][1] basso': 'alt+b',
    'M[4][1] dx': 'alt+c',
    'M[4][1] alto': 'alt+d',
    'M[4][2] sx': 'alt+e',
    'M[4][2] basso': 'alt+f',
    'M[4][2] dx': 'alt+g',
    'M[4][2] alto': 'alt+h',
    'M[4][3] sx': 'alt+i',
    'M[4][3] basso': 'alt+j',
    'M[4][3] dx': 'alt+k',
    'M[4][3] alto': 'alt+l',
    'M[4][4] sx': 'alt+m',
    'M[4][4] basso': 'alt+n',
    'M[4][4] alto': 'alt+o',
    # R5
    'M[5][0] dx': 'alt+p',
    'M[5][0] alto': 'alt+q',
    'M[5][1] sx': 'alt+r',
    'M[5][1] dx': 'alt+s',
    'M[5][1] alto': 'alt+t',
    'M[5][2] sx': 'alt+u',
    'M[5][2] dx': 'alt+v',
    'M[5][2] alto': 'alt+w',
    'M[5][3] sx': 'alt+x',
    'M[5][3] dx': 'alt+y',
    'M[5][3] alto': 'alt+z',
    'M[5][4] sx': 'alt+1',
    'M[5][4] alto': 'alt+2',
}


def send_input_gui(string):
    c1, c2 = string.split('+')
    if c2 != '':  # se si usa CTRL o ALT come opzione
        pyautogui.hotkey(c1, c2)
    else:
        pyautogui.press(c1)


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


# controlla che il range sia valido per controllo orizzontale (e verticale outofline)
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

    # controllo sinistra
    if ((valid_bound(i-1, j-1)) and (matrice[i-1][j-1] == el1)):
        return (f"M[{i-1}][{j-1}] dx")

    elif ((valid_bound(i+2, j-1)) and (matrice[i+2][j-1] == el2)):
        return (f"M[{i+2}][{j-1}] dx")

    # controllo destra
    elif (valid_bound(i-1, j+1) and (matrice[i-1][j+1] == el1)):
        return (f"M[{i-1}][{j+1}] sx")

    elif (valid_bound(i+2, j+1) and (matrice[i+2][j+1] == el2)):
        return (f"M[{i+2}][{j+1}] sx")

    # Controllo in line alto - basso
    elif ((valid_col_bound(i+3)) and (matrice[i+3][j] == el2)):
        return (f"M[{i+3}][{j}] alto")

    elif ((valid_col_bound(i-2)) and (matrice[i-2][j] == el1)):
        return (f"M[{i-2}][{j}] basso")

    # nessuna possibile mossa trovata
    print(
        f">>OUTPUT>> Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")
    return None

# da eliminare i return true con gli indici dell'elemento da tradurre


def check_row_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i][j+1]
    # controllo inline dx e sx:
    if (valid_bound(i, j-2) and (matrice[i][j-2] == el1)):
        return (f"M[{i}][{j-2}] dx")

    elif (valid_bound(i, j+2) and (matrice[i][j+2] == el2)):
        return (f"M[{i}][{j+2}] sx")

    # controllo elementi di sinistra:
    elif (valid_bound(i-1, j-1) and (matrice[i-1][j-1] == el1)):
        print(f"M[{i-1}][{j-1}] basso")

    elif (valid_bound(i+1, j-1) and (matrice[i+1][j-1] == el1)):
        return (f"M[{i+1}][{j-1}] alto")

    # controllo elementi di dx:
    elif (valid_bound(i-1, j+2) and (matrice[i-1][j+2] == el2)):
        return (f"M[{i-1}][{j+2}] basso")

    elif (valid_bound(i+1, j+2) and (matrice[i+1][j+2] == el2)):
        return (f"M[{i+1}][{j+2}] alto")

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
