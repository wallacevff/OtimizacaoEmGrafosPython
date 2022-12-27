from classes.Grafo import Grafo;
from algoritmos.Pontes import Pontes;
from algoritmos.PontosDeArticulacao import PontosDeArticulacao;
from algoritmos.CicloEuleriano import EncontraCicloEuleriano;
from algoritmos.BuscaEmProfundidade import BuscaEmProfundidade;
from algoritmos.ComponentesBiconexas import ComponentesBiconexas;
from EstuturaDeDados.fila import Fila;
from algoritmos.OrdenacaoTopologica import OrdenacaoTopologica;
from algoritmos.Tarjan import Tarjan;
from algoritmos.UpTree import UpTree;
from Opcoes import *;
import sys; 

#from EstuturaDeDados.pilha import Pilha;
def main():
    if(len(sys.argv) < 2):
        MenuPrincipal();
    else:
        txt = input();
        txt = txt.split(" ");
        N = int(txt[0]); #Número de vertices
        M = int(txt[1]); #Número de arestas
        Direcional = txt[2] == "True";
        grafo = Grafo(N, M); #Cria o grafo com o número de vértices e arestas digitados
    #  g = Grafo("1");
        grafo.inserirTudo(Direcional); #Inicializa o Grafo com a Matriz de Adjacência e a Lista de Adjacência
        #grafoEu = Grafo(grafo.N, grafo.M);
        #grafoEu.copiarGrafo(grafo);
        #print(len(grafo.listaAdj[6]))
        grafo.imprimeTudo();
    # g.imprimeTudo(); # Imprime a Lista de Adjacência e a Matriz de Adjacência
    # EncontraCicloEuleriano(grafoEu); #Busca Ciclo Euleriano
        #Pontes(grafo); #Busca Pontes
    # BuscaEmProfundidade(grafo);
    #OrdenacaoTopologica(grafo);
    # UpTree(grafo);
        #ComponentesBiconexas(grafo);
        #Articulacao(grafo);
    # grafo.removeArestaListaAdj(1, 3);
    # grafo.removeArestaListaAdj(1, 2);
    #  OrdenacaoTopologica(grafo);
        #Tarjan(grafo);
    # 
        #print(pilha);
        #pilha.desenpilhar();
        #print(pilha.topo());
        
    
main();