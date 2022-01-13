from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox as mb

from tkcalendar import Calendar, DateEntry

import sqlite3

janela=Tk ()
#Funções


# INICIO DA FUNÇÃO DA TELA DE CRIAR SOLICITAÇÃO --------------------------------------------------------

def nova():
    # janela.destroy()
    janela = Toplevel()

    # from  solicitacoesUsuario import main_usuario
    with sqlite3.connect("details.db") as db:
        cursor=db.cursor()
    

    def add_novo_solicitacao():
        newReq = comboReq.get()
        newTipoReq = comboTipo.get()
        newDescricao = descricao.get("1.0" ,END)
        newLocal = local.get()
        newSala = sala.get()
        newSetor=setor.get()
        newAprovacao=aprovacao.get()
        newDataAbertura = dataAbertura.get()
        newStatus = status.get()
        newPrioridade = prioridade.get()
        newNivel=nivel.get()
        newDataFechamento = dataFechamento.get()
        newTecnico=tecnico.get()
        newFeedback=feedback.get()
        newSolucao=solucao.get()
        newInteracaoUsuario=interacaoUsuario.get()
        newIneracaoTecnico=interacaoTecnico.get()
    
    


        cursor.execute("INSERT INTO solicitacao(requisicao,tipo,descricao,local,sala,setor,aprovacao,dataAbertura,status,prioridade,nivel,previsao,tecnico,feedback,solucao,interacaoUsuario,interacaoTecnico) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (newReq,newTipoReq,newDescricao,newLocal,newSala,newSetor,newAprovacao,newDataAbertura,newStatus,newPrioridade,newNivel,newDataFechamento,newTecnico,newFeedback,newSolucao,newInteracaoUsuario,newIneracaoTecnico))
        db.commit() 
        messagebox.showinfo(message="Solicitação realizado com sucesso")
        db.close() 

        janela.destroy()
        # from main_usuario import solicitacoesUsuario
    


#Funções

    def uv():
            janela.destroy()
            from main_usuario import solicitacoesUsuario

    def cancelar():
            janela.destroy()
            from main_usuario import solicitacoesUsuario


#importar imagens

    img_fundo =PhotoImage(file="image\\nova-solicitação.png")
    img_botao =PhotoImage(file="image\\salvar.png")
    img_botao1 =PhotoImage(file="image\\voltar.png")
    img_botao2 =PhotoImage(file="image\\cancelar.png")

    #img_fundo =PhotoImage(file="/Users/jm/Desktop/Python/image/nova-solicitacao.png")
    #img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/salvar.png")
    #img_botao1 =PhotoImage(file="/Users/jm/Desktop/Python/image/voltar.png")
    #img_botao2 =PhotoImage(file="/Users/jm/Desktop/Python/image/cancelar.png")
 

#criação de labels

    lab_fundo = Label(janela, image=img_fundo)
    lab_fundo.pack()

#Criação de caixas de entrada

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    comboReq = ttk.Combobox(janela,font=("arial", 15), values=["Hardware", " " , "Software","Redes","Banco de dados","Aplicações web" ],state="readonly")
    print(dict(comboReq)) 
    comboReq.current(1)
    comboReq.place(width=212, height=45, x=225, y=202)


    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    comboTipo = ttk.Combobox(janela,font=("arial", 15), values=["Mouse " , " ", "Teclado","Monitor","Teclado e Mouse wirelles","Headset","Webcam","Mouse Pad","Nobreak" ],state="readonly")
    print(dict(comboTipo)) 
    comboTipo.current(1)
    comboTipo.place(width=200, height=45, x=520, y=202)


    descricao = Text(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    descricao.place(width=496, height=230, x=225, y=273)


    local = Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    local.place(width=175, height=45, x=226, y=529)

    sala= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    sala.place(width=140, height=45, x=580, y=529)


    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    setor = ttk.Combobox(janela,font=("arial", 15), values=["Adm" , " " , "D. Pessoal" , "Compras","Engenharia","Qualidade","Produção","Almoxarifado","Segurança do Trabalho" ],state="readonly")
    print(dict(setor)) 
    setor.current(1)
    setor.place(width=176, height=45, x=225, y=605)

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    aprovacao = ttk.Combobox(janela,font=("arial", 15), values=["Alberto Roberto" , " " , "Paulo Vitor" , "Bruna Souza","Maria alves","William Souza ","Patricia Lemos","Alessandro","Carla Lobo" ],state="readonly")
    print(dict(aprovacao)) 
    aprovacao.current(1)
    aprovacao.place(width=140, height=45, x=580, y=605)

#dados invisiveis

    dataAbertura = DateEntry(janela, width=12, background='darkblue', foreground='white', borderwidth=2)
    # dataAbertura.config(state='disabled')
    dataAbertura.place(x=3000, y=320, width=300, height=25)

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    status = ttk.Combobox(janela,font=("arial", 15), values=["","Aberto" ],state="readonly")
    print(dict(status)) 
    status.current(1)
    status.place(width=176, height=45, x=3000, y=605)

    prioridade= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    prioridade.place(width=140, height=45, x=3000, y=529)

    nivel= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    nivel.place(width=140, height=45, x=3000, y=529)

    dataFechamento= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    dataFechamento.place(width=140, height=45, x=3000, y=529)

    tecnico= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    tecnico.place(width=140, height=45, x=3000, y=529)

    feedback= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    solucao= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    interacaoUsuario= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    interacaoTecnico= Entry(janela, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))



#criação de botões

    bt_entrar = Button(janela,bd=0, image=img_botao, command=add_novo_solicitacao)
    bt_entrar.place(width=120, height=50, x=40, y=880)

    bt_tecnico = Button(janela,bd=0, image=img_botao1, command=uv)
    bt_tecnico.place(width=100, height=34, x=670, y=35)

    bt_tecnico = Button(janela,bd=0, image=img_botao2, command=cancelar)
    bt_tecnico.place(width=135, height=50, x=168, y=880)

    janela.title("Help Tech - solicitações")
    janela.geometry("800x1000+200+0")
    # janela.iconbitmap("image/icon.ico")
    janela.resizable(0,0)
    janela.mainloop()


# TERMINO DA FUNÇÃO DA TELA DE CRIAR SOLICITAÇÃO --------------------------------------------------------



def uconsult():
    # janela.destroy()
    # from listaSolicitacaoUsuario import main_usuario

    # root = tk.Tk()
    root = Toplevel()

    root.resizable(0,0)
    root.geometry("800x1000+200+0")
    root.iconbitmap("image/icon.ico")

# titulo do grid
    root.title("Lista de Solicitações Usuário")

    with sqlite3.connect("details.db") as db:
        cursor=db.cursor()

# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
    cursor.execute('SELECT * FROM solicitacao ORDER BY prioridade ="Alta" AND status ="Aberto" DESC')

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    tree=ttk.Treeview(root)
    tree.pack()

    tree['show'] = 'headings'

    s = ttk.Style(root)
    s.theme_use("clam")
    s.configure(".", font=('Helvetica', 11))
    s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
    tree["columns"]=("id","requisicao","tipo","descricao","localizacao","sala","setor","aprovacao","dataAbertura","status","Estimativa","tecnico")

#Atribui a largura das colunas no grid
    tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
    tree.column("requisicao", width=60, minwidth=100,anchor=tk.CENTER)
    tree.column("tipo", width=160, minwidth=50,anchor=tk.CENTER)
    tree.column("descricao", width=70, minwidth=80,anchor=tk.CENTER)
    tree.column("localizacao", width=70, minwidth=100,anchor=tk.CENTER)
    tree.column("sala", width=70, minwidth=50,anchor=tk.CENTER)
    tree.column("setor", width=70, minwidth=60,anchor=tk.CENTER)
    tree.column("aprovacao", width=80, minwidth=100,anchor=tk.CENTER)
    tree.column("dataAbertura", width=50, minwidth=80,anchor=tk.CENTER)
    tree.column("status", width=50, minwidth=60,anchor=tk.CENTER)
    tree.column("Estimativa", width=100, minwidth=100,anchor=tk.CENTER)
    tree.column("tecnico", width=100, minwidth=100,anchor=tk.CENTER)



#Atribui os nomes dos títulos nas colunas grid
    tree.heading("id", text="Id",anchor=tk.CENTER)
    tree.heading("requisicao", text="Requisicao",anchor=tk.CENTER)
    tree.heading("tipo", text="Tipo",anchor=tk.CENTER)
    tree.heading("descricao", text="Descricao Problema",anchor=tk.CENTER)
    tree.heading("localizacao", text="Localizacao",anchor=tk.CENTER)
    tree.heading("sala", text="Sala",anchor=tk.CENTER)
    tree.heading("setor", text="Setor",anchor=tk.CENTER)
    tree.heading("aprovacao", text="Aprovacao",anchor=tk.CENTER)
    tree.heading("dataAbertura", text="Abertura",anchor=tk.CENTER)
    tree.heading("status", text="Status",anchor=tk.CENTER)
    tree.heading("Estimativa", text="Estimativa",anchor=tk.CENTER)
    tree.heading("tecnico", text="Tecnico",anchor=tk.CENTER)


#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
    i = 0
    for ro in cursor:
        if ro[0]%2==0:
            tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[12],ro[13]),tags=("even",))
        else:
            tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[12],ro[13]), tags=("odd",))
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

