#include 'protheus.ch'
#include 'parmtype.ch'
#include 'topconn.ch'

#DEFINE STR_PULA Chr(13)+Chr(10)

/*/{Protheus.doc} mSQLM5BX
Fun��o para consulta gen�rica - cria tela de exibi��o com pesquisa. Permite copiar c�lulas e exportar os dados para arquivo .xml
@author Maicon Macedo
@since 27 jan. 2020
@version 1.0
/*/

User Function mSQLM5BX(cQryZZS,cQryCnd)
	Local cAlias				:= GetNextAlias()
	//Default
	Default cQryZZS		:= ""
	Default cQryCnd		:= ""
	//Private
	Private cConsulta	:= cQryZZS
	Private cCondicao	:= cQryCnd
	Private cQuery			:= ""
	Private cPsqusa		:= ""
	Private cGrpOd		:= ""
	
	BeginSQL Alias cAlias
			SELECT
				ZZS.ZZS_CODE ,
				ZZS.ZZS_TBMAIN ,
				ZZS.ZZS_CPESQ ,
				ISNULL(CONVERT (VARCHAR(8000), CONVERT (VARBINARY(8000), ZZS.ZZS_QUERY) ),'') ZZS_QUERY ,
				ISNULL(CONVERT (VARCHAR(8000), CONVERT (VARBINARY(8000), ZZS.ZZS_CNDCAO) ),'') ZZS_CNDCAO  ,
				ISNULL(CONVERT (VARCHAR(8000), CONVERT (VARBINARY(8000), ZZS.ZZS_ORDER) ),'') ZZS_ORDER 
			FROM
				%table:ZZS% ZZS
			WHERE
				ZZS.D_E_L_E_T_  = ' ' AND ZZS.ZZS_CODE = %Exp:cConsulta%
	EndSQL
	
	cQuery	:= (cAlias)->ZZS_QUERY
	cQuery	+= STR_PULA
	cQuery 	+= cCondicao
	
	cPsqusa	:= (cAlias)->ZZS_CPESQ
	cGrpOd	:= (cAlias)->ZZS_ORDER

	(cAlias)->(DbCloseArea())
	
	MnTTela(cQuery,cPsqusa,cGrpOd)
	
Return

