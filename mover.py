import os
import shutil

#Pasta raiz dos arquivos
os.chdir(r'C:\Código novo GED\entrada')
#Pasta de destino
dest = (r'C:\Código novo GED\arquivo')
revisar = (r'C:\Código novo GED\conferir')


#for f in os.listdir():
#	if f.startswith('LC'):
#		shutil.move(f,dest)
for f in os.listdir():
	if f.startswith('LC  '):
		shutil.move(f,revisar)
for f in os.listdir():
	if f.startswith('LC P'):
		shutil.move(f,revisar)
