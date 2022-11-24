def Ponte(g, p, v, cpre, pre, low, vertices, primeiraExecucao):
    if(primeiraExecucao == True):
        n = g.N;
       # print(n)
        primeiraExecucao = False;
        i = 0;
        while(i < n):
            pre.append(0);
            low.append(0);
            i = i + 1;
    #print(pre)
    s = 0;
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    low[v - 1] = cpre;
    vertices.append(p);
    vertices.append(v);
    vizinhosV =  g.pegarVizinhosVertice(v) #[vizinho for vizinho in g.pegarVizinhosVertice(v) if vizinho not in vertices]
   # print(low)
   # print(vizinhosV)
    for w in vizinhosV:
        if(pre[w - 1] == 0):
            cpre = Ponte(g, v, w, cpre, pre, low, vertices, primeiraExecucao);
            low[v - 1] = min(low[v - 1], low[w - 1]);
            #print("({}, {})".format(v, w))
           # print("Low de {} atualizado para {}".format(w, low[w - 1]))
            
            if(low[w - 1] == pre[w - 1]):
                print("Aresta ({v},{w}) é Ponte\n".format(v=v, w=w));
        if w != p:
            low[v - 1] = min(low[v - 1], pre[w - 1]);
  #  print(low)
    return cpre;