
def calcular(multiplicador1, multiplicador2, sumador):
    resultado = multiplicador1 * multiplicador2 + sumador
    return resultado

if __name__ == "__main__":
    def principal():
        multiplicador1 = float(input("Multiplidor1 :"))
        multiplicador2 = float(input("Multiplidor2 :"))
        sumador = float(input("Sumador:"))
        resultado = calcular(multiplicador1,multiplicador2, sumador)
        print("El resultado es:", resultado)
    principal()