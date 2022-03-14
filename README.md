# Trouve la pompe dans ta région
## Introduction
Ce dépôt contient un programme en Python3 qui permet de trouver l'ensemble des stations-services d'un département donné par ordre de prix décroissant. Ce dépot contient également l'exécutable pour Windows x64.

## Prérequis
### Python3
Aucune bibliothèque extérieure à Python n'est nécessaire pour ce programme. Cependant, le script n'est pas compatible avec Python2 dû à l'utilisation de "BytesIO".

### Création de l'exécutable
J'utilise Cython pour compiler en C puis cl disponible avec Visual C++ v14. Plus d'information pour installer ces outils sur https://wiki.python.org/moin/WindowsCompilers.

Pour installer Cython, utiliser la commande suivvante : ```python3 -m pip install cython```

Le script "setup.bat" permet de créer le fichier c + compiler le programme. Cependant, il peut évoluer selon les paramètres d'installation de Python et des versions des logiciels.

Il faut notamment ajouter la variable d'environnement LIB avec les entrées suivantes :
```
C:\Program Files\Python39\libs
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.31.31103\lib\x64
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\um\x64
C:\Program Files (x86)\Windows Kits\10\Lib\10.0.19041.0\ucrt\x64
```

## Logiciel
Ce script télécharge la liste des stations services depuis le site du gouvernement, tri par département puis affiche les résultats par prix croissants. Toutes les pompes vendant plus de 500m² de carburants doivent être répertorier sur ce site et ont l'obligation de mettre les valeurs à jour.

Pour utiliser le logiciel, il faut utiliser la syntaxe suivante :
```prix.exe <carburant> <departement> [<nombre de stations à afficher>]```