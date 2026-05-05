# Algoritmo-Genético-para-Otimiza-o-do-Problema-da-Mochila-com-Dados-Reais
Este projeto implementa um Algoritmo Genético para resolver o clássico Problema da Mochila 0-1, utilizando dados reais para simular um cenário de maximização de valor sob restrições.

A proposta consiste em selecionar automaticamente um subconjunto de itens que maximize o valor total sem ultrapassar um limite de capacidade, modelando um problema típico de otimização combinatória.

Os dados utilizados representam informações de vendas, onde:

O valor (profit) corresponde ao faturamento gerado
O peso (weight) representa a quantidade transportada

A solução foi desenvolvida utilizando técnicas de Computação Evolutiva, simulando o processo de seleção natural para explorar o espaço de soluções possíveis.

## Como funciona

Cada solução candidata é representada por um vetor binário, indicando a inclusão ou exclusão de itens.

O algoritmo segue as etapas clássicas:

- Inicialização de uma população aleatória
- Avaliação por função de fitness
- Seleção por torneio
- Crossover de ponto único
- Mutação aleatória
- Evolução ao longo de várias gerações

Soluções que violam a restrição de capacidade são penalizadas, garantindo viabilidade ao longo do processo.

## Avaliação do desempenho

O algoritmo foi analisado considerando:

- Evolução do fitness ao longo das gerações
- Melhor solução encontrada
- Média dos resultados em múltiplas execuções
- Tempo de execução
- Comparação entre diferentes tamanhos de instância

Os resultados mostram que o método é capaz de encontrar soluções de alta qualidade de forma eficiente, mesmo em cenários com grande espaço de busca.

## Resultados
- Convergência rápida nas primeiras gerações
- Estabilização do fitness ao longo do tempo
- Boa eficiência computacional
- Escalabilidade para instâncias maiores
  
## Tecnologias utilizadas
- Python
- NumPy
- Implementação manual de Algoritmo Genético


