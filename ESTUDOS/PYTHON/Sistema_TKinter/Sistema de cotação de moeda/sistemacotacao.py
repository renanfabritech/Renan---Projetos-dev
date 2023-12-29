import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry
from datetime import datetime
import pandas as pd
import requests
import numpy as np

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all') #last/:moedas
dicionario_moedas = requisicao.json()
#print(dicionario_moedas)
lista_moedas = list(dicionario_moedas.keys())

def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}"
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f"A cotação da moeda {moeda} no dia {data_cotacao} foi de R${valor_moeda}"

def selecionar_arquivo():
   caminho_arquivo = askopenfilename(title="Selecione o arquivo de moeda")
   var_caminhoarquivo.set(caminho_arquivo)
   if caminho_arquivo:
       label_arquivoselecionado['text'] = f"Arquivo selecionado: {caminho_arquivo}"

def atualizar_cotacoes():
    # Ler o dataframe de moeda
    df = pd.read_excel(var_caminhoarquivo.get())
    moedas = df.iloc[:, 0]
    # Pegar a data inicio e data fim das cotações
    data_inicial = calendario_datainicial.get()
    data_final = calendario_datafinal.get()
    ano_inicial = data_inicial[-4:]
    mes_inicial = data_inicial[3:5]
    dia_inicial = data_inicial[:2]
    
    ano_final = data_final[-4:]
    mes_final = data_final[3:5]
    dia_final = data_final[:2]
    
    for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano_inicial}{mes_inicial}{dia_inicial}&end_date={ano_final}{mes_final}{dia_final}"
            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d-%m-%y')  # ou outro formato desejado
                if data not in df:
                    df[data] = np.nan
                    
                df.loc[df.iloc[:, 0] == moeda, data] = bid
    df.to_excel("teste.xlsx")
    label_atualizarcotacoes['text'] = "Arquivo atualizado com sucesso"
    print(link)
                
            
    # Para cada moeda
        # Pegar todas as cotações daquela moeda
        # Criar uma coluna em um novo dataframe com todas as cotações daquela moeda
    # Criar um arquivo com todas as cotações
    


janela = tk.Tk()

janela.title('Ferramenta de cotação de moedas')

label_cotacaomoeda = tk.Label(text="Cotação de 1 moeda especifica", borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar moeda", borderwidth=2, relief='solid')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionardia = tk.Label(text="Selecione o dia que deseja pegar a cotação", borderwidth=2, relief='solid')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_pegarcotacao = tk.Button(text="Pegar cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

#Cotação de várias Moedas
label_cotacaovariasmoedas = tk.Label(text="Cotação de varias moedas", borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionararquivo = tk.Label(text="Selecione um arquivo em excel com as moedas nas coluna A")
label_selecionararquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivos = tk.Button(text="Clique aqui para selecionar", command=selecionar_arquivo)
botao_selecionararquivos.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivoselecionado = tk.Label(text="Nenhum aruivo selecionado", anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')

label_datainicial = tk.Label(text="Data inicial")
label_datafinal = tk.Label(text="Data final")
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

calendario_datainicial = DateEntry(year=2023, locale='pt_br')
calendario_datafinal = DateEntry(year=2023, locale='pt_br')

calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

botao_atualizarcotacoes = tk.Button(text="Atualizar cotações", command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text="fechar", command=janela.quit)
botao_fechar.grid(row=10, column=3, padx=10, pady=10, sticky='nswe')


janela.mainloop()

#F705 - Python impressionador | proximo #706