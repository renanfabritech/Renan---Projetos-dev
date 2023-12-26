import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Cotação de Moeda")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas", fg='white', bg='black', width=40, height=10)
mensagem.grid(row=0, column=0, columnspan=2, sticky="EW")

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada", fg='white', bg='black')
mensagem2.grid(row=1, column=0)

dicionario_cotacoes = {
    'Dolar': 5.47,
    'Euro': 6.54,
    'BitCoin': 20000,
}

moedas = list(dicionario_cotacoes.keys())

moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(janela, text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'
    else:
        pass  # Exibir mensagem de cotação não encontrada

botao = tk.Button(janela, text="Buscar cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

mensagem3 = tk.Label(janela, text="Caso queira pegar mais de uma cotação ao mesmo tempo, digite uma moeda em cada linha")
mensagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(janela, width=10, height=5)
caixa_texto.grid(row=5, column=0, stick='nswe')

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}: {cotacao}')

    mensagem4 = tk.Label(janela, text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)

botao_multiplascotacoes = tk.Button(janela, text="Buscar cotações", command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=5, column=1)

janela.mainloop()


#F694 - Python impressionador 