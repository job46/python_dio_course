import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        """Initialize the cliente with an address and an empty list of accounts."""
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """Perform a transaction on the given account."""
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Add an account to the cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """Initialize a PessoaFisica cliente with name, birth date, CPF, and address."""
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        """Initialize an account with balance, account number, and historical records."""
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_nova_conta(cls, cliente, numero):
        """Factory method to create a new account."""
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """Withdraw a given amount if the balance is sufficient."""
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        if valor > self._saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        """Deposit a given amount if it is positive."""
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        """Initialize a checking account with withdrawal limits."""
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        """Withdraw a given amount considering limits on value and number of withdrawals."""
        numero_saques = sum(1 for t in self.historico.transacoes if t["tipo"] == "Saque")
        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False
        if numero_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False
        return super().sacar(valor)

    def __str__(self):
        return f"""Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.cliente.nome}\n"""


class Historico:
    def __init__(self):
        """Initialize an empty transaction history."""
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Record a transaction with details like type, value, and timestamp."""
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


def mostrar_menu():
    """Display the main menu and return user input."""
    menu_text = """\n
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]  Sair
    => """
    return input(textwrap.dedent(menu_text))


def buscar_cliente_por_cpf(cpf, clientes):
    """Find a client by CPF, returning the first match or None if not found."""
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)


def recuperar_primeira_conta(cliente):
    """Retrieve the first account of a client or print a message if no accounts exist."""
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]


def processar_deposito(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    conta = recuperar_primeira_conta(cliente)
    if conta:
        cliente.realizar_transacao(conta, Deposito(valor))


def processar_saque(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    conta = recuperar_primeira_conta(cliente)
    if conta:
        cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_primeira_conta(cliente)
    if conta:
        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes
        if not transacoes:
            print("Nenhuma movimentação registrada.")
        else:
            for transacao in transacoes:
                print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f} em {transacao['data']}")
        print(f"\nSaldo: R$ {conta.saldo:.2f}")
        print("==========================================")


def main():
    clientes = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            processar_deposito(clientes)
        elif opcao == "s":
            processar_saque(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Opção inválida! Tente novamente. @@@")

if __name__ == "__main__":
    main()
