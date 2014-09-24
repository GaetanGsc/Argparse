import argparse



parser = argparse.ArgumentParser()

parser.add_argument("temps", type = int, help = "Donner le temps total de la playlist en minute")
parser.add_argument("nom", help = "Donner le nom du fichier de sortie de la playlist")
parser.add_argument("format",choices =['m3u','xspf'], help = "Donner le nom du fichier de sortie : M3U ou XSPF")

parser.add_argument("--genre", help = "Donner le genre de la musique")
parser.add_argument("--genrequantite", help = "Donner la quantite du genre en %")
parser.add_argument("--artiste", help = "Donner le nom de l'artiste")
parser.add_argument("-- artistequantite", help = "Donner la quantite d'artiste en %")
parser.add_argument("--album", help = "Donner le titre de l'ablum")
parser.add_argument("--titre", help = "Donner le titre de la musique")


args = parser.parse_args()

print(args.temps)
print(args.nom)
print(args.format)

print(args.genre)
print(args.genrequantite)
print(args.artiste)
print(args.artistequantite)
print(args.album)
print(args.titre)