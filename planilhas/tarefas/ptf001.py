from database import Session, Usuario, Tarefa

# Funções CRUD para Usuários
def criar_usuario(nome, email):
    session = Session()
    novo_usuario = Usuario(nome=nome, email=email)
    session.add(novo_usuario)
    session.commit()
    session.close()

def ler_usuarios():
    session = Session()
    usuarios = session.query(Usuario).all()
    session.close()
    return usuarios

def atualizar_usuario(usuario_id, nome=None, email=None):
    session = Session()
    usuario = session.query(Usuario).get(usuario_id)
    if nome:
        usuario.nome = nome
    if email:
        usuario.email = email
    session.commit()
    session.close()

def deletar_usuario(usuario_id):
    session = Session()
    usuario = session.query(Usuario).get(usuario_id)
    session.delete(usuario)
    session.commit()
    session.close()

# Funções CRUD para Tarefas
def criar_tarefa(descricao, usuario_id):
    session = Session()
    nova_tarefa = Tarefa(descricao=descricao, usuario_id=usuario_id)
    session.add(nova_tarefa)
    session.commit()
    session.close()

def ler_tarefas():
    session = Session()
    tarefas = session.query(Tarefa).all()
    session.close()
    return tarefas

def atualizar_tarefa(tarefa_id, descricao=None):
    session = Session()
    tarefa = session.query(Tarefa).get(tarefa_id)
    if descricao:
        tarefa.descricao = descricao
    session.commit()
    session.close()

def deletar_tarefa(tarefa_id):
    session = Session()
    tarefa = session.query(Tarefa).get(tarefa_id)
    session.delete(tarefa)
    session.commit()
    session.close()
