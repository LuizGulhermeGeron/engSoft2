

class BancoDeDados:
    def __init__(self):
        self.buffer = ["Carro 1","Carro 2"]

    def limparBuffer(self):
        self.buffer = []
        print("Buffer limpo.")

    def listar(self, entidade):
        if entidade == "carro":
            if self.buffer == []:
                self.buffer = ["Carro 33"]
                return ["Carro 33"]
            else:
                return self.buffer

class ProxyBancoDeDados:
    def __init__(self):
        self.bancoDeDados = BancoDeDados()

    def limparBuffer(self):
        self.bancoDeDados.limparBuffer()

    def listar(self, entidade):
        self.bancoDeDados.limparBuffer()
        return self.bancoDeDados.listar(entidade)

class CRUDCarro:
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def listar(self):
         for carro in self.bancoDeDados.listar("carro"):
             print(carro)

bd = BancoDeDados()
pbd = ProxyBancoDeDados()
cc = CRUDCarro(pbd)
cc.listar()