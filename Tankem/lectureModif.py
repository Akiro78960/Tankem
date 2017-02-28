# -*- coding:utf-8 -*-

from Tkinter import Tk
from tkFileDialog import askopenfilename
import csv
import os
import sys
import common


#methode d'ouverture de la fenetre pour choisir le fichier
def choisirFichierCSV():
    Tk().withdraw() #enleve la petite fenetre qui ne sert a rien
    filename = askopenfilename(filetypes=[("CSV files","*.csv"), ("all files", "*")], defaultextension= "*.csv")
    return filename

DAO = common.internal.BalanceDAODTO.DAOBalanceCsv.DAOBalanceCsv()
DAO.read("test.csv")


'''
print ("Voulez vous utiliser un fichier csv existant ou en creer un nouveau ?")
reponse = raw_input("pesez C pour creer ou U pour ouvrir un CSV ")
if str.upper(reponse) == str.upper('c'):
    print ("creation de fichier")
    with open("test.csv","wb") as csvfile :
        csvwriter = csv.writer(csvfile,delimiter=";")
        csvwriter.writerow(["Name","Value"])
        os.system("start excel.exe " + "test.csv")
        print("fichier test.csv créer")
    
else:
    print ("choisir un fichier CSV")
    nomFichier = choisirFichierCSV()
    os.system("start excel.exe " + nomFichier)


'''