class ContaBancaria:

    def __init__(self, titular, saldo):

        self.titular = titular
        self.saldo = saldo

    
    def depositar(self, valor):

        self.saldo += valor
        print (self.saldo)


    def sacar(self, valor):

        if valor <= self.saldo:

            self.saldo -= valor
            print(self.saldo)

        else:
            print("Saldo insuficiente")


    def mostrar_saldo(self):
        
        print(f"Saldo atual: {self.saldo}")


#----------CRIAÇÃO DOS OBJETOS-------------

conta1 = ContaBancaria("Albert", 2000)
conta2 = ContaBancaria("Carla", 700)

print(f"Conta bancária de: {conta1.titular}")

conta1.depositar(100)
conta1.sacar(200)
conta1.mostrar_saldo()

print(" ")

print(f"Conta bancária de: {conta2.titular}")

conta2.depositar(50)
conta2.sacar(770)
conta2.mostrar_saldo()