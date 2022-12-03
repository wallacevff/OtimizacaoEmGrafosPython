class Fila:
    def __init__(self):
        self.fila = [];
        self.tamanho = 0;
    
    def enfileirar(self, item):
        self.fila.append(item);
        self.tamanho = self.tamanho + 1;
    
    def desenfileirar(self):
        self.tamanho = self.tamanho - 1;
        return self.fila.pop(0);
    
    def primeiro(self):
        top = self.fila[0]
        return top;
    
    def ultimo(self):
        top = self.fila[self.tamanho - 1];
        return top;

    def __str__(self):
        txt = "[";
        if(self.tamanho == 0):
            return "[]";
        for i in range(0, self.tamanho, 1):
            if(i < self.tamanho - 1):
                txt += "{valor}, ".format(valor = self.fila[i]);
            else:
                 txt += "{valor}]".format(valor = self.fila[i]);
        return txt;