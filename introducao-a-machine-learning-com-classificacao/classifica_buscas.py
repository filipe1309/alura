from collections import Counter

# using panda data analysis - sudo pip install pandas --upgrade
import pandas as pd

# initial tests: home, busca, logado => comprou
# home, busca
# home, logado
# busca, logado
# busca => 85.71% (7 tests)

# data frame
df = pd.read_csv('busca.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df);
Ydummies_df = Y_df;

X = Xdummies_df.values
Y = Ydummies_df.values

# 90% train, 10% test
#porcentagem_de_treino = 0.9

porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1
tamanho_de_treino = int(porcentagem_de_treino * len(Y))
#tamanho_de_teste = int(len(Y) - tamanho_de_treino)
tamanho_de_teste = porcentagem_de_teste * len(Y)
tamanho_de_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste

#treino_dados = X[:tamanho_de_treino]
#treino_marcacoes = Y[:tamanho_de_treino]

#teste_dados = X[-tamanho_de_teste:]
#teste_marcacoes = Y[-tamanho_de_teste:]

# 0 - 799
treino_dados = X[0:tamanho_de_treino]
treino_marcacoes = Y[0:tamanho_de_treino]

# 800 - 899
fim_de_teste = int(tamanho_de_treino + tamanho_de_teste)
teste_dados = X[tamanho_de_treino:fim_de_teste]
teste_marcacoes = Y[tamanho_de_treino:fim_de_teste]

# 900 - 999
validacao_dados = X[fim_de_teste:]
validacao_marcacoes = Y[fim_de_teste:]

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
	modelo.fit(treino_dados, treino_marcacoes)

	resultado = modelo.predict(teste_dados)
	acertos = (resultado == teste_marcacoes)
	# diferencas = resultado - teste_marcacoes

	# acertos = [d for d in diferencas if d == 0]
	total_de_acertos = sum(acertos)
	total_de_elementos = len(teste_dados)
	taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

	msg = "Taxa de acerto do algoritmo: {0}: {1}".format(nome, taxa_de_acerto)
	print(msg)
	return taxa_de_acerto


from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)


if resultadoMultinomial > resultadoAdaBoost:
	vencedor = modeloMultinomial
else:
	vencedor = modeloAdaBoost

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
acerto_base = max(Counter(teste_marcacoes).itervalues())
# acerto_de_um = list(Y).count('sim') # len(Y[Y==1]) # sum(Y)
# acerto_de_zero = list(Y).count('nao') # len(Y[Y==0]) # len(Y) - acerto_de_um
taxa_de_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)
print("Total de testes %d" % len(teste_dados))