import os
import platform
path = os.getcwd() #Répertoire courant

class Personne:
    "Liste de toutes les personnes rattachées au logiciel. (Clients, employés, acteurs des films)"
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

        self.__listeClients = []
        self.__listeEmployes = []
        self.__listeActeurs = []
        self.__listeFilms = []

    @property
    def nom(self):
        return self.__nom
    @property
    def prenom(self):
        return self.__prenom

    @nom.setter
    def nom(self, newNom):
        self.__nom = newNom
    @prenom.setter
    def prenom(self, newPrenom):
        self.__prenom = newPrenom

    #Get d'une classe
    def getClients(self):
        return self.__listeClients
    def getEmployes(self):
        return self.__listeEmployes
    def getActeurs(self):
        return self.__listeActeurs
    def getFilms(self):
        return self.__listeFilms

    #Ajout dans une classe
    def addClient(self, client):
        self.__listeClients.append(client)
    def addEmploye(self, employe):
        self.__listeEmployes.append(employe)
    def addActeur(self, acteur):
        self.__listeActeurs.append(acteur)
    def addFilm(self, film):
        self.__listeFilms.append(film)

    #Effacage dans une classe (À n'utiliser qu'avec précaution)
    def delClient(self, client):
        self.__listeClients.remove(client)
    def delEmploye(self, employe):
        self.__listeEmployes.remove(employe)
    def delActeur(self, acteur):
        self.__listeActeurs.remove(acteur)
    def delFilm(self, film):
        self.__listeFilms.remove(film)


    def __str__(self):
        return "{},{}".format(self.nom, self.prenom)

registre = Personne("O'Nyme", "Anne") #Ne jamais enlever!


class Client(Personne):
    "Clients avec leur nom, prénom, ainsi que d'autres informations pertinentes à leur sujet."
    def __init__(self, nom, prenom, email, user, code, date, grade):
        Personne.__init__(self, nom, prenom)
        self.__email = email
        self.__user = user
        self.__code = code
        self.__date = date
        self.__grade = grade
        self.__listeCartesCredit = []


    @property
    def email(self):
        return self.__email
    @property
    def user(self):
        return self.__user
    @property
    def code(self):
        return self.__code
    @property
    def date(self):
        return self.__date
    @property
    def grade(self):
        return self.__grade

    @email.setter
    def email(self,newEmail):
        self.__email = newEmail
    @user.setter
    def user(self, newUser):
        self.__user = newUser
    @code.setter
    def code(self, newCode):
        self.__code = newCode
    @date.setter
    def date(self, newDate):
        self.__date = newDate
    @grade.setter
    def grade(self, newGrade):
        self.__grade = newGrade

    def getListeCartesCredit(self):
        return self.__listeCartesCredit
    def getNombreCartesCredit(self):
        return len(self.__listeCartesCredit)

    def addCarte(self, carteCredit):
        self.__listeCartesCredit.append(carteCredit)
    def delCarte(self, CarteCredit):
        self.__listeCartesCredit.remove(CarteCredit)


    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.nom, self.prenom, self.email, self.user, self.code, self.date, self.grade)

class Employe(Personne):
    "Employés avec leur nom, prénom, ainsi que d'autres informations pertinentes à leur sujet."
    def __init__(self, nom, prenom, email, user, code, date, grade):
        Personne.__init__(self, nom, prenom)
        self.__email = email
        self.__user = user
        self.__code = code
        self.__date = date
        self.__grade = grade


    @property
    def email(self):
        return self.__email
    @property
    def user(self):
        return self.__user
    @property
    def code(self):
        return self.__code
    @property
    def date(self):
        return self.__date
    @property
    def grade(self):
        return self.__grade

    @email.setter
    def email(self, newEmail):
        self.__email = newEmail
    @user.setter
    def user(self, newUser):
        self.__user = newUser
    @code.setter
    def code(self, newCode):
        self.__code = newCode
    @date.setter
    def date(self, newDate):
        self.__date = newDate
    @grade.setter
    def grade(self, newGrade):
        self.__grade = newGrade


    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.nom, self.prenom, self.email, self.user, self.code, self.date, self.grade)

