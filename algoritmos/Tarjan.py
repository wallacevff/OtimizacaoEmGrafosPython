from EstuturaDeDados.pilha import Pilha
from classes.Grafo import Grafo;

def CFC (v):
    global cpre;
    cpre = cpre + 1;
    pre[v - 1] = cpre;
    low[v - 1] = cpre;
    vis[v - 1] = 1;
    pilha.empilha(v);
   # print(pilha);
   # print(vis)
    #print("Vizinhos de {} : {}".format(v, g.pegarVizinhosVertice(v)));
    for w in g.pegarVizinhosVertice(v):
        if(pre[w - 1] == 0):
           # print(low)
            CFC(w);
        if(vis[w - 1] == 1):
          #  print("Low de {} : {} --- Low de {} : {}".format(v, low[v - 1], w, low[w - 1]));
            low[v - 1] = min(low[v - 1], low[w - 1]);
           # print("Pilha: {}".format(pilha));
           # print("Pre: {}".format(pre));
           # print("Low: {}".format(low));
           # print("Vis: {}".format(vis));
            #print(low);
    if(low[v - 1] == pre[v - 1]):
        texto = "Novo Componente: [";
        first = True;
        #print("Novo Componente:");
        while(True):
            p = pilha.desempilha();
            if(first == True):
                texto += "{}".format(p);
                #print("{}".format(p));
                first = False;
            else:
                texto += " {}".format(p);
                #print(" {}".format(p));
            if(p == v):
                texto += "]";
                print(texto + "\r\n");
                break;
            vis[p - 1] = 0;
def Tarjan(grafo : Grafo):
    global g;
    global cpre;
    global pre;
    global low;
    global vis;
    global pilha;
    pilha = Pilha();
    low = [];
    pre = [];
    vis = [];
    cpre = 0;
    g = grafo;

    for i in range(0, g.N):
        pre.append(0);
        low.append(0);
        vis.append(0);
    
    for vertice in g.vertices:
        if pre[vertice - 1] == 0:
            CFC(vertice);
    #print(low)