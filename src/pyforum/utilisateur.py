 
import csv
import ast

class Utilisateur:
    def __init__(self, identifiant, nom_utilisateur, courriel, mot_de_passe, forums_inscrits=None):
        self.identifiant = identifiant
        self.nom_utilisateur = nom_utilisateur
        self.courriel = courriel
        self.mot_de_passe = mot_de_passe
        self.forums_inscrits = forums_inscrits if forums_inscrits is not None else []

    def joindre_forum(self, forum_id):
        if forum_id not in self.forums_inscrits:
            self.forums_inscrits.append(forum_id)

    def __str__(self):
        return (f"Utilisateur(id={self.identifiant}, nom_utilisateur='{self.nom_utilisateur}', "
                f"courriel='{self.courriel}', forums_inscrits={self.forums_inscrits})")

    def to_user(self):
        return {
            "identifiant": self.identifiant,
            "nom_utilisateur": self.nom_utilisateur,
            "courriel": self.courriel,
            "mot_de_passe": self.mot_de_passe,
            "forums_inscrits": self.forums_inscrits
        }

    @classmethod
    def from_user(cls, data):
        return cls(
            identifiant=data["identifiant"],
            nom_utilisateur=data["nom_utilisateur"],
            courriel=data["courriel"],
            mot_de_passe=data["mot_de_passe"],
            forums_inscrits=data.get("forums_inscrits", [])
        )

    @staticmethod
    def charger_depuis_csv(utilisateur):
        utilisateurs = []
        with open("src/pyforum/data/user.csv",mode="r" , newline='', encoding='utf-8') as csvfile:
            lecteur = csv.DictReader(csvfile)
            for ligne in lecteur:
                utilisateur = Utilisateur(
                    identifiant=int(ligne["identifiant"]),
                    nom_utilisateur=ligne["nom_utilisateur"],
                    courriel=ligne["courriel"],
                    mot_de_passe=ligne["mot_de_passe"],
                    forums_inscrits=ast.literal_eval(ligne["forums_inscrits"])  # convertit "[100, 101]" → [100, 101]
                )
                utilisateurs.append(utilisateur)
        return utilisateurs
