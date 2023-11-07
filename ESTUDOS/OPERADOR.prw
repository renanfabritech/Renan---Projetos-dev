#include 'protheus.ch'
#include 'parmtype.ch'

User Function OPERADOR()

    Local nNum1 := 10
    Local nNum2 := 20

    //Alert(nNum1 + nNum2)
    //Alert(nNum2 - nNum1)
    //Alert(nNum1 * nNum2)
    //Alert(nNum2 / nNum1)
    //Alert(nNum2 % nNum)

//OPERADORES RELACIONAIS
    Alert(nNum1 < nNum2)
    Alert(nNum1 > nNum2)
    Alert(nNum1 = nNum2)
    Alert(nNum1 == nNum2) // == Exatamente igual
    Alert(nNum1 <= nNum2)
    Alert(nNum1 >= nNum2)
    Alert(nNum1 != nNum2) // != Diferença

//OPERADORES DE ATRIBUIÇÃO
    nNum1 := 10
    nNum1 += nNum2
    nNum1 -= nNum2
    nNum1 *= nNum2
    nNum1 /= nNum2
    //nNum1 %= nNum2

Return
