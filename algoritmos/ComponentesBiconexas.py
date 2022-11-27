from EstuturaDeDados.pilha import Pilha;
def Blocos(g, p, v, cpre, primeiraExecucao):
    if(primeiraExecucao == True):
        primeiraExecucao = False;
        i = 0;
        n = g.N;
        while i < n:
            pre.append(0);
            low.append(0);
            i+=1;
    vizinhosV = g.pegarVizinhosVertice(v);
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    low[v - 1] = pre[v - 1];
    #print("Vértice: {}\nVizinhos: {}".format(v, vizinhosV))
    for w in vizinhosV:
        if v < w : aresta = [v, w]; 
        else: aresta = [w, v];
        #print(aresta)
        #print("Vizinho {} de {}".format(w, v));
        if(aresta not in arestas): #Verifica aresta marcada
            pilha.empilha(aresta);
            #print("Epilhando... {}".format(pilha));
            arestas.append(aresta); #Marca aresta;
        if(pre[w -1] == 0):
            cpre = Blocos(g, v, w, cpre, primeiraExecucao);
            if(pre[v - 1] <= low[w - 1]):
                while(pilha.tamanho > 0):
                    #print("Desempilhando... {}".format(pilha));
                    print(" {}".format(pilha.desempilha()));            
            low[v - 1] = min(low[v - 1], low[w - 1]);
        elif w != p:
            low[v -1] = min(low[v -1], pre[w - 1]);

    return cpre;

def ComponentesBiconexas(g):
    global pre;
    global low;
    global cpre;
    global arestas;
    global pilha;
    global aresta;
    
    aresta = [];
    pilha = Pilha();
    arestas = [];
    pre = [];
    low = []; 
    cpre = 0;
    Blocos(g, 8, 8, cpre, True);
    for vertice in g.vertices:
        if(pre[vertice - 1] == 0):
            Blocos(g, vertice, vertice, cpre, False);
    #print("Acabou... {}".format(pilha));
    #print(" Arestas:")
    #for aresta in arestas:
        #print(" {}".format(aresta));
   # print(g.vertices);
   # print(arestas);
    return;