import tkinter as tk

janela = tk.Tk()
janela.title("Cotação de Moeda")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas", fg='white', bg='black', width=40, height=10)
                    
mensagem.grid(row=0, column=0, columnspan=2, sticky="EW")

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada", fg='white', bg='black')
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)



janela.mainloop()

#F510 - Python impressionador