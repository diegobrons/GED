#
#		TESTE DE CONDIÇÕES IF PARA RESOLVER O PROBLEMA DA 
#					FORMATAÇÃO DO CAMPO PÁGINA.
#
#_______________________Módulos para importar________________________
#
import PyPDF2
import os
import shutil
#
#//_____________________Estrutura das pastas_________________________
#
#						Pasta raiz dos arquivos.
os.chdir(r'\\SERVIDOR\Users\Public\Código GED\PDF\Entrada')
#						Pasta de destino
dest = (r'\\SERVIDOR\Users\Public\Código GED\PDF\Arquivo')
#						Revisão de arquivos.
revisar = (r'\\SERVIDOR\Users\Public\Código GED\PDF\Revisão')
#
#________________________Começo do código _____________________________
#
#	Essa seção do código acessa a pasta onde estão os arquivos 
#	Define uma variável com eles e utiliza a biblioteca PyPDF2 
#	Para acessar e ler o conteúdo dos pedidos.
#
for f in os.listdir(): # Para os arquivos na pasta os.chdir
    arqu = (f) # Define f em 'arqu'.
    # print(arqu) # Pode ser utilizado para demonstrar o processo.
    reader = PyPDF2.PdfFileReader (arqu,'rb') # Acesso ao pdf.
    p = reader.getPage(0) # Ler texto da pág.
    texto = p.extractText() # Extrair o conteúdo.
#print(texto) #Esta parte pode ser utilizada para ver como o módulo 
#	está lendo o documento.
#
# ______________________Pesquisando no documento.___________________
#	Nesta parte defini o termo "LC" como referência para pesquisar o
# Número do pedido e substituir alguns caracteres que estão sendo 
# mal interpretados pelo código.
#
#
#                   PESQUISAR NÚMERO DO PEDIDO                       
#
    pos = texto.find("LC")  # Palavra para pesquisar
    pedido = (texto[pos:pos + 8])  # +8 caracteres
    f1 = pedido.strip ('LC ') #Excluir o "LC" e deixar os n
    f2 = f1.replace ("O","0") #Substituir O por 
    f3 = f2.replace ("I","1") #Substituir i por 1
    f4 = f3.replace (",","")
    f5 = f4.replace (".","")
    f6 = f5.replace (" ","")
    f7 = f6.isalnum()
    f8 = ("LC " + f6)  #Acrescentar LC antes do número do pedido
    # print (f7,f8)
    
                    # PESQUISAR PÁGINA DO PEDIDO                       
    pos_pag = texto.find ('Página')
    pag = (texto[pos_pag:pos_pag + 11])
    t1 = pag.strip ('Página ')
    t2 = t1.replace ('.','')
    t3 = t2.replace ('d','')
    t4 = t3.replace ('l','1')
    t5 = t4.replace ('i','1')
    t6 = t5.replace ('d','')
    t7 = t6.replace ("e","")
    t8 = t7.replace ("I","1")
    t9 = t8.replace ("L","1")
    t10 = t9.replace ("11","1")
    t11 = t10,int()
    t12 = t11.isalnum()
    # t8 = ('Página '+ t7)
    print (t9,t12)
#_____________________MOVER E RENOMEAR________________________________
#
#	Esta parte do código é responsavel por identificar o que vai para
# onde, levando em consideração as regras if e else . 
#
#
#   arquivo = os.rename(arqu, f5+' ' +pag+'.pdf')
#if f.startswith ('LC'):
#shutil.move(arqu,revisar)