class Acteur(Personne):
    "Acteurs avec leur nom, prénom et numéro identificateur (le numéro identificateur est inutile)."
    def __init__(self, nom, prenom, numero):
        Personne.__init__(self, nom, prenom)
        self.__numero = numero
        self.__listeFilmsJoues = []


    @property
    def numero(self):
        return self.__numero

    def getListeFilmsJoues(self):
        return self.__listeFilmsJoues
    def getNombreFilm(self):
        return len(self.__listeFilmsJoues)

    def addFilm(self, film):
        self.__listeFilmsJoues.append(film)
    def delFilm(self, film):
        self.__listeFilmsJoues.remove(film)


    def __str__(self):
        return "{},{},{}".format(self.nom, self.prenom, self.numero)


class CarteDeCredit():
    "Liste de toutes les cartes de crédit pour chaque client."
    def __init__(self, numeroCarte, numeroSecurite, dateExpiration, type):
        self.__numeroCarte = numeroCarte
        self.__numeroSecurite = numeroSecurite
        self.__dateExpiration = dateExpiration
        self.__type = type

    def getNumeroCarte(self):
        return self.__numeroCarte
    def getNumeroSecurite(self):
        return self.__numeroSecurite
    def getDateExpiration(self):
        return self.__dateExpiration
    def getType(self):
        return self.__type


    def __str__(self):
        return "{},{},{},{}".format(self.getNumeroCarte(), self.getNumeroSecurite(), self.getDateExpiration(), self.getType())

class FilmsJoues():
    "Liste de toutes les informations pertinentes sur les acteurs par rapport à leurs films joués."
    def __init__(self, nomFilm, nomPersonnage, debutEmploit, finEmploit, cachet):
        self.__nomFilm = nomFilm
        self.__nomPersonnage = nomPersonnage
        self.__debutEmploit = debutEmploit
        self.__finEmploit = finEmploit
        self.__cachet = cachet

    def getNomFilm(self):
        return self.__nomFilm
    def getNomPersonnage(self):
        return self.__nomPersonnage
    def getDebutEmploit(self):
        return self.__debutEmploit
    def getFinEmploit(self):
        return self.__finEmploit
    def getCachet(self):
        return self.__cachet


    def __str__(self):
        return r"{}§{}§{}§{}§{}".format(self.getNomFilm(), self.getNomPersonnage(), self.getDebutEmploit(), self.getFinEmploit(), self.getCachet())


class Film:
    "Liste de tous les films sur la plateforme"
    def __init__(self, nom, duree, description):
        self.__nom = nom
        self.__duree = duree
        self.__description = description

        self.__listeGenres = []

    @property
    def nom(self):
        return self.__nom
    @property
    def duree(self):
        return self.__duree
    @property
    def description(self):
        return self.__description

    @nom.setter
    def nom(self, newNom):
        self.__nom = newNom
    @duree.setter
    def duree(self, newDuree):
        self.__duree = newDuree
    @description.setter
    def description(self, newDescription):
        self.__description = newDescription

    def getListeGenres(self):
        return self.__listeGenres

    def getGenres(self):
        return self.__listeGenres

    def addGenre(self, genre):
        self.__listeGenres.append(genre)

    def delGenre(self, genre):
        self.__listeGenres.remove(genre)


    def __str__(self):
        return r"{}§{}§{}".format(self.nom, self.duree, self.description)

class Genre():
    "Genre donné à un film"

    def __init__(self, nom, description):
        self.__nom = nom
        self.__description = description

    @property
    def nom(self):
        return self.__nom
    @property
    def description(self):
        return self.__description

    @nom.setter
    def nom(self, newNom):
        self.__nom = newNom
    @description.setter
    def description(self, newDescription):
        self.__description = newDescription

    def __str__(self):
        return r"{}§{}".format(self.nom, self.description)


