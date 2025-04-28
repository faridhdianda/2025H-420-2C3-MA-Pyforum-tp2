# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD

def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")

def main():
    # Initialisation de la base de données
    db = BD()

    while True:
        afficher_menu()

        # Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")
            username = input("Entrez le nom d'utilisateur: ")
            courriel = input("Entrez le courriel: ")
            mot_de_passe = input("Entrez le mot de passe: ")

            utilisateur = {
                'username': username,
                'courriel': courriel,
                'mot_de_passe': mot_de_passe
            }

            db.creer_utilisateur(**utilisateur)

        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")
            nom = input("Entrez le nom du forum: ")
            description = input("Entrez une description du forum: ")

            db.creer_forum(nom, description)

        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")
            titre = input("Entrez le titre de la publication: ")
            contenu = input("Entrez le contenu de la publication: ")
            date_creation = input("Entrez la date de création (format AAAA-MM-JJ): ")
            auteur_nom = input("Entrez le nom d'utilisateur de l'auteur: ")
            forum_nom = input("Entrez le nom du forum: ")

            auteur = db.obtenir_utilisateur_par_nom(auteur_nom)
            forum = db.obtenir_forum_par_nom(forum_nom)

            if auteur and forum:
                db.creer_publication(titre, contenu, date_creation, auteur.id, forum.id)
            else:
                print("[Erreur] Auteur ou forum introuvable.")

        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
            contenu = input("Entrez le contenu du commentaire: ")
            auteur_nom = input("Entrez le nom d'utilisateur de l'auteur du commentaire: ")
            titre_publication = input("Entrez le titre de la publication à commenter: ")

            auteur = db.obtenir_utilisateur_par_nom(auteur_nom)
            publication = db.obtenir_publication_par_titre(titre_publication)

            if auteur and publication:
                db.creer_commentaire(contenu, auteur.id, publication.id)
            else:
                print("[Erreur] Auteur ou publication introuvable.")

        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")
            username = input("Entrez votre nom d'utilisateur: ")
            nom_forum = input("Entrez le nom du forum que vous voulez rejoindre: ")

            utilisateur = db.obtenir_utilisateur_par_nom(username)
            forum = db.obtenir_forum_par_nom(nom_forum)

            if utilisateur and forum:
                if utilisateur.id not in db.utilisateurs_forums:
                    db.utilisateurs_forums[utilisateur.id] = []
                if forum.id not in db.utilisateurs_forums[utilisateur.id]:
                    db.utilisateurs_forums[utilisateur.id].append(forum.id)
                    print(f"[Info] {username} a rejoint le forum {nom_forum}.")
                else:
                    print(f"[Info] {username} est déjà membre de ce forum.")
            else:
                print("[Erreur] Utilisateur ou forum introuvable.")

        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)  # Pause de 1 seconde pour rendre l'interface plus agréable

if __name__ == "__main__":
    main()
