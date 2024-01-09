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

    # Test de soustraction
    def test_soustraire(self):
        resultat = self.calc.soustraire(10, 4)
        # Vérifier si le résultat est égal à 6
        self.assertEqual(resultat, 6)

    # Test de multiplication
    def test_multiplier(self):
        resultat = self.calc.multiplier(10, 4)
        # Vérifier si le résultat est égal à 40
        self.assertEqual(resultat, 40)

    # Test de division
    def test_diviser(self):
        resultat = self.calc.diviser(9, 3)
        # Vérifier si le résultat est égal à 3
        self.assertEqual(resultat, 3)
    # Test de division par zéro#
        
        

        

         
# Exécuter les tests si le script est exécuté directement
if __name__ == '__main__':# appelle la fonction main du module unittest
    unittest.main()

