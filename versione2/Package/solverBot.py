import pyautogui
from colorama import Fore, Style
import os
import cv2

if __name__ == "__main__" or __name__ == 'solverBot':
    import decoratori
    import print_coloured as p
else:

    from Package import decoratori
    from Package import print_coloured as p


# Setting
os.system("color")  # abilita i colori nella shell


# Global
delay_keyPress_single = 0.04
delay_keyPress_combo = 0.01
num_righe = 6
num_colonne = 5
offset = 100

# {Fore.GREEN}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} \t
# 6a

mm1 = [
    [1, 2, 3, 3, 5],
    [2, 1, 1, 5, 5],
    [5, 5, 3, 2, 1],
    [1, 3, 3, 4, 2],
    [1, 2, 2, 3, 3],
    [5, 5, 3, 1, 5]
]

mm2 = [
    [0, 1, 3, 4, 5],
    [4, 3, 2, 1, 4],
    [1, 2, 3, 4, 5],
    [2, 2, 3, 1, 1],
    [1, 2, 2, 4, 4],
    [1, 2, 4, 4, 5]
]

mm3 = [
    [3, 3, 1, 1, 2],
    [3, 4, 1, 1, 4],
    [1, 2, 4, 3, 3],
    [1, 3, 4, 4, 2],
    [3, 3, 1, 2, 3],
    [2, 2, 1, 3, 1]
]


mm4 = [
    [6, 4, 3, 2, 1],
    [1, 2, 0, 4, 6],
    [6, 4, 3, 2, 1],
    [1, 2, 0, 4, 6],
    [6, 9, 3, 6, 1],
    [1, 2, 0, 4, 6]
]

mm5 = [
    [1, 0, 1, 0, 1],
    [2, 9, 2, 9, 2],
    [3, 0, 3, 0, 3],
    [4, 1, 4, 3, 4],
    [6, 2, 6, 2, 6],
    [7, 3, 7, 3, 7]
]


mm6 = [
    [4, 3, 1, 1, 2],
    [1, 2, 4, 4, 3],
    [4, 3, 1, 3, 1],
    [2, 3, 1, 2, 3],
    [1, 4, 3, 4, 1],
    [4, 3, 4, 3, 4]
]

dizionario_movimenti = {
    # R0
    'M[0][0] basso': 'a+',
    'M[0][0] dx': 'b+',
    'M[0][1] sx': 'c+',
    'M[0][1] basso': 'd+',
    'M[0][1] dx': 'e+',
    'M[0][2] sx': 'f+',
    'M[0][2] basso': 'g+',
    'M[0][2] dx': 'h+',
    'M[0][3] sx': 'i+',
    'M[0][3] basso': 'j+',
    'M[0][3] dx': 'k+',
    'M[0][4] sx': 'l+',
    'M[0][4] basso': 'm+',
    # R1
    'M[1][0] basso': 'n+',
    'M[1][0] dx': 'o+',
    'M[1][0] alto': 'p+',
    'M[1][1] sx': 'q+',
    'M[1][1] basso': 'r+',
    'M[1][1] dx': 's+',
    'M[1][1] alto': 't+',
    'M[1][2] sx': 'u+',
    'M[1][2] basso': 'v+',
    'M[1][2] dx': 'x+',
    'M[1][2] alto': 'y+',
    'M[1][3] sx': 'z+',
    'M[1][3] basso': 'w+',
    'M[1][3] dx': '1+',
    'M[1][3] alto': '2+',
    'M[1][4] sx': '3+',
    'M[1][4] basso': '4+',
    'M[1][4] alto': '5+',
    # R2
    'M[2][0] basso': '6+',
    'M[2][0] dx': '7+',
    'M[2][0] alto': '8+',
    'M[2][1] sx': '9+',
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
    'M[3][3] sx': 'ctrl+w',
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
    'M[5][2] alto': 'alt+x',
    'M[5][3] sx': 'alt+y',
    'M[5][3] dx': 'alt+z',
    'M[5][3] alto': 'alt+w',
    'M[5][4] sx': 'alt+1',
    'M[5][4] alto': 'alt+2',
}


@decoratori.timestamp_decorator
def send_input_gui(string):
    p.print_red_ts(f"COMANDO PASSATO: {string}")

    c1, c2 = string.split('+')
    if c2 != '':  # se si usa CTRL o ALT come opzione
        p.print_green_ts(f"Pressed Key: {c1}+{c2}")
        pyautogui.hotkey(c1, c2, interval=delay_keyPress_combo)
    else:
        p.print_green_ts(f"Pressed Key: {c1}")
        pyautogui.press(c1, interval=delay_keyPress_single)


# Funzione che ritorna l'indice di colonna del primo elemento di una successione di 2
def check_adj_row(l):
    for i in range(len(l)):  # range 0-4
        '''print(
            f'check index {i} -> is M[{i}]-> {l[i]} == M[{i+1}]-> {l[i+1]}')'''
        if (i == 4):
            return -1
        elif l[i] == 5:  # stella
            return i+offset
        else:
            if l[i] == l[i+1]:
                return i


