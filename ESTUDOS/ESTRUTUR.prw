#include 'protheus.ch'
#include 'parmtype.ch'

user function ESTRUTUR()

Local nNum1 := 22
Local nNum2 := 100
        
    if  (nNum1 = nNum2)
        MsgInfo("A variavel nNum1 é igual a nNum2")
    elseif (nNum1 > nNum2)
        MsgAlert("A variavel é maior")
    elseif (nNum1 != nNum2)
        Alert("A variavel nNUm1 é diferente de nNum2")
        
    Endif

Return
