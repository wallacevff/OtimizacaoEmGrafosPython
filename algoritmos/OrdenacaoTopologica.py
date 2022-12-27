# g => O grafo no qual o algoritmo vai rodar
# p => O vértice v
# v => O vértice w

def Imprime(u, first):
    global maiorCaminho;
    if first:
        maiorCaminho = maiorCaminho + "{}".format(u).rjust(2, " ");
    else:
        maiorCaminho = maiorCaminho + " -> " + "{}".format(u).rjust(2, " "); 
    for w in g.pegarVizinhosVertice(u):
        if(Dm[w - 1] == (Dm[u - 1] - 1)):
            Imprime(w, False);
            break;

def imprimeMaiorDistancia():
    i = 0;
    for v in Dm:
        i = i + 1;
        print("{}".format(i).rjust(2, " ") + ": {}".format(v).rjust(2, " "));


def OrdTop(u, v):
    global os;
    global mc;
    Marcados.append(v);
    vizinhosV = g.pegarVizinhosVertice(v);
    for w in vizinhosV:
        if (w not in Marcados):
            OrdTop(v, w);
        Dm[v - 1] = max(Dm[v - 1], Dm[w - 1] + 1);
    ot[os] = v;
    os = os - 1;
    mc = max(mc, Dm[v - 1]);




def OrdenacaoTopologica(grafo):
    global Marcados;
    global os;
    global ot;
    global n;
    global g;
    global mc;
    global Dm;
    global ot;
    global maiorCaminho;
    ot = [];
    Dm = [];
    maiorCaminho = "Maior caminho:\r\n" + " " * 3;
    g = grafo;
    n = len(grafo.vertices);
    mc = 0;
    os = n - 1;
    Marcados = [];
    for vertice in g.vertices:
        Dm.append(0);
        ot.append(0);
    for vertice in g.vertices:
        if(vertice not in Marcados):
            OrdTop(vertice, vertice);
    for vertice in g.vertices:
        if(Dm[vertice - 1] == mc):
            Imprime(vertice, True);
            maiorCaminho = maiorCaminho + "\r\n" + " " * 3;
    
    print("Ordenação Topológica: {}".format(ot));
    print("Distancia Máxima: {}".format(Dm));
    imprimeMaiorDistancia();
    print(maiorCaminho);
    #print(g.vertices[1:]);


