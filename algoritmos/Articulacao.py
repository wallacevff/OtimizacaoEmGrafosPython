# g => O grafo no qual o algoritmo vai rodar
# p => O vértice v
# v => O vértice w

def PA(g, p, v, cpre, primeiraExecucao):
    if(primeiraExecucao == True):
        n = g.N;
        primeiraExecucao = False;
        i = 0;
        while(i < n): #Inicializa os vetores pre e low
            pre.append(0);
            low.append(0);
            pa.append(0);
            i = i + 1;
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    low[v - 1] = cpre;
    pa[v - 1] = 0;
    vizinhosV =  g.pegarVizinhosVertice(v)
    vertices.append(v);
    for w in vizinhosV:
        if(pre[w - 1] == 0):
            cpre = PA(g, v, w, cpre, primeiraExecucao);
            if(pre[v - 1] <= low [w - 1]):
                pa[v - 1] = pa[v - 1] + 1;
            low[v - 1] = min(low[v - 1], low[w - 1]);
        if (w != p):
            low[v - 1] = min(low[v - 1], low[w - 1]);
    return cpre;


def Articulacao(g):
    global pre;
    global low;
    global pa;
    pre = [];
    low = [];
    pa = [];
    global vertices;
    global aresta;
    aresta = [];
    global pontes;
    pontes = [];
    vertices = [];
    cpre = PA(g, 1, 1, 0, True);
    
    for vertice in g.vertices:
        if(vertice not in vertices):
            if(pre[vertice - 1] == 0):
                cpre = PA(g, vertice, vertice, cpre, False);

    for vertice in g.vertices:
        if((vertice - 1) == 0 and pa[0] > 1):
            print("Vértice 1 é ponto de articulação\r\n");
        elif ((vertice - 1) != 0 and pa[vertice - 1] > 0):
            print("Vértice {} é ponto de Articulação".format((vertice)));

    print("Vetor Pre: {}\nVetor Low: {}\nPontos de Articulação: {} ".format(pre, low, pa));

    #print (g.vertices);