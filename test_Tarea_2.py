import Tarea_2 # Se importa el programa que se quiere probar

def test_Ejercicio_1(): # Se realiza test con valores numericos A>B
    func = Tarea_2.Ejercicio_1(7,4) # Entradas
    assert func == (11,3,28) # Se esperan estos valores
    
def test1_Ejercicio_1(): # Se realiza test con valores numericos A<B
    func = Tarea_2.Ejercicio_1(4,7)
    assert func == (-1) # Se espera un error
    
def test2_Ejercicio_1():
    func = Tarea_2.Ejercicio_1("A",4) # Se realiza test con valores A literal y B numerico
    assert func == (-1) # Se espera un error