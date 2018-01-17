# using panda data analysis - sudo pip install pandas --upgrade
import pandas as pd
# data frame
df = pd.read_csv('busca.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df);
Ydummies_df = Y_df;

X = Xdummies_df.values
Y = Ydummies_df.values

# algoritmo burro que soh tem 1 como resposta, ou que chita somente 1, 
# e para contar os acertos, basta apenas efetuas a soma dos 1's da coluna de marcacoes 
total_de_acertos = sum(Y)
total_de_elementos = len(Y)

taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acertos)
print(total_de_elementos)