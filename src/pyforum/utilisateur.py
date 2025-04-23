
class Utilisateur:
    def __init__(self, identifiant, nom_utilisateur, courriel, mot_de_passe, forums_inscrits=None):
        self.identifiant = identifiant
        self.nom_utilisateur = nom_utilisateur
        self.courriel = courriel
        self.mot_de_passe = mot_de_passe
        self.forums_inscrits = forums_inscrits if forums_inscrits is not None else []

    def inscrire_forum(self, forum_id):
        """Alias pour joindre_forum"""
        self.joindre_forum(forum_id)

    def joindre_forum(self, forum_id):
        if forum_id not in self.forums_inscrits:
            self.forums_inscrits.append(forum_id)

    def __str__(self):
        return (f"Utilisateur(id={self.identifiant}, nom_utilisateur='{self.nom_utilisateur}', "
                f"courriel='{self.courriel}', forums_inscrits={self.forums_inscrits})")

    def to_dict(self):
        return {
            "identifiant": self.identifiant,
            "nom_utilisateur": self.nom_utilisateur,
            "courriel": self.courriel,
            "mot_de_passe": self.mot_de_passe,
            "forums_inscrits": self.forums_inscrits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            identifiant=data["identifiant"],
            nom_utilisateur=data["nom_utilisateur"],
            courriel=data["courriel"],
            mot_de_passe=data["mot_de_passe"],
            forums_inscrits=data.get("forums_inscrits", [])
        )
