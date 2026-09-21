import csv
import pathlib from pathlib

CAMINHO ="../pulsodavida/database/dados.csv"
import pandas as pd

def carregar_dados():
    dados = pd.read_csv(CAMINHO, sep=";")
    print("Dados carregados com sucesso!")
    return dados







def main(): 




    if __name__ == __main__:
        main()
