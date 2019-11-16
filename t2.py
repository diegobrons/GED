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
    print(arqu)
    reader = PyPDF2.PdfFileReader (arqu,'rb')  # função para ler o arquivo
    p = reader.getPage(0) #Pegar a página
    texto = p.extractText() # Extrair o conteúdo
    print(texto)
    pos = texto.find("LC")  # Palavra para pesquisar
    pedido = (texto[pos:pos + 8])  # +8 caracteres
    pos_pag = texto.find ('Página')
    pag = (texto[pos_pag:pos_pag + 8])
    cli = texto.find ('Cliente')
    cliente = (texto[cli:cli + 20])
    print (pag)
    print(pedido)

    #arquivo = os.rename(arqu, pedido+' ' +pag+'.pdf')
   # if f.startswith ('LC'):
      #  shutil.move(arqu,dest)
