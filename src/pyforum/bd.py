from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum
from pyforum.publication import Publication
from pyforum.commentaire import Commentaire

class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums: list[Forum] = []
        self.publications: list[Publication] = []
        self.commentaires: list[Commentaire] = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")

    def creer_utilisateur(self, username: str, courriel: str, mot_de_passe: str) -> Utilisateur:
        # Vérifier si l'utilisateur existe déjà
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            return None

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id, username, courriel, mot_de_passe)
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u
        return None

    def creer_forum(self, nom: str, description: str = "") -> Forum:
        # Vérifier si le forum existe déjà
        if nom in [f.nom for f in self.forums]:
            print(f"[Simulé] Le forum {nom} existe déjà.")
            return None

        new_id = max([f.id for f in self.forums], default=0) + 1
        forum = Forum(new_id, nom, description)
        self.forums.append(forum)
        print(f"[Simulé] Sauvegarde du forum: {forum}")

        return forum

    def creer_publication(self, titre: str, contenu: str, date_creation: str, id_auteur: int, id_forum: int) -> Publication:
        new_id = max([p.id for p in self.publications], default=0) + 1
        publication = Publication(new_id, titre, contenu, date_creation, id_auteur, id_forum)
        self.publications.append(publication)
        print(f"[Simulé] Sauvegarde de la publication: {publication}")

        return publication

    def creer_commentaire(self, contenu: str, id_auteur: int, id_publication: int) -> Commentaire:
        new_id = max([c.id for c in self.commentaires], default=0) + 1
        commentaire = Commentaire(new_id, id_auteur, contenu, id_publication)
        self.commentaires.append(commentaire)
        print(f"[Simulé] Sauvegarde du commentaire: {commentaire}")

        return commentaire

    def obtenir_forum_par_nom(self, nom_forum: str):
        for f in self.forums:
            if f.nom == nom_forum:
                return f
        return None

    def obtenir_publication_par_titre(self, titre_publication: str):
        for p in self.publications:
            if p.titre == titre_publication:
                return p
        return None

    def mettre_a_jour_forum(self, forum: Forum) -> Forum:
        for idx, f in enumerate(self.forums):
            if f.id == forum.id:
                self.forums[idx] = forum
                print(f"[Simulé] Mise à jour du forum: {forum}")
                return forum
        print(f"[Erreur] Forum avec ID {forum.id} non trouvé.")
        return None
