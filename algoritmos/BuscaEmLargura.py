from EstuturaDeDados.fila import Fila;

def BL(g, p, v):
    global cpre;
    aresta = [p, v];
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    fila.enfileirar(aresta);
    vizinhosV = g.pegarVizinhosVertice(v);
    while fila.tamanho > 0:
        arestaTmp = fila.primeiro;
        p = arestaTmp[0];
        t = arestaTmp[1];
        for w in vizinhosV:
            if pre[w] == 0:
                aresta = [v, w]
                fila.enfileirar(aresta);
        fila.desenfileirar(aresta)



    return ;

def BuscaEmLargura(g):
    global fila;
    global pre;
    global aresta;
    global cpre;
    fila = Fila();
    aresta = [];
    cpre = 0;
    pre = [];
    BL(g, 1, 1)
    return;
