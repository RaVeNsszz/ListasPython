[1,463,15] #lista de nùmeros
["Alice","Ana","Maria","Luiza"]#lista de strings
["pera",45.[5,11]]#a lista n necessarianmente contèm apenas alementos
lista = []#lista vazia
ex:. lista=[1,2,3,4,5]
numerosprimos = [1,3,5,7,23]#[0,1,2,3,4]
print(numerosprimos[2])# vai sempre iniciar na posição 0
numerosprimos[2] = 10 #substitui 5 por 10
print(numerosprimos[2])
print(numerosprimos.index(5))#acessar a posição do valor #qual o indice q 5 esta la em numerosprimos?
lista.append(item)#adicionar no final da lista
#ex: queijos.append("ricota")
# queijos["cheddar","reino",gorgonzola","provolone","ricota"]-> lista[0,1,2,3,4]
lista.insert(pos,item)#add em qualquer posição,sem apagar oq ja tem-> pos=posição
#queilos.insert(2,"brie")vai ficar ->["c","r","brie","g","pro","ri"] ai a lista agr é [0,1,2,3,4,5]

print(queijos[-1])#no caso do incice ter valor negativo, vc pode acessar o valor dentro do indice dessa forma
Operador in em listas #"pergunta" se um elemento está na lista
#ex.: queijos = ["cheddar',"reino,"coalho",'provolone"]
"reino" in queijos # reino está em queijos? True
"gorgonzola" in queijos # Gorgonzola está em queijos? False

for i in queijos: #ler os itens de uma lista
    print(i)#para cada elemento na lista a cada vez q ele rodar, vai ficar andando pelo codigo
    i = "ched"
    i = "reino"
    #cada vez q printar será um novo valor
    #pq n uma variável q faca mais sentido? tipo: para cada queijo na lista queijo faça tal coisa
for queijos in queijos:
    print(queijos) #n muda o valor na lista
#para saber o tamanho da lista:
    len(queijos)
#para modificar itens, é necessário ter controle dos índices(posições)
    numeros = [1,2,3,4,5] #o tamanho é 5
    for i in range(len(numeros)): #ler cada elemento da lista, len de numeros é 5 mesmo q for i in range(5)

        numeros[i]=numeros[i]+2#vai somar cada numero mais 2# a cada passagem ele vai usar o valor do indice para modificar a lista
# i = 0 = 1 + 2 
# i = 1 = 2 + 2
# i = 2 = 3 + 2
# i = 3 = 4 + 2
# i = 4 = 5 + 2

# a nova lista será -> numeros = [3,4,5,6,7]

Particionamento
e se so quisesse usar só parte da lista?

letras = ["a","b","c","d","e","f"]
print(letras[1:3] #-> ["b","c"]item de indice 1 ate a anterior ao indice 3
print(letras[:4]) #-> ["a","b","c","d"] do inicio da lista ate o item anterior ao de indice 4
print(letras[3:]) #-> ["d","e","f"] item de indice 3 ate o fim da lista
sendo negativo vamos do ultimo ate o primeiro
      ex
      letras[-1]#é o primerio de traz pra frente q seria "f"

remove item
    remover o item#sabendo onde ele ta
      letras = ["a","b","c"]
      del letras[1] #sem parenteses mesmo
      print(letras)

    remove mais de um item
      letras = ["a","b","c","d","e","f"]
      del letras[1:5]
      print(letras)# [a,f]
      
    remove mais guarda para imprimir
      letras = ["a","b","c"]
      x = letars.pop(1)#me permite usar o valor depois
      print(letras) ou
      print(x) #para recuperar

      se n passar o indice do pop, apaga o ult item
      y = letras.pop()
      print(letras) 
      print(y)
      #quando n sabe a posição
      remover tal coisa da lita tal
      queijos = ["cheddar","reino","coalho","provolone"]
      queijos.remove("coalho")
      print(queijos)
      # se colocar dnv vai da erro pois ele vai ta removido de la!
      


      
