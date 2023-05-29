# trab1_SC_CipVig
Implementação da cifra de Vigenere
Programa desafio I: 

O codigo constante no arquivo cifraVig.py contem o algoritmo que impementa um codificador/decodificador baseado na cifra de Vigenere.
para executar o programa segue o comando "python3 -u cifraVig" (o mesmo se aplica para o prgrama cipherBreak), ainda assim é constante
no arquivo zip o arquivo "spec" com os executaveis dos programas.


O programa cifraVig recebe quatro parametros na inicializacao que indicam a operacao a ser executada:
*"c" para cifrar um texto.
*"d" para decifrar um texto
*"i"para mais informacoes de uso do programa.
*"//" para parar o programa

*param texto: str - texto a ser cifrado ou decifrado
*param chave: str - palavra chave utilizada para cifrar ou decifrar o texto
*param modo: str - modo de operação, 'cifrar' ou 'decifrar'
*return: str - texto cifrado ou decifrado

Se a opcao de operacao escolhida for "c" ou "d" serao pedidas duas strings, texto para cifrar ou decifra e palavra chave 
respectivamente

Apos a escolha da opcao desejada, deve ser fornecido o texto a ser cifrado/decifrado seguido de enter para a proxima etapa.
Na sequencia deve ser fornecida uma palavra chave para a criptografia/descriptografia.
As funcoes criptografar e descriptografar possuem os mesmos passos opcao, texto, chave. 

Se a opcao de operacao escolhida for "c" ou "d" serao pedidas duas strings, texto para cifrar ou decifra e palavra chave 
respectivamente

Obs: quando a opcao "d" for escolhida, deve ser fornecido exatamente o texto cifrado na operacao anterior. Caso um texo 
diferente do cifrado, na primeira operacao de cifra, o programa ira apresentar um texto diferente do original cifrado. 
O mesmo serve para o caso de a palavra chave fornecida para decifrar seja diferente da cifra original. 
O programa nao faz diferenciacao de letras maiusculas ou minusculas.


Programa desafio II:

O codigo constante no arquivo cipherBreak.py implementa a quebra da criptografia de Vigenere, baseado na analise de Kasiski.
A analise consiste:
*Mapeamento e contagem de padroes no texto cifrado (como sequencias que se repetem)
*Registro das distancias (medidas em caracteres) para que seja feita uma estimativa do tamanho da chave pelo resultado do 
minimo divisor comum entre as distancias das palavras que sistematicamente se repetem.
*Tenho estimado o temnaho da chave o texto eh dividido em blocos com o tamanho da chave estimada.
*Analisa-se separadamente os caracteres de cada bloco, o primeiro caractere da primeira string com o primeiro caractere da segunda
e assim por diante.
*A estimativa de frequencia dos caracteres que mais se repetem em cada posicao dos blocos cifrados indica os possiveis caracteres 
que compoe a chave da cifra.  

Para que o programa funcione basta que execute-o como citado acima e seja fornecido um numero inteiro como sendo a estimativa do 
tamanho da chave. O objetivo do programa eh receber um texto cifrado, e a partir de analise de frequencia, retornar a chave utilizada
para criptografia. 

Obs: a versao atual do programa cipherBreak, nao esta executando adequadamente o procedimento para descoberta da chave, sendo necessario
que se forneca manualmente a estimativa do tamanho da chave a ser descoberta. Ainda assim a chave apresentada pode nao servir para 
tornar o texto cifrado completamente legivel. 

"""
