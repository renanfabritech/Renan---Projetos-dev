#include 'protheus.ch'
#include 'parmtype.ch'

user function banco001()
    Local aArea := SB1->(GetArea())
    //Local cMsg := ""

    DbSelectArea("SB1")
    SB1->(DbSetorder(1)) //Posiciona no indice 1
    SB1->(DbGoTop())

    //posiciona o produto cod informado
    if SB1->(DbSeek(FWFilial("SB1")+ "010101002"))
        Alet(SB1->B1_DESC)

    EndIf

    RestArea(aArea)

return
