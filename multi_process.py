from multiprocessing import Process
import time

def worker(process_id):
    for _ in range(5):
        time.sleep(1)
        print(f"Processo {process_id} in esecuzione")

if __name__ == "__main__":
    # Numero di processi da avviare
    num_processes = 3

    # Lista per mantenere riferimenti ai processi
    processes = []

    # Avvia i processi
    for i in range(num_processes):
        # Crea un nuovo processo con la funzione worker
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Attendi che tutti i processi completino l'esecuzione
    for p in processes:
        p.join()

    print("Fine dello script")