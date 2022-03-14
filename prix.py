# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as et
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

def prixCarburant(array, carburant):
    if carburant == "Go":
        c = array.get("Gazole")
    if carburant == "E10":
        carburant = "E10" if array.get("E10") is not None else "SP95" if array.get("SP95") is not None else "SP98"
        c = array.get("E10", array.get("SP95", array.get("SP98")))
    if carburant == "SP":
        carburant = "SP95" if array.get("SP95") is not None else "SP98"
        c = array.get("SP95", array.get("SP98"))
    return (carburant, c['prix'], c['modif']) if c != None else None
    
def secondElement(array):
    return array['prix']
            

if __name__ == "__main__":
    #Defines arguments
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("La syntaxte du programme est : 'python3 prix.py <carburant> <departement> [<nombre de stations à afficher>]'") 
        exit(1)
    if sys.argv[1] not in ['E10', 'SP', 'Go']:
        print("L'essence doit être du type : 'E10', 'SP' ou 'Go'") 
        exit(2)
    if not sys.argv[2].isnumeric() or int(sys.argv[2]) > 99 or sys.argv[2] == "0":
        print("Le departement doit être entre 1 et 99") 
        exit(3)
    if len(sys.argv) < 4 or not sys.argv[3].isnumeric():
        nbToDisplay = None
    else:
        nbToDisplay = int(sys.argv[3])
    
    #Define code postal in 2 digits
    cp = int(sys.argv[2])*1000
    
    #Parametres
    #nbToDisplay contient le nombre de stations à afficher
    carburant = sys.argv[1]
    resp = urlopen("https://donnees.roulez-eco.fr/opendata/instantane")
    
    #Creation du fichier prix carburant depuis le site du gouvernement
    zipfile = ZipFile(BytesIO(resp.read()))
    tree = et.parse(zipfile.open(zipfile.namelist()[0]))
    root = tree.getroot()
    
    extract=[]

    # Create extract array
    for x in root.findall('pdv'):
        if int(x.attrib['cp']) >= cp and int(x.attrib['cp']) < cp+1000:
            output = {"ville": x.find('ville').text.upper(), "adresse": x.find('adresse').text.upper()}
            for y in x.findall('prix'):
                output[y.attrib['nom']] = {"prix":y.attrib['valeur'], "modif":y.attrib['maj']}
            extract.append(output)
            
    # Create output
    finalList = []
    for x in extract:
        prix = prixCarburant(x, carburant)
        if prix != None:
            finalList.append({"ville":x['ville'], "adresse":x['adresse'], "carburant":prix[0], "prix":prix[1], "modif":prix[2]})
            
    # Display elements
    finalList.sort(key=secondElement)
    for x in finalList[:nbToDisplay]:
        print(x['ville'] + " - " + x['adresse'] + "\n-------> Dernière update : " + x['modif'] + "\n-------> " + x['carburant'] + ": " + x['prix'] + "€\n")

    input("Appuyer sur entrer pour terminer le programme")