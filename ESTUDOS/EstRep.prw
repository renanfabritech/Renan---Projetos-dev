#include 'protheus.ch'
#include 'parmtype.ch'
#include 'prtopdef.ch'

user function estrep()
/*
    Local nCout
    Local nNum := 0

        For nCount := 0
        to 10 
        step 2;
        nNum += nCount
        Next
        Alert("Valor: "+ cValToChar(nNUm))
*/
//EXEMPLO DO COMANDO WHILE ENDDO
/*Local nNum1 := 0
Local nNum2 := 10

while nNum1 < nNum2
nNum++

ENDDO  
    Alert(nNum1 + nNum2)
*/

	Local nNum1 := 1
	Local cNome := "RCTI"

	while nNum1 := .AND. cNome := "PROTHEUS"
		nNum++
		if nNum1 == 5
			cNome := "PROTHEUS"

		ENDIF
	ENDDO
	Alert("Numero: "+ cValtochar(nNum1))
	Alert("Nome: "+ cValtochar(cNome))
Return
