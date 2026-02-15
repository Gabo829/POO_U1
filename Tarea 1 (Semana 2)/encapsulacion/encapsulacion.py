class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes.")

    def obtener_saldo(self):
        return self.__saldo

if __name__ == "__main__":
    cuenta = CuentaBancaria("Gabo", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)
    print("Saldo:", cuenta.obtener_saldo())
