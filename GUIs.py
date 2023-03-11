
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from functools import partial
import os
import platform
import time
import requests
import shutil

import Personne

class infomations:
    "Est responsable de la détention d'informations lors des navigations entre les fenêtres"
    def __init__(self):
        self.wasActive = False
        self.isParametreOpen = False
        self.personneConnecte = (None, None, None, None, None, None, None)
        self.cartesPersonneConnecte = []
        self.film = ""
        self.acteur = ""


info = infomations()

wasActive = False


path = os.getcwd()#Répertoire courant
def getLocalisationImages():
    "Défini le chemin de sauvegarde des images"
    try:
        if platform.system() == "Windows":
            localisation = r"/Images/"
            signe = r"p\p"
            bonSigne = signe.replace("p", "")
            vraiLocalisation = localisation.replace("/", bonSigne)
            localisationFichier = path + vraiLocalisation
            #print("Succès, le système d'exploitation détecté est " + platform.system())
            return localisationFichier
        else:
            localisationFichier = path + r"/Images/"
            #print("Succès, le système d'exploitation détecté est " + platform.system())
            return localisationFichier
    except:
        print("Erreur quant à la détection du système d'exploitation")
        return path + r"/Images/"

def getLocalisationBandeAnnonces():
    "Défini le chemin de sauvegarde des bande-annonces"
    try:
        if platform.system() == "Windows":
            localisation = r"/Bande annonces/"
            signe = r"p\p"
            bonSigne = signe.replace("p", "")
            vraiLocalisation = localisation.replace("/", bonSigne)
            localisationFichier = path + vraiLocalisation
            #print("Succès, le système d'exploitation détecté est " + platform.system())
            return localisationFichier
        else:
            localisationFichier = path + r"/Bande annonces/"
            #print("Succès, le système d'exploitation détecté est " + platform.system())
            return localisationFichier
    except:
        print("Erreur quant à la détection du système d'exploitation")
        return path + r"/Bande annonces/"

localisationImages = getLocalisationImages()
localisationBandeAnnonces = getLocalisationBandeAnnonces()

localisationImagesGitHub = r"https://raw.githubusercontent.com/Creativipi/Rewind/imageMain/Images/"

class addCarteApp():
    "Responsable de l'ajout de nouvelles cartes"
    def __init__(self):
        self.fen = Tk()

        self.fen.title("Ajout d'une carte")

        self.numeroCarteTxt = StringVar()
        self.numeroSecuriteTxt = StringVar()

        self.dateExpirationMoisTxt = StringVar()
        self.dateExpirationAnneeTxt = StringVar()
        self.typeTxt = StringVar()

        # Avertissement
        self.alerteNumero = Label(self.fen, text="", foreground="#eaa")
        self.alerteNumero.grid(row=2, column=0, sticky="e")

        self.alerteSecurite = Label(self.fen, text="", foreground="#eaa")
        self.alerteSecurite.grid(row=3, column=0, sticky="e")

        self.alerteDate = Label(self.fen, text="", foreground="#eaa")
        self.alerteDate.grid(row=4, column=0, sticky="e")

        self.alerteType = Label(self.fen, text="", foreground="#eaa")
        self.alerteType.grid(row=5, column=0, sticky="e")

        self.approuvement = Label(self.fen, text="", foreground="#aea")
        self.approuvement.grid(row=6, column=5, sticky="w")

        #Option
        optionMois = [
            "[Mois]",
            "01 (Janvier)",
            "02 (Février)",
            "03 (Mars)",
            "04 (Avril)",
            "05 (Mai)",
            "06 (Juin)",
            "07 (Juillet)",
            "08 (Août)",
            "09 (Septembre)",
            "10 (Octobre)",
            "11 (Novembre)",
            "12 (Décembre)"
        ]
        optionType = ["Sélection du type", "Visa", "MasterCard"]

        self.dateExpirationMoisTxt.set(optionMois[0])
        self.dateExpirationAnneeTxt.set(self.getOptionAnnee()[0])
        self.typeTxt.set(optionType[0])

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        self.label = Label(self.fen, text="Entrez les informations nécessaire pour l'ajout de votre carte.").grid(row=0, column=0, sticky="w")
        self.label = Label(self.fen, text=r"(Tout caractère n'étant pas un chiffre sera ignoré lors de la vérification, sentez-vous à l'aise de mettre des espaces ou des tirets au besoin)", foreground="#443").grid(row=1, column=0, columnspan=6, sticky="w")
        self.btnConfirmer = Button(self.fen, text="Confirmer", command=self.confirmer).grid(row=6, column=2, columnspan=3)
        self.boutRetourCompte = Button(self.fen, text="Retour", command=self.retourCartes).grid(row=7, column=6)

        # Boites de texte

        self.numeroCarteLabel = Label(self.fen, text="Numéro de la carte :").grid(row=2, column=1)
        self.numeroCarteEntry = Entry(self.fen, textvariable=self.numeroCarteTxt)
        self.numeroCarteEntry.grid(row=2, column=2, columnspan=3)
        self.infoNumeroCarteLabel = Label(self.fen, text="(16 chiffres)").grid(row=2, column=5, sticky="w")

        self.numeroSecuriteLabel = Label(self.fen, text="Numéro de Sécurité :").grid(row=3, column=1)
        self.numeroSecuriteEntry = Entry(self.fen, textvariable=self.numeroSecuriteTxt)
        self.numeroSecuriteEntry.grid(row=3, column=2, columnspan=3)
        self.infoSecuriteLabel = Label(self.fen, text="(Numéro à trois chiffres derrière la carte)").grid(row=3, column=5, sticky="w")

        self.dateExpirationLabel = Label(self.fen, text="Date d'expiration :").grid(row=4, column=1)
        self.dateExpirationMoisEntry = OptionMenu(self.fen, self.dateExpirationMoisTxt, *optionMois).grid(row=4, column=2)
        self.labelSeparation = Label(self.fen, text="/").grid(row=4, column=3)
        self.dateExpirationAnneeEntry = OptionMenu(self.fen, self.dateExpirationAnneeTxt, *self.getOptionAnnee()).grid(row=4, column=4)

        self.typeLabel = Label(self.fen, text="Type de carte").grid(row=5, column=1)
        self.typeEntry = OptionMenu(self.fen, self.typeTxt, *optionType).grid(row=5, column=2, columnspan=3)

        self.fen.mainloop()

    def avertissement(self, liste):
        "Fait apparaître des messages d'avertissement où il est nécessaire"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="La carte n'est pas valide", foreground="#eaa")
        self.approuvement.grid(row=6, column=5, sticky="w")

        self.alerteNumero.destroy()
        self.alerteNumero = Label(self.fen, text="", foreground="#eaa")
        self.alerteNumero.grid(row=2, column=0, sticky="e")

        self.alerteSecurite.destroy()
        self.alerteSecurite = Label(self.fen, text="", foreground="#eaa")
        self.alerteSecurite.grid(row=3, column=0, sticky="e")

        self.alerteDate.destroy()
        self.alerteDate = Label(self.fen, text="", foreground="#eaa")
        self.alerteDate.grid(row=4, column=0, sticky="e")

        self.alerteType.destroy()
        self.alerteType = Label(self.fen, text="", foreground="#eaa")
        self.alerteType.grid(row=5, column=0, sticky="e")

        if liste[0] == True and liste[1] == True and liste[2] == True and liste[3] == True and liste[4] == True:
            self.approuvement.destroy()
            self.approuvement = Label(self.fen, text="La carte fait déjà parti de votre liste", foreground="#eea")
            self.approuvement.grid(row=6, column=5, sticky="w")

            self.alerteNumero.destroy()
            self.alerteNumero = Label(self.fen, text="", foreground="#e33")
            self.alerteNumero.grid(row=2, column=0, sticky="e")

            self.alerteSecurite.destroy()
            self.alerteSecurite = Label(self.fen, text="", foreground="#e33")
            self.alerteSecurite.grid(row=3, column=0, sticky="e")

            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="", foreground="#e33")
            self.alerteDate.grid(row=4, column=0, sticky="e")

            self.alerteType.destroy()
            self.alerteType = Label(self.fen, text="", foreground="#e33")
            self.alerteType.grid(row=5, column=0, sticky="e")

        #Selon chaque erreur
        if liste[0] == False:
            self.alerteNumero.destroy()
            self.alerteNumero = Label(self.fen, text="Ce numéro n'est pas composé de 16 chiffres", foreground="#eaa")
            self.alerteNumero.grid(row=2, column=0, sticky="e")

        if liste[1] == False:
            self.alerteSecurite.destroy()
            self.alerteSecurite = Label(self.fen, text="Ce numéro n'est pas composé de 3 chiffre", foreground="#eaa")
            self.alerteSecurite.grid(row=3, column=0, sticky="e")

        if liste[2] == False and liste[3] == False:
            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="Le mois et l'année ne sont pas sélectionnés", foreground="#eaa")
            self.alerteDate.grid(row=4, column=0, sticky="e")

        elif liste[2] == False and liste[3] == True:
            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="Le mois n'est pas sélectionné", foreground="#eaa")
            self.alerteDate.grid(row=4, column=0, sticky="e")

        elif liste[2] == True and liste[3] == False:
            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="L'année n'est pas sélectionnée", foreground="#eaa")
            self.alerteDate.grid(row=4, column=0, sticky="e")

        if liste[4] == False:
            self.alerteType.destroy()
            self.alerteType = Label(self.fen, text="Le type n'est pas sélectionné", foreground="#eaa")
            self.alerteType.grid(row=5, column=0, sticky="e")

        self.fen.after(200, partial(self.suiteAvertissement, liste))
    def suiteAvertissement(self, liste):
        "Change la couleur des messages d'avertissement"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="La carte n'est pas valide", foreground="#e33")
        self.approuvement.grid(row=6, column=5, sticky="w")

        if liste[0] == True and liste[1] == True and liste[2] == True and liste[3] == True and liste[4] == True:
            # De base
            self.approuvement.destroy()
            self.approuvement = Label(self.fen, text="La carte fait déjà parti de votre liste", foreground="#dd3")
            self.approuvement.grid(row=6, column=5, sticky="w")

        # Selon chaque erreur
        if liste[0] == False:
            self.alerteNumero.destroy()
            self.alerteNumero = Label(self.fen, text="Ce numéro n'est pas composé de 16 chiffres", foreground="#e33")
            self.alerteNumero.grid(row=2, column=0, sticky="e")

        if liste[1] == False:
            self.alerteSecurite.destroy()
            self.alerteSecurite = Label(self.fen, text="Ce numéro n'est pas composé de 3 chiffre", foreground="#e33")
            self.alerteSecurite.grid(row=3, column=0, sticky="e")

        if liste[2] == False and liste[3] == False:
            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="Le mois et l'année ne sont pas sélectionnés", foreground="#e33")
            self.alerteDate.grid(row=4, column=0, sticky="e")

        elif liste[2] == False and liste[3] == True:
            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="Le mois n'est pas sélectionné", foreground="#e33")
            self.alerteDate.grid(row=4, column=0, sticky="e")

        elif liste[2] == True and liste[3] == False:
            self.alerteDate.destroy()
            self.alerteDate = Label(self.fen, text="L'année n'est pas sélectionnée", foreground="#e33")
            self.alerteDate.grid(row=4, column=0, sticky="e")

        if liste[4] == False:
            self.alerteType.destroy()
            self.alerteType = Label(self.fen, text="Le type n'est pas sélectionné", foreground="#e33")
            self.alerteType.grid(row=5, column=0, sticky="e")

    def getOptionAnnee(self):
        "Permet l'affichage d'un nombre d'années prédéfini pour la création d'une carte de crédit"
        listeAnnees = ["[Année]"]
        nombreAnneesAv = 20

        for x in range(nombreAnneesAv):
            listeAnnees.append(str((int(time.strftime("%Y")) + x) % 100))

        return listeAnnees


    def retourCartes(self):
        "Permet de retourner à la fenêtre de l'affichage des cartes"
        self.fen.destroy()
        cartesApp()

    def confirmer(self):
        "Vérifie et accepte une carte si elle est moindrement valable ou envoie un avertissement"
        print("Numéro : {}, numéro de sécutité : {}, date : {}/{}, type : {}".format(filterDigits(self.numeroCarteTxt.get()),
                                                                                     filterDigits(self.numeroSecuriteTxt.get()),
                                                                                     filterDigits(self.dateExpirationMoisTxt.get()),
                                                                                     filterDigits(self.dateExpirationAnneeTxt.get()),
                                                                                     self.typeTxt.get()))

        client = info.personneConnecte
        checklist = [False, False, False, False, False]
        verdict = True

        #Vérification
        if len(filterDigits(self.numeroCarteTxt.get())) == 16:
            checklist[0] = True
        if len(filterDigits(self.numeroSecuriteTxt.get())) == 3:
            checklist[1] = True
        if self.dateExpirationMoisTxt.get() != "[Mois]":
            checklist[2] = True
        if self.dateExpirationAnneeTxt.get() != self.getOptionAnnee()[0]:
            checklist[3] = True
        if self.typeTxt.get() != "Sélection du type":
            checklist[4] = True

        for check in checklist:
            if check == False:
                verdict = False

        if verdict == True:
            #print("Carte potentielle!")
            for carte in info.cartesPersonneConnecte:
                if str(carte) == "{},{},{}/{},{}".format(filterDigits(self.numeroCarteTxt.get()),
                                                         filterDigits(self.numeroSecuriteTxt.get()),
                                                         filterDigits(self.dateExpirationMoisTxt.get()),
                                                         filterDigits(self.dateExpirationAnneeTxt.get()),
                                                         self.typeTxt.get()):
                    #print("Je vais avertir mon boss!!! >:c")
                    self.avertissement(checklist)
                    verdict = False


            if verdict == True:
                #La carte passe
                print("Carte passé")

                try:
                    carte = Personne.CarteDeCredit(filterDigits(self.numeroCarteTxt.get()),
                                                   filterDigits(self.numeroSecuriteTxt.get()),
                                                   "{}/{}".format(filterDigits(self.dateExpirationMoisTxt.get()),
                                                    filterDigits(self.dateExpirationAnneeTxt.get())),
                                                   self.typeTxt.get())

                    info.cartesPersonneConnecte.append(carte)

                    client.addCarte(carte)
                    Personne.sauvegardeClients()
                    Personne.sauvegardeCartes()

                    self.approuvement.destroy()
                    self.approuvement = Label(self.fen, text="Carte approuvée!", foreground="#3b3")
                    self.approuvement.grid(row=6, column=5, sticky="w")

                except:

                    self.approuvement.destroy()
                    self.approuvement = Label(self.fen, text="Un problème est survenu lors de l'ajout de la carte", foreground="#dd3")
                    self.approuvement.grid(row=6, column=5, sticky="w")

                    print("une erreur est survenue lors de l'ajout de la carte")

                #Approuvement
                self.alerteNumero.destroy()
                self.alerteNumero = Label(self.fen, text="", foreground="#eaa")
                self.alerteNumero.grid(row=2, column=0, sticky="e")

                self.alerteSecurite.destroy()
                self.alerteSecurite = Label(self.fen, text="", foreground="#eaa")
                self.alerteSecurite.grid(row=3, column=0, sticky="e")

                self.alerteDate.destroy()
                self.alerteDate = Label(self.fen, text="", foreground="#eaa")
                self.alerteDate.grid(row=4, column=0, sticky="e")

                self.alerteType.destroy()
                self.alerteType = Label(self.fen, text="", foreground="#eaa")
                self.alerteType.grid(row=5, column=0, sticky="e")


                #Reset
                self.numeroCarteTxt.set("")
                self.numeroSecuriteTxt.set("")

                self.dateExpirationMoisTxt.set("[Mois]")
                self.dateExpirationAnneeTxt.set("[Année]")
                self.typeTxt.set("Sélection du type")


        else:
            #print("Je vais avertir mon boss!!! >:c")
            self.avertissement(checklist)

