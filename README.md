# Algoritmo em Python para a disciplina Otimizaçao em Grafos
Versão do Python: 3.10

## Como executar:
    
    python ./Main.py < "./GrafosTxt/ArquivoGrafo.txt"

    Ou
    
    python3 ./Main.py < "./GrafosTxt/<ArquivoGrafo.txt>

## Exemplo de Execução:
#### Grafo que não possuí ciclo Euleriano
#####  Descobrir se o Grafo abaixo possui ciclo Euleriano.
![Grafo 01](./GrafosPnG/Grafo%2001.png "Grafo 01")
    
    
 python3 ./Main.py < "./GrafosTxt/Grafo 01.txt"
    
    Output:
        Lista de Adjacência
        1 -> 3 -> 2
        2 -> 4 -> 5 -> 1
        3 -> 5 -> 1
        4 -> 2 -> 5
        5 -> 3 -> 6 -> 4 -> 2
        6 -> 5


        Matriz de Adjacência
            1 2 3 4 5 6
        1 | 0 1 1 0 0 0
        2 | 1 0 0 1 1 0
        3 | 1 0 0 0 1 0
        4 | 0 1 0 0 1 0
        5 | 0 1 1 1 0 1
        6 | 0 0 0 0 1 0

        Nao possui ciclo Euleriano. Caminho Euleriano encontrado:
        [2, 4, 5, 2, 1]

#### Grafo que possuí ciclo Euleriano
#####  Descobrir se o Grafo abaixo possui ciclo Euleriano.

![Grafo 02](./GrafosPnG/Grafo%2002.png "Grafo 02")

python3 ./Main.py < "./GrafosTxt/Grafo 02.txt"

    Lista de Adjacência
    1 -> 2 -> 4
    2 -> 1 -> 3 -> 4 -> 5
    3 -> 2 -> 4
    4 -> 1 -> 2 -> 3 -> 5
    5 -> 2 -> 4


    Matriz de Adjacência
        1 2 3 4 5
    1 | 0 1 0 1 0
    2 | 1 0 1 1 1
    3 | 0 1 0 1 0
    4 | 1 1 1 0 1
    5 | 0 1 0 1 0

    Ciclo Euleriano: {1, 2, 3, 4, 2, 5, 4, 1}

#####  Descobrir se o Grafo abaixo possui pontes.
![Grafo 09](./GrafosPnG/Grafo%2008.png "Grafo 02")

python3 ./Main.py < "./GrafosTxt/Grafo 08.txt"

    Lista de Adjacência
    2 -> 1 -> 4 -> 5
    3 -> 1 -> 5
    4 -> 2 -> 5
    5 -> 2 -> 3 -> 4 -> 6
    6 -> 5 -> 7 -> 8
    7 -> 6 -> 8
    8 -> 6 -> 7


    Matriz de Adjacência
        1  2  3  4  5  6  7  8
    1 | 0  1  1  0  0  0  0  0
    2 | 1  0  0  1  1  0  0  0
    3 | 1  0  0  0  1  0  0  0
    4 | 0  1  0  0  1  0  0  0
    5 | 0  1  1  1  0  1  0  0
    6 | 0  0  0  0  1  0  1  1
    7 | 0  0  0  0  0  1  0  1
    8 | 0  0  0  0  0  1  1  0

    Aresta (5,6) é Ponte

    Vetor Pre: [1, 2, 5, 3, 4, 6, 7, 8]
    Vetor Low: [1, 1, 1, 1, 1, 6, 6, 6]


    #####  Descobrir se o Grafo abaixo possui pontes.
![Grafo 09](./GrafosPnG/Grafo%2009.png "Grafo 02")

python3 ./Main.py < "./GrafosTxt/Grafo 09.txt"


    Lista de Adjacência
    1 -> 2 -> 3
    2 -> 1 -> 3
    3 -> 1 -> 2 -> 6
    4 -> 5 -> 6
    5 -> 4 -> 6
    6 -> 3 -> 4 -> 5


    Matriz de Adjacência
        1  2  3  4  5  6
    1 | 0  1  1  0  0  0
    2 | 1  0  1  0  0  0
    3 | 1  1  0  0  0  1
    4 | 0  0  0  0  1  1
    5 | 0  0  0  1  0  1
    6 | 0  0  1  1  1  0

    Aresta (3,6) é Ponte

    Vetor Pre: [1, 2, 3, 5, 6, 4]
    Vetor Low: [1, 1, 1, 4, 4, 4]

#####  Componentes Biconexas.
![Grafo 07](./GrafosPnG/Grafo%2007.png "Grafo 07")

    python3 ./Main.py < "./GrafosTxt/Grafo 07.txt"

    Lista de Adjacência
    1 -> 2 -> 7 -> 8
    2 -> 1 -> 3 -> 4
    3 -> 2 -> 4 -> 5
    4 -> 2 -> 3 -> 6
    5 -> 3 -> 6
    6 -> 4 -> 5
    7 -> 1 -> 8
    8 -> 1 -> 7


    Matriz de Adjacência
        1  2  3  4  5  6  7  8
    1 | 0  1  0  0  0  0  1  1
    2 | 1  0  1  1  0  0  0  0
    3 | 0  1  0  1  1  0  0  0
    4 | 0  1  1  0  0  1  0  0
    5 | 0  0  1  0  0  1  0  0
    6 | 0  0  0  1  1  0  0  0
    7 | 1  0  0  0  0  0  0  1
    8 | 1  0  0  0  0  0  1  0

    [3, 5]
    [5, 6]
    [4, 6]
    [2, 4]
    [3, 4]
    [2, 3]
    [1, 2]
    [1, 8]
    [7, 8]
    [1, 7]