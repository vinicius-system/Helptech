from tkinter import *
from tkinter import messagebox as mb
import sqlite3

janela = Tk()




#Funções

def y():

    with sqlite3.connect('details.db') as db:
         c = db.cursor()
         u = db.cursor()

    newLogin = en_login.get()
    newSenha = senha.get()
    

#Select na tabela de usuarios para encontrar o login e senha
    c.execute('SELECT perfil , login , senha FROM usuario WHERE login = ? and senha = ? AND perfil = "Técnico"',(newLogin,newSenha))
    u.execute('SELECT perfil , login , senha FROM usuario WHERE login = ? and senha = ? AND perfil = "Usuário"',(newLogin,newSenha))




#Se o usuario e senha estiverem corretos ele irá abrir a pagina de selecão de tec ou usuario
    if c.fetchall():
     
     janela.destroy()
     from main_tecnico import login 
     db.commit()
     db.close()

    elif u.fetchall():  
    
     janela.destroy()
     from main_usuario import login  
     db.commit()
     db.close()

    else:

     mb.showerror(title="Erro",message="Usuario ou senha incorretos")


#variáveis globais
esconda_senha = StringVar()

#importar imagens

img_fundo =PhotoImage(file="image\\fundoLogin.png")
img_botao =PhotoImage(file="image\\entrar.png")


#criação de labels

lab_fundo = Label(janela, image=img_fundo)
lab_fundo.pack()

#Criação de caixas de entrada

en_login = Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15), justify="left")
en_login.place(width=352, height=45, x=238, y=456)

senha = Entry(janela, textvariable=esconda_senha, show="*", bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15), justify="left")
senha.place(width=352, height=45, x=238, y=583)

#criação de botões

entrar = Button(janela,bd=0, image=img_botao, command=y)
entrar.place(width=140, height=50, x=340, y=701)



janela.title("Help Tech - Login")
janela.geometry("800x1000+200+0")
janela.iconbitmap("image/icon.ico")
janela.resizable(width=0, height=0)
janela.mainloop()