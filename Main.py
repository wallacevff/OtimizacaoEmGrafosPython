from classes.Grafo import Grafo;
from algoritmos.Pontes import Pontes;
from algoritmos.CicloEuleriano import EncontraCicloEuleriano;

def main():
    txt = input();
    txt = txt.split(" ");
    N = int(txt[0]); #Número de vertices
    M = int(txt[1]); #Número de arestas
    
    grafo = Grafo(N, M); #Cria o grafo com o número de vértices e arestas digitados

    grafo.inserirTudo(False); #Inicializa o Grafo com a Matriz de Adjacência e a Lista de Adjacência
    grafoEu = grafo;
    grafo.imprimeTudo(); # Imprime a Lista de Adjacência e a Matriz de Adjacência
    #EncontraCicloEuleriano(grafoEu); #Busca Ciclo Euleriano
    Pontes(grafo); #Busca Pontes
    
   # grafo.removeArestaListaAdj(1, 3);
   # grafo.removeArestaListaAdj(1, 2);
    
    
   # 
    #print(pilha);
    #pilha.desenpilhar();
    #print(pilha.topo());
    
    
main();