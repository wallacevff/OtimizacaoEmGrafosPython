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
        Lista de Adjascencia
        1 -> 3 -> 2
        2 -> 4 -> 5 -> 1
        3 -> 5 -> 1
        4 -> 2 -> 5
        5 -> 3 -> 6 -> 4 -> 2
        6 -> 5


        Matriz de Adjascencia
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

    Lista de Adjascencia
    1 -> 2 -> 4
    2 -> 1 -> 3 -> 4 -> 5
    3 -> 2 -> 4
    4 -> 1 -> 2 -> 3 -> 5
    5 -> 2 -> 4


    Matriz de Adjascencia
        1 2 3 4 5
    1 | 0 1 0 1 0
    2 | 1 0 1 1 1
    3 | 0 1 0 1 0
    4 | 1 1 1 0 1
    5 | 0 1 0 1 0

    Ciclo Euleriano: {1, 2, 3, 4, 2, 5, 4, 1}
