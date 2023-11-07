#include 'protheus.ch'
#include 'parmtype.ch'

    static cStatic :=''

user function ESCOPO1()
    //Varieveis locais
    Local nVar0 := 1
    Local nVar1 := 20

    //variaveis private
    Private CPri := 'private!'

    //variavel public
    Public __cPublic := 'RCTI'

    TestEscop(nVar0, @nVar1)

Return
//--------------Função Static

static Function TestEscop(nValor1, nValor2)

    Local __cPublic := 'Alterei'
    Default nValor1 := 0

    //Alterando conteudo da variavel
    nValor2 := 10

    //Mostrar conteudo da variavel private
    Alert("Private: "+ cPri)

    //Alterar o valor da variavel public
    Alert("Publica: "+ __cPublic)

    MsgAlert(nValor2)
    Alert("Variavel Static: "+ cStatic)
