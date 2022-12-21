class Grafo:
    def __init__(self, n, m):
        self.N = n; self.M = m;
        self.matrizAdj = [] #Matriz de Adjacencia
        self.matrizInc = [] #Matriz de Incidencia
        self.listaAdj = [] #Lista de Adjacencia
        self.vertices = []; #Vertices do Grafo
        for i in range(0,n):
            self.vertices.append(i + 1);
            self.matrizAdj.append([]);
            self.matrizInc.append([]);
            self.listaAdj.append(i);
            self.listaAdj[i] = [];
            for j in range(0, n):
                self.matrizAdj[i].append(0);
            for k in range(0, m):
                self.matrizInc.append(0);
        
    def inserirListaAdj(self, u, v, direcional):
        self.listaAdj[u - 1].append(v)
        if(direcional != True):
            self.listaAdj[v - 1].append(u)

    def inserirRangeListaAdj(self, direcional):
        for i in range(0, self.M):
            st = input();
            u, v = st.split(" ");
            u = int(u);
            v = int(v);
            self.inserirListaAdj(u, v, direcional);
    
    def imprimirListaAdj(self):
      impressao = "\r\nLista de Adjacência\r\n";
      for i in range(0, len(self.listaAdj)):
        #self.listaAdj[i].sort();
        impressao += "{vertice}".format(vertice = i + 1).rjust(2, " ");
        for j in range(0, len(self.listaAdj[i])):            
            impressao += " -> {vizinho}".format(vizinho = self.listaAdj[i][j]);
        impressao += "\r\n";
      print(impressao);

    def inserirMatrizAdj(self, u, v, direcional):
        if(direcional != True):
            self.matrizAdj[u -1][v- 1] = 1;
            self.matrizAdj[v -1][u- 1] = 1;
        else:
            self.matrizAdj[u -1][v- 1] = 1;
        return;

    def inserirRangeMatrizAdj(self, direcional):
        for i in range(0, self.M):
            st = input();
            u, v = st.split(" ");
            u = int(u);
            v = int(v);
            self.inserirMatrizAdj(u, v, direcional);
        return
    
    def strMatrizAdj(self):
        impressao = "";
        for i in range(0, self.N):
            if(i == 0):
                impressao += "    {linha}  ".format(linha = i + 1);
            else:
                impressao += "{linha}  ".format(linha = i + 1);
        impressao += "\r\n";
        for i in range(0, self.N):
            impressao += "{linha} | ".format(linha = i + 1);
            for j in range(0, self.N):
                impressao += "{coluna}  ".format(coluna = self.matrizAdj[i][j])
            impressao += "\r\n";
        return impressao;

    def imprimirMatrizAdj(self):
        impressao = "\r\nMatriz de Adjacência\r\n";
        for i in range(0, self.N):
            if(i == 0):
                impressao += "     {linha}  ".format(linha = i + 1);
            else:
                impressao += "{linha}  ".format(linha = i + 1);
        impressao += "\r\n";
        for i in range(0, self.N):
            impressao += "{linha}".format(linha = i + 1).rjust(2, " ") + " | ";
            for j in range(0, self.N):
                impressao += "{coluna}  ".format(coluna = self.matrizAdj[i][j]).rjust(2, " ")
            impressao += "\r\n";
        print(impressao)

    def inserirTudo(self, direcional):
        for i in range(0, self.M):
            st = input();
            u, v = st.split(" ");
            u = int(u);
            v = int(v);
            self.inserirMatrizAdj(u, v, direcional);
            self.inserirListaAdj(u, v, direcional);
    
    def pegarVizinhosVertice(self, n):
        return self.listaAdj[n -1];

    def removeArestaListaAdj(self, u, v):
        self.listaAdj[u -1].remove(v);
        self.listaAdj[v - 1].remove(u);
        return;

    def imprimeTudo(self):
        self.imprimirListaAdj();
        self.imprimirMatrizAdj();

    def copiarGrafo(self, g):
        for i in range(0, len(g.listaAdj)):
            for j in range(0, len(g.listaAdj[i])):
                self.listaAdj[i].append(g.listaAdj[i][j]);
        for i in range(0, len(g.matrizAdj)):
            for j in range(0, len(g.matrizAdj[i])):
                self.matrizAdj[i][j] = g.matrizAdj[i][j];


    def __str__(self):
        return self.strMatrizAdj();
