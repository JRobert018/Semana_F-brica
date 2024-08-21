def soma(a,b):
   return(a+b)

def soma1(a,b):
   a+b

def a(a,b):
   calculo = a + b
   return calculo
print(soma(5,1))#com retorno
print(soma1(2,2))#sem retorno
print(f'resultado = {a(5,5)}')


#parâmetro são as variáveis que são definidas pela função.
#argumentos são os vaores que serão atribuidos as variáeis.

def n(nome,sobrnome):
   return nome, sobrnome
print(n('Roberto','filho'))