class addEmployeApp():
    "Responsable de la création des nouveaux comptes employés"
    def __init__(self):
        self.fen = Tk()

        self.prenomTxt = StringVar()
        self.nomTxt = StringVar()
        self.userTxt = StringVar()
        self.emailTxt = StringVar()
        self.code1Txt = StringVar()
        self.code2Txt = StringVar()
        self.gradeTxt = StringVar()

        self.fen.title("Création d'un compte employé")

        # Avertissement
        self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
        self.alertePrenom.grid(row=1, column=3, sticky="w")

        self.alerteNom = Label(self.fen, text="", foreground="#eaa")
        self.alerteNom.grid(row=2, column=3, sticky="w")

        self.alerteUser = Label(self.fen, text="", foreground="#eaa")
        self.alerteUser.grid(row=3, column=3, sticky="w")

        self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
        self.alerteEmail.grid(row=4, column=3, sticky="w")

        self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode1.grid(row=5, column=3, sticky="w")

        self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode2.grid(row=6, column=3, sticky="w")

        self.alerteGrade = Label(self.fen, text="", foreground="#eaa")
        self.alerteGrade.grid(row=7, column=3, sticky="w")

        self.approuvement = Label(self.fen, text="", foreground="#aea")
        self.approuvement.grid(row=8, column=3, sticky="w")

        self.optionGrade = ["Choisir le garde", "1", "2", "3", "4", "5"]
        self.gradeTxt.set(self.optionGrade[0])

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        self.label = Label(self.fen, text="Entrez les informations nécessaire à la création du compte").grid(row=0)
        self.btnConfirmer = Button(self.fen, text="Confirmer", command=self.confirmer).grid(row=8, column=1)
        self.boutRetour = Button(self.fen, text=" Retour ", command=self.retour).grid(row=9, column=3, sticky="e")

        # Boites de texte

        self.prenomLabel = Label(self.fen, text="Prénom :").grid(row=1, column=0)
        self.prenomEntry = Entry(self.fen, textvariable=self.prenomTxt).grid(row=1, column=1)

        self.nomLabel = Label(self.fen, text="Nom :").grid(row=2, column=0)
        self.nomEntry = Entry(self.fen, textvariable=self.nomTxt).grid(row=2, column=1)

        self.userLabel = Label(self.fen, text="Nom d'utilisateur :").grid(row=3, column=0)
        self.userEntry = Entry(self.fen, textvariable=self.userTxt).grid(row=3, column=1)

        self.emailLabel = Label(self.fen, text="Adresse email :").grid(row=4, column=0)
        self.emailEntry = Entry(self.fen, textvariable=self.emailTxt).grid(row=4, column=1)

        self.code1Label = Label(self.fen, text="Mot de passe :").grid(row=5, column=0)
        self.code1Entry = Entry(self.fen, textvariable=self.code1Txt, show="*").grid(row=5, column=1)

        self.code2Label = Label(self.fen, text="Confirmation mot de passe :").grid(row=6, column=0)
        self.code2Entry = Entry(self.fen, textvariable=self.code2Txt, show="*").grid(row=6, column=1)

        self.gradeLabel = Label(self.fen, text="Grade :").grid(row=7, column=0)
        self.gradeEntry = OptionMenu(self.fen, self.gradeTxt, *self.optionGrade).grid(row=7, column=1)

        self.fen.mainloop()


    def avertissement(self, liste):
        "Fait apparaître des messages d'avertissement où il est nécessaire"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Le compte est invalide", foreground="#eaa")
        self.approuvement.grid(row=8, column=3, sticky="w")

        self.alertePrenom.destroy()
        self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
        self.alertePrenom.grid(row=1, column=3, sticky="w")

        self.alerteNom.destroy()
        self.alerteNom = Label(self.fen, text="", foreground="#eaa")
        self.alerteNom.grid(row=2, column=3, sticky="w")

        self.alerteUser.destroy()
        self.alerteUser = Label(self.fen, text="", foreground="#eaa")
        self.alerteUser.grid(row=3, column=3, sticky="w")

        self.alerteEmail.destroy()
        self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
        self.alerteEmail.grid(row=4, column=3, sticky="w")

        self.alerteCode1.destroy()
        self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode1.grid(row=5, column=3, sticky="w")

        self.alerteCode2.destroy()
        self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode2.grid(row=6, column=3, sticky="w")

        self.alerteGrade.destroy()
        self.alerteGrade = Label(self.fen, text="", foreground="#eaa")
        self.alerteGrade.grid(row=7, column=3, sticky="w")

        # Selon chaque erreur
        if liste[0] == False:
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="Aucun prénom n'a été écrit", foreground="#eaa")
            self.alertePrenom.grid(row=1, column=3, sticky="w")

        if liste[1] == False:
            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="Aucun nom n'a été écrit", foreground="#eaa")
            self.alerteNom.grid(row=2, column=3, sticky="w")

        if self.userTxt.get() == "":
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Aucun nom d'utilisateur n'a été écrit", foreground="#eaa")
            self.alerteUser.grid(row=3, column=3, sticky="w")
        elif liste[2] == False:
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Le nom d'utilisateur a déjà été utilisée", foreground="#eaa")
            self.alerteUser.grid(row=3, column=3, sticky="w")

        if liste[4] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email est invalide", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if self.emailTxt.get() == "":
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="Aucune adresse email n'a été écrit", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")
        elif liste[3] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email déjà été utilisée", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if liste[5] == False and liste[6] == False:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#eaa")
            self.alerteCode2.grid(row=6, column=3, sticky="w")
        elif liste[6] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#eaa")
            self.alerteCode1.grid(row=5, column=3, sticky="w")

        if liste[5] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#eaa")
            self.alerteCode1.grid(row=5, column=3, sticky="w")
        elif len(self.code2Txt.get()) < 8:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#eaa")
            self.alerteCode2.grid(row=6, column=3, sticky="w")

        if liste[7] == False:
            self.alerteGrade.destroy()
            self.alerteGrade = Label(self.fen, text="Le grade n'a pas été sélectionné", foreground="#eaa")
            self.alerteGrade.grid(row=7, column=3, sticky="w")

        if liste[8] == False:
            txts = [self.prenomTxt.get(), self.nomTxt.get(), self.userTxt.get(), self.emailTxt.get(), self.code1Txt.get(), self.code2Txt.get()]
            somme = ""
            for ligne in txts:
                somme = somme + detectCaratere(ligne)
            self.approuvement.destroy()
            self.approuvement = Label(self.fen, text=compilationCaractere(somme), foreground="#eaa")
            self.approuvement.grid(row=7, column=3, sticky="w")

        self.fen.after(200, partial(self.suiteAvertissement, liste))
    def suiteAvertissement(self, liste):
        "Change la couleur des messages d'avertissement"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Le compte est invalide", foreground="#e33")
        self.approuvement.grid(row=8, column=3, sticky="w")

        # Selon chaque erreur
        if liste[0] == False:
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="Aucun prénom n'a été écrit", foreground="#e33")
            self.alertePrenom.grid(row=1, column=3, sticky="w")

        if liste[1] == False:
            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="Aucun nom n'a été écrit", foreground="#e33")
            self.alerteNom.grid(row=2, column=3, sticky="w")

        if self.userTxt.get() == "":
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Aucun nom d'utilisateur n'a été écrit", foreground="#e33")
            self.alerteUser.grid(row=3, column=3, sticky="w")
        elif liste[2] == False:
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Le nom d'utilisateur a déjà été utilisée", foreground="#e33")
            self.alerteUser.grid(row=3, column=3, sticky="w")

        if liste[4] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email est invalide", foreground="#e33")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if self.emailTxt.get() == "":
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="Aucune adresse email n'a été écrit", foreground="#e33")
            self.alerteEmail.grid(row=4, column=3, sticky="w")
        elif liste[3] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email déjà été utilisée", foreground="#e33")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if liste[5] == False and liste[6] == False:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#e33")
            self.alerteCode2.grid(row=6, column=3, sticky="w")
        elif liste[6] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#e33")
            self.alerteCode1.grid(row=5, column=3, sticky="w")

        if liste[5] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#e33")
            self.alerteCode1.grid(row=5, column=3, sticky="w")
        elif len(self.code2Txt.get()) < 8:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#e33")
            self.alerteCode2.grid(row=6, column=3, sticky="w")

        if liste[7] == False:
            self.alerteGrade.destroy()
            self.alerteGrade = Label(self.fen, text="Le grade n'a pas été sélectionné", foreground="#e33")
            self.alerteGrade.grid(row=7, column=3, sticky="w")

        if liste[8] == False:
            txts = [self.prenomTxt.get(), self.nomTxt.get(), self.userTxt.get(), self.emailTxt.get(), self.code1Txt.get(), self.code2Txt.get()]
            somme = ""
            for ligne in txts:
                somme = somme + detectCaratere(ligne)
            self.approuvement.destroy()
            self.approuvement = Label(self.fen, text=compilationCaractere(somme), foreground="#e33")
            self.approuvement.grid(row=7, column=3, sticky="w")

    def retour(self):
        "Permet de retourner à la fenêtre de l'affichage des comptes"
        self.fen.destroy()
        gererComptesApp()

    def confirmer(self):
        "Vérifie et accepte un compte s'il est moindrement valable ou envoie un avertissement"
        checklist = [False, False, True, True, False, False, False, False, True]
        verdict = True

        # Vérification
        if self.prenomTxt.get() != "":
            checklist[0] = True
        if self.nomTxt.get() != "":
            checklist[1] = True
        for employe in Personne.registre.getEmployes():
            if employe.user == self.userTxt.get() or employe.user == "":
                checklist[2] = False
        for client in Personne.registre.getClients():
            if client.user == self.userTxt.get():
                checklist[2] = False
        for employe in Personne.registre.getEmployes():
            if employe.email == self.emailTxt.get():
                checklist[3] = False
        for client in Personne.registre.getClients():
            if client.email == self.emailTxt.get():
                checklist[3] = False
        if "@" in self.emailTxt.get():
            checklist[4] = True
        if len(self.code1Txt.get()) >= 8:
            checklist[5] = True
        if self.code1Txt.get() == self.code2Txt.get():
            checklist[6] = True
        if self.gradeTxt.get() != self.optionGrade[0]:
            checklist[7] = True
        if detectCaratere(self.prenomTxt.get()) != "":
            checklist[8] = False
        elif detectCaratere(self.nomTxt.get()) != "":
            checklist[8] = False
        elif detectCaratere(self.userTxt.get()) != "":
            checklist[8] = False
        elif detectCaratere(self.emailTxt.get()) != "":
            checklist[8] = False
        elif detectCaratere(self.code1Txt.get()) != "":
            checklist[8] = False
        elif detectCaratere(self.code2Txt.get()) != "":
            checklist[8] = False

        for check in checklist:
            if check == False:
                verdict = False

        if verdict == True:
            print("Nouveau compte employé!")


            try:
                employe = Personne.Employe(self.nomTxt.get(), self.prenomTxt.get(), self.emailTxt.get(), self.userTxt.get(), self.code1Txt.get(), time.strftime("%d/%m/%Y"), self.gradeTxt.get())

                Personne.registre.addEmploye(employe)
                Personne.sauvegardeEmployes()

                self.approuvement.destroy()
                self.approuvement = Label(self.fen, text="Le compte a été crée", foreground="#aea")
                self.approuvement.grid(row=8, column=3, sticky="w")

                self.fen.after(200, self.suiteApprouvement)

            except:

                # ~Approuvement~
                self.approuvement.destroy()
                self.approuvement = Label(self.fen, text="Un problème est survenu lors de la création du compte", foreground="#dd3")
                self.approuvement.grid(row=8, column=3, sticky="w")

                print("Une erreur est survenue lors de la création du compte")


            # Reset
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
            self.alertePrenom.grid(row=1, column=3, sticky="w")

            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="", foreground="#eaa")
            self.alerteNom.grid(row=2, column=3, sticky="w")

            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="", foreground="#eaa")
            self.alerteUser.grid(row=3, column=3, sticky="w")

            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
            self.alerteCode1.grid(row=5, column=3, sticky="w")

            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
            self.alerteCode2.grid(row=6, column=3, sticky="w")

            self.alerteGrade.destroy()
            self.alerteGrade = Label(self.fen, text="", foreground="#eaa")
            self.alerteGrade.grid(row=7, column=3, sticky="w")


            self.prenomTxt.set("")
            self.nomTxt.set("")
            self.userTxt.set("")
            self.emailTxt.set("")
            self.code1Txt.set("")
            self.code2Txt.set("")
            self.gradeTxt.set(self.optionGrade[1])

        else:
            #print("Je vais avertir mon boss!!! >:c")
            self.avertissement(checklist)

    def suiteApprouvement(self):
        "Change la couleur du message d'approuvement"
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Le compte a été crée", foreground="#4e4")
        self.approuvement.grid(row=8, column=3, sticky="w")

