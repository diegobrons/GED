import PyPDF2
import os
import shutil

#Pastas
#Pasta raiz dos arquivos
os.chdir(r'C:\Código novo GED\entrada')
#Pasta de destino
dest = (r'C:\Código novo GED\arquivo')
revisar = (r'C:\Código novo GED\conferir')

for f in os.listdir():
    arqu = (f)
#    print(arqu)
    reader = PyPDF2.PdfFileReader (arqu,'rb')  # função para ler o arquivo
    p = reader.getPage(0) #Pegar a página
    texto = p.extractText() # Extrair o conteúdo
    #print(texto)
   
    #Inicio da formatação do texto para salvar
    pos = texto.find("LC")  # Palavra para pesquisar
    pedido = (texto[pos:pos + 8])  # +8 caracteres
    f1 = pedido.strip('LC ') #Excluir o "LC" e deixar os n
    f2 = f1.replace("O","0") #Substituir O por 0
    f3 = f2.replace("I","1") #Substituir i por 1
    f4 = f3.replace(",","conferir")
    f5 = ("LC " + f4)  #Acrescentar LC antes do número do pedido
    

#encontrar o número igual do pedido (NAO FUNCIONA POIS NAO TEM REFERENCIA)
#   comp1 = texto.find(f3)
#   comp2 = (texto[comp1:comp1+20])
#   print (f5 + comp2)
#   print (f5)
       
   
    pos_pag = texto.find ('Página')
    pag = (texto[pos_pag:pos_pag + 8])
#    cli = texto.find ('Cliente')
#    cliente = (texto[cli:cli + 20])
#    print (pag)
#    print(pedido)

# **--MOVER E RENOMEAR--**
 
    arquivo = os.rename(arqu, f5+' ' +pag+'.pdf')
#        if f.startswith ('LC'):
#            shutil.move(arqu,revisar)

