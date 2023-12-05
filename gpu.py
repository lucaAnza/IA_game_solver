import torch

# Verifica la disponibilità della GPU e imposta il dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Dimensione dell'array
array_size = 1000000

# Genera un tensore casuale su GPU
gpu_tensor = torch.rand(array_size, device=device)

# Esegui la somma
result = torch.sum(gpu_tensor)

# Trasferisci il risultato dalla GPU alla CPU se necessario
result_cpu = result.cpu().item()

# Stampare il risultato
print("Risultato della somma sulla GPU:", result_cpu)
print(device)
