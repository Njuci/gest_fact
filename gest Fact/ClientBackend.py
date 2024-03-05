from tkinter.messagebox import showerror


class ClientBackend:
    def __init__(self):
        self.curseur = None

    def __init__(self,cursor=None):
        # id,nom,adresse,telephone
        self.idClient = 0
        self.nomClient = ""
        self.adresse = ""
        self.telephone = ""
        self.cursor = cursor

    # Récupérer les clients dans la base de données
    def allClients(self):
        try:
            self.cursor.execute("select * from customer")
            return self.cursor.fetchall()
        except Exception as e:
            showerror("Affichage", str(e))
            return False

    # Ajouter un client dans la base de données
    def addClient(self, idClient, nomClient, adresse, telephone):
        try:
            # adding this in the db idcli,nomcli,adrcli,numtel
            self.cursor.execute("insert into customer(idcli,nomcli,adrcli,numtel) values(%s,%s,%s,%s)",
                           (idClient, nomClient, adresse, telephone))
            return True
        except Exception as e:
            showerror("Ajout", str(e))
            return False

    # Modifier un client dans la base de données
    def updateClient(self, clientId, nomClient, adresse, telephone):
        try:
            self.cursor.execute("update customer set nomcli=%s,adrcli=%s,numtel=%s where idcli=%s",
                           (nomClient, adresse, telephone, clientId))
            return True
        except Exception as e:
            showerror("Modification", str(e))
            return False

    # Supprimer un client dans la base de données
    def deleteClient(self, clientId):
        try:
            self.cursor.execute("delete from customer where idcli=%s", (clientId,))
            return True
        except Exception as e:
            showerror("Suppression", str(e))
            return False