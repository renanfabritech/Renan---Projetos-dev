#include 'protheus.ch'
#include 'parmtype.ch'

user function DoCase()

    Local cData := "22/05/1989"

    Do Case 

        Case cData == "14/06/1994"
            Alert("Não é meu anioversário")
        Case cData == "22/05/1989"
            Alert("É meu anioversário!  "+ cData)

            OtherWise 
            MsgAlert("Não sei que dia é hoje!")

    EndCase

Return
