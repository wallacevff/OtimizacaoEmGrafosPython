
def CicloEuleriano(grafo, pilha):
    v = grafo.vertices[0];
    ciclo = [];
    vizinhancaV = grafo.pegarVizinhosVertice(v);
    tamanhoVizinhanca = len(vizinhancaV);
    pilha.empilha(v);
    #print(vizinhancaV);
    texto = "Ciclo Euleriano: {";
    while(pilha.tamanho > 0):
        v = pilha.topo();
        if(tamanhoVizinhanca > 0):
            w = vizinhancaV[tamanhoVizinhanca - 1];
        else:
            w = None;
        pilha.empilha(w);
        #print(pilha)
        if(w == None or v == None):
            break;
        grafo.removeArestaListaAdj(v, w);
        vizinhancaV = grafo.pegarVizinhosVertice(w);
        tamanhoVizinhanca = len(vizinhancaV);
       # print(vizinhancaV)
       # print("--- {w} ---".format(w = w))
       # print(v)
       # print(pilha.topo)
       # print("{v}, {w}".format(v = v, w = w))
        #grafo.removeArestaListaAdj(v, w);
        while(pilha.tamanho > 0 and tamanhoVizinhanca == 0):
            w = pilha.desenpilha();
            ciclo.append(w);
            texto += "{w}".format(w = w);
            
            if(pilha.tamanho > 0 and tamanhoVizinhanca == 0):
                texto += ", ";
    if(ciclo[0] != ciclo[len(ciclo) - 1]):
        print("Nao possui ciclo Euleriano. Caminho Euleriano encontrado: ");
        print(ciclo);
        return
    texto += "}";
    print(texto);
    return