Static Function MnTTela(cSentenca,cPesqui,cGrpOrd)
	Local aArea						:= GetArea()
	Local oAreaPesq
	Local oAreaDados
	Local oAreaAcao
	Local nTamBtn					:= 60
	Local oBtnExcl
	Local oBtnLimp
	Local oBtnFchr
	Local nPos							:= 0
	//Default
	DEFAULT cSentenca		:= ""
	DEFAULT cPesqui 			:= ""
	DEFAULT cGrpOrd			:= ""
	//Private
	Private cConsSQL			:= cSentenca
	Private cPsqsaSQL			:= cPesqui
	Private cOrdrsQL			:= cGrpOrd
	Private aEstrutr				:= {} // Estrutura da Grid - baseada na consulta QRY_TMP
	Private cQryNm				:= ""
	//MsDialog - por inteiro
	Private oDltTela
	Private nTelaLarg			:= 1000
	Private nTelaAltu				:= 0600
	//Area Pesquisa
	Private oGetPesq			:= Space(100)
	Private cGetPesq			:= Space(100)
	//Area dos Dados
	Private oMSNew	
	Private aCabecAux			:= {}
	Private aColsAux				:= {}
	Private aCombo				:= {}
	Private cCombo1			:= ""
	
	//Chama a montagem da Estrutura do MSDialog na Area de Dados
	MnTEstr()
	
	DEFINE MSDIALOG oDlgTela TITLE "Consulta de Dados - "+cConsulta FROM 000, 000 TO nTelaAltu, nTelaLarg COLORS 0, 16777215 PIXEL STYLE DS_MODALFRAME
		@ 003,003 GROUP oAreaPesq TO 025, (nTelaLarg/2)-3 PROMPT "Pesquisar:" OF oDlgTela COLOR 0, 16777215 PIXEL
		
			FOR nPos := 1 To Len(aCabecAux)
				cCampoAtu := aCabecAux[nPos][1]
				Aadd( aCombo, cCampoAtu )
			NEXT
		@ 010,006 COMBOBOX cCombo1 ITEMS aCombo SIZE (nTelaLarg/2)-450,010 OF oDlgTela PIXEL
		@ 010,060 MSGET oGetPesq VAR cGetPesq SIZE (nTelaLarg/2)-72, 010 OF oDlgTela COLORS 0, 16777215 VALID (VldPesq()) PIXEL
		
		@ 028,003 GROUP oAreaDados TO (nTelaAltu/2)-28, (nTelaLarg/2)-3 PROMPT "Dados: " OF oDlgTela COLOR 0, 16777215 PIXEL
			oMSNew := MsNewGetDados():New(	035, 006,;
																					(nTelaAltu/2)-31,;
																					(nTelaLarg/2)-6,;
																					GD_INSERT+GD_DELETE+GD_UPDATE,;
																					"AllwaysTrue()",;
																					,"", , , ; //cTudoOk , Inici Campos, Alteracao, Congelamento
																					999,;
																					, , , ; // Campo Ok, Super Del, Delete
																					oDlgTela,;
																					aCabecAux,;	// Array do Cabe�alho
																					aColsAux	)	// Array das Colunas
			oMSNew:lActive := .F.
			
			PopDados()
			
		@ (nTelaAltu/2)-25, 003 GROUP oAreaAcao TO (nTelaAltu/2)-3 , (nTelaLarg/2)-3 PROMPT "A��es: " OF oDlgTela COLOR 0, 16777215 PIXEL
			@ (nTelaAltu/2)-19, (nTelaLarg/2)-((nTamBtn*1)+06) BUTTON oBtnExcl PROMPT "Exportar"		SIZE nTamBtn, 013	OF oDlgTela ACTION (GeraExcel()) 	PIXEL
			@ (nTelaAltu/2)-19, (nTelaLarg/2)-((nTamBtn*2)+09) BUTTON oBtnLimp PROMPT "Resetar"		SIZE nTamBtn, 013	OF oDlgTela ACTION (btReset()) 	PIXEL
			@ (nTelaAltu/2)-19, (nTelaLarg/2)-((nTamBtn*3)+12) BUTTON oBtnFchr PROMPT "Fechar"			SIZE nTamBtn, 013	OF oDlgTela ACTION (btFecha()) 	PIXEL
			
		oMSNew:oBrowse:SetFocus()
		
	ACTIVATE MSDIALOG oDlgTela CENTERED
	
	RestArea(aArea)
			
Return

/*---------------------------------------------------------------------------------------------------------*
*	MnTEstr - Montagem da tela de dados
*---------------------------------------------------------------------------------------------------------*/
Static Function MnTEstr()
	Local aAreaX3		:= SX3->(GetArea())
	Local cQuery		:= ""
	Local nAtual			:= 0

	//Definir como zero os valores das Colunas e do Cabe�alho
	aCabecAux 	:= {}
	aColsAux		:= {}
	
	//Senten�a SQL = SELECT + FROM + WHERE + GROUP BY / ORDER BY
	cQuery := cConsSQL + " " + cOrdrSQL
	
	If Select ("QRY_TMP") <> 0
		DbSelectArea("QRY_TMP")
		DbCloseArea()
	EndIf
	
	TCQuery cQuery New Alias "QRY_TMP"
	
	aEstrutr := QRY_TMP->(DbStruct())
	
	QRY_TMP->(DbCloseArea())
	
	DbSelectArea("SX3")
	SX3->(DbSetOrder(2))
	SX3->(DbGoTop())
	
	For nAtual := 1 To Len(aEstrutr)
		cCampoAtu := aEstrutr[nAtual][1]
		
		If SX3->(DbSeek(cCampoAtu))
			aAdd(aCabecAux, { X3Titulo(),;
												cCampoAtu,;
												PesqPict(SX3->X3_ARQUIVO, cCampoAtu),;
												SX3->X3_TAMANHO,;
												SX3->X3_DECIMAL,;
												".F.",;
												".F.",;
												SX3->X3_TIPO,;
												"",;
												"" 	}	)
		Else
			aAdd(aCabecAux, { Capital(StrTran(cCampoAtu, '_', ' ')),;
												cCampoAtu,;
												"",;
												aEstrutr[nAtual][3],;
												aEstrutr[nAtual][4],;
												".F.",;
												".F.",;
												aEstrutr[nAtual][2],;
												"",;
												"" 	}	)
		EndIf
	
	Next
	
	RestArea(aAreaX3)

