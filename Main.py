

import Personne
import GUIs

import time

registre = Personne.Personne("O'Nyme", "Anne")
Personne.recuperationAll()

print(time.strftime("Mise en fonction de l'application Rewind, bonne session!\n---/Aujourd'hui nous sommes le %d %m %Y/---"))

GUIs.logInApp()