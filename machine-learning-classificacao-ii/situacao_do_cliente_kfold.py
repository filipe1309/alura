from collections import Counter
from sklearn.cross_validation import cross_val_score
import numpy as np
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

treino_dados = X[0:tamanho_de_treino]
treino_marcacoes = Y[0:tamanho_de_treino]

validacao_dados = X[tamanho_de_treino:]
validacao_marcacoes = Y[tamanho_de_treino:]

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes):
	k = 10
	# faz o fit adn predict variando os treinos e testes de acordo com a variavel k
	scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv = k)
	# taxa de acerto = media dos scores
	taxa_de_acerto = np.mean(scores)

	msg = "Taxa de acerto do {0}: {1}".format(nome, taxa_de_acerto)
	print msg
	return taxa_de_acerto

resultados = {}

from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state = 0))
resultadoOneVsRest = fit_and_predict("OneVsRest", modeloOneVsRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVsRest] = modeloOneVsRest

from sklearn.multiclass import OneVsOneClassifier
modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state = 0))
resultadoOneVsOne = fit_and_predict("OneVsOne", modeloOneVsOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVsOne] = modeloOneVsOne

from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes)
resultados[resultadoMultinomial] = modeloMultinomial

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoost] = modeloAdaBoost

print resultados

maximo = max(resultados)
vencedor = resultados[maximo]

print "Vencedor: "
print vencedor

vencedor.fit(treino_dados, treino_marcacoes)
resultado = vencedor.predict(validacao_dados)

acertos = (resultado == validacao_marcacoes)
# diferencas = resultado - teste_marcacoes

# acertos = [d for d in diferencas if d == 0]
total_de_acertos = sum(acertos)
total_de_elementos = len(validacao_marcacoes)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
print(msg)



# a eficacia do algoritmo que chuta tudo um unico valor
acerto_base = max(Counter(validacao_marcacoes).itervalues())
# acerto_de_um = list(Y).count('sim') # len(Y[Y==1]) # sum(Y)
# acerto_de_zero = list(Y).count('nao') # len(Y[Y==0]) # len(Y) - acerto_de_um
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)
print("Total de testes %d" % len(validacao_dados))
