#!-*- coding: utf-8 -*-

texto1 = "Se eu comprar cinco anos antecipados, eu ganho algum desconto?"
texto1 = "O exercício 15 do curso de Java 1 está com a resposta errada"
texto1 = "Existe algum para cuidar do marketing da minha empresa"

import pandas as pd

classificacoes = pd.read_csv('emails.csv')
textosPuros = classificacoes['email']
textosQuebrados = textosPuros.str.lower().str.split(' ')

print textosQuebrados

dicionario = set()
for lista in textosQuebrados:
	dicionario.update(lista)

totalDePalavras = len(dicionario)
tuplas = zip(dicionario, xrange(totalDePalavras))
# Dicionario palavra: numero/posicao
tradutor = {palavra:indice for palavra,indice in tuplas}

texto = textosQuebrados[0]
vetor = [0] * totalDePalavras
for palavra in texto:
	if palavra in tradutor:
		posicao = tradutor[palavra]
		vetor[posicao] += 1

print texto
print vetor
