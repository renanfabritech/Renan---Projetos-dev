#include 'protheus.ch'
#include 'parmtype.ch'

user function DoCase()

    Local cData := "22/05/1989"

    Do Case 

        Case cData == "14/06/1994"
            Alert("N�o � meu aniovers�rio")
        Case cData == "22/05/1989"
            Alert("� meu aniovers�rio!  "+ cData)

            OtherWise 
            MsgAlert("N�o sei que dia � hoje!")

    EndCase

Return