Return

/*---------------------------------------------------------------------------------------------------------*
*	Fun��o PodDados - para popular os dados da grid da tela
*---------------------------------------------------------------------------------------------------------*/
Static Function PopDados()
	Local cQuery			:= ""
	Local cPesq				:= ""
	Local cOrdr				:= ""
	Local nAtual				:= 0
	Local nCampAux		:= 1
	Local nPos					:= 0
	Private cQrySQL		:= GetNextAlias()
	
	cQryNm := cQrySQL
	
	aColsAux	:= {}
	
	cQuery	:= cConsSQL + STR_PULA
	cOrdr		:= cOrdrSQL
	
	If !Empty(cGetPesq)
		If 'WHERE' $ cQuery
			cQuery += " AND "
		Else
			cQuery += " WHERE "
		EndIf
		
		nPos := aScan( aCabecAux , {|x| AllTrim(UPPER(x[1])) == UPPER(cCombo1)  } )
		
		cPesq := aCabecAux[nPos][2]
		
		cQuery += " (UPPER(" + cPesq + ") LIKE '%" + UPPER(AllTrim(cGetPesq)) + "%' )" + STR_PULA
		
		cQuery += cOrdr
	Else
		cQuery += STR_PULA + cOrdr
	EndIf
	
	cQuery := ChangeQuery(cQuery)
	
	dbUseArea(.T.,"TOPCONN",TcGenQry(,,cQuery),cQrySQL,.T.,.T.)
	
	//Tratamento da exibi��o dos campos de Data e N�meros
	For nAtual := 1 to Len(aCabecAux)
		If aCabecAux[nAtual][8] == "D"
			TcSetField(cQrySQL, aCabecAux[nAtual][2],'D')
		ElseIf aCabecAux[nAtual][8] == "N"
			TcSetField(cQrySQL, aCabecAux[nAtual][2],'N', aCabecAux[nAtual][4],aCabecAux[nAtual][5])
		EndIf
	Next
	
	While (cQrySQL)->(!EoF())
		nCampAux := 1
		aAux	:= {}
		
		For nAtual := 1 To Len(aEstrutr)
			cCampoAtu := aEstrutr[nAtual][1]
			
			If aEstrutr[nAtual][2] $ "N;D"
				aAdd(aAux, &( (cQrySQL)->(cCampoAtu) ) )
			Else
				aAdd(aAux, cValToChar( &( (cQrySQL)->(cCampoAtu)  ) ) )
			EndIf		
		Next
		aAdd(aAux, .F. )
		
		aAdd(aColsAux, aClone(aAux) )
		
		(cQrySQL)->(DbSkip() )
	
	EndDo
	
	// Caso a senten�a n�o retorne dado nenhum = passar linhas em branco
	If Len(aColsAux) == 0
		aAux := {}
		
		For nAtual := 1 To Len(aEstrutr)
			aAdd(aAux, '')
		Next
		
		aAdd(aAux, .F. )
		
		aAdd(aColsAux, aClone(aAux) )
		
	EndIf
	
	oMSNew:SetArray(aColsAux)
	oMSNew:oBrowse:Refresh()
	
Return