class modificationApp():
    "Responsable de la modification des comptes"

    def __init__(self):
        self.fen = Tk()

        self.prenomTxt = StringVar()
        self.nomTxt = StringVar()
        self.userTxt = StringVar()
        self.emailTxt = StringVar()
        self.code1Txt = StringVar()
        self.code2Txt = StringVar()
        self.code3Txt = StringVar()

        self.fen.title("Modfication du compte")

        # Avertissement
        self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
        self.alertePrenom.grid(row=2, column=3, sticky="w")

        self.alerteNom = Label(self.fen, text="", foreground="#eaa")
        self.alerteNom.grid(row=3, column=3, sticky="w")

        self.alerteUser = Label(self.fen, text="", foreground="#eaa")
        self.alerteUser.grid(row=4, column=3, sticky="w")

        self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
        self.alerteEmail.grid(row=5, column=3, sticky="w")

        self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode1.grid(row=6, column=3, sticky="w")

        self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode2.grid(row=7, column=3, sticky="w")

        self.alerteCode3 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode3.grid(row=8, column=3, sticky="w")

        self.approuvement = Label(self.fen, text="", foreground="#aea")
        self.approuvement.grid(row=9, column=3, sticky="w")


        self.prenomTxt.set(info.personneConnecte.prenom)
        self.nomTxt.set(info.personneConnecte.nom)
        self.userTxt.set(info.personneConnecte.user)
        self.emailTxt.set(info.personneConnecte.email)

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        self.label = Label(self.fen, text="Entrez les informations que vous voulez modifier de votre compte").grid(row=0, columnspan=2, sticky="w")
        self.underlabel = Label(self.fen, text=r"(Laissez les informations que vous voulez conserver telles qu'elles sont.)", foreground="#443").grid(row=1, columnspan=2, sticky="w")
        self.btnConfirmer = Button(self.fen, text="Confirmer", command=self.confirmer).grid(row=9, column=1)
        self.boutRetourInfo = Button(self.fen, text="Retour", command=self.retourInfo).grid(row=10, column=3, sticky="e")

        # Boites de texte

        self.prenomLabel = Label(self.fen, text="Prénom :").grid(row=2, column=0)
        self.prenomEntry = Entry(self.fen, textvariable=self.prenomTxt).grid(row=2, column=1)

        self.nomLabel = Label(self.fen, text="Nom :").grid(row=3, column=0)
        self.nomEntry = Entry(self.fen, textvariable=self.nomTxt).grid(row=3, column=1)

        self.userLabel = Label(self.fen, text="Nom d'utilisateur :").grid(row=4, column=0)
        self.userEntry = Entry(self.fen, textvariable=self.userTxt).grid(row=4, column=1)

        self.emailLabel = Label(self.fen, text="Adresse email :").grid(row=5, column=0)
        self.emailEntry = Entry(self.fen, textvariable=self.emailTxt).grid(row=5, column=1)

        self.code1Label = Label(self.fen, text="Nouveau mot de passe :").grid(row=6, column=0)
        self.code1Entry = Entry(self.fen, textvariable=self.code1Txt, show="*").grid(row=6, column=1)

        self.code2Label = Label(self.fen, text="Confirmation nouveau mot de passe :").grid(row=7, column=0)
        self.code2Entry = Entry(self.fen, textvariable=self.code2Txt, show="*").grid(row=7, column=1)

        self.code3Label = Label(self.fen, text="Ancien mot de passe :").grid(row=8, column=0)
        self.code3Entry = Entry(self.fen, textvariable=self.code3Txt, show="*").grid(row=8, column=1)

        self.fen.mainloop()

    def avertissement(self, liste):
        "Fait apparaître des messages d'avertissement où il est nécessaire"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Les informations du compte n'ont pas été changées", foreground="#eaa")
        self.approuvement.grid(row=9, column=3, sticky="w")

        self.alertePrenom.destroy()
        self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
        self.alertePrenom.grid(row=2, column=3, sticky="w")

        self.alerteNom.destroy()
        self.alerteNom = Label(self.fen, text="", foreground="#eaa")
        self.alerteNom.grid(row=3, column=3, sticky="w")

        self.alerteUser.destroy()
        self.alerteUser = Label(self.fen, text="", foreground="#eaa")
        self.alerteUser.grid(row=4, column=3, sticky="w")

        self.alerteEmail.destroy()
        self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
        self.alerteEmail.grid(row=5, column=3, sticky="w")

        self.alerteCode1.destroy()
        self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode1.grid(row=6, column=3, sticky="w")

        self.alerteCode2.destroy()
        self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode2.grid(row=7, column=3, sticky="w")

        # Selon chaque erreur
        if liste[0] == False:
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="Aucun prénom n'a été écrit", foreground="#eaa")
            self.alertePrenom.grid(row=2, column=3, sticky="w")

        if liste[1] == False:
            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="Aucun nom n'a été écrit", foreground="#eaa")
            self.alerteNom.grid(row=3, column=3, sticky="w")

        if self.userTxt.get() == "":
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Aucun nom d'utilisateur n'a été écrit", foreground="#eaa")
            self.alerteUser.grid(row=4, column=3, sticky="w")
        elif liste[2] == False:
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Le nom d'utilisateur a déjà été utilisée", foreground="#eaa")
            self.alerteUser.grid(row=4, column=3, sticky="w")

        if liste[4] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email est invalide", foreground="#eaa")
            self.alerteEmail.grid(row=5, column=3, sticky="w")

        if self.emailTxt.get() == "":
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="Aucune adresse email n'a été écrit", foreground="#eaa")
            self.alerteEmail.grid(row=5, column=3, sticky="w")
        elif liste[3] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email déjà été utilisée", foreground="#eaa")
            self.alerteEmail.grid(row=5, column=3, sticky="w")

        if liste[5] == False and liste[6] == False:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#eaa")
            self.alerteCode2.grid(row=7, column=3, sticky="w")
        elif liste[6] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#eaa")
            self.alerteCode1.grid(row=6, column=3, sticky="w")

        if liste[5] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#eaa")
            self.alerteCode1.grid(row=6, column=3, sticky="w")
        elif len(self.code2Txt.get()) == 0:
            pass
        elif len(self.code2Txt.get()) < 8:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#eaa")
            self.alerteCode2.grid(row=7, column=3, sticky="w")

        if self.code3Txt.get() == "":
            self.alerteCode3.destroy()
            self.alerteCode3 = Label(self.fen, text="Aucun code n'est entré", foreground="#eaa")
            self.alerteCode3.grid(row=8, column=3, sticky="w")
        elif liste[7] == False:
            self.alerteCode3.destroy()
            self.alerteCode3 = Label(self.fen, text="Le code entré est incorrect", foreground="#eaa")
            self.alerteCode3.grid(row=8, column=3, sticky="w")

        self.fen.after(200, partial(self.suiteAvertissement, liste))

    def suiteAvertissement(self, liste):
        "Change la couleur des messages d'avertissement"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Les informations du compte n'ont pas été changées", foreground="#e33")
        self.approuvement.grid(row=9, column=3, sticky="w")

        # Selon chaque erreur
        if liste[0] == False:
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="Aucun prénom n'a été écrit", foreground="#e33")
            self.alertePrenom.grid(row=2, column=3, sticky="w")

        if liste[1] == False:
            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="Aucun nom n'a été écrit", foreground="#e33")
            self.alerteNom.grid(row=3, column=3, sticky="w")

        if self.userTxt.get() == "":
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Aucun nom d'utilisateur n'a été écrit", foreground="#e33")
            self.alerteUser.grid(row=4, column=3, sticky="w")
        elif liste[2] == False:
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Le nom d'utilisateur a déjà été utilisée", foreground="#e33")
            self.alerteUser.grid(row=4, column=3, sticky="w")

        if liste[4] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email est invalide", foreground="#e33")
            self.alerteEmail.grid(row=5, column=3, sticky="w")

        if self.emailTxt.get() == "":
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="Aucune adresse email n'a été écrit", foreground="#e33")
            self.alerteEmail.grid(row=5, column=3, sticky="w")
        elif liste[3] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email déjà été utilisée", foreground="#e33")
            self.alerteEmail.grid(row=5, column=3, sticky="w")

        if liste[5] == False and liste[6] == False:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#e33")
            self.alerteCode2.grid(row=7, column=3, sticky="w")
        elif liste[6] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#e33")
            self.alerteCode1.grid(row=6, column=3, sticky="w")

        if liste[5] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#e33")
            self.alerteCode1.grid(row=6, column=3, sticky="w")
        elif len(self.code2Txt.get()) == 0:
            pass
        elif len(self.code2Txt.get()) < 8:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#e33")
            self.alerteCode2.grid(row=7, column=3, sticky="w")

        if self.code3Txt.get() == "":
            self.alerteCode3.destroy()
            self.alerteCode3 = Label(self.fen, text="Aucun code n'est entré", foreground="#e33")
            self.alerteCode3.grid(row=8, column=3, sticky="w")
        elif liste[7] == False:
            self.alerteCode3.destroy()
            self.alerteCode3 = Label(self.fen, text="Le code entré est incorrect", foreground="#e33")
            self.alerteCode3.grid(row=8, column=3, sticky="w")

    def retourInfo(self):
        "Permet de retourner à la fenêtre de l'affichage des infos du compte"
        self.fen.destroy()
        infoApp()

    def confirmer(self):
        "Vérifie et accepte les nouvelles informations si elles sont moindrement valable ou envoie un avertissement"
        checklist = [False, False, True, True, False, False, False, False]
        verdict = True

        # Vérification
        if self.prenomTxt.get() != "":
            checklist[0] = True
        if self.nomTxt.get() != "":
            checklist[1] = True
        for employe in Personne.registre.getEmployes():
            if employe.user == self.userTxt.get() or employe.user == "":
                checklist[2] = False
        for client in Personne.registre.getClients():
            if client.user == self.userTxt.get():
                checklist[2] = False
        for employe in Personne.registre.getEmployes():
            if employe.email == self.emailTxt.get():
                checklist[3] = False
        for client in Personne.registre.getClients():
            if client.email == self.emailTxt.get():
                checklist[3] = False
        if "@" in self.emailTxt.get():
            checklist[4] = True
        if len(self.code1Txt.get()) >= 8 or len(self.code1Txt.get()) == 0:
            checklist[5] = True
        if self.code1Txt.get() == self.code2Txt.get():
            checklist[6] = True
        if self.code3Txt.get() == info.personneConnecte.code:
            checklist[7] = True

        if self.userTxt.get() == info.personneConnecte.user:
            checklist[2] = True
        if self.emailTxt.get() == info.personneConnecte.email:
            checklist[3] = True

        for check in checklist:
            if check == False:
                verdict = False

        if verdict == True:
            print("Modification du compte!")

            for client in Personne.registre.getClients():
                if client == info.personneConnecte:

                    try:

                        client.nom = self.nomTxt.get()
                        client.prenom = self.prenomTxt.get()
                        client.user = self.userTxt.get()
                        client.email = self.emailTxt.get()

                        info.personneConnecte.nom = self.nomTxt.get()
                        info.personneConnecte.prenom = self.prenomTxt.get()
                        info.personneConnecte.user = self.userTxt.get()
                        info.personneConnecte.email = self.emailTxt.get()


                        if self.code1Txt.get() != "":
                            client.code = self.code1Txt.get()
                            info.personneConnecte.code = self.code1Txt.get()

                        Personne.sauvegardeClients()

                        # Approuvement
                        self.approuvement.destroy()
                        self.approuvement = Label(self.fen, text="Les informations du compte ont été modifiées", foreground="#aea")
                        self.approuvement.grid(row=9, column=3, sticky="w")


                        self.fen.after(200, self.suiteApprouvement)
                    except:

                        # ~Approuvement~
                        self.approuvement.destroy()
                        self.approuvement = Label(self.fen, text="Un problème est survenu lors de la modification du compte", foreground="#dd3")
                        self.approuvement.grid(row=9, column=3, sticky="w")
                        print("Une erreur est survenue lors de la création du compte")

            for employe in Personne.registre.getEmployes():
                if employe == info.personneConnecte:

                    try:

                        employe.nom = self.nomTxt.get()
                        employe.prenom = self.prenomTxt.get()
                        employe.user = self.userTxt.get()
                        employe.email = self.emailTxt.get()

                        info.personneConnecte.nom = self.nomTxt.get()
                        info.personneConnecte.prenom = self.prenomTxt.get()
                        info.personneConnecte.user = self.userTxt.get()
                        info.personneConnecte.email = self.emailTxt.get()

                        if self.code1Txt.get() != "":
                            employe.code = self.code1Txt.get()
                            info.personneConnecte.code = self.code1Txt.get()

                        Personne.sauvegardeEmployes()

                        # Approuvement
                        self.approuvement.destroy()
                        self.approuvement = Label(self.fen, text="Les informations du compte ont été modifiées", foreground="#aea")
                        self.approuvement.grid(row=9, column=3, sticky="w")

                        self.fen.after(200, self.suiteApprouvement)
                    except:

                        # ~Approuvement~
                        self.approuvement.destroy()
                        self.approuvement = Label(self.fen, text="Un problème est survenu lors de la modification du compte", foreground="#dd3")
                        self.approuvement.grid(row=9, column=3, sticky="w")
                        print("Une erreur est survenue lors de la création du compte")

            # Reset alertes
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
            self.alertePrenom.grid(row=2, column=3, sticky="w")

            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="", foreground="#eaa")
            self.alerteNom.grid(row=3, column=3, sticky="w")

            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="", foreground="#eaa")
            self.alerteUser.grid(row=4, column=3, sticky="w")

            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
            self.alerteEmail.grid(row=5, column=3, sticky="w")

            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
            self.alerteCode1.grid(row=6, column=3, sticky="w")

            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
            self.alerteCode2.grid(row=7, column=3, sticky="w")

            self.alerteCode3.destroy()
            self.alerteCode3 = Label(self.fen, text="", foreground="#eaa")
            self.alerteCode3.grid(row=8, column=3, sticky="w")

            # Reset cases
            self.prenomTxt.set(info.personneConnecte.prenom)
            self.nomTxt.set(info.personneConnecte.nom)
            self.userTxt.set(info.personneConnecte.user)
            self.emailTxt.set(info.personneConnecte.email)
            self.code1Txt.set("")
            self.code2Txt.set("")
            self.code3Txt.set("")


        else:
            #print("Je vais avertir mon boss!!! >:c")
            self.avertissement(checklist)

    def suiteApprouvement(self):
        "Change la couleur de l'approuvement"
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Les informations du compte ont été modifiées", foreground="#4a4")
        self.approuvement.grid(row=9, column=3, sticky="w")