def getLocalisationSauvegarde():
    "Défini le chemin de sauvegarde des informations sur les comptes et les films"
    try:
        if platform.system() == "Windows":
            localisation = r"/Sauvegardes/"
            signe = r"p\p"
            bonSigne = signe.replace("p", "")
            vraiLocalisation = localisation.replace("/", bonSigne)
            localisationFichier = path + vraiLocalisation
            print("Succès, le système d'exploitation détecté est " + platform.system())
            return localisationFichier
        else:
            localisationFichier = path + r"/Sauvegardes/"
            print("Succès, le système d'exploitation détecté est " + platform.system())
            return localisationFichier
    except:
        print("Erreur quant à la détection du système d'exploitation")
        return path + r"/Sauvegardes/"

localisationSauvegarde = getLocalisationSauvegarde()


#Sauvegardes
def sauvegardeClients():

    try:
        fichier = open(localisationSauvegarde + r"Répertoire des clients.txt", 'w')
        numeroClient = 1

        for client in registre.getClients():

            #print(client)

            if len(registre.getClients()) == numeroClient:
                fichier.write(str(client))
            else:
                fichier.write(str(client) + "\n")
            numeroClient = numeroClient + 1

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des informations des clients")
    except:
        print("Une erreur est survenue lors de la sauvegarde des informations des clients")
def sauvegardeEmployes():

    try:
        fichier = open(localisationSauvegarde + r"Répertoire des employés.txt", 'w')
        numeroEmploye = 1

        for employe in registre.getEmployes():

            #print(employe)

            if len(registre.getEmployes()) == numeroEmploye:
                fichier.write(str(employe))
            else:
                fichier.write(str(employe) + "\n")
            numeroEmploye = numeroEmploye + 1

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des informations des employés")
    except:
        print("Une erreur est survenue lors de la sauvegarde des informations des employés")
def sauvegardeActeurs():

    try:
        fichier = open(localisationSauvegarde + r"Répertoire des acteurs.txt", 'w')
        numeroActeur = 1

        for acteur in registre.getActeurs():

            #print(acteur)

            if len(registre.getActeurs()) == numeroActeur:
                fichier.write(str(acteur))
            else:
                fichier.write(str(acteur) + "\n")
            numeroActeur = numeroActeur + 1

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des informations des acteurs")
    except:
        print("Une erreur est survenue lors de la sauvegarde des informations des acteurs")
def sauvegardeCartes():

    try:
        fichier = open(localisationSauvegarde + r"Répertoire des cartes.txt", 'w')

        for client in registre.getClients():
            #print(client)
            numeroCarte = 1

            for carte in client.getListeCartesCredit():

                #print(carte.getNumeroCarte())
                if len(client.getListeCartesCredit()) == numeroCarte:
                    fichier.write(str(carte))
                else:
                    fichier.write(str(carte) + ";")
                numeroCarte = numeroCarte + 1

            fichier.write("\n")

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des informations des cartes")
    except:
        print("Une erreur est survenue lors de la sauvegarde des informations des cartes")
def sauvegardeFilmsJoues():

    try:

        fichier = open(localisationSauvegarde + r"Répertoire des films joués.txt", 'w')

        for acteur in registre.getActeurs():

            #print(acteur)
            numeroFilm = 1

            for film in acteur.getListeFilmsJoues():
                #print(film.getNomFilm())
                if len(acteur.getListeFilmsJoues()) == numeroFilm:
                    fichier.write(str(film))
                else:
                    #print(str(film))
                    #print(fichier)
                    fichier.write(str(film) + ";")
                numeroFilm = numeroFilm + 1

            fichier.write("\n")

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des films joués")
    except:
        print("Une erreur est survenue lors de la sauvegarde des films joués")

