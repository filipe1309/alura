import csv

def carregar_acessos():
	
	# dados
	X = []
	# marcacoes
	Y = []

	arquivo = open('acesso.csv', 'rb')
	leitor = csv.reader(arquivo)
	leitor.next() # pula a primeira linha
	for home,como_funciona,contato,comprou in leitor:

		dado = [int(home), int(como_funciona), int(contato)]
		X.append(dado)
		Y.append(int(comprou))

	return X, Y

def carregar_buscas():
	
	# dados
	X = []
	# marcacoes
	Y = []

	arquivo = open('busca.csv', 'rb')
	leitor = csv.reader(arquivo)
	leitor.next() # pula a primeira linha
	for home,busca,logado,comprou in leitor:

		dado = [int(home), busca, int(logado)]
		X.append(dado)
		Y.append(int(comprou))

	return X, Y