def check_adj_row2(l):
    temp_adj = []
    for i in range(len(l)):  # range 0-4
        if (i == 4):
            break
        elif l[i] == 5:  # stella
            # Per fare in modo che esista sempre un elemento temp_adj[0]
            temp_adj.append(-1)
            temp_adj[0] = i+offset
            return temp_adj
        else:
            if l[i] == l[i+1]:
                temp_adj.append(i)
    return temp_adj


# MANCA: controllo in line se indice minore di 4


def check_adj_column(M, j):
    for i in range(6):
        if (i == 5):
            return -1
        else:
            if M[i][j] == M[i+1][j]:
                return i


def check_adj_column2(M, j):
    temp_adj = []
    for i in range(6):
        if (i == 5):
            break
        else:
            if M[i][j] == M[i+1][j]:
                temp_adj.append(i)
    return temp_adj


# controlla che il range sia valido per controllo orizzontale (e verticale outofline)
def valid_bound(i, j):
    if ((i >= 0 and i <= 5) and (j >= 0 and j <= 4)):
        return True
    p.print_red_ts(f"(((OOB)))")
    return False


# controlla che il range sia valido per controllo verticale
def valid_col_bound(i):
    if (i >= 0 and i <= 5):
        return True
    p.print_red_ts(f"(((OOB)))")
    return False

# @decoratori.timestamp_decorator


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
    p.print_red_ts(
        f"Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")
    return False


# @decoratori.timestamp_decorator
def check_row_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i][j+1]
    # controllo inline dx e sx:
    if (valid_bound(i, j-2) and (matrice[i][j-2] == el1)):
        return (f"M[{i}][{j-2}] dx")

    elif (valid_bound(i, j+3) and (matrice[i][j+3] == el2)):
        return (f"M[{i}][{j+3}] sx")

    # controllo elementi di sinistra:
    elif (valid_bound(i-1, j-1) and (matrice[i-1][j-1] == el1)):
        return (f"M[{i-1}][{j-1}] basso")

    elif (valid_bound(i+1, j-1) and (matrice[i+1][j-1] == el1)):
        return (f"M[{i+1}][{j-1}] alto")

    # controllo elementi di dx:
    elif (valid_bound(i-1, j+2) and (matrice[i-1][j+2] == el2)):
        return (f"M[{i-1}][{j+2}] basso")

    elif (valid_bound(i+1, j+2) and (matrice[i+1][j+2] == el2)):
        return (f"M[{i+1}][{j+2}] alto")

    # nessuna possibile mossa trovata
    p.print_red_ts(
        f"Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")
    return False


def check_hop_adj_row(l):
    temp_hops = []
    for i in range(len(l)):
        if (i == 3):
            break
        elif l[i] == l[i+2]:
            temp_hops.append(i)
    return temp_hops


def check_hop_adj_col(M, j):
    temp_hops = []
    for i in range(6):
        if (i == 4):
            break
        else:
            if M[i][j] == M[i+2][j]:
                temp_hops.append(i)
    return temp_hops


def check_hop_row_feasibility(i, j, M):
    el1 = M[i][j]
    # controllo superiore:
    if ((valid_bound(i-1, j+1)) and (M[i-1][j+1] == el1)):
        return (f"M[{i-1}][{j+1}] basso")
    elif ((valid_bound(i+1, j+1)) and (M[i+1][j+1] == el1)):
        return (f"M[{i+1}][{j+1}] alto")

    p.print_red_ts(f"Nessuna mossa valida trovata per hop M[{i}][{j}]\n")
    return False


def check_hop_column_feasibility(i, j, M):
    el1 = M[i][j]
    if ((valid_bound(i+1, j-1)) and (M[i+1][j-1] == el1)):
        return (f"M[{i+1}][{j-1}] dx")
    elif ((valid_bound(i+1, j+1)) and (M[i+1][j+1] == el1)):
        return (f"M[{i+1}][{j+1}] sx")
    p.print_red_ts(f"Nessuna mossa valida trovata per hop M[{i}][{j}]\n")
    return False


