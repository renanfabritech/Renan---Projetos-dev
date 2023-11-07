#include 'protheus.ch'
#include 'parmtype.ch'
#include 'topconn.ch'

user function banco003()
    
    Local aArea := SB1->(GetArea()) //vetor aArea
    Local cQuery := ""              // variavel cQuery
    Local aDados := ()              // retorno

    cQuery := " SELECT "
    cQuery += " B1_COD AS CODIGO, "
    cQuery += " B1_DESC AS DESCRICAO "
    cQuery += " FROM "
    cQuery += " "+ RetSQLName("SB1")+ "SB1"
    cQuery += " WHERE "
    cQuery += " B1_MSBLQL != '1' "

    //Executando a consulta acima
    TcQuery cQuery New Alias "TMP"

    while ! TMP->(EoF())
        AADD(aDados, TMP->CODIGO)
        AADD(aDados, TMP->DESCRICAO)
        TMP->(DbSkip())
    EndDo 

        Alert(Len(aDados))

        For nCount := 1 to Len(aDados)
            MsgInfo(aDados(nCount))
        Next nCount
        
        TMP->(DbCloseArea())
        RestArea(aArea)


return
