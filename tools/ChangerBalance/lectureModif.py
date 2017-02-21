# -*- coding:utf-8 -*-

import cx_Oracle

print ("Voulez vous creer un fichier csv existant ou en generer un nouveau ?")
reponse = raw_input("")
if reponse == upper('c'):
    print ("creation de fichier")
    