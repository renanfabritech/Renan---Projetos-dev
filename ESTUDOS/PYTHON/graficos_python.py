vendas_meses = [1500, 1727 , 1350 , 5214 , 9651, 5412, 6587, 54785, 4548, 85412, 54124, 887452]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

#plotar grafico
import matplotlib.pyplot as plt


plt.plot([vendas_meses])
plt.ylabel('LOJAS AMERICANAS')
plt.xlabel('VENDAS MESES')
plt.show()