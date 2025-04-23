from datetime import datetime

class Publication:
    def __init__(self, identifiant, titre, contenu, date_creation, auteur_id, forum_id, commentaires=None):
        self.identifiant = identifiant
        self.titre = titre
        self.contenu = contenu
        self.date_creation = date_creation if isinstance(date_creation, str) else date_creation.strftime("%Y-%m-%d %H:%M:%S")
        self.auteur_id = auteur_id
        self.forum_id = forum_id
        self.commentaires = commentaires if commentaires is not None else []

    def ajouter_commentaire(self, commentaire_id):
        if commentaire_id not in self.commentaires:
            self.commentaires.append(commentaire_id)

    def __str__(self):
        return (f"Publication(id={self.identifiant}, titre='{self.titre}', auteur={self.auteur_id}, "
                f"forum={self.forum_id}, date='{self.date_creation}', "
                f"nb_commentaires={len(self.commentaires)})")

    def to_dict(self):
        return {
            "identifiant": self.identifiant,
            "titre": self.titre,
            "contenu": self.contenu,
            "date_creation": self.date_creation,
            "auteur_id": self.auteur_id,
            "forum_id": self.forum_id,
            "commentaires": self.commentaires
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            identifiant=data["identifiant"],
            titre=data["titre"],
            contenu=data["contenu"],
            date_creation=data["date_creation"],
            auteur_id=data["auteur_id"],
            forum_id=data["forum_id"],
            commentaires=data.get("commentaires", [])
        )
