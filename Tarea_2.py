# Funcion que realiza suma, resta y multiplicacion

''' Se define la funcion con dos entradas la cual
retornara suma, resta y multiplicacion
 en caso de que los valores sean A<B o (A o B) sean
 String retorna un -1'''
def Ejercicio_1(A, B):
    # Condicion igual a String
    if(isinstance(A, str) or isinstance(B, str)):
        print("ERROR por String")
        # Retorna un -1
        return(-1)
    # Condicion A<B
    elif(A < B):
        print("ERROR por Comparacion")
        # Retorna un -1
        return(-1)
    else:
        return(A+B, A-B, A*B)
# Si no se cumplieron las condiciones anteriores
# retorna suma, resta y multiplicacion

