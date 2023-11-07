
#include 'parmtype.ch'
#include 'protheus.ch'
#include 'prtopdef.ch'

user function AVETOR2()

Local aVetor := (10,20,30)

//AADD() - Permite inserir a inserção de um item em um array ja existente
//AINS() - Permite a inserção de um lemento em qualquer posição do array
//ACLONE() - Realiza a cópia de um array para outro
//ADEL() - Permite a exclusão de um elemento do array, tornando o ultima valor NULL
//ASIZE() - Redefine a estrutura de uma array pre-existente, adiconando ou removendo
//LEN() - Retorna a quantidade de elementos de um array

    //AaDd(aVetor,40)
    //Alert(Len(aVetor))

    //AIns(aVetor,2)
    //aVetor[2] := 200
    //Alert(aVetor[2])
    //Alert(Len(aVetor))

/*
    aVetor2 := AClone(aVetor)
        For nCount :=1 to len(aVetor2)
            Alert(aVetor2(nCout))
*/
/*
    Adel (aVetor2)
    Alert(aVetor[3])
    Alert(Len(aVetor))
*/

    Asize (aVetor,2)
    Alert(Len(aVetor))