#importar imagens
    img_botao =PhotoImage(file="image\\voltar.png")
    #img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/voltar.png")



# feedback

# Parte de pesquisa de solicitação


    def update():

        conn = sqlite3.connect('details.db')

        c = conn.cursor()
    
        record_id = delete_box.get()

        c.execute("""UPDATE solicitacao SET
        

            feedback = :feedbackUsuario


        
            WHERE id = :id""",
            {

            'feedbackUsuario': feedback_editor.get(),

        
        

            'id': record_id
       
            })
     
        mb.showinfo(message="Feedback recebido com sucesso !") 
     
        conn.commit()
        conn.close()  
        editor.destroy()          


    def edit():

        global editor

        editor = Toplevel()
        editor.title('Editando Registro')
        editor.iconbitmap("image/icon.ico")
        #editor.geometry("1000x1000+200+0")


        #importar imagens
        img_fundo1 =PhotoImage(file="image//feedback.png")
        img_b1 =PhotoImage(file="image\\enviar.png")
        img_b2 =PhotoImage(file="image\\cancelar.png")

        #img_fundo1 =PhotoImage(file="/Users/jm/Desktop/Python/image/feedback.png")
        #img_b1 =PhotoImage(file="/Users/jm/Desktop/Python/image/enviar.png")
        #img_b2 =PhotoImage(file="/Users/jm/Desktop/Python/image/cancelar.png")


        # img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/voltar.png")
        #criação de labels

        lab_fundo = Label(editor, image=img_fundo1)
        lab_fundo.pack()



        conn = sqlite3.connect('details.db')
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("SELECT * FROM solicitacao WHERE id = " + record_id)
        records = c.fetchall()

            # Criando variaveis globais para boxes

        global feedback_editor



