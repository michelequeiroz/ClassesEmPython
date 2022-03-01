class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Deposito realizado. Saldo: R$ {self.__saldo}')

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f'Saque falhou. Saldo: R$ {self.__saldo}')
            return 'Saldo insuficiente.'
        self.__saldo -= valor
        print(f'Saque realizado. Saldo: R$ {self.__saldo}')
        return valor


    class ContaPoupanca(ContaBancaria):
        def __init__(self, numero, titular):
            self.rendimento = 0.5
            super().__init__(numero, titular)

    class ContaInvestimento(ContaBancaria):
        def __init__(self, numero, titular, gerente):
            self.gerente = gerente
            super().__init__(numero, titular)

        def sacar(self, valor):
            print('Verificando prazo de investimento...')
            print('Calculando impostos e taxas...')
            print('realizando saque...')
            return super().sacar(valor)