def sauvegardeFilms():

    try:
        fichier = open(localisationSauvegarde + r"Répertoire des films.txt", 'w')
        numeroFilm = 1

        for film in registre.getFilms():

            #print(film)

            if len(registre.getFilms()) == numeroFilm:
                fichier.write(str(film))
            else:
                fichier.write(str(film) + "\n")
            numeroFilm = numeroFilm + 1

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des informations des films")
    except:
        print("Une erreur est survenue lors de la sauvegarde des informations des films")
def sauvegardeGenres():

    try:
        fichier = open(localisationSauvegarde + r"Répertoire des genres.txt", 'w')

        for film in registre.getFilms():

            #print(film)
            numeroGenre = 1

            for genre in film.getListeGenres():

                #print(genre.nom)
                if len(film.getListeGenres()) == numeroGenre:
                    fichier.write(str(genre))
                else:
                    fichier.write(str(genre) + ";")
                numeroGenre = numeroGenre + 1

            fichier.write("\n")

        fichier.close()

        print("Tout s'est bien passé lors de la sauvegarde des informations des genres")
    except:
        print("Une erreur est survenue lors de la sauvegarde des informations des genres")


#Récupération des données sauvegardées
def recuperationClients():

    listeClients = []

    try:

        fichier = open(localisationSauvegarde + "Répertoire des clients.txt", 'r')
        ligneClient = fichier.readlines()

        for client in ligneClient:
            try:
                infos = client.replace("\n", "")
                splitInfos = infos.split(",")
                cl = Client(splitInfos[0], splitInfos[1], splitInfos[2], splitInfos[3], splitInfos[4], splitInfos[5], splitInfos[6])
                listeClients.append(cl)
            except:
                print("La sauvegarde des clients est corrompue")

        fichier.close()

        #print("Tout s'est bien passé lors de la récupération des informations sur les clients")
    except:
        print("Une erreur est survenue lors de la récupération des informations sur les clients")
    finally:
        return listeClients
def recuperationEmployes():

    listeEmployes = []

    try:

        fichier = open(localisationSauvegarde + "Répertoire des employés.txt", 'r')
        ligneEmploye = fichier.readlines()

        for employe in ligneEmploye:
            try:
                infos = employe.replace("\n", "")
                splitInfos = infos.split(",")
                emp = Employe(splitInfos[0], splitInfos[1], splitInfos[2], splitInfos[3], splitInfos[4], splitInfos[5], splitInfos[6])
                listeEmployes.append(emp)
            except:
                print("La sauvegarede des employés est corrompue")

            fichier.close()

        #print("Tout s'est bien passé lors de la récupération des informations sur les employés")
    except:
        print("Une erreur est survenue lors de la récupération des informations sur les employés")
    finally:
        return listeEmployes
def recuperationActeurs():

    listeActeurs = []

    try:

        fichier = open(localisationSauvegarde + "Répertoire des acteurs.txt", 'r')
        ligneActeur = fichier.readlines()

        for acteur in ligneActeur:
            try:
                infos = acteur.replace("\n", "")
                splitInfos = infos.split(",")
                act = Acteur(splitInfos[0], splitInfos[1], int(splitInfos[2]))
                listeActeurs.append(act)
            except:
                print("La sauvegarde des acteurs est corrompue")

            fichier.close()

        #print("Tout s'est bien passé lors de la récupération des informations sur les acteurs")
    except:
        print("Une erreur est survenue lors de la récupération des informations sur les acteurs")
    finally:
        return listeActeurs
def recuperationCartes():

    listeClientsCarte = []

    try:

        fichier = open(localisationSauvegarde + "Répertoire des cartes.txt", 'r')
        ligneCarte = fichier.readlines()

        for client in ligneCarte:

            listeCartes = []

            try:
                if client != "\n":
                    cartes = client.split(";")

                    for item in cartes:
                        infos = item.replace("\n", "")
                        splitInfos = infos.split(",")
                        c = CarteDeCredit(splitInfos[0], splitInfos[1], splitInfos[2], splitInfos[3])
                        listeCartes.append(c)

                    listeClientsCarte.append(listeCartes)
                else:
                    listeClientsCarte.append(listeCartes)
            except:
                print("La sauvegarde des cartes est corrompue")

            fichier.close()

        #print("Tout s'est bien passé lors de la récupération des informations des cartes")
    except:
        print("Une erreur est survenue lors de la récupération des informations sur les cartes")
    finally:
        return listeClientsCarte
