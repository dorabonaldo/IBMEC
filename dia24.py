print ("Olá", "mundo")

print ("Olá", "mundo", sep="-")

print ("Olá", "python", end="!\n")

print ("2023", "04", "18", sep="/")

print ("nome", "sobrenome", "email", sep=";")

print ("loading", end= " ")
print ("[OK]")

nome = input ("entre com o seu nome: ")

print ("Olá", nome) 

itens = input ("digite itens separaos por vírgula: ").split(",")

print ("itens:", itens)

idade = input ("me diga sua idade: ")
idade = int(idade)

print("Daqui a cinco anos, você terá", idade + 5, "anos.")

