# g => O grafo no qual o algoritmo vai rodar
# p => O vértice v
# v => O vértice w

def Ponte(g, p, v, cpre, primeiraExecucao):
    if(primeiraExecucao == True):
        n = g.N;
        primeiraExecucao = False;
        i = 0;
        while(i < n): #Inicializa os vetores pre e low
            pre.append(0);
            low.append(0);
            i = i + 1;
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    low[v - 1] = cpre;
    aresta = [p, v]
    vizinhosV =  g.pegarVizinhosVertice(v)
    #vizinhosV.append(v);
    vertices.append(v);
    #print("Vertice: {w}\nAresta: ({ver},{w})\nVizinhos: {viz}\nPre: {pre}\nLow: {low}".format(ver = p, pre=pre, low = low, w = v, viz = vizinhosV));
    for w in vizinhosV:
        #print("   Analisando o vizinho {} de {} com pre: {} e low: {}".format(w,v,pre[w-1], low[w-1]));
        #print("   Low de {} atual: {}".format(v, low[v - 1]));
        if(pre[w - 1] == 0):
            cpre = Ponte(g, v, w, cpre, primeiraExecucao);
            low[v - 1] = min(low[v - 1], low[w - 1]);
            #print("   Aresta ({}, {})".format(v, w))
            #print("   Low de {} atualizado para {}".format(w, low[w - 1]))
            if(low[w - 1] == pre[w - 1]):
                pontes.append(aresta);
                print("Aresta ({v},{w}) é Ponte\n".format(v=v, w=w));
        if (w != p):
            low[v - 1] = min(low[v - 1], low[w - 1]);
            #print("   Low de {} atualizado para {}\n   Low Atual: {}".format(v, low[w - 1], low));
    return cpre;


def Pontes(g):
    global pre;
    global low;
    pre = [];
    low = [];
    global vertices;
    global aresta;
    aresta = [];
    global pontes;
    pontes = [];
    vertices = [];
    cpre = Ponte(g, 1, 1, 0, True);
    
    for vertice in g.vertices:
        if(vertice not in vertices):
            if(pre[vertice - 1] == 0):
                cpre = Ponte(g, vertice, vertice, cpre, False);
    print("Vetor Pre: {}\nVetor Low: {}".format(pre, low));
    #print (g.vertices);