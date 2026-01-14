class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def status(self):
        if self.nota >= 7:
            print(f"O aluno {self.nome} está aprovado com média {self.nota}")

        else:
            print(f"O aluno {self.nome} está reprovado com média {self.nota}")

aluno1 = Aluno("Antônio", 17, 8.5)
aluno2 = Aluno("Júlia", 18, 7)
aluno3 = Aluno("Luís", 16, 6)

aluno1.status()
aluno2.status()
aluno3.status()
