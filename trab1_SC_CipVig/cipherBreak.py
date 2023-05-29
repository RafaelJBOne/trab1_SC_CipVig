import unicodedata


#entrada text desafio 1
print("                Texto Desafio II- Análise de Frequência                  ")
texto= "rvgllakieg tye tirtucatzoe.  whvnvvei i winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg, drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl.  wzty a pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis.  zf khep blt keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv."



#tratamento das entradas

palavra1= texto.upper()
texto_sem_pontuacao = "".join(c for c in palavra1 if c.isalnum() or c.isspace())
texto_sem_espacos1 = texto_sem_pontuacao.strip()
texto_sem_espacos = texto_sem_espacos1.replace(" ", "")
texto_sem_acentos = ''.join((c for c in unicodedata.normalize('NFD', texto_sem_espacos) if unicodedata.category(c) != 'Mn'))
senha = []

# Impressão Texto Original
print("1)Texto original:                                            ")
print("                                                           ")
print(texto)

# Impressão das quantidade de palavras
palavras = palavra1.split()
contagem2 = len(palavras)
print("Número de palavras no texto original: ",contagem2)
print("                                                           ")

# Impressão Texto Tratado
print("2)Texto sem espaços, em branco, sem pontuacao e sem acentos: ")                                                                  
print("                                                           ")
print(texto_sem_acentos)
print("                                                           ")


# Cria um dicionário vazio para armazenar a contagem de cada letra
contagem = {} 

# Percorre o texto e atualiza a contagem de cada letra
for letra in texto_sem_acentos:
    if letra.isalpha(): # Verifica se a letra é uma letra do alfabeto
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

 
ocorrenciatotal=0
itens=0

# Imprime a contagem de cada letra 
print("3)Análise de frequencia dos caracteres.")
print("                                                             ")
for letra, ocorrencias in contagem.items():
    print("A letra '{}' aparece {} vezes no texto.".format(letra, ocorrencias))
    ocorrenciatotal = ocorrenciatotal+ocorrencias
    itens = itens+1
print("                                                             ")
print("3.1)Frequência dos caracteres em Dicionário (contagem)       ")
print("                                                             ")
print(contagem)
print("                                                             ")

# Imprime a lista ordenda de tuplas 
ordenado=[]
print("                                                             ")
print("4)Frenquência de caracteres em lista de tuplas(Indice,letra):") 
print("                                                             ")

for i in sorted(contagem, key = contagem.get):
    ordenado_contagem= i ,contagem[i]
    ordenado.append(ordenado_contagem)
    
print (ordenado) 

# Imprime a ocorrência das letras em inglês
ordenado_ingles=[]
ordenado_contagem1=[]
ordenado_inglesoc=[]
print("                                                             ")
print("5)Frenquência caracteres da ocorrência (Texto,Inglês) :")
print("                                                             ")
ordenado_ingles=["Z","Q","X","J","K","V","B","P","Y","G","F","W","M","U","C","L","D","R","H","S","N","I","O","A","T","E"]
      
for i in range(len(ordenado)):
    ordenado_contagem1= ordenado[i][0], ordenado_ingles[i]
    ordenado_inglesoc.append(ordenado_contagem1)
    
print (ordenado_inglesoc)
print("                                                             ")
print("As cinco maiores frequência (E,I,T,R,V) podem estar formando um padrão")


# Passos para achar a possibilidade de chaves

# Inserir o tanaho da chave

tamanho_senha= int(input("Favor inserir tamanho da chave: " ))

for pos in range(0,tamanho_senha,1):
   primeira=[]
   ordenado_multiplo=[]
   for letra in range(pos,len(texto_sem_acentos),5):
       primeira.append(texto_sem_acentos[letra])
   print("                                                           ")    
   print("6)Lista de letras", pos+1 ,"posição e seus múltiplos com:",len(primeira),"elementos")
   print("                                                           ")
   print(primeira)
   #print("                                                           ")
   for i in range(0,len(primeira),1):
       for y in range(0,len(ordenado_inglesoc),1):
           if ordenado_inglesoc[y][0] == primeira[i]:
              ordenado_multiplo.append(ordenado_inglesoc[y])
   print("6.1)Lista de tupla(texto,inglês) da", pos+1,"e seus múltiplos com:",len(ordenado_multiplo),"elementos")           
   print(" Ordenado multiplo                                         ")
   print (ordenado_multiplo)
   print("                                                           ")
   
    
