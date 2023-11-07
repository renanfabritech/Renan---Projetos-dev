#include 'protheus.ch'
#include 'parmtype.ch'

user function Variavel()

    Local nNum := 66
    Local lLogic := .T.
    Local cCarac := "string"
    Local dData := DATE()
    Local aArray := {"Joao", "Maria", "Jose"}
    Local bBloco := {|| nValor := 2, MsgAlert("O numero e: "+ cValToChar(nValor))}

    Alert(nNum)
    Alert(lLogic)
    Alert(cValToChar(cCarac))
    Alert(dData)
    Alert(aArray[1])
    Eval(bBloco)

Return
