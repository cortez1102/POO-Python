class Titular:
    def __init__(self, cpf, nome, sobrenome):
        self.__cpf = cpf
        self.__nome = nome
        self.__sobrenome = sobrenome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_sobrenome(self):
        return self.__sobrenome

    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    def extrato_reduzido(self):
        return f"Número da Conta: {self.__numero}\nSaldo: R$ {self.__saldo:.2f}"

    def extrato_normal(self):
        titular = self.__titular
        return f"Nome: {titular.get_nome()} {titular.get_sobrenome()}\nCPF: {titular.get_cpf()}\nNúmero da Conta: {self.__numero}\nSaldo: R$ {self.__saldo:.2f}"

    def dados_titular(self):
        titular = self.__titular
        return f"Nome: {titular.get_nome()} {titular.get_sobrenome()}\nCPF: {titular.get_cpf()}"

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def saque(self, valor):
        if valor <= self.__saldo + self.__limite:
            self.__saldo -= valor
            return True
        return False

    def transferencia(self, destino, valor):
        if self.saque(valor):
            destino.deposito(valor)
            return True
        return False

if __name__ == '__main__':

    titular = Titular("123.456.789-00", "Joao", "Silva")
    conta = Conta("1234-5", titular)
    print(f"Endereço do objeto titular: {id(titular)}")
    print(f"Endereço do objeto conta: {id(conta)}")
    print("Dados do Titular:")
    print(f"Nome: {titular.get_nome()} {titular.get_sobrenome()}")
    print(f"Sobrenome: {titular.get_sobrenome()}")
    print(f"CPF: {titular.get_cpf()}")

    titular.set_nome("Jose")
    print(f"Novo Nome do Titular: {titular.get_nome()}")

    print("\nDados da Conta:")
    print(conta.dados_titular())

    conta.get_titular().set_nome("Maria")
    print(f"\nNovo Nome do Titular pela Conta: {conta.get_titular().get_nome()}")

    conta.deposito(500)
    print("\nExtrato Reduzido:")
    print(conta.extrato_reduzido())

    conta.saque(200)
    print("\nExtrato Reduzido após saque:")
    print(conta.extrato_reduzido())

    conta_destino = Conta("5432-1", Titular("987.654.321-00", "Pedro", "Santos"))
    conta.transferencia(conta_destino, 100)
    print("\nExtrato Reduzido após transferência:")
    print(conta.extrato_reduzido())
    print("\nExtrato Reduzido da Conta Destino após transferência:")
    print(conta_destino.extrato_reduzido())
