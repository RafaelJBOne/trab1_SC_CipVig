"""
Trabalho de Sguranca Computacional

Professor: 	Joao Jose Costa Gondim 

Alunos/matriculas:
Pericles Junior de Carvalho 180129520  
Rafael de Jesus Bento Oliveira 190115777

Implementação da cifra de Vigenere
*param texto: str - texto a ser cifrado ou decifrado
*param chave: str - palavra chave utilizada para cifrar ou decifrar o texto
*param modo: str - modo de operação, 'cifrar' ou 'decifrar'
*return: str - texto cifrado ou decifrado

O programa recebe quatro parametros na inicializacao que indicam a operacao a ser executada:
*"c" para cifrar um texto.
*"d" para decifrar um texto
*"i"para mais informacoes de uso do programa.
*"//" para parar o programa

Se a opcao de operacao escolhida for "c" ou "d" serao pedidas duas strings, texto para cifrar ou decifra e palavra chave 
respectivamente

Obs: quando a opcao "d" for escolhida, deve ser fornecido exatamente o texto cifrado na operacao anterior. Caso um texo 
diferente do cifrado, na primeira operacao de cifra, o programa ira apresentar um texto diferente do original cifrado. 
O mesmo serve para o caso de a palavra chave fornecida para decifrar seja diferente da cifra original. 
O programa nao faz diferenciacao de letras maiusculas ou minusculas.
"""
def vigenere(texto, chave, modo):
    
    # Transforma o texto e a chave em maiusculas
    texto = texto.upper()
    texto = "".join(c for c in texto if c.isalnum() or c.isspace())
    chave = chave.upper()
        
    # Cria uma lista com o alfabeto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Inicializa a variavel para armazenar o texto cifrado ou decifrado
    resultado = ''
    
    # Percorre cada letra do texto
    for i in range(len(texto)):
        # Verifica se a letra do texto e uma letra do alfabeto
        if texto[i] in alfabeto:
            # Se for, obtem o indice da letra da chave correspondente
            j = alfabeto.index(chave[i % len(chave)])
            
            # Se o modo for 'cifrar', soma o indice da letra do texto com o indice da letra da chave
            if modo == 'cifrar':
                k = (alfabeto.index(texto[i]) + j) % 26
            # Se o modo for 'decifrar', subtrai o indice da letra do texto pelo indice da letra da chave
            else:
                k = (alfabeto.index(texto[i]) - j) % 26
                
            # Adiciona a letra correspondente ao indice obtido ao resultado
            resultado += alfabeto[k]
        else:
            # Se não for uma letra do alfabeto, adiciona ao resultado sem cifrar ou decifrar
            resultado += texto[i]
    
    return resultado


print("Este programa impementa a cifra de Vigenere")        
# True wilhe para manter fucionamento continuo do programa 
while 1:
    print("Digite uma das opcoes:\n(c) para cifrar | (d) para decifrar | (i) para mais informacoes: | (//) para parar o programa")
    opcao = input(">> ") 

    # Estrutura condicional para fazer o controle das opcoes escolhidas
    match opcao:
        # Cifrar texto
        case 'c':
            texto = input("Digite o texto a ser cifrado:\n>> ")
            chave = input("Digite a chave da cifra\n>> ")
            result = vigenere(texto,chave,"cifrar")
            print(f"\nTexto cifrado:\n>> {result}")
            print("")
        # Decifrar texto
        case 'd':
            texto = input("Digite o texto a ser decifrado:\n>> ")
            chave = input("Digite a palavra chave\n>> ")
            result = vigenere(texto,chave,"decifrar")
            print(f"\nTexto decifrado:\n>> {result}")
            print("")
        # Informacoes de uso
        case 'i':
            print("Devem ser fornecidas duas strings, a primeira sendo o texto original, a segunda sendo uma palavra chave.\nAmbas devem ser compostas por letras do alfabeto portugues sem acentos.")
            print("\nTexto para Cifra: mensagem a ser cifrada.")
            print("\nPalavra Chave: palavra utilizada tanto para realizar a cifra do texto original, quanto para decifra-lo.")
            print("\nEncerrar: digite (//) para encerrar o programa.")
            print("")
        # Opcao de parada
        case '//':
            break
        # Tratativa para input invalido
        case _:
            print("Os parametros validos sao:\n (c) para cifrar um texto\n (d) para decifrar um texto\n (i) para informacoes")
            print("")
            
            
#rvgllakieg
#regulating