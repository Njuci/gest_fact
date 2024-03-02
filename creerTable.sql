
drop table if exists Vente;
drop table if exists  Paiement;
drop table if exists Facture;
drop table if exists Article;
drop table if exists Customer;


create table Article(
codArt Varchar(4) PRIMARY KEY, 
desiArt Varchar(20),
prix Float(12,2)

);
create table Customer(
idcli Varchar(4) Primary Key,
nomcli Varchar(15),
adrcli Varchar(25),
numtel Varchar(14) 
);
create table Facture (
idFact Varchar(5) PRIMARY KEY,
datfact date,
reduction float(2),
idcli Varchar(4),
constraint pf_fact foreign key (idcli) References Customer(idcli) 
);
create table Vente(
codArt Varchar(4),
idfact Varchar(5),
quantite Int,
constraint pk_vente primary key(codArt,idfact),
constraint pk_v_art foreign key (codArt) References Article(codArt),
constraint pk_v_fact foreign key(idFact) References Facture(idFact)

);

create table Paiement(
datepaie date,
idfact varchar(5),
montant float(12,2),
constraint pk_p_fact foreign key(idFact) References Facture(idFact)



);