@decoratori.timestamp_decorator
def scan_matrice(matrice):
    mossa = False
    for i in range(6):  # controllo per righe
        if mossa == True:
            break
        #### LOGICA CON LISTA DI INDICI:####

        l_adj = check_adj_row2(matrice[i])  # Ritorna indice di colonna

        if len(l_adj) == 0:
            p.print_red_ts(f"Nessun elemento adiacente nella riga: {i}\n")
        # Condizione Stella
        elif l_adj[0] >= offset:
            c = l_adj[0]
            c = c-offset
            p.print_magenta_ts(f"Stella trovata in posizione [{i}][{c}]")
            if (i == 5):    # Nel caso la stella sia in fondo
                send_input_gui(dizionario_movimenti[f'M[{i}][{c}] alto'])
            else:
                send_input_gui(dizionario_movimenti[f'M[{i}][{c}] basso'])
            mossa = True
            break
        # Condizione di adiacenza sulla riga
        elif len(l_adj) > 0:
            p.print_green_ts(f"Trovati elementi simili nella riga {i}")
            p.print_magenta_ts(f"Inizio controllo feasibility <Row {i}>")

            # CONTROLLO RIGA
            # ciclo per iterare gli indici con adiacenze
            for k in range(len(l_adj)):
                p.print_green_ts(f"Controllo coppia adiacente n.{k+1}")
                move = check_row_feasibility(i, l_adj[k], matrice)
                if move and isinstance(move, str):  # mossa valida trovata
                    p.print_magenta_ts("pass!")
                    send_input_gui(dizionario_movimenti[move])
                    mossa = True
                    break
                print()
        # condizione no adiacenza della riga
        else:
            p.print_red_ts(
                f"Errore non determinato -> check SolverBot.scan_matrice() \n")

    # CONTROLLO COLONNE
    exit = False
    if mossa != True:
        p.print_magenta_ts("    -->>Controllo colonne<<--    \n")
        for j in range(5):  # controllo per colonne
            if exit == True:
                break
            col_adj = check_adj_column2(matrice, j)
            if len(col_adj) > 0:  # condizione di adiacenza
                p.print_green_ts(f"Trovati elementi simili nella colonna: {j}")

                # CONTROLLO COLONNA
                for k in range(len(col_adj)):
                    p.print_green_ts(f"Controllo coppia adiacente n.{k}")
                    move2 = check_column_feasibility(col_adj[k], j, matrice)
                    if move2 and isinstance(move2, str):  # mossa valida trovata
                        p.print_magenta_ts("pass!")
                        send_input_gui(dizionario_movimenti[move2])
                        exit = True
                        mossa = True
                        break
                    print()
            else:
                p.print_red_ts(f"Nessun elemento adiacente nella colonna: {j}")

    if mossa != True:
        p.print_cyan_ts(
            f"Nessuna soluzione trovata per adiacenze... Inizio controllo by hop")
        # CONTROLLO HOP ORIZZONTALI
        for i in range(6):
            if mossa == True:
                break
            hops_or = check_hop_adj_row(matrice[i])
            if len(hops_or) == 0:
                p.print_red_ts(f"Nessun hop nella riga {i}")
                continue
            # hop trovato!
            else:
                p.print_green_ts(f"Trovati due hop nella riga {i}")
                p.print_magenta_ts(f"Inzio controllo feasibility <Row {i}>")
                for k in range(len(hops_or)):
                    p.print_green_ts(f"Controllo hop n.{k+1}")
                    move = check_hop_row_feasibility(i, hops_or[k], matrice)
                    if move and isinstance(move, str):
                        p.print_magenta_ts("pass!")
                        send_input_gui(dizionario_movimenti[move])
                        mossa = True
                        break

        # CONTROLLO HOP VERTICALI
        if mossa != True:
            p.print_magenta_ts("    -->>Controllo hop colonne<<-- \n")
            for j in range(5):
                if mossa == True:
                    break
                hops_vert = check_hop_adj_col(matrice, j)
                if len(hops_vert) == 0:
                    p.print_red_ts(f"Nessun hop nella colonna {j}")
                    continue
                else:
                    p.print_green_ts(f"Trovati due hop nella colonna {j}")

                    for k in range(len(hops_vert)):
                        p.print_green_ts(f"Controllo coppia adiacenze n.{k+1}")
                        move2 = check_hop_column_feasibility(
                            hops_vert[k], j, matrice)
                        if move2 and isinstance(move2, str):
                            p.print_magenta_ts("pass!")
                            send_input_gui(dizionario_movimenti[move2])
                            mossa = True
                            break
        if mossa != True:
            p.print_red_ts("NESSUNA MOSSA VALIDA ---> CHECK: scan_matrice\n")


# Funzione che passata un img aperta con opencv2, restituisce una matrice di immagini ritagliate


def matrix_from_img(img, delay=200, open_img=False):
    # Dimnensione immagine
    altezza_immagine, larghezza_immagine, _ = img.shape

    # Calcola le dimensioni delle celle nella tua nuova griglia
    larghezza_cella = larghezza_immagine // num_colonne
    altezza_cella = altezza_immagine // num_righe

    coordinate_celle = []

    matrice_immagini = [
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for riga in range(num_righe):
        for colonna in range(num_colonne):
            # Calcola le coordinate della cella corrente
            x1 = colonna * larghezza_cella
            y1 = riga * altezza_cella
            x2 = x1 + larghezza_cella
            y2 = y1 + altezza_cella

            # Aggiungi le coordinate alla lista
            coordinate_celle.append((x1, y1, x2, y2))

            # Ritaglia la cella dall'immagine
            cell_img = img[y1:y2, x1:x2]
            # cv2.imshow("Cella Ritagliata", cell_img)
            # cv2.waitKey(2000)
            matrice_immagini[riga].append(cell_img)

    if (open_img):
        cont = 1
        for i in range(num_righe):
            for j in range(num_colonne):
                cv2.imshow(f"Immagine {cont}",
                           matrice_immagini[i][j])
                cv2.waitKey(delay)
                cont += 1
        cv2.destroyAllWindows()

    return matrice_immagini


# MAIN
if (__name__ == '__main__'):
    scan_matrice(mm6)