import pandas as pd
import os 

# Importando os arquivos
caminho_padrao = r'C:\Users\renan.goncalves\Documents\Python\Python e BI'

# Lendo os arquivos CSV com tratamento de codificação
cotacao_df = pd.read_csv(os.path.join(caminho_padrao, r'teste.csv'), sep=';')
lucro_df = pd.read_csv(os.path.join(caminho_padrao, r'teste1.csv'), sep=';')

# Limpando apenas as colunas desejadas
#cotacao_df = cotacao_df[['moeda']]
#lucro_df = lucro_df[['cliente']]

# Mesclando e renomeando dataframes
result = pd.merge(cotacao_df, lucro_df, on='cliente')

# Visualizando as primeiras linhas do dataframe resultante
print(result.head())