def recuperationFilmsJoues():

    listeActeurFilm = []

    try:

        fichier = open(localisationSauvegarde + r"Répertoire des films joués.txt", 'r')
        ligneActeur = fichier.readlines()

        for acteur in ligneActeur:

            listeFilms = []
            try:
                if acteur != "\n":

                    films = acteur.split(";")

                    for item in films:
                        infos = item.replace("\n", "")
                        splitInfos = infos.split("§")
                        f = FilmsJoues(splitInfos[0], splitInfos[1], splitInfos[2], splitInfos[3], splitInfos[4])
                        listeFilms.append(f)

                    listeActeurFilm.append(listeFilms)
                else:
                    listeActeurFilm.append([])
            except:
                print("La sauvegarde des acteurs est corrompue")

            fichier.close()

        #print("Tout s'est bien passé lors de la récupération des films joués")
    except:
        print("Une erreur est survenue lors de la récupération des films joués")
    finally:
        return listeActeurFilm

def recuperationFilms():

    listeFilms = []

    try:

        fichier = open(localisationSauvegarde + "Répertoire des Films.txt", 'r')
        ligneFilm = fichier.readlines()

        for film in ligneFilm:
            try:
                infos = film.replace("\n", "")
                splitInfos = infos.split("§")
                flm = Film(splitInfos[0], splitInfos[1], splitInfos[2])
                listeFilms.append(flm)
            except:
                print("La sauvegarde des films est corrompue")

        fichier.close()

        #print("Tout s'est bien passé lors de la récupération des informations sur les films")
    except:
        print("Une erreur est survenue lors de la récupération des informations sur les films")
    finally:
        return listeFilms
def recuperationGenres():

    listeFilmsGenre = []

    try:

        fichier = open(localisationSauvegarde + "Répertoire des genres.txt", 'r')
        ligneGenre = fichier.readlines()

        for film in ligneGenre:

            listeGenres = []

            try:
                if film != "\n":
                    genres = film.split(";")

                    for item in genres:
                        infos = item.replace("\n", "")
                        splitInfos = infos.split("§")
                        gnr = Genre(splitInfos[0], splitInfos[1])
                        listeGenres.append(gnr)

                    listeFilmsGenre.append(listeGenres)
                else:
                    listeFilmsGenre.append(listeGenres)
            except:
                print("La sauvegarde des genres est corrompue")

            fichier.close()

        #print("Tout s'est bien passé lors de la récupération des informations des genres")
    except:
        print("Une erreur est survenue lors de la récupération des informations sur les genres")
    finally:
        return listeFilmsGenre

def recuperationAll():

    numeroClient = 0
    numeroActeur = 0
    numeroFilm = 0

    for client in recuperationClients():
        #print(client)
        registre.addClient(client)

        for carte in recuperationCartes()[numeroClient]:
            #print(carte)
            client.addCarte(carte)
        numeroClient = numeroClient + 1

    for employe in recuperationEmployes():
        #print(employe)
        registre.addEmploye(employe)

    for acteur in recuperationActeurs():
        #print(acteur)
        registre.addActeur(acteur)

        for filmJoue in recuperationFilmsJoues()[numeroActeur]:
            #print(filmJoue.nom)
            acteur.addFilm(filmJoue)
        numeroActeur = numeroActeur + 1

    for film in recuperationFilms():
        #print(film)
        registre.addFilm(film)

        for genre in recuperationGenres()[numeroFilm]:
            #print(genre)
            film.addGenre(genre)
        numeroFilm = numeroFilm + 1