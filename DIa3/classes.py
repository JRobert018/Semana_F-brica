class Carro:
   def __init__(self,modelo,marca,cor):
      #Definição dos atributos da classe.
      self.modelo = modelo
      self.marca = marca 
      self.cor = cor

   #Funções da classe
   def acelerar(self):# O comando self serve para referênciar ao própio obejto.
      print(f"{self.modelo} acelerou 90km!")

   def frear(self):
      print(f"{self.modelo} freou!")
   
class Caminhao(Carro):
   def buzinar(self):
      print(f"{self.modelo} buzinou!")

#Definindo os detalhes 
onix = Carro(marca="GM",modelo="Onix",cor="Branco")
chain = Caminhao(marca="GM",modelo="Scania",cor="Preto")

onix.acelerar()
chain.buzinar()

print(f"detalhes do caminão:{chain.marca},{chain.cor}")
print(onix.modelo)