class cartesApp():
    "Permet de voir les cartes d'un client et leurs informations liées"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("Cartes liées au compte")
        self.fen.geometry("1000x500")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        #Afficheur de cartes

        self.carteLabel = Label(self.fen, text="Liste des cartes actives:").grid(row=0, column=0)

        self.btnAjout = Button(self.fen, text="Ajouter une carte", command=self.addCarte).grid(row=2, column=0)
        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).grid(row=3, column=0, sticky="n")

        numCarte = 1
        valEqua = 1

        self.scrollingFrame = Frame(self.fen)

        self.listeCartesLabel = Label(self.scrollingFrame, text="Liste des cartes liées au compte:").grid(row=4, column=1, sticky="w")

        self.canvasC = Canvas(self.scrollingFrame, height=400, width=852, background="#d3d5d2")
        self.frameC = Frame(self.canvasC, background="#d3d5d2")
        self.scrollerC = Scrollbar(self.scrollingFrame, orient="vertical", command=self.canvasC.yview)  # Rendu visible si slef.frameC est trop grand pour le canvas

        self.canvasC.create_window((0, 0), window=self.frameC, anchor="nw")


        for carte in info.cartesPersonneConnecte:

            self.nomCarteLabel = Label(self.frameC, text="Carte numéro {} :".format(numCarte, carte.getNumeroCarte())).grid(row=valEqua, column=1, sticky="w")
            self.btnSupprimer = Button(self.frameC, text="Supprimer cette carte de la liste", command=partial(self.delCarte, info.personneConnecte, carte)).grid(row=valEqua + 1, column=1, sticky="w")
            self.nomCarteLabel = Label(self.frameC, text="     Numéro carte : {}   Numéro sécurité : {}".format(carte.getNumeroCarte(), carte.getNumeroSecurite())).grid(row=valEqua + 1, column=2, sticky="w")
            self.nomCarteLabel = Label(self.frameC, text="     Date d'expiration : en {}   Type : {}".format(getTempsCarte(carte.getDateExpiration()), carte.getType())).grid(row=valEqua + 2, column=2, sticky="w")

            numCarte = numCarte + 1
            valEqua = valEqua + 3

        if info.cartesPersonneConnecte == []:
            self.AvertissementCarteLabel = Label(self.fen, text="Aucune carte de crédit n'est inscite à votre compte.\nPour en ajouter une, veuiller cliquer sur « Ajouter une carte ».", foreground="#443").grid(row=1, column=1, rowspan=3, columnspan=2)

        self.frameC.update()
        self.canvasC.configure(yscrollcommand=self.scrollerC.set, scrollregion=("0", "0", "0", str(self.frameC.winfo_height())))

        self.canvasC.grid(row=5, column=1)
        self.scrollerC.grid(row=5, column=3, sticky="ns")

        self.scrollingFrame.grid(row=3, column=1, sticky="e")

        self.fen.mainloop()

    def addCarte(self):
        "Permet d'aller à la fenêtre d'ajout des cartes"
        self.fen.destroy()
        addCarteApp()

    def delCarte(self, client, carte):
        "Envoie un message d'avertissement avant de supprimer la carte"
        avertissement = messagebox.askyesno("Avertissement", "Voulez-vous vraiment supprimer cette carte?\n    Numéro : " + str(carte.getNumeroCarte()) + ".")
        if avertissement == 1:

            self.fen.destroy()
            try:

                info.cartesPersonneConnecte.remove(carte)

                client.delCarte(carte)

                Personne.sauvegardeClients()
                Personne.sauvegardeCartes()
            except:
                print("une erreur est survenue lors de la supression de la carte")
            cartesApp()


    def retour(self):
        "Permet de retourner à la fenêtre principale"
        self.fen.destroy()
        mainWindow()

