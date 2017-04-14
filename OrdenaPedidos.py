#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import collections

def calcRecorrencias(listagem, array_possib):
        """
        Método para calcular a recorrência dos totais na lista de possibilidades.
        :param listagem: lista dos totais para encontrar recorrência
        :param array_prob: array com as possibilidades de combinações.
        :return: array com as recorrências
        """
        lista = []
        for total in listagem:
            lista.append([total,(np.count_nonzero(array_possib[:,2] == total))])
        array_return = np.array(lista)
        if len(array_return)>0:
            array_return = array_return[array_return[:, 1].argsort()]
        return array_return

def ordenaPedidos(listaPreco, listaFrete, listaTotal):
    """
    Método para verificar as possíveis combinações de resultado entre Preço e Frete para se
    chegar ao total, em seguida ordenar pelo total de forma crescente.
    :param listaPreco: lista de preços dos itens comprados e ordenada de forma crescente.
    :param listaFrete: lista de fretes das compras e ordenada de forma crescente.
    :param listaTotal: lista de totais das compras e ordenados de forma crescente.
    :return: dicionário com os preços, fretes e totais agrupados corretamente e ordenando por total.
    """
    #Crio uma lista de possíveis combinações entre frete e preço.
    possibilidades = []
    for preco in listaPreco:
        for frete in listaFrete:
            if (preco+frete) in listaTotal:
                possibilidades.append([preco,frete,preco+frete])
    #Transformo a linha em uma matriz bidimensional.
    array_p = np.array(possibilidades)
    #Crio uma matriz com a recorrência em que os totais se repetem dentro das possibilidades.
    array_r = calcRecorrencias(listaTotal,array_p)

    #loop enquanto tiver valores dentro da matriz que não teve seu agrupamento correto.
    pedidosFinal = []
    while len(array_r) > 0:
        qtdReccorencias = len(array_r)
        for i,x in array_r:
            #dentro da matriz eu vejo se algum total não se repete, então começo por ele.
            if x == 1:
                #pego sua posição na matriz
                indiceTotal = np.where(array_p[:,2] == i)
                frete = int(array_p[indiceTotal,1])
                item = int(array_p[indiceTotal,0])
                total = int(array_p[indiceTotal,2])
                #adiciono a combinação correta em uma lista
                pedidosFinal.append([frete,item,total])
                #excluo da matriz de possiveis resultados, uma vez que já encontrei o correto.
                array_p = np.delete(array_p,(indiceTotal),axis=0)
                #procuro na matriz de possibilidades onde se repete o preço que eu já encontrei e excluo.
                indiceItens = [g for (g,v) in enumerate(array_p[:,0]) if v==item]
                array_p = np.delete(array_p,(indiceItens),axis=0)
                #procuro na matriz de possibilidades onde se repete o frete que eu já encontrei e excluo.
                indiceFretes = [g for (g,v) in enumerate(array_p[:,1]) if v==frete]
                array_p = np.delete(array_p,(indiceFretes),axis=0)
                #removo o total encontrado da lista de totais.
                listaTotal.remove(i)
        """
        Recalculo as recorrências mediantes as exclusões que eu fiz e refaço o loop para ver se mais alguem
        ficou com apenas uma repetição, caso não haja alteração na matriz de recorrencia eu forço a saida do
        loop para não entrar em loop infinito.
        """
        array_r = calcRecorrencias(listaTotal,array_p)
        if qtdReccorencias == len(array_r):
            break

    #matriz final ordenada por total.
    pedidosFinal = np.array(pedidosFinal)
    pedidosFinal = pedidosFinal[pedidosFinal[:, 2].argsort()]

    #monto o dicionário ordenado e retorno o resultado.
    n = 0
    dicPedidos = collections.OrderedDict()
    for x,y,z in pedidosFinal:
        n = n + 1
        pedido = collections.OrderedDict()
        pedido["frete"] = x
        pedido["preco_itens"] = y
        pedido["total"] = z
        dicPedidos["pedido"+str(n)] = pedido
    return dicPedidos


