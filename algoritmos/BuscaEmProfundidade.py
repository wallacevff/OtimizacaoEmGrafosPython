def BP(g, p, v, cpre, primeiraExecucao):
    if(primeiraExecucao == True):
        primeiraExecucao = False;
        i = 0;
        n = g.N;
        while i < n:
            pre.append(0);
            i+=1;
    vizinhosV = g.pegarVizinhosVertice(v);
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    for w in vizinhosV:
        if(pre[w -1] == 0):
            cpre = BP(g, v, w, cpre, primeiraExecucao);
    return cpre;

def BuscaEmProfundidade(g):
    global pre;
    global cpre;
    pre = []; 
    cpre = 0;
    BP(g, 2, 2, cpre, True);
    for vertice in g.vertices:
        if(pre[vertice - 1] == 0):
            BP(g, vertice, vertice, cpre, False);
    
    print(g.vertices);
    print(pre);
    return;