class infoApp():
    "Permet de voir les informations liées à un compte"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("Informations sur le compte")
        self.fen.geometry("750x500")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")


        self.prenomLabel = Label(self.fen, text="Prénom : {} ".format(info.personneConnecte.prenom)).grid(row=1, column=0)
        self.nomLabel = Label(self.fen, text="Nom : {} ".format(info.personneConnecte.nom)).grid(row=2, column=0)
        self.emailLabel = Label(self.fen, text="Adresse email : {} ".format(info.personneConnecte.email)).grid(row=3, column=0)
        self.userLabel = Label(self.fen, text="Nom d'utilisateur : {} ".format(info.personneConnecte.user)).grid(row=4, column=0)
        self.dateLabel = Label(self.fen, text="Date d'arrivée : le {} ".format(getTempsComplet(info.personneConnecte.date))).grid(row=5, column=0)
        self.btnModificateur = Button(self.fen, text="Modifier les informations du compte", command=self.modification).grid(row=9, column=0)

        if info.personneConnecte.grade == "Client":
            self.gradeLabel = Label(self.fen, text="Niveau : {} ".format(info.personneConnecte.grade)).grid(row=6, column=0)

            self.btnCartes = Button(self.fen, text="Voir mes cartes de crédit liées au compte", command=self.voirCartes).grid(row=8, column=0)
            self.btnSupprimer = Button(self.fen, text="Supprimer mon compte", command=partial(self.suppressionClient, info.personneConnecte)).grid(row=10, column=0)
        else:
            self.gradeLabel = Label(self.fen, text="Grade : {} ".format(info.personneConnecte.grade)).grid(row=6, column=0)
            self.btnSupprimer = Button(self.fen, text="Supprimer mon compte", command=partial(self.suppressionEmploye, info.personneConnecte)).grid(row=10, column=0)


        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).grid(row=11, column=0)

        self.fen.mainloop()

    def voirCartes(self):
        "Permet d'aller à la fenêtre de l'affichage des cartes"
        self.fen.destroy()
        cartesApp()

    def modification(self):
        "Permet d'aller à la fenêtre de modification du compte"
        self.fen.destroy()
        modificationApp()

    def suppressionClient(self, client):
        "Permet la suppression du compte après avertissement s'il s'agit d'un client"
        avertissement = messagebox.askyesno("Avertissement", "Voulez-vous vraiment supprimer votre compte?\n   Aucun retour en arrière ne sera possible.")
        if avertissement == 1:

            self.fen.destroy()
            try:

                Personne.registre.delClient(client)

                Personne.sauvegardeClients()
                Personne.sauvegardeCartes()

                info.personneConnecte = (None, None, None, None, None, None, None)
                info.cartesPersonneConnecte = []
                print("---Le compte de {} {} a été supprimé!---".format(info.personneConnecte.prenom, info.personneConnecte.nom))
            except:
                print("Une erreur est survenue lors de la supression de la carte")
            logInApp()

    def suppressionEmploye(self, employe):
        "Permet la suppression du compte après avertissement s'il s'agit d'un employé"
        avertissement = messagebox.askyesno("Avertissement", "Voulez-vous vraiment supprimer votre compte?\n   Aucun retour en arrière ne sera possible.")
        if avertissement == 1:

            self.fen.destroy()
            try:

                Personne.registre.delEmploye(employe)

                Personne.sauvegardeEmployes()

                info.personneConnecte = (None, None, None, None, None, None, None)
                info.cartesPersonneConnecte = []
                print("---Le compte de {} {} a été supprimé!---".format(info.personneConnecte.prenom, info.personneConnecte.nom))
            except:
                print("Une erreur est survenue lors de la supression de la carte")
            logInApp()

    def retour(self):
        "Permet de retourner à la fenêtre principale"
        self.fen.destroy()
        mainWindow()

class infoGenre():
    "Permet de voir les informations reliées aux genres du film sélectionné"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("Informations sur les genres")
        self.fen.geometry("750x500")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        emplacement = 2

        # Informations générales

        if len(info.film.getGenres()) > 1:
            self.titreLabel = Label(self.fen, text="Genres avec leur définition :").grid(row=1, column=0)

            for genre in info.film.getGenres():
                self.listeFilmLabel = Label(self.fen, text="    {} : {}".format(genre.nom, genre.description.replace(r"\n", "\n"))).grid(row=emplacement, column=1, sticky="w")
                emplacement = emplacement + 1
        else:
            self.titreLabel = Label(self.fen, text="Genre avec sa définition :").grid(row=1, column=0)
            self.listeFilmLabel = Label(self.fen, text="    {} : {}".format(info.film.getGenres()[0].nom, info.film.getGenres()[0].description.replace(r"\n", "\n"))).grid(row=emplacement, column=1, sticky="w")
            emplacement = emplacement + 1


        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).grid(row=emplacement, column=3)


        self.fen.mainloop()

    def retour(self):
        "Permet de retourner à la fenêtre des informations sur le film"
        self.fen.destroy()
        infoFilm()

class infoActeur():
    "Permet de voir les informations reliées à l'acteur sélectionné"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("Informations sur l'acteur")
        self.fen.geometry("750x500")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")



        emplacement = 3

        # Informations générales
        self.titreLabel = Label(self.fen, text="Prénom et nom de l'acteur : {} {} ".format(info.acteur.prenom, info.acteur.nom)).grid(row=1, column=0)
        if len(info.acteur.getListeFilmsJoues()) > 1:
            self.listeFilmLabel = Label(self.fen, text="Liste des films joués :").grid(row=2, column=1, sticky="w")

            for filmJoue in info.acteur.getListeFilmsJoues():
                self.nomFilmLabel = Label(self.fen, text="    {}".format(filmJoue.getNomFilm())).grid(row=emplacement, column=1, sticky="w")
                emplacement = emplacement + 1
        else:
            self.listeFilmLabel = Label(self.fen, text="Film joué : {}".format(info.acteur.getListeFilmsJoues()[0].getNomFilm())).grid(row=2, column=1, sticky="w")


        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).grid(row=emplacement, column=3)


        self.fen.mainloop()

    def retour(self):
        "Permet de retourner à la fenêtre des informations sur le film"
        self.fen.destroy()
        info.acteur = ""
        infoFilm()

class infoFilm():
    "Permet de voir les informations reliées aux films"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("Informations sur le film")
        self.fen.geometry("1000x600")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")


        emplacement = 6

        if info.film != "":

            # Informations générales
            self.titreLabel = Label(self.fen, text="Titre : {} ".format(info.film.nom)).grid(row=1, column=0)
            self.dureeLabel = Label(self.fen, text="Durée : {}".format(info.film.duree, info.film.description)).grid(row=2, column=1, sticky="w")
            self.resumeLabel = Label(self.fen, text="Résumé : {}".format(info.film.description.replace(r"\n", "\n"))).grid(row=3, column=1, sticky="w")

            # Partie des genres
            if len(info.film.getGenres()) != 1:
                allGenres = ""
                numeroGenre = 1
                for genre in info.film.getGenres():

                    if numeroGenre == 1:
                        allGenres = genre.nom
                    elif numeroGenre != len(info.film.getGenres()):
                        allGenres = "{}, {}".format(allGenres, genre.nom)
                    else:
                        allGenres = "{} et {}".format(allGenres, genre.nom)

                    numeroGenre = numeroGenre + 1

                self.genreLabel = Label(self.fen, text="Genres : {}".format(allGenres)).grid(row=4, column=1, sticky="w")
                self.btnInfoGenre = Button(self.fen, text="Informations sur les genres", command=self.infoGenre).grid(row=4, column=2, sticky="w")
            else:
                self.genreLabel = Label(self.fen, text="Genre : {}".format(info.film.getGenres()[0].nom)).grid(row=4, column=1, sticky="w")
                self.btnInfoGenre = Button(self.fen, text="Informations sur le genre", command=self.infoGenre).grid(row=4, column=2, sticky="w")

            # Partie des acteurs
            self.hautActeursLabel = Label(self.fen, text="Acteurs ayant joués dans ce film :").grid(row=5, column=1, sticky="w")
            for acteur in Personne.registre.getActeurs():

                for filmJoue in acteur.getListeFilmsJoues():

                    if filmJoue.getNomFilm() == info.film.nom:
                        self.acteurNomLabel = Label(self.fen, text="    Prénom et nom : {} {}".format(acteur.prenom, acteur.nom)).grid(row=emplacement, column=1, sticky="w")
                        self.acteurPersonageLabel = Label(self.fen, text="    Nom du personnage joué : {}    Cachet fait : {}".format(filmJoue.getNomPersonnage(), filmJoue.getCachet())).grid(row=emplacement + 1, column=1, sticky="w")
                        self.acteurDatesLabel = Label(self.fen, text="    Date d'emploit : le {}    Date de fin de contract : le {}".format(getTempsComplet(filmJoue.getDebutEmploit()), getTempsComplet(filmJoue.getFinEmploit()))).grid(row=emplacement + 2, column=1, sticky="w")
                        self.btnInfoActeur = Button(self.fen, text="Informations sur l'acteur", command=partial(self.infoActeur, acteur)).grid(row=emplacement, column=2, sticky="w")
                        emplacement = emplacement + 3


        else:
            self.titreLabel = Label(self.fen, text="Malheureusement, une erreur est survenue lors de la colecte des informations").grid(row=1, column=0)


        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).grid(row=emplacement, column=3)

        self.fen.mainloop()

    def infoGenre(self):
        "Permet d'aller à la fenêtre des informations sur les genres du film"
        self.fen.destroy()
        infoGenre()

    def infoActeur(self, acteur):
        "Permet d'aller à la fenêtre des informations sur les acteurs du film"
        self.fen.destroy()
        info.acteur = acteur
        infoActeur()

    def retour(self):
        "Permet de retourner à la fenêtre principale"
        self.fen.destroy()
        info.film = ""
        mainWindow()

