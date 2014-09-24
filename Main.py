import argparse

parser = argparse.ArgumentParser()

# parametre
parser.add_argument("temps", type = int, help = "Donner le temps total de la playlist en minute")
parser.add_argument("nomfichier", help = "Donner le nom du fichier de sortie de la playlist")
parser.add_argument("format",choices =['m3u','xspf'], help = "Donner le nom du fichier de sortie : M3U ou XSPF")

# parametre secondaire
parser.add_argument("--genre", nargs=2, help = "Donner le genre de la musique")
parser.add_argument("--artiste", nargs=2, help = "Donner le nom de l'artiste")
parser.add_argument("--album", nargs=2, help = "Donner le titre de l'ablum")
parser.add_argument("--titre", help = "Donner le titre de la musique")


args = parser.parse_args()
#print(int(args.genre[1]))



#fonction pour vérifier le pourcentage (le deuxieme argument du parametre secondaite)
def verifier_pourcentage(pourcentage):
    try:
        int (pourcentage[1])
        if int(pourcentage[1])>0 and int(pourcentage[1])<=100:
            print(str(int(pourcentage[1])))
        else:
            print("Recommencez, donnez un nombre entre 0 et 100 !")
    except ValueError:
            print("Recommencez, donnez un nombre entre 0 et 100!")

verifier_pourcentage(args.genre)
verifier_pourcentage(args.artiste)
verifier_pourcentage(args.album)


"""print(args.temps)
print(args.nomfichier)
print(args.format)
print(args.genre)
print(args.artiste)
print(args.album)
print(args.titre)"""
