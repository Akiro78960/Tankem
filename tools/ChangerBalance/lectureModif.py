# -*- coding:utf-8 -*-

import cx_Oracle
from Tkinter import Tk
from tkFileDialog import askopenfilename


#methode d'ouverture de la fenetre pour choisir le fichier
def choisirFichierCSV():
    Tk().withdraw() #enleve la petite fenetre qui ne sert a rien
    filename = askopenfilename(filetypes=[("CSV files","*.csv"), ("all files", "*")], defaultextension= "*.csv")
    return filename



print ("Voulez vous utiliser un fichier csv existant ou en creer un nouveau ?")
reponse = raw_input("pesez C pour creer ou U pour ouvrir un CSV ")
if str.upper(reponse) == str.upper('c'):
    print ("creation de fichier")
    
else:
    print ("choisir un fichier CSV")
    nomFichier = choisirFichierCSV()



