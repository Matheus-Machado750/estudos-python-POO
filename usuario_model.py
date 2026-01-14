class Usuario:

    def __init__(self, nome, email, senha, ativo=True):

        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

    def desativar(self):

        self.ativo = False
        return f"Úsuario {self.nome} desativado"


    def alterar_senha(self, senha_atual, nova_senha):
        
        if senha_atual != self.senha:

            return "Senha atual incorreta"
        
        else:

            self.senha = nova_senha
            return f"Senha do úsuario {self.nome} alterada com sucesso"
    

    def dados(self):

        return {
            "nome" : self.nome,
            "email" : self.email,
            "ativo" : self.ativo
        }
    
    
#-------CRIAÇÃO DOS OBJETOS----------
    
user1 = Usuario("Jurandir", "jurandir@gmil.com", "12345")
user2 = Usuario("Beto", "beto@gmail.com", "67890")
user3 = Usuario("Nóe", "noe@gmail.com", "11111")


print(f"{user1.alterar_senha('12345', '14798')}")
print("")
print(f"{user2.dados()}")
print("")
print(user3.desativar())