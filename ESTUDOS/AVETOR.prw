#include 'protheus.ch'
#include 'parmtype.ch'

user function AVETOR()

//Array s�o cole��es de valores, semelhantes a uma lista
//cada item em um array � referenciado pela indica�a�ao de sua posi��o numerica

Local dData := Date()
Local a Valores := {"Jo�o",dData,100}

Alert(aValores[2])//Existe a posi��o 2 do array
Alert(aValores[3])

return 
