import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb

# from tkcalendar import Calendar, DateEntry
import sqlite3

root = tk.Tk()
root.resizable(0, 0)
root.geometry("800x1000+200+0")
root.iconbitmap("image/icon.ico")


# titulo do grid
root.title("Lista de Usuários")

with sqlite3.connect("details.db") as db:
    cursor=db.cursor()

# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
cursor.execute('SELECT * FROM usuario')

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tree=ttk.Treeview(root)
tree.pack()

tree['show'] = 'headings'

s = ttk.Style(root)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
tree["columns"]=("id","nome","email","setor","perfil","matricula","ramal")

#Atribui a largura das colunas no grid
tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
tree.column("nome", width=160, minwidth=60,anchor=tk.CENTER)
tree.column("email", width=160, minwidth=60,anchor=tk.CENTER)
tree.column("setor", width=70, minwidth=70,anchor=tk.CENTER)
tree.column("perfil", width=70, minwidth=100,anchor=tk.CENTER)
tree.column("matricula", width=70, minwidth=100,anchor=tk.CENTER)
tree.column("ramal", width=70, minwidth=70,anchor=tk.CENTER)


#Atribui os nomes dos títulos nas colunas grid
tree.heading("id", text="Id",anchor=tk.CENTER)
tree.heading("nome", text="Nome",anchor=tk.CENTER)
tree.heading("email", text="Email",anchor=tk.CENTER)
tree.heading("setor", text="Setor",anchor=tk.CENTER)
tree.heading("perfil", text="Perfil",anchor=tk.CENTER)
tree.heading("matricula", text="Matricula",anchor=tk.CENTER)
tree.heading("ramal", text="Ramal",anchor=tk.CENTER)

#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
i = 0
for ro in cursor:
	if ro[0]%2==0:
		tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]),tags=("even",))
	else:
		tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]), tags=("odd",))
	i = i + 1

#  Cor de fundo dos quadrados do grid
tree.tag_configure("even",foreground="black",background="white")
tree.tag_configure("odd",foreground="black",background="white")

# Scrollbar para ajudar na visualicação caso o grid seja enorme
hsb = ttk.Scrollbar(root,orient="horizontal")
hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side = BOTTOM)

vsb = ttk.Scrollbar(root,orient="vertical")
vsb.configure(command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side = RIGHT)


#Função de alterar os dados na tabela (OBS: SÓ IRÁ ALTERAR O CAMPO DE TÉCNICO E STATUS !)

def update():

    conn = sqlite3.connect('details.db')

    c = conn.cursor()
    
    record_id = delete_box.get()

    c.execute("""UPDATE usuario SET
        
        login = :mudancaLogin,
        senha = :mudancaSenha
        
        WHERE id = :id""",
        {
        'mudancaLogin': login_editor.get(),
        'mudancaSenha': senha_editor.get(),

        'id': record_id
       
        })
     
    mb.showinfo(message="Usuário Alterado com sucesso !") 
     
    conn.commit()
    conn.close()  
    editor.destroy()          


def edit():

    global editor



    editor = Toplevel()
    editor.title('Editando Registro')
    editor.iconbitmap("image/icon.ico")
    editor.resizable(0,0)
    #editor.geometry("1000x800")
    
   
    #importar imagens
    

    img_fundo =PhotoImage(file="image//cadastro-fundo.png")
    img_botao =PhotoImage(file="image\\salvar.png")
    img_b3 =PhotoImage(file="image//excluir.png")
    img_b2 =PhotoImage(file="image\\cancelar.png")
    lab_fundo = Label(editor, image=img_fundo)
    lab_fundo.pack()


    conn = sqlite3.connect('details.db')



    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("SELECT * FROM usuario WHERE id = " + record_id)
    records = c.fetchall()

# Variaveis globais

    global login_editor
    global senha_editor
    global id_editor


#Criação de caixas de entrada

    nome_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    nome_editor.place(width=645, height=45, x=80, y=290)

    email_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    email_editor.place(width=645, height=45, x=80, y=385)

    setor_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    setor_editor.place(width=300, height=45, x=80, y=490)

    perfil_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    perfil_editor.place(width=300, height=45, x=420, y=490)

    matricula_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    matricula_editor.place(width=300, height=45, x=420, y=595)

    ramal_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    ramal_editor.place(width=300, height=45, x=77, y=595)

    login_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    login_editor.place(width=320, height=45, x=80, y=845)

    senha_editor = Entry(editor,show="*", bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    senha_editor.place(width=295, height=45, x=425, y=845)

    id_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))


    for record in records: 
       
        id_editor.insert(0, record[0])
        nome_editor.insert(0, record[1])
        email_editor.insert(0, record[2])
        setor_editor.insert(0, record[3])
        perfil_editor.insert(0, record[4])
        matricula_editor.insert(0, record[5])
        ramal_editor.insert(0, record[6])    
        login_editor.insert(0, record[7])    
        senha_editor.insert(0, record[8])
           


    bt_entrar = Button(editor,bd=0, image=img_botao, command=update)
    bt_entrar.place(width=100, height=45, x=80, y=900)

    bt_excluir = Button(editor,bd=0, image=img_b3, command=excluir)
    bt_excluir.place(width=100, height=45, x=190, y=900)

    bt_cancelar = Button(editor,bd=0, image=img_b2, command=cancelar)
    bt_cancelar.place(width=130, height=45, x=300, y=900)



    editor.mainloop()
def cancelar():
    root.destroy()
    from listaEditUsuario import EditandoRegistro

 #Função de Excluir os dados na tabela (OBS: SÓ IRÁ ALTERAR O CAMPO DE TÉCNICO E STATUS !)   


def excluir():
    conn = sqlite3.connect('details.db')
    c = conn.cursor()
    
    c.execute("DELETE from usuario WHERE  id = " + id_editor.get())

    id_editor.delete(0, END)

    mb.showinfo(message="Usuário Excluido com sucesso !") 


    conn.commit()
    conn.close()
    editor.destroy()


def voltar2():
    root.destroy()
    from main_tecnico import listaEdit

    

# Criando labels da parte de pesquisa

delete_box_label = Label(root,text = "ID Usuário:")
delete_box_label.place(x = 174, y = 250)

delete_box = Entry(root,text = "")
delete_box.place(x=290, y=250, width=300, height=25)


#imagem de voltar
img_botao1 =PhotoImage(file="image//voltar.png")



# Criando um button de Update
edit_btn = Button(root, text="Pesquisar", command=edit)
edit_btn.place(x=290, y=320, width=300, height=25)

#botão de voltar
voltar2 = Button(root,bd=0, image=img_botao1, command=voltar2)
voltar2.place(width=100, height=45, x=685, y=940)







root.update()
root.mainloop()