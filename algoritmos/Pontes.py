# g => O grafo no qual o algoritmo vai rodar
# p => O vértice v
# v => O vértice w

def Ponte(g, p, v, cpre, pre, low, primeiraExecucao):
    if(primeiraExecucao == True):
        n = g.N;
        primeiraExecucao = False;
        i = 0;
        while(i < n): #Inicializa os vetores pre e low
            pre.append(0);
            low.append(0);
            i = i + 1;
    s = 0;
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    low[v - 1] = cpre;
    vizinhosV =  g.pegarVizinhosVertice(v)
    for w in vizinhosV:
        if(pre[w - 1] == 0):
            cpre = Ponte(g, v, w, cpre, pre, low, primeiraExecucao);
            low[v - 1] = min(low[v - 1], low[w - 1]);
            #print("({}, {})".format(v, w))
           # print("Low de {} atualizado para {}".format(w, low[w - 1]))
            if(low[w - 1] == pre[w - 1]):
                print("Aresta ({v},{w}) é Ponte\n".format(v=v, w=w));
        if w != p:
            low[v - 1] = min(low[v - 1], pre[w - 1]);
    return cpre;


def Pontes(g): #Função que vai chamar a função de inicializa as variaveis
    pre = []
    low = []
    Ponte(g, 1, 1, 0, pre, low, True);