from classes.Grafo import Grafo;

def Busca(p):
    if(pai[p - 1] != p):
        pai[p - 1] = Busca(pai[p - 1]);
    return pai[p - 1];

def Uniao(p, q):
    Pp = Busca(p);
    Pq = Busca(q);
    if(Pp < Pq):
        pai[Pq - 1] = Pp;
    else:
        pai[Pp - 1] = Pq;

def UpTree(grafo: Grafo):
    global pai;
    componente = 0;
    pai = [];
    marcados = [];
    #pai = [1, 1, 2, 3, 2, 3, 5];
    for vertice in grafo.vertices:
        pai.append(vertice);
    #Uniao(1, 6);
    #print(pai)
    for vertice in grafo.vertices:
        for v in grafo.pegarVizinhosVertice(vertice):
            if(v not in marcados):
                Uniao(vertice, v);
                marcados.append(v);
                #marcados.append(vertice);
    
    for v in grafo.vertices:
        if(pai[v - 1] == v):
            componente += 1;
   # Busca(6);
    print("Árvore: {}".format(pai));
    if(componente == 1):
        print("Conexo");
    else:
        print("Desconexo");
    print(marcados);