# Criação de boxes

        idSolicitacao_editor = Entry(editor,text = "")
        idSolicitacao_editor.place(x=205, y=204, width=395, height=45)

        requisicao_editor = Entry(editor,text = "")
    
        comboTipo_editor = Entry(editor,text = "")
   
        descricaoProblema_editor = Entry(editor,text = "")
        descricaoProblema_editor.place(x=205, y=265, width=395, height=45)

        localizacao_editor = Entry(editor,text = "")
   
        sala_editor = Entry(editor,text = "")
    
        comboSetor_editor = Entry(editor,text = "")
    
        aprovacao_editor = Entry(editor,text = "")
    
        dataAbertura_editor = Entry(editor, width=12)
        dataAbertura_editor.place(x=205, y=586, width=105, height=45)

        comboStatus_editor = Entry(editor, width=12)
        comboStatus_editor.place(x=205, y=327, width=395, height=45)

        feedback_editor = Entry(editor, width=12)
        feedback_editor.place(x=205, y=650, width=395, height=148)

        solucao_editor = Entry(editor, width=12)
        solucao_editor.place(x=205, y=464, width=395, height=100)

        dataFechamento_editor = Entry(editor, width=12)
        dataFechamento_editor.place(x=497, y=586, width=105, height=45)

        tecnico_editor = Entry(editor, width=12)
        tecnico_editor.place(x=205, y=397, width=395, height=45)



        for record in records: 
        
            idSolicitacao_editor.insert(0, record[0])
            requisicao_editor.insert(0, record[1])
            comboTipo_editor.insert(0, record[2])
            descricaoProblema_editor.insert(0, record[3])
            localizacao_editor.insert(0, record[4])
            sala_editor.insert(0, record[5])
            comboSetor_editor.insert(0, record[6])    
            aprovacao_editor.insert(0, record[7])    
            dataAbertura_editor.insert(0, record[8])    
            comboStatus_editor.insert(0, record[9])   
            dataFechamento_editor.insert(0, record[12])  
            tecnico_editor.insert(0, record[13])  
            feedback_editor.insert(0, record[14])
            solucao_editor.insert(0, record[15])  





    # Criando um button para Alterar um registro (função update)
        edit_btn = Button(editor,bd=0, image=img_b1, command=update)
        edit_btn.place(width=110, height=45, x=40, y=880)

        bt_entrar = Button(editor,bd=0, image=img_b2, command=cancelar)
        bt_entrar.place(width=130, height=45, x=160, y=880)
    
        editor.mainloop()

    def cancelar():
        editor.destroy()
        
    def v():
        root.destroy()
        from main_usuario import listaSolicitacaoUsuario





    

