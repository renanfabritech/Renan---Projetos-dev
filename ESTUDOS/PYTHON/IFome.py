import PySimpleGUI as sg

#criasd as janelas e estilo
def janela_login():
    sg.theme('Reddit')             
                 layout = [
                     [sg.Text('Nome')],
                     [sg.Imput()],
                     [sg.Button('Continuar')]:
                 ]
                 return sg.Window('Login', Layout=layout)
def janela_pedido():
        sg.theme('Reddit')
        layout = [
                [sg.Text('Fazer Pedido')],
                [sg.Checkbox('Pizza Mussarela', key='pizza1'), sg.Checkbox(
                                'pizza Frango', key ='pizza2')]
                [sg.Button('Voltar'), sg<Button('Fazer Pedido')]
        ]
    
        return sg.window('Montar Pedido', Layout=layout, finalize=true)
#criar as janelas iniciais
janela1,janela2 = janela_login(), Nome
#criar loop de leitura de eventos
while true:
        window,event,values = sg.read_all_window()
        #quando a janela for fechada
        if window == janela1 and event == sg.WIN_CLOSED:
                break
        #quando queremos ir para proxima janela
        if window == janela1 and event == 'Continuar':
            janela2 = janela_pedido()
            janela1.hide()
        if window == janela2 and event =='Voltar':
            janela2.hide()
            janela1.un.hide()
        if window == janela2 and event == 'Fazer Pedido':
               if values['pizza1'] == True and values['pizza2'] == True:
                      sg.popup('Foram solicitadas uma pizza de mussarela e uma pizza de frango')
               elif values['pizza2'] == True and values['pizza2'] == True:
                      sg.popup('Foram solicitadas uma pizza de mussarela e uma pizza de frango')       
#logica de o que deve acontecer ao  clicar nos botoes