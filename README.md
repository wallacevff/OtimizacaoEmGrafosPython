Versão do Python: 3.10
Como executar:
    python ./Main.py < "./GrafosTxt/<ArquivoGrafo.txt>

    Ou

    python3 ./Main.py < "./GrafosTxt/<ArquivoGrafo.txt>

Exemplo de Execução:
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
