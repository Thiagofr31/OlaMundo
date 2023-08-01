# input é uma função que permite perguntar algo ao ususario
nome = input("Qual é o seu nome? ")

print("Olá, ", nome, ". Tudo bem com você?")

print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d: ",d)

print("Tipo da variavel a: ", type (a)) # tipo inteiro (numeros inetiros)
print("Tipo da variavel b: ", type (b)) # tipo float (números reais)
print("Tipo da variavel c: ", type (c)) # tipo string (alfanumérico)
print("Tipo da variavel d: ", type (d)) # tipo boolean (True ou False)


a = 20
print("a: ", a)
b = "São Paulo"
print("b: ", b)
print("Tipo da variavel a: ", type (a))
print("Tipo da variavel b: ", type (b))

a = input("Informe um número: ")
b = input("Informe outro número: ")
print("a: ", a, "- b: ", b)
print("Tipo da variavel a: ", type(a))
print("Tipo da variavel b: ", type(b))
c = a + b
print("c: ", c)
print("Tipo da variavel c: ", type(c))
d = int(a)
print("d: ",d)
print("Tipo da variavel d: ", type (d))

a = int(input("Informe um número: "))
b = int(input("Informe outro número"))