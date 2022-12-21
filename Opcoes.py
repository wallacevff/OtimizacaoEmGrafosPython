from classes.Grafo import Grafo
from algoritmos.Pontes import Pontes
from algoritmos.Articulacao import Articulacao
from algoritmos.CicloEuleriano import EncontraCicloEuleriano
from algoritmos.BuscaEmProfundidade import BuscaEmProfundidade
from algoritmos.ComponentesBiconexas import ComponentesBiconexas
from EstuturaDeDados.fila import Fila
from algoritmos.OrdTop import OrdenacaoTopologica


def MenuPrincipal():
    opcao = input("Escolha Uma Opção: \r\n[1] => Inserir grafo manualmente\r\n[2] => Usar grafo existente\r\n");
    if (opcao == "1"):
        txt = input();
        txt = txt.split(" ");
        N = int(txt[0]);  # Número de vertices
        M = int(txt[1]);  # Número de arestas
    if (opcao == "2"):
        EscolherGrafo();

def EscolherGrafo():
    num = input("Escolha o número do Grafo: ");
    #f = open("GrafosTxT/Grafo 0{}.txt".format(num), "r");
    num = num.rjust(2, "0");
    print(num);
     #   if(not a):
    #        EndOfFile = True;
   #     else:
    #        print(a);
MenuPrincipal();