# Criando labels da parte de pesquisa


    delete_box_label = Label(root,text = "ID Solicitação:")
    delete_box_label.place(x = 30, y = 250)

    delete_box = Entry(root,text = "")
    delete_box.place(x=150, y=250, width=300, height=25)

    edit_btn = Button(root, text="Pesquisar", command=edit)
    edit_btn.place(x=480, y=250, width=150, height=25)


    voltar = Button(root,bd=0, image=img_botao, command=v)
    voltar.place(width=100, height=45, x=670, y=233)




    root.update()
    root.mainloop()    


def sair():
    janela.destroy()
    from login import main_usuario



#importar imagens

img_fundo =PhotoImage(file="image\\fundo-usuario.png")
img_botao =PhotoImage(file="image\\criar.png")
img_botao1 =PhotoImage(file="image\\consultar.png")
img_botao2 =PhotoImage(file="image\\sair.png")

#img_fundo =PhotoImage(file="/Users/jm/Desktop/Python/image/fundo-usuario.png")
#img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/criar.png")
#img_botao1 =PhotoImage(file="/Users/jm/Desktop/Python/image/consultar.png")
#img_botao2 =PhotoImage(file="/Users/jm/Desktop/Python/image/sair.png")




#criação de labels

lab_fundo = Label(janela, image=img_fundo)
lab_fundo.pack()

#criação de botões

bt_user = Button(janela,bd=0, image=img_botao, command=nova)
bt_user.place(width=120, height=54, x=350, y=350)

bt_tecnico = Button(janela,bd=0, image=img_botao1, command=uconsult)
bt_tecnico.place(width=150, height=54, x=340, y=640)

bt_sair = Button(janela,bd=0, image=img_botao2, command=sair)
bt_sair.place(width=60, height=30, x=710, y=30)


janela.title("Help Tech - Menu usuário ") 
janela.geometry("800x1000+100+0")
janela.resizable(0,0)
janela.iconbitmap("image/icon.ico")
janela.mainloop()