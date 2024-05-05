import pytest
from primos import primos

def test_primos_rango_vacio():
    assert primos(14, 16) == [], "Debe retornar una lista vacía si no hay primos en el rango"

def test_primos_rango_con_primos():
    assert primos(1, 10) == [2, 3, 5, 7], "Debe retornar la lista de primos en el rango 1 a 10"

def test_primos_rango_negativo():
    assert primos(-10, 2) == [2], "Debe manejar rangos que incluyen números negativos y retornar primos válidos"

def test_primos_rango_un_numero_primo():
    assert primos(13, 13) == [13], "Debe retornar el número si el rango es un solo número primo"

def test_primos_rango_un_numero_no_primo():
    assert primos(4, 4) == [], "Debe retornar una lista vacía si el rango es un solo número no primo"