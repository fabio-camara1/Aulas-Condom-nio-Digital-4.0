class Aminal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def Comer(self):
        print(f"o {self.nome} esta comendo")


class Gato(Aminal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def EmitirSom(self):
        print(f"o {self.nome} foi miando")

    def Come(self, comida):
        print(f"o {self.nome} esta comendo {comida} ")


class Cachorro(Aminal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def EmitirSom(self):
        print(f"o {self.nome} foi latir")

    def Come(self, comida):
        print(f"o {self.nome} esta comendo {comida} ")


class Vaca(Aminal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def EmitirSom(self):
        print(f"o {self.nome} foi mugi")


gato = Gato("Janson", "azul")
gato.Come("Peixe")
gato.EmitirSom()
