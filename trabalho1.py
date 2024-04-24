def imprimir_informações(nome, idade, cidade):
    print("nome: ", nome, sep=" ", end="-")
    print("idade: ", idade, sep=" ", end="-")
    print("cidade: ", cidade, end="!")

def operação (): 
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    operação = input("digite a operação desejada (+, -, *, /): ")

    if operação == '+':
        resultado = num1 + num2
    elif operação == '-':
        resultado = num1 - num2
    elif operação == '*':
        resultado = num1 * num2
    elif operação == '/': 
        resultado = num1 / num2
    print("resultado:", resultado )


def itens_lista ():
    itens = input ("insira os itens da lista de compras, separados por virgula: ").split(',')
    print ("itens: ", itens)
    
def conversão_temperatura ():
    grausc = float (input("digite a temperatura em graus celsius: "))
    grausf = (grausc * 9/5) + 32
    print ("a temperatura em graus farenheit é igual a ", grausf)

def pedir_nomes ():
    nomes  = []
    while True:
        nome = input ("lewis hamilton oito vezes campeão mundial (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)
    print ("nomes digitados:")
    for nome in nomes:
        print (nome)
        
