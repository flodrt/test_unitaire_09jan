import pytest
from calcul import*

#!pip install pytest

import pytest
from calcul import Calcul

# Fixture pour créer une instance de la classe Calcul pour chaque test
@pytest.fixture
def calculatrice():
    return Calcul()

def test_additionnerPositifs(calculatrice):
    valeur_a = 10
    valeur_b = 15    
    valeur_attendue = 25
    valeur_obtenue = calculatrice.additionner(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue


def test_additionnerPositifEtNegatif(calculatrice):
    valeur_a = -10
    valeur_b = 15    
    valeur_attendue = 5
    valeur_obtenue = calculatrice.additionner(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue


def test_additionnerNegatifs(calculatrice):
    valeur_a = -10
    valeur_b = -15 
    valeur_attendue = -25
    valeur_obtenue = calculatrice.additionner(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue

def test_soustraireNegatifs(calculatrice):
    valeur_a = -10
    valeur_b = 15 
    valeur_attendue = -25
    valeur_obtenue = calculatrice.soustraire(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue
    
def test_multiplier(calculatrice):
    valeur_a = -10
    valeur_b = -15 
    valeur_attendue = 150
    valeur_obtenue = calculatrice.multiplier(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue 
    
def test_diviser(calculatrice):
    valeur_a = 15
    valeur_b = 3
    valeur_attendue = 5
    valeur_obtenue = calculatrice.diviser(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue      

def test_diviser(calculatrice):
    valeur_a = 21
    valeur_b = 7
    valeur_attendue = 3
    valeur_obtenue = calculatrice.diviser(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue      

def test_diviser_par_zero(calculatrice):
    with pytest.raises(ZeroDivisionError, match="Division par zéro impossible"):
        calculatrice.diviser(6, 0)