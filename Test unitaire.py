import Personne
import GUIs

import unittest

class TestMonCode(unittest.TestCase):

    def testPersonne(self):
        choseEnTest = Personne.Client("Paquet", "Mortimer", r"ok@k.com", "Oui, ceci est un username", "Ouiceciestuncode", "02/19/2022", "Client")
        self.assertEqual(choseEnTest.nom, "Paquet")

    def testGUIs(self):
        choseEnTest = GUIs.getTempsComplet("14/03/1592")
        self.assertEqual(choseEnTest, "14 mars 1592")

if __name__ == "__main__":
    unittest.main()