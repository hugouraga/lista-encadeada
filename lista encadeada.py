class No:
    def __init__(self,item = None,proximo = None):
        self.item = item
        self.proximo = proximo
class Lista:
    def __init__(self):
        self.primeiro = self.ultimo = No()
    def vazia(self):
        return self.primeiro == self.ultimo
    def inserir(self,item):
        self.ultimo.proximo = No(item)
        self.ultimo = self.ultimo.proximo
    def inserirInicio(self, item):
        self.primeiro.proximo = No(item,self.primeiro.proximo)
        if self.vazia():
            self.ultimo = self.primeiro.proximo
    def inserirOrdenado(self,item):
        if vazia():
            self.inserir(item)
        anteiror = self.primeiro
        atual = self.primeiro.proximo
        while not atual is None and atual.item < item:
            anterior = atual
            atual = anteiror.proximo
        anterior.proximo = No(item,atual)
        if atual is None:
            self.ultimo = anteiror.proximo
    def pesquisa(self, item):
        aux = self.primeiro.proximo
        while not aux in None and aux.item != item:
            aux = aux.proximo
        return aux is None and None or aux.item
    def removerInicio(self):
        if self.vazia():
            return None
        aux = self.primeiro.proximo
        self.primeiro.proximo = aux.proximo
        item = aux.item
        if aux == self.ultimo:
            self.ultimo = self.primeiro
        aux.proximo = None
        del aux
        return item
    def removerFim(self):
        if self.vazia():
            return None
        aux = self.primeiro
        while aux.proximo != self.ultimo:
            aux = aux.proximo
        item = self.ultimo.item
        ultimo = aux
        aux = ultimo.proximo
        ultimo.proximo = None
        del aux
        return item
