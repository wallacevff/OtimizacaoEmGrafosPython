from classes.Grafo import Grafo
from algoritmos.Ponte import *;
from EstuturaDeDados.pilha import *;

def main():
    txt = input();
    txt = txt.split(" ");
    N = int(txt[0]);
    M = int(txt[1]);
    grafo = Grafo(N, M)
    #grafo.inserirRangeMatrizAdj(False);
    #grafo.inserirRangeListaAdj(False);
    grafo.inserirTudo(False);
    pre = []
    low = []
    vertices = []
    Ponte(grafo, 1, 1, 0, pre, low, vertices, True);
   # grafo.removeArestaListaAdj(1, 3);
   # grafo.removeArestaListaAdj(1, 2);
   # grafo.imprimeTudo();
   # pilha = Pilha();
   # CicloEuleriano(grafo, pilha)
    #print(pilha);
    #pilha.desenpilhar();
    #print(pilha.topo());
    
    
main();