class gererComptesApp():
    "Permet de voir les informations des tout les comptes et de les supprimer"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("Gestionnaire des comptes")
        self.fen.geometry("1000x500")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        #Afficheur des employées et des clients

        self.listeLabel = Label(self.fen, text="Liste des comptes liés à l'application:").grid(row=0, column=0)

        self.btnAjout = Button(self.fen, text="Ajouter un employé", command=self.addEmploye).grid(row=2, column=0)
        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).grid(row=3, column=0, sticky="n")

        numEmploye = 0
        valEquaE = 0

        numClient = 0
        valEquaC = 0

        self.scrollingFrame = Frame(self.fen)

        # ///Partie des employés///
        self.listeEmployeLabel = Label(self.fen, text="Liste des employés:").grid(row=2, column=1, sticky="w")

        self.canvasE = Canvas(self.scrollingFrame, height=190, width=780, background="#d3d5d2")
        self.frameE = Frame(self.canvasE, background="#d3d5d2")
        self.scrollerE = Scrollbar(self.scrollingFrame, orient="vertical", command=self.canvasE.yview) # Rendu visible si slef.frameE est trop grand pour le canvas

        self.canvasE.create_window((0, 0), window=self.frameE, anchor="nw")


        for employe in Personne.registre.getEmployes():
            self.nomEmployeLabel = Label(self.frameE, text="Employé numéro {} : {} {}".format(numEmploye + 1, employe.prenom, employe.nom), background="#b3b5b2", foreground="#fff").grid(row=valEquaE, column=1, sticky="w")
            self.btnSupprimer = Button(self.frameE, text="Supprimer ce compte employé", command=partial(self.delEmploye, employe)).grid(row=valEquaE + 1, column=1, sticky="w")
            self.nomCarteLabel = Label(self.frameE, text="     Nom d'utilisateur : {}   Adresse couriel : {}".format(employe.user, employe.email), background="#b3b5b2", foreground="#fff").grid(row=valEquaE + 1, column=2, sticky="w")
            self.nomCarteLabel = Label(self.frameE, text="     Code de son compte : {}   Date d'ajout à l'équipe : le {}    Grade : {}".format(employe.code, getTempsComplet(employe.date), employe.grade), background="#b3b5b2", foreground="#fff").grid(row=valEquaE + 2, column=2, sticky="w")



            numEmploye = numEmploye + 1
            valEquaE = valEquaE + 3


        self.frameE.update()
        self.canvasE.configure(yscrollcommand=self.scrollerE.set, scrollregion=("0", "0", "0", str(self.frameE.winfo_height())))

        self.canvasE.grid(row=3, column=1)
        self.scrollerE.grid(row=3, column=3, sticky="ns")

        # ///Partie des clients///

        self.listeClientsLabel = Label(self.scrollingFrame, text="Liste des clients:").grid(row=4, column=1, sticky="w")

        self.canvasC = Canvas(self.scrollingFrame, height=190, width=780, background="#d3d5d2")
        self.frameC = Frame(self.canvasC, background="#d3d5d2")
        self.scrollerC = Scrollbar(self.scrollingFrame, orient="vertical", command=self.canvasC.yview)  # Rendu visible si slef.frameC est trop grand pour le canvas

        self.canvasC.create_window((0, 0), window=self.frameC, anchor="nw")

        for client in Personne.registre.getClients():
            self.nomEmployeLabel = Label(self.frameC, text="Client numéro {} : {} {}".format(numClient + 1, client.prenom, client.nom), background="#b3b5b2", foreground="#fff").grid(row=valEquaC, column=1, sticky="w")
            self.btnSupprimer = Button(self.frameC, text="Supprimer ce compte client", command=partial(self.delClient, client)).grid(row=valEquaC + 1, column=1, sticky="w")
            self.nomCarteLabel = Label(self.frameC, text="     Nom d'utilisateur : {}   Adresse couriel : {}".format(client.user, client.email), background="#b3b5b2", foreground="#fff").grid(row=valEquaC + 1, column=2, sticky="w")
            self.nomCarteLabel = Label(self.frameC, text="     Code de son compte : {}   Date de création de son compte : le {}".format(client.code, getTempsComplet(client.date)), background="#b3b5b2", foreground="#fff").grid(row=valEquaC + 2, column=2, sticky="w")

            numClient = numClient + 1
            valEquaC = valEquaC + 3
        if Personne.registre.getClients() == []:
            self.aucunClientLabel = Label(self.frameC, text="Aucun client :(", background="#d3d5d2", foreground="#b3b5b2").grid(rowspan=3)

        self.frameC.update()
        self.canvasC.configure(yscrollcommand=self.scrollerC.set, scrollregion=("0", "0", "0", str(self.frameC.winfo_height())))

        self.canvasC.grid(row=5, column=1)
        self.scrollerC.grid(row=5, column=3, sticky="ns")

        self.scrollingFrame.grid(row=3, column=1, sticky="e")


        self.fen.mainloop()


    def addEmploye(self):
        "Permet d'aller à la fenêtre d'ajout d'employé"
        self.fen.destroy()
        addEmployeApp()

    def delEmploye(self, employe):
        "Permet la suppression du compte après avertissement pour un employé"
        if employe == info.personneConnecte:
            print("C'est ton compte!")
            avertissement = messagebox.askyesno("Avertissement", "Voulez-vous vraiment supprimer votre compte?\n   Aucun retour en arrière ne sera possible.")
            if avertissement == 1:

                self.fen.destroy()

                try:

                    Personne.registre.delEmploye(employe)

                    Personne.sauvegardeEmployes()

                    info.personneConnecte = (None, None, None, None, None, None, None)
                    info.cartesPersonneConnecte = []
                    print("---Le compte de {} {} a été supprimé!---".format(employe.prenom, employe.nom))
                except:
                    print("Une erreur est survenue lors de la suppression du compte de {} {}".format(employe.prenom, employe.nom))
                logInApp()
        else:
            avertissement = messagebox.askyesno("Avertissement", "Voulez-vous vraiment supprimer le compte de {} {}?\n   Aucun retour en arrière ne sera possible.".format(employe.prenom, employe.nom))
            if avertissement == 1:

                self.fen.destroy()

                try:

                    Personne.registre.delEmploye(employe)

                    Personne.sauvegardeEmployes()

                    print("---Le compte de {} {} a été supprimé!---".format(employe.prenom, employe.nom))
                except:
                    print("Une erreur est survenue lors de la suppression du compte de {} {}".format(employe.prenom, employe.nom))
                gererComptesApp()


    def delClient(self, client):
        "Permet la suppression du compte après avertissement pour un client"
        avertissement = messagebox.askyesno("Avertissement", "Voulez-vous vraiment supprimer le compte de {} {}?\n   Aucun retour en arrière ne sera possible.".format(client.prenom, client.nom))
        if avertissement == 1:

            self.fen.destroy()
            try:

                Personne.registre.delClient(client)

                Personne.sauvegardeClients()
                Personne.sauvegardeCartes()

                print("---Le compte de {} {} a été supprimé!---".format(client.prenom, client.nom))
            except:
                print("Une erreur est survenue lors de la suppression du compte de {} {}".format(client.prenom, client.nom))
            gererComptesApp()


    def retour(self):
        "Permet de retourner à la fenêtre principale"
        self.fen.destroy()
        mainWindow()

class parametreApp():
    "Permet de naviguer entre plusieurs fenêtres"
    def __init__(self):
        self.fen = Tk()

        self.fen.title("Paramètres du compte")
        self.fen.geometry("300x500")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        self.btnRetour = Button(self.fen, text="Retour", command=self.retour).pack()
        self.btnInfoCompte = Button(self.fen, text="Informations sur le compte", command=self.showInfo).pack()
        if info.personneConnecte.grade == "Client":
            self.btnCartes = Button(self.fen, text="Voir les cartes de crédit liées à mon compte", command=self.voirCartes).pack()
        elif info.personneConnecte.grade == "1":
            self.btnGererCompte = Button(self.fen, text="Gerer les comptes", command=self.gererComptes).pack()

        self.btnLogOut = Button(self.fen, text="Déconnexion", command=self.logOut).pack()


        self.fen.mainloop()

    def retour(self):
        "Permet de retourner à la fenêtre principale"
        self.fen.destroy()
        mainWindow()

    def showInfo(self):
        "Permet d'aller à la fenêtre des informations sur le compte"
        self.fen.destroy()
        infoApp()

    def voirCartes(self):
        "Permet d'aller à la fenêtre de l'affichage des cartes"
        self.fen.destroy()
        cartesApp()

    def gererComptes(self):
        "Permet d'aller à la fenêtre de l'affichage des comptes"
        self.fen.destroy()
        gererComptesApp()

    def logOut(self):
        "Permet de se déconnecter"
        print("---{} {} est déconnecté!---".format(info.personneConnecte.prenom, info.personneConnecte.nom))
        info.personneConnecte = (None, None, None, None, None, None, None)
        info.cartesPersonneConnecte = []
        self.fen.destroy()
        logInApp()


class mainWindow():
    "Fenêtre principale où l'on peut voir les « films »"

    def __init__(self):
        self.fen = Tk()

        # Haut
        self.fen.title("レwind")
        self.fen.geometry("1133x700")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
            pass
        except:
            print("Erreur dans l'affichage du logo")

        # Bandes
        self.topUserLabel = Label(self.fen, background="#232522", foreground="#ddd",font="Helvetica 16 bold", text="Bienvenue, {} {} {}".format(info.personneConnecte.prenom, info.personneConnecte.nom, " "*300), height="2", anchor="w").grid(row=0, column=0, columnspan=200, sticky="w")
        self.filmsAffichesLabel = Label(self.fen, background="#aaa", foreground="#333", font="Helvetica 10 bold", text="Voici les films à l'affiche {}".format( " "*300), height="2", anchor="w").grid(row=1, column=0, columnspan=200, sticky="w")
        self.rempliseurPourColone = Label(self.fen, text="{}".format(" "*50)).grid(row=2, column=0, sticky="w")
        self.btnParametres = Button(self.fen, text="Paramètres", command=self.openParametre).grid(row=0, column=10)

        # Avertissement
        self.alerteCarte = Label(self.fen, text="", foreground="#eaa")
        self.alerteCarte.grid(row=4, column=0, sticky="e")

        # Remplisseurs

        self.row2 = Label(self.fen).grid(row=2)
        self.column2 = Label(self.fen).grid(column=2)

        # Vidéos

        #self.film1Label = Label(self.fen, background="#aca", text="Les Hommes en noir").grid(row=4, column=1)
        self.btnJouer1 = Button(self.fen, text="Jouer ce film", command=partial(self.openFile, r"Les Hommes en noir - Bande Annonce.mp4")).grid(row=6, column=1)
        self.btnInfo1 = Button(self.fen, text="Infos", command=partial(self.infoFilm, "Les Hommes en noir")).grid(row=7, column=1)
        #self.film2Label = Label(self.fen, background="#aca", text="Le Grinch").grid(row=4, column=3)
        self.btnJouer1 = Button(self.fen, text="Jouer ce film", command=partial(self.openFile, r"Le Grinch - Bande Annonce.mp4")).grid(row=6, column=3)
        self.btnInfo1 = Button(self.fen, text="Infos", command=partial(self.infoFilm, "Le Grinch")).grid(row=7, column=3)

        # Images des affiches

        try:
            # Vérifie si l'image de « Les Hommes en noir » est dans le fichier
            if os.path.isfile(localisationImages + r"Les Hommes en noir 333x500.png"):
                print("Fichier « Les Hommes en noir 333x500.png » trouvé!")
            else:
                print("Aucun fichier « Les Hommes en noir 333x500.png » de trouvé")

                lien = localisationImagesGitHub + r"Les%20Hommes%20en%20noir%20333x500.png"

                reponse = requests.get(lien, stream=True)

                if reponse.status_code == 200:

                    # Évite le fichier téléchargé d'avoir une largeur de zéro
                    reponse.raw.decode_content = True

                    # Ouvre un fichier local
                    with open("Les Hommes en noir 333x500.png",'wb') as f:
                        shutil.copyfileobj(reponse.raw, f)

                    print("Image téléchargée avec succès: ", "Les Hommes en noir 333x500.png")

                    shutil.move(path + r"\Les Hommes en noir 333x500.png", localisationImages + r"Les Hommes en noir 333x500.png")
                    #print("Image déplacée")
                else:
                    print("L'image n'a pas pue être obtenue")

            # Vérifie si l'image de « Le Grinch » est dans le fichier
            if os.path.isfile(localisationImages + r"Le Grinch 354x500.png"):
                print("Fichier « Le Grinch 354x500.png » trouvé!")
            else:
                print("Aucun fichier « Le Grinch 354x500.png » de trouvé")

                lien = localisationImagesGitHub + r"Le%20Grinch%20354x500.png"

                reponse = requests.get(lien, stream=True)

                if reponse.status_code == 200:

                    # Évite le fichier téléchargé d'avoir une largeur de zéro
                    reponse.raw.decode_content = True

                    # Ouvre un fichier local
                    with open(r"Le Grinch 354x500.png", 'wb') as f:
                        shutil.copyfileobj(reponse.raw, f)

                    print("Image téléchargée avec succès: ", r"Le Grinch 354x500.png")

                    shutil.move(path + r"\Le Grinch 354x500.png", localisationImages + r"Le Grinch 354x500.png")
                    #print("Image déplacée")
                else:
                    print("L'image n'a pas pue être obtenue")
        except:
            print("Il est impossible au script d'accéder aux images en ligne")


        # Images des affiches
        try:
            image1 = PhotoImage(file=localisationImages + r"Les Hommes en noir 333x500.png")
            image2 = PhotoImage(file=localisationImages + r"Le Grinch 354x500.png")

            self.affiche1 = Canvas(self.fen, width=350, height=450)
            self.affiche2 = Canvas(self.fen, width=350, height=450)

            self.affiche1.create_image(0, -20, anchor=NW, image=image1)
            self.affiche2.create_image(0, -30, anchor=NW, image=image2)

            self.affiche1.grid(row=3, column=1)
            self.affiche2.grid(row=3, column=3)
            #print("Tout s'est bien passé lors de l'acquisition des images")
        except:
            print("Erreur dans l'acquisition des images")

        self.fen.mainloop()

    def openFile(self, fileName):
        "Permet d'ouvrir le fichier de la vidéo"
        if info.personneConnecte.grade.isdigit() or info.cartesPersonneConnecte != []:
            program = localisationBandeAnnonces + fileName
            print("{} ouvert".format(program))

            os.system('"%s"' % program)
        else:
            #print("Accès aux films refusé, ajouez une carte de crédit au compte")
            self.avertissement()

    def avertissement(self):
        "Fait apparaître des messages d'avertissement"
        # Avertissement
        self.alerteCarte.destroy()
        self.alerteCarte = Label(self.fen, text="Il faut au moins enregistrer une carte au compte pour visionner un film.", foreground="#eaa")
        self.alerteCarte.grid(row=4, column=0, sticky="e")

        self.fen.after(200, self.suiteAvertissement)
    def suiteAvertissement(self):
        "Change la couleur du message d'avertissement"
        # Avertissement
        self.alerteCarte.destroy()
        self.alerteCarte = Label(self.fen, text="Il faut au moins enregistrer une carte au compte pour visionner un film.", foreground="#e33")
        self.alerteCarte.grid(row=4, column=0, sticky="e")


    def infoFilm(self, titre):
        "Permet d'aller à la fenêtre de l'affichage des infos du film"
        for film in Personne.registre.getFilms():
            if film.nom == titre:
                info.film = film

        if info.film == "":
            print("Une erreur est survenue lors de la tentative d'affichage des informations")
        self.fen.destroy()
        infoFilm()

    def openParametre(self):
        "Permet d'aller à la fenêtre de l'affichage des paramètres"
        self.fen.destroy()
        parametreApp()


