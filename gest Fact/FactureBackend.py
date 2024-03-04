import mysql.connector

class FactBackend:
    def __init__(self,idFact,DateFac,Reduction,IdCli,curseur):
        self.IdFac=idFact
        self.Reduction=Reduction
        self.DateFac=DateFac
        self.IdCli=IdCli
        self.curseur=curseur
    def save(self):
        sql = 'INSERT INTO Articles (CodeArticle, desiArticle, prix) VALUES (%s,%s,%s)'
        val = ('0002','Biscuit',300)
        self.curseur.execute(sql,val)

    def getData(self):
        try:
            sql = 'SELECT Facture.idFact,Facture.datfact,Facture.reduction,Facture.idcli, Customer.nomcli FROM Facture INNER JOIN Customer ON Facture.idcli=Customer.idcli'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('BAC4 INFO', str(exp))
        