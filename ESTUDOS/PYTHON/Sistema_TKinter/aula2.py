import tkinter as tk

janela = tk.Tk()
janela.title("Cotação de Moeda")
mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas", 
                    fg='white', bg='black', width=40, height=10)
mensagem.pack()

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada", 
                    fg='white', bg='black', width=40, height=10)
mensagem2.pack()

janela.mainloop()

#F508 - Python impressionador