class signUpApp():
    "Responsable de la création des nouveaux comptes clients"

    def __init__(self):
        self.fen = Tk()

        self.prenomTxt = StringVar()
        self.nomTxt = StringVar()
        self.userTxt = StringVar()
        self.emailTxt = StringVar()
        self.code1Txt = StringVar()
        self.code2Txt = StringVar()

        self.fen.title("Création d'un compte")

        # Avertissement
        self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
        self.alertePrenom.grid(row=1, column=3, sticky="w")

        self.alerteNom = Label(self.fen, text="", foreground="#eaa")
        self.alerteNom.grid(row=2, column=3, sticky="w")

        self.alerteUser = Label(self.fen, text="", foreground="#eaa")
        self.alerteUser.grid(row=3, column=3, sticky="w")

        self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
        self.alerteEmail.grid(row=4, column=3, sticky="w")

        self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode1.grid(row=5, column=3, sticky="w")

        self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode2.grid(row=6, column=3, sticky="w")

        self.approuvement = Label(self.fen, text="", foreground="#aea")
        self.approuvement.grid(row=7, column=3, sticky="w")

        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                #print("Je ne sais pas quoi faire pour le logo...")
                pass
        except:
            print("Erreur dans l'affichage du logo")

        self.label = Label(self.fen, text="Entrez les informations nécessaire à la création de votre compte").grid(row=0)
        self.btnConfirmer = Button(self.fen, text="Confirmer", command=self.confirmer).grid(row=7, column=1)
        self.boutRetourCompte = Button(self.fen, text="J'ai déjà un compte", command=self.retourCompte).grid(row=8, column=3, sticky="e")

        # Boites de texte

        self.prenomLabel = Label(self.fen, text="Prénom :").grid(row=1, column=0)
        self.prenomEntry = Entry(self.fen, textvariable=self.prenomTxt).grid(row=1, column=1)

        self.nomLabel = Label(self.fen, text="Nom :").grid(row=2, column=0)
        self.nomEntry = Entry(self.fen, textvariable=self.nomTxt).grid(row=2, column=1)

        self.userLabel = Label(self.fen, text="Nom d'utilisateur :").grid(row=3, column=0)
        self.userEntry = Entry(self.fen, textvariable=self.userTxt).grid(row=3, column=1)

        self.emailLabel = Label(self.fen, text="Adresse email :").grid(row=4, column=0)
        self.emailEntry = Entry(self.fen, textvariable=self.emailTxt).grid(row=4, column=1)

        self.code1Label = Label(self.fen, text="Mot de passe :").grid(row=5, column=0)
        self.code1Entry = Entry(self.fen, textvariable=self.code1Txt, show="*").grid(row=5, column=1)

        self.code2Label = Label(self.fen, text="Confirmation mot de passe :").grid(row=6, column=0)
        self.code2Entry = Entry(self.fen, textvariable=self.code2Txt, show="*").grid(row=6, column=1)

        self.fen.mainloop()

    def avertissement(self, liste):
        "Fait apparaître des messages d'avertissement où il est nécessaire"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Le compte est invalide", foreground="#eaa")
        self.approuvement.grid(row=7, column=3, sticky="w")

        self.alertePrenom.destroy()
        self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
        self.alertePrenom.grid(row=1, column=3, sticky="w")

        self.alerteNom.destroy()
        self.alerteNom = Label(self.fen, text="", foreground="#eaa")
        self.alerteNom.grid(row=2, column=3, sticky="w")

        self.alerteUser.destroy()
        self.alerteUser = Label(self.fen, text="", foreground="#eaa")
        self.alerteUser.grid(row=3, column=3, sticky="w")

        self.alerteEmail.destroy()
        self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
        self.alerteEmail.grid(row=4, column=3, sticky="w")

        self.alerteCode1.destroy()
        self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode1.grid(row=5, column=3, sticky="w")

        self.alerteCode2.destroy()
        self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
        self.alerteCode2.grid(row=6, column=3, sticky="w")


        # Selon chaque erreur
        if liste[0] == False:
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="Aucun prénom n'a été écrit", foreground="#eaa")
            self.alertePrenom.grid(row=1, column=3, sticky="w")

        if liste[1] == False:
            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="Aucun nom n'a été écrit", foreground="#eaa")
            self.alerteNom.grid(row=2, column=3, sticky="w")

        if self.userTxt.get() == "":
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Aucun nom d'utilisateur n'a été écrit", foreground="#eaa")
            self.alerteUser.grid(row=3, column=3, sticky="w")
        elif liste[2] == False:
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Le nom d'utilisateur a déjà été utilisée", foreground="#eaa")
            self.alerteUser.grid(row=3, column=3, sticky="w")

        if liste[4] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email est invalide", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if self.emailTxt.get() == "":
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="Aucune adresse email n'a été écrit", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")
        elif liste[3] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email déjà été utilisée", foreground="#eaa")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if liste[5] == False and liste[6] == False:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#eaa")
            self.alerteCode2.grid(row=6, column=3, sticky="w")
        elif liste[6] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#eaa")
            self.alerteCode1.grid(row=5, column=3, sticky="w")

        if liste[5] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#eaa")
            self.alerteCode1.grid(row=5, column=3, sticky="w")
        elif len(self.code2Txt.get()) < 8:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#eaa")
            self.alerteCode2.grid(row=6, column=3, sticky="w")

        if liste[7] == False:
            txts = [self.prenomTxt.get(), self.nomTxt.get(), self.userTxt.get(), self.emailTxt.get(), self.code1Txt.get(), self.code2Txt.get()]
            somme = ""
            for ligne in txts:
                somme = somme + detectCaratere(ligne)
            self.approuvement.destroy()
            self.approuvement = Label(self.fen, text=compilationCaractere(somme), foreground="#eaa")
            self.approuvement.grid(row=7, column=3, sticky="w")


        self.fen.after(200, partial(self.suiteAvertissement, liste))
    def suiteAvertissement(self, liste):
        "Change la couleur des messages d'avertissement"
        # De base
        self.approuvement.destroy()
        self.approuvement = Label(self.fen, text="Le compte est invalide", foreground="#e33")
        self.approuvement.grid(row=7, column=3, sticky="w")


        # Selon chaque erreur
        if liste[0] == False:
            self.alertePrenom.destroy()
            self.alertePrenom = Label(self.fen, text="Aucun prénom n'a été écrit", foreground="#e33")
            self.alertePrenom.grid(row=1, column=3, sticky="w")

        if liste[1] == False:
            self.alerteNom.destroy()
            self.alerteNom = Label(self.fen, text="Aucun nom n'a été écrit", foreground="#e33")
            self.alerteNom.grid(row=2, column=3, sticky="w")

        if self.userTxt.get() == "":
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Aucun nom d'utilisateur n'a été écrit", foreground="#e33")
            self.alerteUser.grid(row=3, column=3, sticky="w")
        elif liste[2] == False:
            self.alerteUser.destroy()
            self.alerteUser = Label(self.fen, text="Le nom d'utilisateur a déjà été utilisée", foreground="#e33")
            self.alerteUser.grid(row=3, column=3, sticky="w")

        if liste[4] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email est invalide", foreground="#e33")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if self.emailTxt.get() == "":
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="Aucune adresse email n'a été écrit", foreground="#e33")
            self.alerteEmail.grid(row=4, column=3, sticky="w")
        elif liste[3] == False:
            self.alerteEmail.destroy()
            self.alerteEmail = Label(self.fen, text="L'adresse email déjà été utilisée", foreground="#e33")
            self.alerteEmail.grid(row=4, column=3, sticky="w")

        if liste[5] == False and liste[6] == False:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#e33")
            self.alerteCode2.grid(row=6, column=3, sticky="w")
        elif liste[6] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Les deux codes ne sont pas identiques", foreground="#e33")
            self.alerteCode1.grid(row=5, column=3, sticky="w")

        if liste[5] == False:
            self.alerteCode1.destroy()
            self.alerteCode1 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#e33")
            self.alerteCode1.grid(row=5, column=3, sticky="w")
        elif len(self.code2Txt.get()) < 8:
            self.alerteCode2.destroy()
            self.alerteCode2 = Label(self.fen, text="Le code n'a pas au moins 8 caractères", foreground="#e33")
            self.alerteCode2.grid(row=6, column=3, sticky="w")

        if liste[7] == False:
            txts = [self.prenomTxt.get(), self.nomTxt.get(), self.userTxt.get(), self.emailTxt.get(), self.code1Txt.get(), self.code2Txt.get()]
            somme = ""
            for ligne in txts:
                somme = somme + detectCaratere(ligne)
            self.approuvement.destroy()
            self.approuvement = Label(self.fen, text=compilationCaractere(somme), foreground="#e33")
            self.approuvement.grid(row=7, column=3, sticky="w")

    def retourCompte(self):
        "Permet d'aller à la fenêtre de connection"
        self.fen.destroy()
        logInApp()

    def confirmer(self):
        "Vérifie les informations données et commence la connexion si elles correspondent"
        checklist = [False, False, True, True, False, False, False, True]
        verdict = True

        # Vérification
        if self.prenomTxt.get() != "":
            checklist[0] = True
        if self.nomTxt.get() != "":
            checklist[1] = True

        for employe in Personne.registre.getEmployes():
            if employe.user == self.userTxt.get()  or employe.user == "":
                checklist[2] = False
        for client in Personne.registre.getClients():
            if client.user == self.userTxt.get():
                checklist[2] = False
        for employe in Personne.registre.getEmployes():
            if employe.email == self.emailTxt.get():
                checklist[3] = False
        for client in Personne.registre.getClients():
            if client.email == self.emailTxt.get():
                checklist[3] = False
        if "@" in self.emailTxt.get():
            checklist[4] = True
        if len(self.code1Txt.get()) >= 8:
            checklist[5] = True
        if self.code1Txt.get() == self.code2Txt.get():
            checklist[6] = True
        if detectCaratere(self.prenomTxt.get()) != "":
            checklist[7] = False
        elif detectCaratere(self.nomTxt.get()) != "":
            checklist[7] = False
        elif detectCaratere(self.userTxt.get()) != "":
            checklist[7] = False
        elif detectCaratere(self.emailTxt.get()) != "":
            checklist[7] = False
        elif detectCaratere(self.code1Txt.get()) != "":
            checklist[7] = False
        elif detectCaratere(self.code2Txt.get()) != "":
            checklist[7] = False

        for check in checklist:
            if check == False:
                verdict = False

        if verdict == True:
            #print("Nouveau Compte!")

            try:
                client = Personne.Client(self.nomTxt.get(), self.prenomTxt.get(), self.emailTxt.get(), self.userTxt.get(), self.code1Txt.get(), time.strftime("%d/%m/%Y"), "Client")

                Personne.registre.addClient(client)
                Personne.sauvegardeClients()
                Personne.sauvegardeCartes()

                # Apporte les informations
                info.personneConnecte = client
                # Aucune carte de crédit de déjà ajoutée

                self.fen.destroy()
                mainWindow()
            except:

                # ~Approuvement~
                self.approuvement.destroy()
                self.approuvement = Label(self.fen, text="Un problème est survenu lors de la création du compte", foreground="#dd3")
                self.approuvement.grid(row=7, column=3, sticky="w")

                self.alertePrenom.destroy()
                self.alertePrenom = Label(self.fen, text="", foreground="#eaa")
                self.alertePrenom.grid(row=1, column=3, sticky="w")

                self.alerteNom.destroy()
                self.alerteNom = Label(self.fen, text="", foreground="#eaa")
                self.alerteNom.grid(row=2, column=3, sticky="w")

                self.alerteUser.destroy()
                self.alerteUser = Label(self.fen, text="", foreground="#eaa")
                self.alerteUser.grid(row=3, column=3, sticky="w")

                self.alerteEmail.destroy()
                self.alerteEmail = Label(self.fen, text="", foreground="#eaa")
                self.alerteEmail.grid(row=4, column=3, sticky="w")

                self.alerteCode1.destroy()
                self.alerteCode1 = Label(self.fen, text="", foreground="#eaa")
                self.alerteCode1.grid(row=5, column=3, sticky="w")

                self.alerteCode2.destroy()
                self.alerteCode2 = Label(self.fen, text="", foreground="#eaa")
                self.alerteCode2.grid(row=6, column=3, sticky="w")

                # Reset
                self.prenomTxt.set("")
                self.nomTxt.set("")
                self.userTxt.set("")
                self.emailTxt.set("")
                self.code1Txt.set("")
                self.code2Txt.set("")

                print("Une erreur est survenue lors de la création du compte")




        else:
            #print("Je vais avertir mon boss!!! >:c")
            self.avertissement(checklist)

