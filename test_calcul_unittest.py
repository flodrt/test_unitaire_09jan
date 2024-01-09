import unittest
from calcul import Calcul

#class de test heritant de unitest.testcase
class TestCalcul(unittest.TestCase):

    #methode de configuration a executer avant chaque test 
    def setUp(self):
        #initialisation des ressources necessaire pour les test 
        self.calc=Calcul() #ibnstancie un objet calc a la class Calcul grace au self

    #test d'addition
    def test_additionner(self):
        resultat = self.calc.additionner(3,5)
        #test 
        self.assertEqual(resultat,8,"commentaire spéciale")

    def test_additionner(self):
        resultat = self.calc.additionner(2,5)
        #test test
        self.assertEqual(resultat,7,"commentaire spéciale")

    

