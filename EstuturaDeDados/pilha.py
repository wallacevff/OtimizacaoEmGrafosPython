class Pilha:
    def __init__(self):
        self.pilha = [];
        self.tamanho = 0;
    
    def empilha(self, item):
        self.pilha.append(item);
        self.tamanho = self.tamanho + 1;
    
    def desenpilha(self):
        top = self.topo()
        self.tamanho = self.tamanho - 1;
        self.pilha.pop();
        return top;
    
    def topo(self):
        top = self.pilha[self.tamanho - 1];
        return top;

    def __str__(self):
        txt = "[";
        if(self.tamanho == 0):
            return "[]";
        for i in range(self.tamanho - 1, -1, -1):
            if(i > 0):
                txt += "{valor}, ".format(valor = self.pilha[i]);
            else:
                 txt += "{valor}]".format(valor = self.pilha[i]);
        return txt;