class logInApp():
    "Fenêtre de connection à l'accueil"

    def __init__(self):
        self.fen = Tk()

        self.userTxt = StringVar()
        self.codeTxt = StringVar()

        self.fen.title("Connexion")


        try:
            if platform.system() == "Windows":
                self.fen.iconbitmap(localisationImages + r"Rewind logo.ico")
            else:
                print("Désolé, je ne sais pas quoi faire pour ce qui est des logos :(...")
        except:
            print("Erreur dans l'affichage du logo")

        self.label = Label(self.fen, text="Entrez votre nom d'utilisatur et votre mot de passe").grid(row=0)
        self.boutNouveauCompte = Button(self.fen, text="Créer un nouveau compte", command=self.nouveauCompte).grid(row=5, column=3)
        self.btnConfirmer = Button(self.fen, text="Confirmer", command=self.confirmer).grid(row=4, column=1)

        #Avertissement
        self.alerteLabel = Label(self.fen, text="", foreground="#e33")
        self.alerteLabel.grid(row=4, column=0)

        # Boites de texte
        self.userLabel = Label(self.fen, text="Nom d'utilisateur ou email:").grid(row=1, column=0)
        self.userEntry = Entry(self.fen, textvariable=self.userTxt).grid(row=1, column=1)
        self.codeLabel = Label(self.fen, text="Mot de passe:").grid(row=2, column=0)
        self.codeEntry = Entry(self.fen, textvariable=self.codeTxt, show="*").grid(row=2, column=1)

        self.fen.mainloop()

    def nouveauCompte(self):
        "Permet d'aller à la fenêtre de création de compte"
        self.fen.destroy()
        signUpApp()

    def avertissement(self):
        "Fait apparaître des messages d'avertissement où il est nécessaire"
        self.alerteLabel.destroy()

        self.alerteLabel = Label(self.fen, text="Les informations écrites ne sont pas liés à un compte", foreground="#eaa")
        self.alerteLabel.grid(row=4, column=0)

        self.fen.after(200, self.suiteAvertissement)
    def suiteAvertissement(self):
        "Change la couleur des messages d'avertissement"
        self.alerteLabel.destroy()

        self.alerteLabel = Label(self.fen, text="Les informations écrites ne sont pas liés à un compte", foreground="#e33")
        self.alerteLabel.grid(row=4, column=0)

    def confirmer(self):
        "Vérifie les informations données et crée un compte si elles sont valables"
        tableClients = []
        tableEmployes = []
        found = False
        numeroTable = 0

        # Recherche des employés
        try:


            for employe in Personne.registre.getEmployes():
                tableEmployes.append(employe)


            identifiant = str(self.userTxt.get())
            code = str(self.codeTxt.get())

            while numeroTable != len(tableEmployes) and found == False:

                print("---------- Employé numéro {} ----------".format(numeroTable+1))
                if identifiant == str(tableEmployes[numeroTable].user) and code == str(tableEmployes[numeroTable].code)\
                        or identifiant == str(tableEmployes[numeroTable].email) and code == str(tableEmployes[numeroTable].code):
                    #print("Gotcha!")
                    #print(tableEmployes[numeroTable])
                    info.personneConnecte = tableEmployes[numeroTable]
                    info.cartesPersonneConnecte = info.personneConnecte.grade
                    self.fen.destroy()
                    print("---{} {} est connecté!---".format(info.personneConnecte.prenom, info.personneConnecte.nom))
                    mainWindow()
                    found = True
                    break

                else:
                    #print("Hold it!!!")

                    """ #Verification des données (test)
                    print(tableEmployes[numeroTable].user)
                    print(self.userTxt.get())
                    print(tableEmployes[numeroTable].code)
                    print(self.codeTxt.get())
                    """


                numeroTable = numeroTable + 1

            if found == True:
                print("Les employés ont été passés")
            else:
                print("Données d'enregistrements incomprises parmis les employé")

        except:
            print("Grosse erreur quant à l'acquisition des données des employés")


        # Recherche des clients

        numeroTable = 0

        try:


            for client in Personne.registre.getClients():
                tableClients.append(client)


            identifiant = str(self.userTxt.get())
            code = str(self.codeTxt.get())
            while numeroTable != len(tableClients) and found == False:

                print("---------- Client numéro {} ----------".format(numeroTable+1))
                if identifiant == str(tableClients[numeroTable].user) and code == str(tableClients[numeroTable].code)\
                        or identifiant == str(tableClients[numeroTable].email) and code == str(tableClients[numeroTable].code):
                    #print("Gotcha!")
                    #print(tableClients[numeroTable])

                    #Apporte les informations
                    info.personneConnecte = tableClients[numeroTable]
                    #Apporte les cartes
                    for carte in Personne.Client.getListeCartesCredit(info.personneConnecte):
                        info.cartesPersonneConnecte.append(carte)

                    self.fen.destroy()
                    print("---{} {} est connecté!---".format(info.personneConnecte.prenom, info.personneConnecte.nom))
                    mainWindow()
                    found = True
                    break

                else:
                    #print("Hold it!!!")

                    """ #Vérification des données (test)
                    print(tableClients[numeroTable].user)
                    print(self.userTxt.get())
                    print(tableClients[numeroTable].code)
                    print(self.codeTxt.get())
                    """


                numeroTable = numeroTable + 1

            if found == True:
                print("Les clients ont été passés")
            else:
                print("Données d'enregistrements incomprises parmis les clients")

                self.avertissement()
        except:
            print("Grosse erreur quant à l'acquisition des données des clients")


def getTempsCarte(date):
    "Renvoie sous forme textuelle en français une date de carte de crédit sous la forme « [mois]/[année] »"
    indice = date.split("/")

    mois = ""

    if indice[0] == "01":
        mois = "janvier"
    elif indice[0] == "02":
        mois = "février"
    elif indice[0] == "03":
        mois = "mars"
    elif indice[0] == "04":
        mois = "avril"
    elif indice[0] == "05":
        mois = "mai"
    elif indice[0] == "06":
        mois = "juin"
    elif indice[0] == "07":
        mois = "juillet"
    elif indice[0] == "08":
        mois = "août"
    elif indice[0] == "09":
        mois = "septembre"
    elif indice[0] == "10":
        mois = "octobre"
    elif indice[0] == "11":
        mois = "novembre"
    elif indice[0] == "12":
        mois = "décembre"
    else:
        mois = "§"

    return "{} 20{}".format(mois, indice[1])

def getTempsComplet(date):
    "Renvoie sous forme textuelle en français une date complette sous la forme « [jour]/[mois]/[année] »"
    indice = date.split("/")

    mois = ""

    if indice[0] == "01":
        indice[0] = "1er"
    elif int(indice[0]) % 10 == 0:
        pass
    else:
        indice[0] = indice[0].replace("0", "")

    if indice[1] == "01":
        mois = "janvier"
    elif indice[1] == "02":
        mois = "février"
    elif indice[1] == "03":
        mois = "mars"
    elif indice[1] == "04":
        mois = "avril"
    elif indice[1] == "05":
        mois = "mai"
    elif indice[1] == "06":
        mois = "juin"
    elif indice[1] == "07":
        mois = "juillet"
    elif indice[1] == "08":
        mois = "août"
    elif indice[1] == "09":
        mois = "septembre"
    elif indice[1] == "10":
        mois = "octobre"
    elif indice[1] == "11":
        mois = "novembre"
    elif indice[1] == "12":
        mois = "décembre"
    else:
        mois = "§"

    return "{} {} {}".format(indice[0], mois, indice[2])

def filterDigits(text):
    "Enlève tous les caractères dans une chaîne de caractères n'étant pas des chiffres"
    finalText = ""
    for letter in range(len(text)):

        if text[letter].isdigit():
            finalText = str(finalText) + str(text[letter])

    return finalText

def detectCaratere(text):
    "Renvoie les caractères corrompant les sauvegardes d'un texte"

    listeCaracteres = ["§", "Á", "Ï", "Í", "Ý"]
    caracteresDetectes = ""
    ligneFinalle = ""

    for caractere in listeCaracteres:

        if caractere in text:
            caracteresDetectes = caracteresDetectes + caractere

    return caracteresDetectes

def compilationCaractere(text):
    "Renvoie textuellement le message d'erreur sur les caractères"

    ligneFinalle = "Les caractètres "
    nombreCaracteres = len(text)


    for caractere in text:

        if caractere in ligneFinalle:
            nombreCaracteres = nombreCaracteres - 1
        else:
            if ligneFinalle == "Les caractètres " and nombreCaracteres == 1:
                ligneFinalle = "Le caractère « {} » n'est pas utilisable".format(caractere)
                nombreCaracteres = 0
            elif nombreCaracteres == 1:
                ligneFinalle =  "{} et « {} » ne sont pas utilisables".format(ligneFinalle, caractere)
                nombreCaracteres = 0
            elif ligneFinalle == "Les caractètres ":
                ligneFinalle = ligneFinalle + "« {} »".format(caractere)
                nombreCaracteres = nombreCaracteres - 1
            else:
                ligneFinalle = ligneFinalle + ", « {} »".format(caractere)
                nombreCaracteres = nombreCaracteres - 1

    return ligneFinalle

if __name__ == "__main__" and info.wasActive == False:
    info.wasActive = True
    logInApp()