/*---------------------------------------------------------------------------------------------------------*
*	
*---------------------------------------------------------------------------------------------------------*/
Static Function GeraExcel()
	Local oExcel			:= FWMSEXCEL():New()
	Local lOk				:= .F.
	Local cArq				:= ""
	Local cDirTmp		:= "C:\temp\"
	Local nAtual			:= 0
	Local aCampos		:= {}
	Local lDirOk			:= .F.
	
	dbSelectArea(cQryNm)
	(cQryNm)->(dbGoTop())
	
	//Atribuindo fortama��o ao Excel
	//https://html-color.codes
	oExcel:SetTitleSizeFont(12)
	oExcel:SetTitleBold(.T.)
	oExcel:SetTitleFrColor("#2200fc")
	oExcel:SetTitleBgColor("#adadad")
	oExcel:SetFontSize(11)
	oExcel:SetFont("Calibri")
	
	oExcel:AddWorkSheet(cConsulta)
	oExcel:AddTable(cConsulta,cConsulta)
	
	FOR nAtual := 1 To Len(aCabecAux)
		cCampoAtu := aCabecAux[nAtual][1]
		
		oExcel:AddColumn(cConsulta,cConsulta,cCampoAtu,1,1)
	NEXT
	
	While (cQryNm)->(!EoF())
		aCampos := {}
		
		For nAtual := 1 To Len(aCabecAux)
			cCampoAtu := aCabecAux[nAtual][2]
			Aadd( aCampos, & ( (cQryNm)->(cCampoAtu)  ) ) 
		Next
		
		oExcel:AddRow(cConsulta,cConsulta,aCampos)
		
		lOk := .T.
		
		(cQryNm)->(DbSkip())
	
	EndDo
	
	oExcel:Activate()
	
	cArq := cConsulta + "_" + CriaTrab(NIL, .F.) + ".xml"
	
	oExcel:GetXMLFile(cArq)
	
		If ExistDir(cDirTmp,nil, .F.) == .F.
				If MsgYesNo("Diretorio - "+cDirTmp+" - nao encontrado, deseja cria-lo?" ) 
					If  MakeDir(cDirTmp) <> 0
						MsgInfo("Falha ao criar diret�rio " + cDirTmp + " ! Erro: " + cValToChar( FError() )  , "Diret�rio")
					Else
						MsgInfo("Diret�rio " + cDirTmp + " criado com sucesso!" , "Diret�rio")
						lDirOk = .T.
					EndIf
				Else
					MsgInfo("O diret�rio " + cDirTmp + " n�o foi criado!" , "Diret�rio")
				EndIf
		Else
			lDirOk = .T.
		EndIF

	If lDirOk
		If __CopyFile(cArq,cDirTmp + cArq)
			If lOk
				oExcelApp := MSExcel():New()
				oExcelApp:WorkBooks:Open(cDirTmp + cArq)
				oExcelApp:SetVisible(.T.)
				oExcelApp:Destroy()
				
			MsgInfo("O arquivo "+ cArq+" foi gerado corretamente e se encontra no diret�rio: "+cDirTmp)
			EndIf
		Else
			MsgAlert("Erro ao copiar o arquivo!")
		EndIf
	Else
		MsgAlert("Erro ao copiar o arquivo! O Diret�rio n�o existe.")
	EndIf


Return Nil

/*---------------------------------------------------------------------------------------------------------*
*	
*---------------------------------------------------------------------------------------------------------*/
Static Function btReset()
	cGetPesq := Space(100)
	oGetPesq:Refresh()
	
	PopDados()
	
	oGetPesq:SetFocus()
Return

/*---------------------------------------------------------------------------------------------------------*
*	
*---------------------------------------------------------------------------------------------------------*/
Static Function btFecha()
	
	(cQryNm)->(DbCloseArea())
	
	oDlgTela:End()
Return

/*---------------------------------------------------------------------------------------------------------*
*	
*---------------------------------------------------------------------------------------------------------*/
Static Function VldPesq()
	Local lRet := .T.
	
	If "'" $ cGetPesq .Or. "%" $ cGetPesq
		lRet := .F.
		MsgAlert("<b>Pesquisa inv�lida!</b><br>A pesquisa n�o pode conter os carateres <b>'</b> ou <b>%</b>.", "Pesquisa inv�lida")
		
		cGetPesq := Space(100)
		oGetPesq:Refresh()
		oGetPesq:SetFocus()
	EndIF
	
	If lRet
		PopDados()
	EndIf
Return lRet