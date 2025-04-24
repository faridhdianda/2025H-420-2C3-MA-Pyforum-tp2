import csv

class Forum:
    def __init__(self, forum_identification, nom, description=None):
         
        self.identifiant = forum_identification
        self.nom = nom
        self.description = description
        self.publications = []

    def texte_forum(self):
         
        return f"Forum(id={self.forum_id}, name='{self.name}', description='{self.description}', publications={len(self.publications)})"
    @staticmethod
    def lire_fichier_csv(chemin_fichier):
        forums = []
        with open("src/pyforum/data/forum.csv", mode='r', encoding='utf-8') as fichier:
            lecteur_csv = csv.DictReader(fichier)
            for ligne in lecteur_csv:
                forum = Forum(
                    forum_identification=ligne['identifiant'],
                    nom=ligne['nom'],
                    description=ligne.get('description', None)
                )
                forums.append(forum)
        return forums