import pytest
from dominio.paciente import Paciente

paciente1 = Paciente(None,"Lautaro","Villafañe",27,"Boreal",2954337927)

@pytest.mark.parametrize("dato,valor_esperado",[
    (paciente1.id_paciente, None),
    (paciente1.nombre,"Lautaro"),
    (paciente1.apellido,"Villafañe"),
    (paciente1.edad, 27),
    (paciente1.obra_social,"Boreal"),
    (paciente1.telefono,2954337927)
    ])


def test_paciente(dato,valor_esperado):
    assert dato == valor_esperado
    
def test_setter_nombre():
    nuevo_nombre = paciente1.nombre = "Candela"
    assert nuevo_nombre == "Candela"
    
def test_setter_apellido():
    nuevo_apellido = paciente1.apellido = "Pelegrino"
    assert nuevo_apellido == "Pelegrino"
    
def test_setter_edad():
    nueva_edad = 26
    assert nueva_edad == 26
    
def test_setter_obra_social():
    nueva_obra_social = "MET"
    assert nueva_obra_social == "MET"
    
def test_setter_telefono():
    nuevo_telefono = 295533333
    assert nuevo_telefono == 295533333