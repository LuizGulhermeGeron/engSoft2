class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def dirigir(self):
        pass

class Compacto(Carro):
    def dirigir(self):
        print("Dirigindo um carro compacto.")

class Sedan(Carro):
    def dirigir(self):
        print("Dirigindo um sedan.")

class SUV(Carro):
    def dirigir(self):
        print("Dirigindo um SUV.")

class FabricaCarros:
    def produz_carro(self, tipo, modelo, cor):
        if tipo == "compacto":
            return Compacto(modelo, cor)
        elif tipo == "sedan":
            return Sedan(modelo, cor)
        elif tipo == "suv":
            return SUV(modelo, cor)
        else:
            raise ValueError("Tipo de carro inválido.")

class Cliente:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def dirigir_carro(self, tipo, modelo, cor):
        carro = self.fabrica.produz_carro(tipo, modelo, cor)
        carro.dirigir()

fabrica = FabricaCarros()
cliente = Cliente(fabrica)

cliente.dirigir_carro("compacto", "Ford Fiesta", "azul")
cliente.dirigir_carro("sedan", "Toyota Corolla", "prata")
cliente.dirigir_carro("suv", "Jeep Wrangler", "verde")
