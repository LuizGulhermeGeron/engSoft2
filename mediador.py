class MediadorViagem:
    def __init__(self):
        self.tipo_viagem = TipoViagem(self)
        self.preco_viagem = PrecoViagem(self)
        self.distancia_viagem = DistanciaViagem(self)
    
    def iniciar_viagem(self):
        self.tipo_viagem.obter_tipo()
    
    def tipo_selecionado(self, tipo):
        if tipo == "praia":
            self.preco_viagem.obter_preco()
        else:
            self.distancia_viagem.obter_distancia()

    def preco_definido(self, preco):
        self.distancia_viagem.obter_distancia()

    def distancia_definida(self, distancia):
        print("\nInformações da viagem:")
        print("Tipo de viagem:", self.tipo_viagem.tipo)
        print("Preço da viagem:", self.preco_viagem.preco)
        print("Distância da viagem:", self.distancia_viagem.distancia)
        self.recomendar_lugares()

    def recomendar_lugares(self):
        print("\nRecomendações de lugares:")
        if self.tipo_viagem.tipo == "praia":
            if self.preco_viagem.preco < 50000 :
            	print("1. Florianópolis, Brasil")
            else:
                if self.distancia_viagem.distancia < 10000:
                    print("1. Cancún, México")
                else:
                    print("1. Phuket, Tailândia")
        else:
            if self.distancia_viagem.distancia < 10000:
                print("1. Cartagena, Colômbia")
            else:
                print("1. Roma, Itália")
                print("2. Kyoto, Japão")


class TipoViagem:
    def __init__(self, mediador):
        self.mediador = mediador
        self.tipo = None
    
    def obter_tipo(self):
        while True:
            tipo = input("Digite o tipo de viagem (praia, cidade histórica, etc.): ").strip().lower()
            if tipo:
                self.tipo = tipo
                self.mediador.tipo_selecionado(self.tipo)
                break
            else:
                print("Tipo de viagem não pode estar vazio.")


class PrecoViagem:
    def __init__(self, mediador):
        self.mediador = mediador
        self.preco = None
    
    def obter_preco(self):
        while True:
            preco_str = input("Digite o preço da viagem: ").strip()
            try:
                preco = float(preco_str)
                if preco <= 0:
                    print("O preço da viagem deve ser maior que zero.")
                else:
                    self.preco = preco
                    self.mediador.preco_definido(self.preco)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico para o preço.")


class DistanciaViagem:
    def __init__(self, mediador):
        self.mediador = mediador
        self.distancia = None
    
    def obter_distancia(self):
        while True:
            distancia_str = input("Digite a distância da viagem em quilômetros: ").strip()
            try:
                distancia = float(distancia_str)
                if distancia < 0:
                    print("A distância da viagem não pode ser negativa.")
                else:
                    self.distancia = distancia
                    self.mediador.distancia_definida(self.distancia)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico para a distância.")



mediador = MediadorViagem()
mediador.iniciar_viagem()
