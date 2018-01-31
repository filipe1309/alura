#!-*- coding: utf-8 -*-

texto1 = "Se eu comprar cinco anos antecipados, eu ganho algum desconto?"
texto1 = "O exercício 15 do curso de Java 1 está com a resposta errada"
texto1 = "Existe algum para cuidar do marketing da minha empresa"

import pandas as pd

classificacoes = pd.read_csv('emails.csv')
textosPuros = classificacoes['email']
textosQuebrados = textosPuros.str.lower().str.split(' ')

dicionario = set()
for lista in textosQuebrados:
	dicionario.update(lista)

totalDePalavras = len(dicionario)
tuplas = zip(dicionario, xrange(totalDePalavras))
# Dicionario palavra: numero/posicao
tradutor = {palavra:indice for palavra,indice in tuplas}

def vetorizar_texto(texto, tradutor):
	vetor = [0] * len(tradutor)
	for palavra in texto:
		if palavra in tradutor:
			posicao = tradutor[palavra]
			vetor[posicao] += 1
	return vetor
	
print vetorizar_texto(textosQuebrados[0], tradutor)
print vetorizar_texto(textosQuebrados[1], tradutor)
print vetorizar_texto(textosQuebrados[2], tradutor)

vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
print vetoresDeTexto