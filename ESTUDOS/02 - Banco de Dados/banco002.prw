#include 'protheus.ch'
#include 'parmtype.ch'

user function banco002()

    Local aArea := SB1->(GetArea)
    Local cMsg := ''

    DbSelectArea("SB1")
    SB1->(DbSetOrder(1))
    SB1->(DbGoTop())

    cMsg := Posiocne(   'SB1',;
                        1,;
                        FWXFilial('SB1')+'0010101002',;
                        'B1_DESC'    )
    Alert ("Descrição Produto: " +cMsg, "Aviso")

    RestArea(aArea)

return
