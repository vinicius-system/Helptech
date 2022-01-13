from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox as mb

from tkcalendar import Calendar, DateEntry

import sqlite3

janela=Tk ()


# FUNÇÃO DA TELA DE CRIAR UMA SOLICITAÇÃO ------------------------------------------
def novoTicket():
    #janela.destroy()
    #from solicitacoesTecnico import main_tecnico
 
    janela = Toplevel()
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

#Funções

    def uv():
        janela.destroy()
        from main_tecnico import solicitacoesTecnico

    

    def cancelar():
        janela.destroy()
        from main_tecnico import solicitacoesTecnico
    
    #importar imagens

    img_fundo =PhotoImage(file="image\\nova-solicitação.png")
    img_botao =PhotoImage(file="image\\salvar.png")
    img_botao1 =PhotoImage(file="image\\voltar.png")
    img_botao2 =PhotoImage(file="image\\cancelar.png")

    #img_fundo =PhotoImage(file="/Users/jm/Desktop/Python/image/nova-solicitacao.png")
    #img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/salvar.png")
    #img_botao1 =PhotoImage(file="/Users/jm/Desktop/Python/image/voltar.png")
    #img_botao2 =PhotoImage(file="/Users/jm/Desktop/Python/image/cancelar.png")
 
# criação de labels

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
    comboTipo = ttk.Combobox(janela,font=("arial", 15), values=["Mouse C/ Fio" , " ", "Teclado C/ Fio","Monitor","Teclado e Mouse wirelles","Headset","Webcam","Mouse Pad","Nobreak" ],state="readonly")
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
    setor = ttk.Combobox(janela,font=("arial", 15), values=["Adm" , "D. Pessoal" , "Compras","Engenharia","Qualidade","Produção","Almoxarifado","Segurança do Trabalho" ],state="readonly")
    print(dict(setor)) 
    setor.current(1)
    setor.place(width=176, height=45, x=225, y=605)

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    aprovacao = ttk.Combobox(janela,font=("arial", 15), values=["Alberto Roberto" , "Paulo Vitor" , "Bruna Souza","Maria alves","William Souza ","Patricia Lemos","Alessandro","Carla Lobo" ],state="readonly")
    print(dict(aprovacao)) 
    aprovacao.current(1)
    aprovacao.place(width=140, height=45, x=580, y=605)

#dados invisiveis

    dataAbertura = DateEntry(janela, width=12, background='darkblue', foreground='white', borderwidth=2)
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
    janela.iconbitmap("image/icon.ico")
    janela.resizable(0,0)
    janela.mainloop()

  
# TERMINO DA FUNÇÃO DE CRIAR CRIAR UMA SOLICITAÇÃO ------------------------------------------









# FUNÇÃO DA TELA DE CADASTRAR UM USUARIO ------------------------------------------

def cadastro():
    # janela.destroy()

    cadastro = Toplevel()

    with sqlite3.connect("details.db") as db:
        cursor=db.cursor()


    with sqlite3.connect("details.db") as db:
        cursor=db.cursor()

    def add_novo_usuario():
        newNome = nome.get()
        newEmail = email.get()
        newSetor = comboSetor.get()
        newPerfil = comboPerfil.get()
        newMatricula = matricula.get()
        newTelefone = ramal.get()
        newLogin = login.get()
        newSenha = senha.get()

# # TRATAMENTO PARA IMPEDIR QUE HAJA UM CADASTRO COM O MESMO USERNAME NO BANCO
        cursor.execute("SELECT COUNT(*) from usuario WHERE login = '"+ newLogin +"' ")
        result = cursor.fetchone()

        if int(result[0]) > 0:
            error["text"] = "Error: O usuário já possui cadastro no Sistema"
        else:
            
            cursor.execute("INSERT INTO usuario(nome,email,setor,perfil,matricula,ramal,login,senha) VALUES(?,?,?,?,?,?,?,?)",
        (newNome,newEmail,newSetor,newPerfil,newMatricula,newTelefone,newLogin,newSenha))
            db.commit() 
            messagebox.showinfo(message="Usuário cadastrado com sucesso")
            db.close() 
            cadastro.destroy()
        from main_tecnico import cadastro_tecnico
    
    def cancelar():
        cadastro.destroy()
        from main_tecnico import cadastro_tecnico

# Mensagem de erro
    error = Message(text="", width=200)
    error.place(x = 144, y = 5)
    error.config(padx=0)


#variáveis gloabais

    esconda_senha=StringVar()

