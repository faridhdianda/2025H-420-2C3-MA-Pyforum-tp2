class Commentaire:
    def __init__(self, identifiant, auteur_id, contenu, publication_id):
        self.identifiant = identifiant
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id

    def __str__(self):
        return (f"Commentaire(id={self.identifiant}, auteur={self.auteur_id}, "
                f"publication={self.publication_id}, contenu='{self.contenu}')")

    def to_dict(self):
        return {
            "identifiant": self.identifiant,
            "auteur_id": self.auteur_id,
            "contenu": self.contenu,
            "publication_id": self.publication_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            identifiant=data["identifiant"],
            auteur_id=data["auteur_id"],
            contenu=data["contenu"],
            publication_id=data["publication_id"]
        )
