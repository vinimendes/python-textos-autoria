import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def removendo_pontos(texto):
    carac = ""
    for i in texto:
        if not (i == "." or i == "," or i == ":" or i == ";" 
               or i == "(" or i == ")" or i == '"' or i == "[" or i == "]"):
            carac = carac + i
    return carac

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +"  (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +"  (aperte enter para sair):")    
    return textos

def separa_sentencas(texto):
    setencas = re.split(r'[.!?]+', texto)
    if setencas[-1] == '':
        del setencas[-1]
    return setencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    textos = as_a
    ass_cp = as_b
    listaValorAss = []
    for i in textos:
        listaF = []
        listaA = calcula_assinatura(i)
        for i in range(0, 6):
            listaF.append(abs(listaA[i] - ass_cp[i]))
        listaValorAss.append(float(sum(listaF) / 6))
    return listaValorAss

def calcula_assinatura(texto):
    # Calc WAL
    palavrasSemPonto = removendo_pontos(texto)
    listaPalavras = separa_palavras(palavrasSemPonto)
    total = 0
    for i in listaPalavras:
        total = total + len(i)
    novoWal = float(total / len(listaPalavras))
    # Calc Type_Token
    numPalavDif = n_palavras_diferentes(listaPalavras)
    novoTtr = float(numPalavDif / len(listaPalavras))
    # Calc Hapax
    numPalavUnic = n_palavras_unicas(listaPalavras)
    novoHlr = float(numPalavUnic / len(listaPalavras))
    # Calc Tam Médio
    listSentenc = separa_sentencas(texto)
    total = 0
    for i in listSentenc:
        total = total + len(i)
    novoSal = float(total / len(listSentenc))
    # Calc Complexidade Sentenca
    total = 0
    for i in listSentenc:
        listFrase = separa_frases(i)
        total = total + len(listFrase)
    novoSac = float(total / len(listSentenc))
    # Calc numero médio da frase
    totalCarac = 0
    
    for i in listSentenc:
        listFrase = separa_frases(i)
        for i in listFrase:
            totalCarac = totalCarac + len(i)
    novoPal = float(totalCarac / total)

    return [novoWal, novoTtr, novoHlr, novoSal, novoSac, novoPal]



def avalia_textos(textos, ass_cp):
    listaValorAss = compara_assinatura(textos, ass_cp)
    # Compara qual texto 
    numInd = 1
    
    for i in listaValorAss:
        if numInd < len(listaValorAss):
            if i > listaValorAss[numInd]:
                menorValor = listaValorAss[numInd]
                numDoTexto = numInd

            else:
                menorValor = i
                numDoTexto = numInd - 1
            numInd += 1
    resultado = numDoTexto + 1
    return resultado

# Inicio do Programa

ass_cp = le_assinatura()
textos = le_textos()

print("O autor do texto " + str(avalia_textos(textos, ass_cp)) + " está infectado com COH-PIAH")