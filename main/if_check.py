def valid_bound(i, j):
    if ((i >= 0 and i <= 5) and (j >= 0 and j <= 4)):
        print(f"[  i={i} e j={j}  ]")
        return True
    print("(((Elemento out of bounds)))")
    return False


i = 2
j = 5

if valid_bound(i, j):
    print("ERRORE")