#importar imagens

    img_fundo =PhotoImage(file="image\\cadastro-fundo.png")
    img_b1 =PhotoImage(file="image\\salvar.png")
    img_b2 =PhotoImage(file="image\\cancelar.png")

    #img_fundo =PhotoImage(file="/Users/jm/Desktop/Python/image/cadastro-fundo.png")
    #img_b1 =PhotoImage(file="/Users/jm/Desktop/Python/image/salvar.png")
    #img_b2 =PhotoImage(file="/Users/jm/Desktop/Python/image/cancelar.png")

#criação de labels

    lab_fundo = Label(cadastro, image=img_fundo)
    lab_fundo.pack()


#Criação de caixas de entrada

    nome = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    nome.place(width=645, height=45, x=80, y=290)

    email = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    email.place(width=645, height=45, x=80, y=385)

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    comboSetor = ttk.Combobox(cadastro, font=("arial", 15), values=["RH", "TI","Admministrativo","D. Pessoal" ],state="readonly")
    print(dict(comboSetor)) 
    comboSetor.current(1)
    comboSetor.place(width=300, height=45, x=80, y=490)

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", bg="#d9d9d9")
    comboPerfil = ttk.Combobox(cadastro, font=("arial", 15), values=["Usuário", "Técnico" ],state="readonly")
    print(dict(comboPerfil)) 
    comboPerfil.current(1)
    comboPerfil.place(width=300, height=45, x=420, y=490)

    matricula = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    matricula.place(width=300, height=45, x=420, y=595)

    ramal = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    ramal.place(width=300, height=45, x=77, y=595)

    login = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    login.place(width=300, height=45, x=80, y=845)

    senha = Entry(cadastro, textvariable=esconda_senha, show="*", bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    senha.place(width=295, height=45, x=425, y=845)

#criação de botões

    bt_entrar = Button(cadastro,bd=0, image=img_b1, command=add_novo_usuario)
    bt_entrar.place(width=100, height=45, x=80, y=897)

    bt_entrar = Button(cadastro,bd=0, image=img_b2, command=cancelar)
    bt_entrar.place(width=130, height=45, x=200, y=897)


    cadastro.title("Help Tech - Cadastro técnico ") 
    cadastro.geometry("800x1000+200+0")
    cadastro.resizable(0,0)
    cadastro.iconbitmap("image/icon.ico")
    cadastro.mainloop()


# TERMINO DA FUNÇÃO DE CADASTRAR UM USUARIO ------------------------------------------


def banco():
    # janela.destroy()
    # from listaSolicitacaoTecnicoFiltroTeste import main_tecnico

    # root = tk.Tk()
    root = Toplevel()
    root.resizable(0, 0)
    root.geometry("800x1000")


# titulo do grid
    root.title("Lista de solicitações")

    with sqlite3.connect("details.db") as db:
        cursor=db.cursor()

# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
    cursor.execute('SELECT * FROM solicitacao ORDER BY status ="Aberto" DESC')

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    tree=ttk.Treeview(root)
    tree.pack()

    tree['show'] = 'headings'

    s = ttk.Style(root)
    s.theme_use("clam")
    s.configure(".", font=('Helvetica', 11))
    s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
    tree["columns"]=("id","requisicao","tipo","descricao","localizacao","sala","setor","aprovacao","dataAbertura","status","prioridade","nivel","Estimativa","tecnico","feedback")

#Atribui a largura das colunas no grid
    tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
    tree.column("requisicao", width=160, minwidth=160,anchor=tk.CENTER)
    tree.column("tipo", width=160, minwidth=160,anchor=tk.CENTER)
    tree.column("descricao", width=70, minwidth=70,anchor=tk.CENTER)
    tree.column("localizacao", width=70, minwidth=100,anchor=tk.CENTER)
    tree.column("sala", width=70, minwidth=100,anchor=tk.CENTER)
    tree.column("setor", width=70, minwidth=70,anchor=tk.CENTER)
    tree.column("aprovacao", width=80, minwidth=80,anchor=tk.CENTER)
    tree.column("dataAbertura", width=30, minwidth=80,anchor=tk.CENTER)
    tree.column("status", width=50, minwidth=50,anchor=tk.CENTER)
    tree.column("prioridade", width=50, minwidth=50,anchor=tk.CENTER)
    tree.column("nivel", width=80, minwidth=100,anchor=tk.CENTER)
    tree.column("Estimativa", width=100, minwidth=120,anchor=tk.CENTER)
    tree.column("tecnico", width=100, minwidth=120,anchor=tk.CENTER)
    tree.column("feedback", width=100, minwidth=120,anchor=tk.CENTER)

#Atribui os nomes dos títulos nas colunas grid
    tree.heading("id", text="id",anchor=tk.CENTER)
    tree.heading("requisicao", text="Requisicao",anchor=tk.CENTER)
    tree.heading("tipo", text="Tipo",anchor=tk.CENTER)
    tree.heading("descricao", text="Descricao",anchor=tk.CENTER)
    tree.heading("localizacao", text="Localizacao",anchor=tk.CENTER)
    tree.heading("sala", text="Sala",anchor=tk.CENTER)
    tree.heading("setor", text="Setor",anchor=tk.CENTER)
    tree.heading("aprovacao", text="Aprovacao",anchor=tk.CENTER)
    tree.heading("dataAbertura", text="DataAbertura",anchor=tk.CENTER)
    tree.heading("status", text="Status",anchor=tk.CENTER)
    tree.heading("prioridade", text="Prioridade",anchor=tk.CENTER)
    tree.heading("nivel", text="Nivel",anchor=tk.CENTER)
    tree.heading("Estimativa", text="Estimativa",anchor=tk.CENTER)
    tree.heading("tecnico", text="Tecnico",anchor=tk.CENTER)
    tree.heading("feedback", text="Feedback",anchor=tk.CENTER)
    


#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
    i = 0
    for ro in cursor:
        if ro[0]%2==0:
            tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]),tags=("even",))
        else:
            tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]), tags=("odd",))
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

        c.execute("""UPDATE solicitacao SET
        
            status = :mudancaStatus,
            prioridade = :mudancaPrioridade,
            nivel = :mudancaNivel,
            previsao = :mudancaDataFechamento,
            tecnico = :assinaturaTecnico

        
            WHERE id = :id""",
            {
            'mudancaStatus': status_editor.get(),
            'mudancaPrioridade': prioridade_editor.get(),
            'mudancaNivel': nivel_editor.get(),
            'mudancaDataFechamento': dataFechamento_editor.get(),
            'assinaturaTecnico': tecnico_editor.get(),
        

            'id': record_id
       
            })
     
        mb.showinfo(message="Solicitação Alterada com sucesso !") 
     
        conn.commit()
        conn.close()  
        editor.destroy()          


    def edit():

        global editor



        editor = Toplevel()
        editor.title('Editando Registro')
        editor.resizable(0, 0)
        editor.iconbitmap("image/icon.ico")
    #editor.geometry("1000x800")
    
   #importar imagens
        img_fundo =PhotoImage(file="image//lista-solicitacao.png")
        lab_fundo = Label(editor, image=img_fundo)
        img_botao =PhotoImage(file="image\\salvar.png")
        img_botao1 =PhotoImage(file="image\\voltar.png")


    
        lab_fundo.pack()


        conn = sqlite3.connect('details.db')



        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("SELECT * FROM solicitacao WHERE id = " + record_id)
        records = c.fetchall()

