import os
import shutil
#Pastas
os.chdir(r'C:\Gestao pdf\pdf')
dest = (r'C:\Gestao pdf\r')
revisar = (r'E:\Projetos Python\Gestao pdf\conferir')

for f in os.listdir():
	if f.startswith('P'):
		shutil.move(f,dest)
