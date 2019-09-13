# Se importa el programa que se quiere probar
import Tarea_2

# Se realiza test con valores numericos A>B


def test_Ejercicio_1():
    # Entradas
    func = Tarea_2.Ejercicio_1(7, 4)
    # Se esperan estos valores
    assert func == (11, 3, 28)


def test1_Ejercicio_1():
    # Se realiza test con valores numericos A<B
    func = Tarea_2.Ejercicio_1(4, 7)
    # Se espera un error
    assert func == (-1)


def test2_Ejercicio_1():
    # Se realiza test con valores A literal y B numerico
    func = Tarea_2.Ejercicio_1("A", 4)
    # Se espera un error
    assert func == (-1)
