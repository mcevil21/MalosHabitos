def Multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto

if __name__=="__==main--":
    multiplicando = float(input("Multiplicando:"))
    multiplicador= float(input("Multiplicador:"))
    resultado = Multiplicacion(multiplicando, multiplicador)
    print (f"{multiplicando}*{multiplicador}*{resultado}")