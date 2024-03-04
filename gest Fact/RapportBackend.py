from tkinter.messagebox import showerror
import datetime

class RapportBackend:
    def __init__(self):
        pass

    # afficher les paiements, ventes , factures et article

    def afficherPaiementVenteArticle(self,cursor):
        # making a request that will return all the payments, sales, invoices, articles and customers
        # only selecting data that are not duplicated
        try:
            # we will order the data by date of payment and id of the invoice to make it more readable
            cursor.execute("select * from paiement p, facture f, vente v, article a, customer c where p.idFact = f.idFact and f.idFact = v.idFact and v.codArt = a.codArt and f.idcli = c.idcli order by p.datepaie, p.idfact")
            unorderData = cursor.fetchall()
            
            data = []
            for i in unorderData:
                # place items in order of table ,  getting all 17 items
                data.append({
                    "datepaie": datetime.datetime(i[0].year,i[0].month,i[0].day).strftime("%d/%m/%Y"), # format date
                    "idfact":i[1],
                    "montant":i[2],
                    # "idFact":i[3],
                    "datfact":i[4],
                    "reduction":i[5],
                    "idcli":i[6],
                    "codArt":i[7],
                    # "idfact":i[8], # "idfact" is the same as "idfact" in "paiement" table
                    "quantite":i[9],
                    # "codeArt":i[10],
                    "desiArt":i[11],
                    "prix":i[12],
                    "idcli": i[13],
                    "nomcli":i[14],
                    "adrcli":i[15],
                    "numtel":i[16],
                    
                    "Montant restant": f"{i[2] - i[5]}"
                })
            # remove duplicated keys, and ids for customers and articles, and facture
            newdata  =[]
            for i in data:
                if i not in newdata:
                    newdata.append(i)
            return newdata
            
        except Exception as e:
            showerror("Affichage",str(e))
            return False


    #     create table Article(
    # codArt Varchar(4) PRIMARY KEY, 
    # desiArt Varchar(20),
    # prix Float(12,2)

    # );
    # create table Customer(
    # idcli Varchar(4) Primary Key,
    # nomcli Varchar(15),
    # adrcli Varchar(25),
    # numtel Varchar(14) 
    # );
    # create table Facture (
    # idFact Varchar(5) PRIMARY KEY,
    # datfact date,
    # reduction float(2),
    # idcli Varchar(4),
    # constraint pf_fact foreign key (idcli) References Customer(idcli) 
    # );
    # create table Vente(
    # codArt Varchar(4),
    # idfact Varchar(5),
    # quantite Int,
    # constraint pk_vente primary key(codArt,idfact),
    # constraint pk_v_art foreign key (codArt) References Article(codArt),
    # constraint pk_v_fact foreign key(idFact) References Facture(idFact)

    # );

    # create table Paiement(
    # datepaie date,
    # idfact varchar(5),
    # montant float(12,2),
    # constraint pk_p_fact foreign key(idFact) References Facture(idFact)



    # );




# class PaiementBackend:
#     # create table Paiement(
#     # datepaie date,
#     # idfact varchar(5),
#     # montant float(12,2),
#     # constraint pk_p_fact foreign key(idFact) References Facture(idFact)
#     def __init__(self):
#         self.curseur=None
#     def __init__(self,date:str,idfact:str,montant:float):
#         self.date = date
#         self.idfact = idfact
#         self.montant = montant
#         self.curseur = None
#     """sauvegarde du paiement dans la base de données"""
#     def savePaiement(self,cursor):
#         try:
#             cursor.execute("insert into paiement values(%s,%s,%s)",(self.date,self.idfact,self.montant))
#             return True
#         except Exception as e:
#             showerror("Enregistrement",str(e))
#             return False
#     """recherche d'un paiement dans la base de données"""
#     def searchPaiement(self,cursor):
#         try:
#             cursor.execute("select * from paiement where idfact=%s",(self.idfact,))
#             return cursor.fetchall()
#         except Exception as e:
#             showerror("Recherche",str(e))
#             return False
#     """modification d'un paiement dans la base de données"""
#     def updatePaiement(self,cursor,element):
#         try:
#             # update paiement where idFact and date = %s only
#             cursor.execute("update paiement set montant=%s where idFact=%s and datepaie=%s",(self.montant,self.idfact,self.date))
#             return True
#         except Exception as e:
#             showerror("Modification",str(e))
#             return False
#     """suppression d'un paiement dans la base de données"""
#     def deletePaiement(self,cursor):
#         try:
#             # delete from paiement where idFact and date = %s and montant = %s
#             cursor.execute("delete from paiement where idFact=%s and datepaie=%s",(self.idfact,self.date))
#             return True
#         except Exception as e:
#             showerror("Suppression",str(e))
#             return False
#     """affichage de tous les paiements dans la base de données"""
#     def allPaiement(self,cursor):
#         try:
#             cursor.execute("select * from paiement")
#             return cursor.fetchall()
#         except Exception as e:
#             showerror("Affichage",str(e))
#             return False
#     def getPaimentWithFactureAndProduct(self,cursor):
#         try:
#             cursor.execute("select * from paiement p, facture f, vente v where p.idFact = f.idFact and f.idFact = v.idFact")
#             return cursor.fetchall()
#         except Exception as e:
#             showerror("Affichage",str(e))
#             return False