class Bicicleta:
    #metodo construtor
    def __init__(self,cor,modelo,ano,valor):  
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
# definindo comportamento do objeto
    def buzinar(self):
        print("Beeeeeeeeeep!")

    def parar(self): 
        print("Bicicleta parando...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm! Bicicleta correndo!")
# formatando o texto de saida para ficar mais visivel ao usuario
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("verde", "caloi ceci", 1993, 500)
b2 = Bicicleta("rosa", "BMX", 2022, 950)

b1.parar()
b1.correr()
b1.buzinar()

print(b2)
