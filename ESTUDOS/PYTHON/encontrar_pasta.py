import os

def verifica_arquivo(caminho_arquivo):
    return os.path.exists(caminho_arquivo)

# Exemplo de uso
caminho_arquivo = "C:\Users\Renan\Documents\Fabritech\Fabritech"

if verifica_arquivo(caminho_arquivo):
    print(f"O arquivo {caminho_arquivo} existe.")
else:
    print(f"O arquivo {caminho_arquivo} não existe.")