# Variaveis globais

        global status_editor
        global prioridade_editor
        global nivel_editor
        global dataFechamento_editor
        global tecnico_editor


#Criação de caixas de entrada


        comboReq_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        comboReq_editor.place(width=176, height=45, x=225, y=202)

        comboTipo_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        comboTipo_editor.place(width=176, height=45, x=582, y=202)

        descricao_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        descricao_editor.place(width=530, height=162, x=228, y=275)

        local_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        local_editor.place(width=176, height=45, x=228, y=529)

        sala_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        sala_editor.place(width=176, height=45, x=582, y=532)

        setor_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        setor_editor.place(width=176, height=45, x=228, y=662)

        aprovacao_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        aprovacao_editor.place(width=176, height=45, x=582, y=662)

#dados invisiveis

        dataAbertura_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    # dataAbertura.config(state='disabled')
        dataAbertura_editor.place(width=176, height=45,x=228, y=467 )

        status_editor = Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    # dataAbertura.config(state='disabled')
        status_editor.place(width=176, height=45, x=582, y=722 )

        prioridade_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        prioridade_editor.place(width=176, height=45, x=228, y=600)

        nivel_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        nivel_editor.place(width=176, height=45, x=582, y=600)

        dataFechamento_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        dataFechamento_editor.place(width=176, height=45, x=582, y=467)

        tecnico_editor= Entry(editor, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
        tecnico_editor.place(width=176, height=45, x=228, y=722)

        for record in records: 
        
            comboReq_editor.insert(0, record[1])
            comboTipo_editor.insert(0, record[2])
            descricao_editor.insert(0, record[3])
            local_editor.insert(0, record[4])
            sala_editor.insert(0, record[5])
            setor_editor.insert(0, record[6])    
            aprovacao_editor.insert(0, record[7])    
            dataAbertura_editor.insert(0, record[8])    
            status_editor.insert(0, record[9])
            prioridade_editor.insert(0, record[10])    
            nivel_editor.insert(0, record[11])    
            dataFechamento_editor.insert(0, record[12])  
            tecnico_editor.insert(0, record[13])  



    # Criando um button para Alterar um registro (função update)
    #edit_btn = Button(editor, text="Alterar Registro", command=update)
    #edit_btn.place(width=140, height=45, x=225, y=920)
        bt_entrar = Button(editor,bd=0, image=img_botao, command=update)
        bt_entrar.place(width=100, height=45, x=50, y=920)
        voltar = Button(editor,bd=0, image=img_botao1, command=voltpesq)
        voltar.place(width=100, height=45, x=170, y=920)


        editor.mainloop()


#importar imagens
        img_botao2 =PhotoImage(file="/Users/jm/Desktop/Python/image/voltar.png")



    def voltpesq():
        root.destroy()
    # from listaSolicitacao import EditandoRegistro

    def voltmain():
        root.destroy()
    # from  main_tecnico  import listaSolicitacao


    def pesquisaStatus():

        global editorStatus


        editorStatus = Toplevel()
        editorStatus.resizable(0, 0)
        editorStatus.geometry("1000x800")


# titulo do grid
        editorStatus.title("Lista de solicitações Abertas")


        with sqlite3.connect("details.db") as db:
             cursor=db.cursor()

        record_idStatusAberto = statusAberto_box.get()


# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
        
        cursor.execute("SELECT * FROM solicitacao WHERE status = 'Aberto'" + record_idStatusAberto )
 
    # c.execute("SELECT * FROM solicitacao WHERE id = " + record_id)

        cursor = cursor.fetchall()

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        tree=ttk.Treeview(editorStatus)
        tree.pack()

        tree['show'] = 'headings'

        s = ttk.Style(editorStatus)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
        tree["columns"]=("id","requisicao","tipo","descricao","localizacao","sala","setor","aprovacao","dataAbertura","status","prioridade","nivel","Estimativa","tecnico","feedback")

#Atribui a largura das colunas no grid
        tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
        tree.column("requisicao", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("tipo", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("descricao", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("localizacao", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("sala", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("setor", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("aprovacao", width=80, minwidth=80,anchor=tk.CENTER)
        tree.column("dataAbertura", width=30, minwidth=80,anchor=tk.CENTER)
        tree.column("status", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("prioridade", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("nivel", width=80, minwidth=100,anchor=tk.CENTER)
        tree.column("Estimativa", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("tecnico", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("feedback", width=100, minwidth=120,anchor=tk.CENTER)

#Atribui os nomes dos títulos nas colunas grid
        tree.heading("id", text="id",anchor=tk.CENTER)
        tree.heading("requisicao", text="Requisicao",anchor=tk.CENTER)
        tree.heading("tipo", text="Tipo",anchor=tk.CENTER)
        tree.heading("descricao", text="Descricao",anchor=tk.CENTER)
        tree.heading("localizacao", text="Localizacao",anchor=tk.CENTER)
        tree.heading("sala", text="Sala",anchor=tk.CENTER)
        tree.heading("setor", text="Setor",anchor=tk.CENTER)
        tree.heading("aprovacao", text="Aprovacao",anchor=tk.CENTER)
        tree.heading("dataAbertura", text="DataAbertura",anchor=tk.CENTER)
        tree.heading("status", text="Status",anchor=tk.CENTER)
        tree.heading("prioridade", text="Prioridade",anchor=tk.CENTER)
        tree.heading("nivel", text="Nivel",anchor=tk.CENTER)
        tree.heading("Estimativa", text="Estimativa",anchor=tk.CENTER)
        tree.heading("tecnico", text="Tecnico",anchor=tk.CENTER)
        tree.heading("feedback", text="Feedback",anchor=tk.CENTER)


#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
        i = 0
        for ro in cursor:
            if ro[0]%2==0:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]), tags=("odd",))
            i = i + 1

#  Cor de fundo dos quadrados do grid
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="black",background="white")

# Scrollbar para ajudar na visualicação caso o grid seja enorme
        hsb = ttk.Scrollbar(editorStatus,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(editorStatus,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)


    def pesquisaStatusEmAndamento():

        global editorStatusEmAndamento


        editorStatusEmAndamento = Toplevel()
        editorStatusEmAndamento.resizable(0, 0)
        editorStatusEmAndamento.geometry("1000x800")


# titulo do grid
        editorStatusEmAndamento.title("Lista de solicitações Em Andamento")


        with sqlite3.connect("details.db") as db:
            cursor=db.cursor()



        record_idStatusEmAndamento = statusEmAndamento_box.get()



# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
        
    
        cursor.execute("SELECT * FROM solicitacao WHERE status = 'Em andamento'" + record_idStatusEmAndamento )
    
    # c.execute("SELECT * FROM solicitacao WHERE id = " + record_id)

        cursor = cursor.fetchall()

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        tree=ttk.Treeview(editorStatusEmAndamento)
        tree.pack()

        tree['show'] = 'headings'

        s = ttk.Style(editorStatusEmAndamento)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
        # Definindo o numero de colunas
        tree["columns"]=("id","requisicao","tipo","descricao","localizacao","sala","setor","aprovacao","dataAbertura","status","prioridade","nivel","Estimativa","tecnico","feedback")

#Atribui a largura das colunas no grid
        tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
        tree.column("requisicao", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("tipo", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("descricao", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("localizacao", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("sala", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("setor", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("aprovacao", width=80, minwidth=80,anchor=tk.CENTER)
        tree.column("dataAbertura", width=30, minwidth=80,anchor=tk.CENTER)
        tree.column("status", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("prioridade", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("nivel", width=80, minwidth=100,anchor=tk.CENTER)
        tree.column("Estimativa", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("tecnico", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("feedback", width=100, minwidth=120,anchor=tk.CENTER)

#Atribui os nomes dos títulos nas colunas grid
        tree.heading("id", text="id",anchor=tk.CENTER)
        tree.heading("requisicao", text="Requisicao",anchor=tk.CENTER)
        tree.heading("tipo", text="Tipo",anchor=tk.CENTER)
        tree.heading("descricao", text="Descricao",anchor=tk.CENTER)
        tree.heading("localizacao", text="Localizacao",anchor=tk.CENTER)
        tree.heading("sala", text="Sala",anchor=tk.CENTER)
        tree.heading("setor", text="Setor",anchor=tk.CENTER)
        tree.heading("aprovacao", text="Aprovacao",anchor=tk.CENTER)
        tree.heading("dataAbertura", text="DataAbertura",anchor=tk.CENTER)
        tree.heading("status", text="Status",anchor=tk.CENTER)
        tree.heading("prioridade", text="Prioridade",anchor=tk.CENTER)
        tree.heading("nivel", text="Nivel",anchor=tk.CENTER)
        tree.heading("Estimativa", text="Estimativa",anchor=tk.CENTER)
        tree.heading("tecnico", text="Tecnico",anchor=tk.CENTER)
        tree.heading("feedback", text="Feedback",anchor=tk.CENTER)


#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
        i = 0
        for ro in cursor:
            if ro[0]%2==0:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]), tags=("odd",))
            i = i + 1


#  Cor de fundo dos quadrados do grid
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="black",background="white")

# Scrollbar para ajudar na visualicação caso o grid seja enorme
        hsb = ttk.Scrollbar(editorStatusEmAndamento,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(editorStatusEmAndamento,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)    


    def pesquisaStatusPendente():

        global editorStatusPendente


        editorStatusPendente = Toplevel()
        editorStatusPendente.resizable(0, 0)
        editorStatusPendente.geometry("1000x800")


# titulo do grid
        editorStatusPendente.title("Lista de solicitações Pendentes")


        with sqlite3.connect("details.db") as db:
            cursor=db.cursor()



        record_idStatusPendente = statusPendente_box.get()



# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
        
    
        cursor.execute("SELECT * FROM solicitacao WHERE status = 'Pendente'" + record_idStatusPendente )
    
    # c.execute("SELECT * FROM solicitacao WHERE id = " + record_id)

        cursor = cursor.fetchall()

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        tree=ttk.Treeview(editorStatusPendente)
        tree.pack()

        tree['show'] = 'headings'

        s = ttk.Style(editorStatusPendente)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
        # Definindo o numero de colunas
        tree["columns"]=("id","requisicao","tipo","descricao","localizacao","sala","setor","aprovacao","dataAbertura","status","prioridade","nivel","Estimativa","tecnico","feedback")

#Atribui a largura das colunas no grid
        tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
        tree.column("requisicao", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("tipo", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("descricao", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("localizacao", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("sala", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("setor", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("aprovacao", width=80, minwidth=80,anchor=tk.CENTER)
        tree.column("dataAbertura", width=30, minwidth=80,anchor=tk.CENTER)
        tree.column("status", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("prioridade", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("nivel", width=80, minwidth=100,anchor=tk.CENTER)
        tree.column("Estimativa", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("tecnico", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("feedback", width=100, minwidth=120,anchor=tk.CENTER)

#Atribui os nomes dos títulos nas colunas grid
        tree.heading("id", text="id",anchor=tk.CENTER)
        tree.heading("requisicao", text="Requisicao",anchor=tk.CENTER)
        tree.heading("tipo", text="Tipo",anchor=tk.CENTER)
        tree.heading("descricao", text="Descricao",anchor=tk.CENTER)
        tree.heading("localizacao", text="Localizacao",anchor=tk.CENTER)
        tree.heading("sala", text="Sala",anchor=tk.CENTER)
        tree.heading("setor", text="Setor",anchor=tk.CENTER)
        tree.heading("aprovacao", text="Aprovacao",anchor=tk.CENTER)
        tree.heading("dataAbertura", text="DataAbertura",anchor=tk.CENTER)
        tree.heading("status", text="Status",anchor=tk.CENTER)
        tree.heading("prioridade", text="Prioridade",anchor=tk.CENTER)
        tree.heading("nivel", text="Nivel",anchor=tk.CENTER)
        tree.heading("Estimativa", text="Estimativa",anchor=tk.CENTER)
        tree.heading("tecnico", text="Tecnico",anchor=tk.CENTER)
        tree.heading("feedback", text="Feedback",anchor=tk.CENTER)


#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
        i = 0
        for ro in cursor:
            if ro[0]%2==0:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]), tags=("odd",))
            i = i + 1


#  Cor de fundo dos quadrados do grid
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="black",background="white")

# Scrollbar para ajudar na visualicação caso o grid seja enorme
        hsb = ttk.Scrollbar(editorStatusPendente,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(editorStatusPendente,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)        

    def pesquisaStatusResolvido():

        global editorStatusResolvido


        editorStatusResolvido = Toplevel()
        editorStatusResolvido.resizable(0, 0)
        editorStatusResolvido.geometry("1000x800")


# titulo do grid
        editorStatusResolvido.title("Lista de solicitações Resolvidas")


        with sqlite3.connect("details.db") as db:
            cursor=db.cursor()



        record_idStatusResolvido = statusResolvido_box.get()



# SELECT NA TABELA DE USUARIO DO BANCO PARA PUXAR AS INFORMAÇÕES
        
    
        cursor.execute("SELECT * FROM solicitacao WHERE status = 'Resolvido'" + record_idStatusResolvido )
    
    # c.execute("SELECT * FROM solicitacao WHERE id = " + record_id)

        cursor = cursor.fetchall()

# Importar a biblioteca tree !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        tree=ttk.Treeview(editorStatusResolvido)
        tree.pack()

        tree['show'] = 'headings'

        s = ttk.Style(editorStatusResolvido)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))

# Definindo o numero de colunas
        # Definindo o numero de colunas
        tree["columns"]=("id","requisicao","tipo","descricao","localizacao","sala","setor","aprovacao","dataAbertura","status","prioridade","nivel","Estimativa","tecnico","feedback")

#Atribui a largura das colunas no grid
        tree.column("id", width=40, minwidth=40,anchor=tk.CENTER)
        tree.column("requisicao", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("tipo", width=160, minwidth=160,anchor=tk.CENTER)
        tree.column("descricao", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("localizacao", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("sala", width=70, minwidth=100,anchor=tk.CENTER)
        tree.column("setor", width=70, minwidth=70,anchor=tk.CENTER)
        tree.column("aprovacao", width=80, minwidth=80,anchor=tk.CENTER)
        tree.column("dataAbertura", width=30, minwidth=80,anchor=tk.CENTER)
        tree.column("status", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("prioridade", width=50, minwidth=50,anchor=tk.CENTER)
        tree.column("nivel", width=80, minwidth=100,anchor=tk.CENTER)
        tree.column("Estimativa", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("tecnico", width=100, minwidth=120,anchor=tk.CENTER)
        tree.column("feedback", width=100, minwidth=120,anchor=tk.CENTER)

#Atribui os nomes dos títulos nas colunas grid
        tree.heading("id", text="id",anchor=tk.CENTER)
        tree.heading("requisicao", text="Requisicao",anchor=tk.CENTER)
        tree.heading("tipo", text="Tipo",anchor=tk.CENTER)
        tree.heading("descricao", text="Descricao",anchor=tk.CENTER)
        tree.heading("localizacao", text="Localizacao",anchor=tk.CENTER)
        tree.heading("sala", text="Sala",anchor=tk.CENTER)
        tree.heading("setor", text="Setor",anchor=tk.CENTER)
        tree.heading("aprovacao", text="Aprovacao",anchor=tk.CENTER)
        tree.heading("dataAbertura", text="DataAbertura",anchor=tk.CENTER)
        tree.heading("status", text="Status",anchor=tk.CENTER)
        tree.heading("prioridade", text="Prioridade",anchor=tk.CENTER)
        tree.heading("nivel", text="Nivel",anchor=tk.CENTER)
        tree.heading("Estimativa", text="Estimativa",anchor=tk.CENTER)
        tree.heading("tecnico", text="Tecnico",anchor=tk.CENTER)
        tree.heading("feedback", text="Feedback",anchor=tk.CENTER)


#inserindo os dados do banco nas colunas (prestar atenção na ordem de "ro" que sempre começará a partir do 0)
        i = 0
        for ro in cursor:
            if ro[0]%2==0:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]),tags=("even",))
            else:
                tree.insert('', i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]), tags=("odd",))
            i = i + 1


#  Cor de fundo dos quadrados do grid
        tree.tag_configure("even",foreground="black",background="white")
        tree.tag_configure("odd",foreground="black",background="white")

# Scrollbar para ajudar na visualicação caso o grid seja enorme
        hsb = ttk.Scrollbar(editorStatusResolvido,orient="horizontal")
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side = BOTTOM)

        vsb = ttk.Scrollbar(editorStatusResolvido,orient="vertical")
        vsb.configure(command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side = RIGHT)        




# Criando labels da parte de pesquisa


    delete_box_label = Label(root,text = "ID Solicitação:")
    delete_box_label.place(x = 30, y = 250)

    delete_box = Entry(root,text = "")
    delete_box.place(x=150, y=250, width=300, height=25)

    edit_btn = Button(root, text="Pesquisar", command=edit)
    edit_btn.place(x=500, y=250, width=300, height=25)


    statusAberto_box_label = Label(root,text = "Status Aberto:")
    statusAberto_box_label.place(x = 30, y = 320)

    statusAberto_box = Entry(root,text = "")
    statusAberto_box.place(x=150, y=320, width=300, height=25)

    filtrarStatusAberto_btn = Button(root, text="Filtrar", command=pesquisaStatus)
    filtrarStatusAberto_btn.place(x=150, y=320, width=300, height=25)


    statusEmAndamento_box_label = Label(root,text = "Status Em Andamento:")
    statusEmAndamento_box_label.place(x = 30, y = 360)

    statusEmAndamento_box = Entry(root,text = "")
    statusEmAndamento_box.place(x=150, y=360, width=300, height=25)

    filtrarStatusEmAndamento_btn = Button(root, text="Filtrar", command=pesquisaStatusEmAndamento)
    filtrarStatusEmAndamento_btn.place(x=150, y=360, width=300, height=25)


    statusPendente_box_label = Label(root,text = "Status Pendente:")
    statusPendente_box_label.place(x = 30, y = 420)

    statusPendente_box = Entry(root,text = "")
    statusPendente_box.place(x=150, y=420, width=300, height=25)

    filtrarStatusPendente_btn = Button(root, text="Filtrar", command=pesquisaStatusPendente)
    filtrarStatusPendente_btn.place(x=150, y=420, width=300, height=25)



    statusResolvido_box_label = Label(root,text = "Status Resolvido:")
    statusResolvido_box_label.place(x = 30, y = 500)

    statusResolvido_box = Entry(root,text = "")
    statusResolvido_box.place(x=150, y=500, width=300, height=25)

    filtrarStatusResolvido_btn = Button(root, text="Filtrar", command=pesquisaStatusResolvido)
    filtrarStatusResolvido_btn.place(x=150, y=500, width=300, height=25)




# Criando um button de Update
# edit_btn = Button(root, text="Pesquisar", command=edit)
# edit_btn.place(x=150, y=420, width=300, height=25)

# filtrarStatusAberto_btn = Button(root, text="Filtrar", command=pesquisaStatus)
# filtrarStatusAberto_btn.place(x=150, y=320, width=300, height=25)


    root.update()
    root.mainloop()






   

def edit():
    # janela.destroy()
    from listaEditUsuario import main_tecnico


def relatorio():
    # janela.destroy()
    # cadastro= Tk()
    cadastro = Toplevel()



    cadastro.title("Help Tech - Relatório ") 
    cadastro.geometry("800x1000+100+0")
    cadastro.resizable(0,0)

#importar imagens

    img_fundo =PhotoImage(file="image\\fundoRelatorio.png")
    img_botao =PhotoImage(file="image\\voltar.png")

    #img_fundo =PhotoImage(file="/Users/jm/Desktop/Python/image/fundoRelatorio.png")
    #img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/voltar.png")


#criação de labels

    lab_fundo = Label(cadastro, image=img_fundo)
    lab_fundo.pack()

#Funções

    def voltar1():
        cadastro.destroy()
        from main_tecnico import relatorio


# # TRATAMENTO PARA IMPEDIR QUE HAJA UM CADASTRO COM O MESMO USERNAME NO BANCO
    conn = sqlite3.connect('details.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(status) from solicitacao Where status is 'Aberto'")
    records1 = c.fetchall()

    c.execute("SELECT COUNT(status) from solicitacao Where status is 'Em andamento'")
    records2 = c.fetchall()

    c.execute("SELECT COUNT(status) from solicitacao Where status is 'Pendente'")
    records3 = c.fetchall()

    c.execute("SELECT COUNT(status) from solicitacao Where status is 'Resolvido'")
    records4 = c.fetchall()



# Mensagem de erro
    error = Message(text="", width=200)
    error.place(x = 144, y = 5)
    error.config(padx=0)


    statusAberto = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    statusAberto.place(width=295, height=45, x=320, y=380)

    statusEmAndamento = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    statusEmAndamento.place(width=295, height=45, x=320, y=490)

    statusPendente = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    statusPendente.place(width=295, height=45, x=320, y=610)

    statusResolvido = Entry(cadastro, bg="#d9d9d9",bd=10, relief="flat",font=("arial", 15))
    statusResolvido.place(width=295, height=45, x=320, y=730)

# botão 

    bt_voltar = Button(cadastro,bd=0, image=img_botao, command=voltar1)
    bt_voltar.place(width=100, height=40, x=675, y=30)




    for record in records1: 
        
        statusAberto.insert(0, record[0])

    for record in records2: 
        
        statusEmAndamento.insert(0, record[0])    

    for record in records3: 
        
        statusPendente.insert(0, record[0])

    for record in records4:     
        
        statusResolvido.insert(0, record[0])    


    cadastro.mainloop()


    from listaEditUsuario import main_tecnico

    
def sair():
    # janela.destroy()
    with sqlite3.connect("details.db") as db:
         cursor=db.cursor()

    from login import main_tecnico

    db.commit()
    db.close()
 






#importar imagens

img_fundo =PhotoImage(file="image\\fundo-tecnico.png")
img_botao =PhotoImage(file="image\\criar.png")
img_botao1 =PhotoImage(file="image\\cadastro.png")
img_botao2 =PhotoImage(file="image\\consultar.png")
img_botao3 =PhotoImage(file="image\\edit.png")
img_botao4 =PhotoImage(file="image\\sair.png")
img_botao5 =PhotoImage(file="image\\relatorio.png")

#img_fundo =PhotoImage(file="/Users/jm/Desktop/Python/image/fundo-tecnico.png")
#img_botao =PhotoImage(file="/Users/jm/Desktop/Python/image/criar.png")
#img_botao1 =PhotoImage(file="/Users/jm/Desktop/Python/image/cadastro.png")
#img_botao2 =PhotoImage(file="/Users/jm/Desktop/Python/image/consultar.png")
#img_botao3 =PhotoImage(file="/Users/jm/Desktop/Python/image/edit.png")
#img_botao4 =PhotoImage(file="/Users/jm/Desktop/Python/image/sair.png")




#criação de labels

lab_fundo = Label(janela, image=img_fundo)
lab_fundo.pack()


#criação de botões

bt_list_atividade = Button(janela,bd=0, image=img_botao, command=novoTicket)
bt_list_atividade.place(width=150, height=50, x=320, y=300)

bt_banco = Button(janela,bd=0, image=img_botao1, command=cadastro)
bt_banco.place(width=150, height=50, x=320, y=450)

bt_cadastro = Button(janela,bd=0, image=img_botao2, command=banco)
bt_cadastro.place(width=150, height=50, x=320, y=600)

bt_edit = Button(janela,bd=0, image=img_botao3, command=edit)
bt_edit.place(width=150, height=50, x=320, y=750)

bt_relatorio = Button(janela,bd=0, image=img_botao5, command=relatorio)
bt_relatorio.place(width=150, height=50, x=320, y=900)

bt_sair = Button(janela,bd=0, image=img_botao4, command=sair)
bt_sair.place(width=60, height=30, x=710, y=30)

janela.title("Help Tech -Menu técnico") 
janela.geometry("800x1000+200+0")
janela.resizable(0,0)
janela.iconbitmap("image/icon.ico")
janela.mainloop()