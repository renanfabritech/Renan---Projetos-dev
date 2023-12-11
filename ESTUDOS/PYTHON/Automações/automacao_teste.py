import time
import pyautogui
import pygetwindow as gw

# Constantes para coordenação
EXCEL_CELL_START = (100, 100)
EXCEL_CELL_HEIGHT = 20

def abrir_aplicativo(aplicativo):
    try:
        app_window = gw.getWindowsWithTitle(aplicativo)[0]
        app_window.activate()
    except IndexError:
        print(f"O aplicativo {aplicativo} não está aberto. Abrindo...")
        pyautogui.hotkey("win", "s")  # Abre a barra de pesquisa no Windows
        time.sleep(1)
        pyautogui.write(aplicativo, interval=0.1)
        pyautogui.press("enter")
        wait_for_window(aplicativo)

def wait_for_window(title, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            gw.getWindowsWithTitle(title)[0]
            return
        except IndexError:
            time.sleep(1)
    raise TimeoutError(f"Timeout esperando pela janela: {title}")

def escrever_no_excel():
    abrir_aplicativo("Excel")
    wait_for_window("Excel")
    
    # Simular o preenchimento das 10 primeiras linhas
    for linha in range(1, 11):
        pyautogui.click(EXCEL_CELL_START[0], EXCEL_CELL_START[1] + (linha - 1) * EXCEL_CELL_HEIGHT)
        pyautogui.write(f"Texto na linha {linha}", interval=0.1)

def escrever_na_tese():
    abrir_aplicativo("Word")
    wait_for_window("Word")
    
    # Simular a escrita detalhada na tese
    texto_tese = """
    Elaborar uma tese completa sobre a ciência da computação envolveria uma análise aprofundada de um tópico específico dentro dessa vasta disciplina. Dado que não tenho informações específicas sobre o tema de interesse, vou propor uma estrutura geral que você pode adaptar de acordo com o foco desejado. Lembre-se de que uma tese geralmente inclui os seguintes elementos:

Introdução:

Contextualização do tema.
Declaração clara do problema de pesquisa.
Justificativa da relevância do estudo.
Formulação de perguntas de pesquisa e/ou hipóteses.
Revisão da Literatura:

Análise crítica de pesquisas anteriores relacionadas ao tema.
Identificação de lacunas no conhecimento existente.
Estabelecimento do embasamento teórico.
Metodologia:

Descrição detalhada dos métodos utilizados para coletar dados.
Justificativa das escolhas metodológicas.
Discussão sobre a validade e confiabilidade dos métodos.
Desenvolvimento/Implementação:

Apresentação dos resultados obtidos.
Detalhes sobre o desenvolvimento prático, se aplicável.
Análise crítica dos resultados à luz das questões de pesquisa.
Discussão:

Interpretação dos resultados em relação à literatura existente.
Exploração de implicações práticas e teóricas.
Discussão de limitações do estudo e possíveis áreas de melhoria.
Conclusão:

Recapitulação dos principais achados.
Resposta às perguntas de pesquisa.
Sugestões para pesquisas futuras.
Referências:

Lista completa de todas as fontes citadas ao longo da tese.
Lembre-se de que o conteúdo específico de cada seção dependerá do tema escolhido. 
Pode ser útil consultar exemplos de teses acadêmicas na área de ciência da computação 
para obter insights sobre estrutura e estilo. Além disso, adaptar-se às diretrizes 
.
Reespecíficas da sua instituição de ensino ou orientador é fundamental.
    """

    pyautogui.write(texto_tese, interval=0.1)

if __name__ == "__main__":
    escrever_no_excel()
    escrever_na_tese()
