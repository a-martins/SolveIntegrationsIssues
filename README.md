# SolveIntegrationsIssues
Desafio -­ Problema de Integração 

Recentemente descobrimos que numa de nossas integrações está ocorrendo um erro inesperado, os pedidos quando chegam, estão com o valor de frete e dos itens na ordem errada! 

Por algum motivo, quando buscamos os dados dos pedidos, os valores do frete, dos itens, e o valor total do pedido, estão ordenados em ordem crescente, porém isso não garante que o frete na posição i, somado com o valor dos itens na posição i, é equivalente ao valor total do pedido na posição i. 

Com a Black Friday chegando, não temos tempo suficiente para esperar que o cliente resolva o chamado que abrimos na loja dele, nós precisamos da sua ajuda para resolver isso! 

Serão fornecidos 3 arrays como entrada, representando, respectivamente, os valores do frete, dos itens e, por fim, o total do pedido. O número de pedidos por requisição ao sistema cliente pode variar entre: 5, 10, 20, 50 e 100. A solução deve levar em consideração pelo menos um dos tamanhos. 

Precisamos de uma função (ou método) que recebe os três arrays como entrada, e gera como saída os pedidos montados com o valor do frete, do item e o respectivo valor total, ordenados de forma crescente pelo valor total. 

Exemplo: 
Tamanho: 
      5 Entrada: [20,25,40,45,50], [25,30,40,50,60], [50,60,70,100,105] 
      Saída:  {pedido1: {frete: 25, preco_itens: 25, total: 50}} 
              {pedido2: {frete: 20, preco_itens: 40, total: 60}} 
              {pedido3: {frete: 40, preco_itens: 30, total: 70}} 
              {pedido4: {frete: 50, preco_itens: 50, total: 100}} 
              {pedido5: {frete: 45, preco_itens: 60, total: 105}}
