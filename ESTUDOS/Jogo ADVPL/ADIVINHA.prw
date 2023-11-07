#include 'protheus.ch'
#include 'parmtype.ch'

user function ADIVINHA()
	Local nNum := Randomize(1,100)
	Local nChute := 0
    Local nTent := 0

	while nChute != nNum
		nChute := Val(FwInputBox("Escolha um numero[1 - 100]",""))
		//Alert(cValToChar(nChute))
		if nChute == nNum
			MsgInfo("Acertou - <b>"+ cValToChar(nChute)+"</b><br>ERROS: "+ cValToChar(nTent),"Fim do Jogo")
		ElseIf nChute > nNum
			MsgAlert("Valor alto","Tente novamente")
            nTent += 1
		else
			MsgAlert("Valor baixo","Tente novamente")
            nTent += 1
		EndIf

return
