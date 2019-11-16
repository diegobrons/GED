from tkinter import *
import mover 
import os
import shutil

janela =Tk()
janela.title("Janela Principal")


#Funções 
def bt_click():
	print("Mover LC")
	
	lb["text"] = "Executado"


#Visual
lb= Label(janela, text="Arquivamento de pedidos")
lb.place(x=300,y=10)

bt= Button(janela,
 width=20, text="Ok")
 
bt.place(x=300, y=30)



janela.geometry("800x600+250+50")
#janela.mainloop ()


