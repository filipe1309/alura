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



from sklearn.multiclass import OneVsRestClassifier
# rodar o algoritmo de claficacao uma vez para cada variavel, 
# deixando na coluna das marcacoes apenas 2 opcoes, 
# possibilitando classificar utilizando os algoritmos ja conhecidos,
# e escolhar como variavel Y, aclassificacao com maior probabilidade (%)
# ex: variaveis Y: a,b,c 
# primeira vez => a ou o resto (b,c) -> probabilidade (%), 
# segunda vez => b ou o resto (a,c) -> probabilidade (%),
# terceira vez => c ou o resto (a,c) -> probabilidade (%),
# (substituindo 2 por 1) 0=>0 1=>1,2 LinearSVC(algoritmo) 0 ou do resto (38%, resto 62%)
# (substituindo 2 por 0) 0=>0,2 1=>1 LinearSVC(algoritmo) 1 ou do resto (44%, resto 56%) -> Variavel Y escolhida como resposta
# (substituindo 1 por 0) 0=>0,1 2=>2 LinearSVC(algoritmo) 2 ou do resto (20%, resto 80%)

from sklearn.svm import LinearSVC
modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state = 0))
resultadoOneVsRest = fit_and_predict("OneVsRest", modeloOneVsRest, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)


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
acerto_base = max(Counter(validacao_marcacoes).itervalues())
# acerto_de_um = list(Y).count('sim') # len(Y[Y==1]) # sum(Y)
# acerto_de_zero = list(Y).count('nao') # len(Y[Y==0]) # len(Y) - acerto_de_um
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)
print("Total de testes %d" % len(validacao_dados))