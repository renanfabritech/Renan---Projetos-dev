#include 'parmtype.ch'
#include 'protheus.ch'
//#include 'prtopdef.ch'

user function BLOCO()

    //Local bBloco := {|| Alert("Ol� Mundo")}
    //    Eval(bBloco)

    //passagem por parametro - bloco de notas
    Local bBloco := {|cMsg| Alert(cMsg)}
        Eval(bBloco,"Ol� mundo")

return
