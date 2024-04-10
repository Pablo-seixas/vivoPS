

# Definindo a classe para representar um usuário do sistema
class Usuario:
    # Método para inicializar um usuário com nome, senha e permissão
    def __init__(self, nome, senha, permissao):
        self.nome = nome
        self.senha = senha
        self.permissao = permissao

    # Método para salvar um novo usuário no sistema
    def salvar(self):
        # Aqui iria o código para salvar o usuário no banco de dados
        print("Usuário", self.nome, "salvo no sistema.")

    # Método para autenticar um usuário no sistema
    def autenticar(self):
        # Aqui iria o código para verificar se o nome de usuário e senha são válidos
        if self.nome == "admin" and self.senha == "admin123":
            return True
        else:
            return False

    # Método para verificar a permissão de um usuário no sistema
    def verificar_permissao(self):
        # Aqui iria o código para verificar qual a permissão do usuário
        if self.nome == "admin":
            return "admin"
        else:
            return "normal"

# Função para cadastrar um novo usuário no sistema
def cadastrar_usuario(nome, senha, permissao):
    # Cria um novo objeto usuário com as informações fornecidas
    usuario = Usuario(nome, senha, permissao)
    # Salva o usuário no sistema
    usuario.salvar()

# Função para permitir que um usuário faça login no sistema
def fazer_login(nome, senha):
    # Cria um objeto usuário com o nome e senha fornecidos
    usuario = Usuario(nome, senha, None)
    # Verifica se as credenciais são válidas
    if usuario.autenticar():
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

# Função para verificar a permissão de um usuário no sistema
def verificar_permissao_usuario(nome):
    # Cria um objeto usuário com o nome fornecido
    usuario = Usuario(nome, None, None)
    # Verifica a permissão do usuário
    permissao = usuario.verificar_permissao()
    if permissao:
        print("Permissão do usuário:", permissao)
    else:
        print("Usuário não encontrado.")

# Teste do código
if __name__ == "__main__":
    cadastrar_usuario("usuario1", "senha123", "normal")
    fazer_login("usuario1", "senha123")
    verificar_permissao_usuario("usuario1")
