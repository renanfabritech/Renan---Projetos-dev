import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail promocionais?", variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceitar termos de uso e politicas de privacidade", variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)

def enviar():
    print(var_promocoes.get())
    if var_promocoes.get():
        print('usuário deseja receber promoções')
    else:
        print('usuário não deseja receber promoções')
    
    if var_politicas.get():
        print('Usuário concordou com os termo de uso e politicas de privacidade')
    else:
        print('Usuário não concordou')

botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()

#F695 - Python impressionador 