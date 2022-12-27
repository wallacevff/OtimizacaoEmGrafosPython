import os
from classes.Grafo import Grafo
from algoritmos.Pontes import Pontes
from algoritmos.PontosDeArticulacao import PontosDeArticulacao
from algoritmos.CicloEuleriano import EncontraCicloEuleriano
from algoritmos.BuscaEmProfundidade import BuscaEmProfundidade
from algoritmos.ComponentesBiconexas import ComponentesBiconexas
from EstuturaDeDados.fila import Fila
from algoritmos.OrdenacaoTopologica import OrdenacaoTopologica
from algoritmos.Tarjan import Tarjan;
from algoritmos.UpTree import UpTree;
from Plot import *;
#from PIL import Image
#files = os.listdir('GrafosPnG');
#im = Image.open("GrafosPnG/Grafo 01.png");
#im.show();

#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#img = mpimg.imread('GrafosPnG/Grafo 01.png')
#imgplot = plt.imshow(img)
#plt.show()



def MenuPrincipal():
    while True:
        opcao = input("Escolha Uma Opção: \r\n[1] => Inserir grafo manualmente\r\n[2] => Usar grafo existente\r\n[3] => Sair\r\nOpção Desejada: ");
        if (opcao == "1"):
            txt = input();
            txt = txt.split(" ");
            N = int(txt[0]);  # Número de vertices
            M = int(txt[1]);  # Número de arestas
            Direcional = txt[2] == "True";
            grafo = Grafo(N, M); #Cria o grafo com o número de vértices e arestas digitados
            EscolherAlgoritmo(grafo);
            grafo.inserirTudo(Direcional);
        if (opcao == "2"):
            EscolherGrafo();
        if(opcao == "3"):
            return;
        elif opcao not in ("1", "2", "3"):
            print("Opção Inválida!");

def EscolherGrafo():
    print("Grafos Disponíveis:");
    files = os.listdir('GrafosTxT');
    showAll();
    pegarNumeroGrafos(files);
    try:
        num = input("Escolha o número do Grafo: ");
        grafo = Grafo(num);
        grafo.imprimeTudo();
        plotGraph(num);
        EscolherAlgoritmo(grafo);
    except:
        print("Grafo não encontrado!");

def pegarNumeroGrafos(files):
    for f in files:
        numero = f.replace(" ", "").replace("Grafo", "").replace(".txt", "");
        print(numero);

def EscolherAlgoritmo(g):
    print("Escolha o Algoritmo: ");
    files = os.listdir('algoritmos');
    for i, f in enumerate(files):
        if(".py" in f):
            print("[{}] => {}".format(i + 1, f.replace(".py", "")));
    op = input("\r\nAlgoritmo escolhido: ");
    if(op == "1"):
        print("Este algorítmo ainda não está concluído");

    elif(op == "2"):
        BuscaEmProfundidade(g);
    elif(op == "3"):
        EncontraCicloEuleriano(g);
    elif(op == "4"):
        ComponentesBiconexas(g);
    elif(op == "5"):
        OrdenacaoTopologica(g);
    elif(op == "6"):
        Pontes(g);
    elif(op == "7"):
        PontosDeArticulacao(g);
    elif(op == "8"):
        Tarjan(g);
    elif(op == "9"):
        UpTree(g);

    print("\r\n");
