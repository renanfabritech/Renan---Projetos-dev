#include 'parmtype.ch'
#include 'protheus.ch'
//#include 'prtopdef.ch'

user function BLOCO()

    //Local bBloco := {|| Alert("Olá Mundo")}
    //    Eval(bBloco)

    //passagem por parametro - bloco de notas
    Local bBloco := {|cMsg| Alert(cMsg)}
        Eval(bBloco,"Olá mundo")

return