#conversão da tupla(texto,ingles) na chave
   print("7)Lista de tupla(texto,inglês)da",pos+1,"posição da chave e seus múltiplos")
   lista2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
   
   
   print("8)Entrada na rotina achachave com atupla(texto,inglês)da",pos+1,"posição da chave e seus múltiplos")
   lista_chaves=[]
   lista_posicao=[]
   lista_chave=[]
   lista_cont=[]
   chave_list=[]
   cont1=[]
   cont=[]
   conta=0;contb=0;contc=0;contd=0;conte=0;contf=0;conth=0
   contg=0;contt=0;conti=0;contj=0;contk=0;contl=0;contm=0
   contn=0;conto=0;contp=0;contq=0;contr=0;conts=0;contv=0
   contw=0;contu=0;contx=0;conty=0;contz=0;contfora=0
   
   for i in range(0,len(ordenado_multiplo),1):
       indice_texto = lista2.index(ordenado_multiplo[i][0])
       indice_ingles = lista2.index(ordenado_multiplo[i][1])
       indice_chave = (indice_texto-indice_ingles)%26
       indice_chavefinal=indice_chave
       chave=(lista2[indice_chavefinal])
       #print("Texto.C","Ingles","Chave")
       #print(ordenado_multiplo[i][0],"     ",ordenado_multiplo[i][1],"     ",chave  )
       #print("                                                          ")
       lista_chaves.append(chave)

   print(f"listas de chaves: {lista_chaves}")
   for i in range(0,len(lista_chaves),1):
       if lista_chaves[i] =="A":
               conta+= 1
       elif lista_chaves[i]=="B":
               contb+= 1
       elif lista_chaves[i]=="C":
               contc+= 1
       elif lista_chaves[i]=="D":
               contd+= 1
       elif lista_chaves[i]=="E":
               conte+= 1
       elif lista_chaves[i]=="F":
               contf+= 1
       elif lista_chaves[i]=="G":
               contg+= 1
       elif lista_chaves[i]=="H":
               conth+= 1
       elif lista_chaves[i]=="I":
               conti+= 1
       elif lista_chaves[i]=="J":
               contj+= 1
       elif lista_chaves[i]=="K":
               contk+= 1
       elif lista_chaves[i]=="L":
               contl+= 1
       elif lista_chaves[i]=="M":
               contm+= 1
       elif lista_chaves[i]=="N":
               contn+= 1
       elif lista_chaves[i]=="O":
               conto+= 1
       elif lista_chaves[i]=="P":
               contp+= 1
       elif lista_chaves[i]=="Q":
               contq+= 1
       elif lista_chaves[i]=="R":
               contr+= 1
       elif lista_chaves[i]=="S":
               conts+= 1
       elif lista_chaves[i]=="T":
               contt+= 1
       elif lista_chaves[i]=="U":
               contu+= 1
       elif lista_chaves[i]=="V":
               contv+= 1
       elif lista_chaves[i]=="W":
               contw+= 1
       elif lista_chaves[i]=="X":
               contx+= 1
       elif lista_chaves[i]=="Y":
               conty+= 1
       elif lista_chaves[i]=="Z":
               contz+= 1
       else:
                contfora+= 1   
    
   lista_posicao=[("A",conta),("B",contb),("C",contc),("D",contd),("E",conte),("F",contf),("G",contg),("H",conth),("I",conti),("J",contj),("K",contk),("L",contl),("M",contm),("N",contn),("O",conto),("P",contp),("Q",contq),("R",contr),("S",conts),("T",contt),("U",contu),("V",contv),("W",contw),("X",contx),("Y",conty),("Z",contz)]         
   print(lista_posicao)
   print("9) Contar a chave de maior ocorrência da", pos+1," posição ")
   lista_ordenada2 = sorted(lista_posicao, key=lambda x: x[1], reverse=True)
   print(lista_ordenada2[0][0])
   senha.append(lista_ordenada2[0][0])
   print(senha)
    
              

