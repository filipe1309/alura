# caracteristicas = gordinho, perna curta, faz auau
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco2, cachorro1, cachorro2, cachorro3]

# 1 = porco, -1 = cachorro
marcacoes = [1, 1, 1, -1, -1, -1]


from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

# cachorro ou porco?
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]

#teste = [misterioso1, misterioso2]
#print(modelo.predict(teste))
#[-1  1]


misterioso3 = [0, 0, 1]
testes = [misterioso1, misterioso2, misterioso3]
marcacoes_teste = [-1, 1, -1]
resultado = modelo.predict(testes)
print(resultado)
#[-1  1 -1]

# 1 1 => 1 - 1 = 0
# -1 -1 => -1 - -1 = -1 + 1 = 0
# -1 1 => -1 - 1 = -2 Errou a predicao
# 1 -1 => 1 - -1 = 1 + 1 = 2 Errou a predicao
# se o array resultante tiver valores diferente de zero, entao houve erro na predicao
diferencas = resultado - marcacoes_teste
print(diferencas)

#total[erro for erro in erros if erro != 0]
acertos = [d for d in diferencas if d==0]

total_de_acertos = len(acertos)
total_de_elementos = len(testes)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
