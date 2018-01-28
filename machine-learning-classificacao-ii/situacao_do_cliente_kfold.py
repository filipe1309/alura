from collections import Counter

# using panda data analysis - sudo pip install pandas --upgrade
import pandas as pd

# data frame
df = pd.read_csv('situacao_do_cliente.csv')

X_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
Y_df = df['situacao']

Xdummies_df = pd.get_dummies(X_df);
Ydummies_df = Y_df;

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_de_treino = 0.8

tamanho_de_treino = int(porcentagem_de_treino * len(Y))
# tamanho_de_validacao = len(Y) - tamanho_de_treino

treino_dados = X[0:tamanho_de_treino]
treino_marcacoes = Y[0:tamanho_de_treino]

validacao_dados = X[tamanho_de_treino:]
validacao_marcacoes = Y[tamanho_de_treino:]


from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.cross_validation import cross_val_score
modelo = OneVsRestClassifier(LinearSVC(random_state=0))
k = 10
# faz o fit adn predict variando os treinos e testes de acordo com a variavel k
scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv = k)

print scores

import numpy as np
media = np.mean(scores)
print media