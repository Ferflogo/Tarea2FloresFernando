# Funcion que realiza suma, resta y multiplicacion

# Se define la funcion con dos entradas la cual retornara suma, resta y multiplicacion
# en caso de que los valores sean A<B o (A o B) sean String retorna un -1
def Ejercicio_1 (A,B):
    if (type(A)==type(str(A))or type(B)==type(str(B)) ): # Condicion igual a String
        print("ERROR por String")
        return -1 # Retorna un -1
    elif (A<B): # Condicion A<B
        print("ERROR por Comparacion")
        return -1 # Retorna un -1
    else :
        return A+B, A-B, A*B # Si no se cumplieron las condiciones anteriores retorna
    # suma, resta y multiplicacion

