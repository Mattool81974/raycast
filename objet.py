#-------------------------------------
#             Objet.py
#-------------------------------------

# Fichier où tous ce qui est nécessaire au fonctionnement des objets dans le jeu se trouve.
# Informations importantes :
# -Chaques classes représente un style d"objet différent :
#     -Objet représente un objet dans le jeu.
#     -Objet_Graphique permet de donner un visuel graphique à un Objet.
#     -Objet_Physique permet de donner de la physique à un Objet.

# Importer les librairies

class Objet:
    """Classe représentant un objet dans le jeu
    """

    def __init__(self, nom: str, position: tuple = (0, 0, 0)) -> None:
        """Créer un objet dans le jeu
        """
        self.nom = nom # Nom de l'objet dans le jeu
        self.position = position # Position de l'objet dans le jeu

    def get_nom(self) -> str:
        """Retourne le nom de l'objet dans le jeu

        Returns:
            str: nom de l'objet dans le jeu
        """
        return self.nom
    
    def get_position(self) -> tuple:
        """Retourne la position de l'objet dans le jeu

        Returns:
            tuple: position de l'objet dans le jeu
        """
        return self.position
    
class Objet_Graphique:
    """Classe représentant un affichage pour un objet
    """

    def __init__(self, objet: Objet, couleur_2d: tuple = (0, 0, 0)) -> None:
        """Créer un affichage pour un objet
        """
        self.couleur_2d = couleur_2d # Couleur affiché sur un rendu 2D
        self.objet = objet # Objet affilié à cet affichage

    def get_couleur_2d(self) -> tuple:
        """Retourne la couleur affiché sur un rendu 2D

        Returns:
            tuple: couleur affiché sur un rendu 2D
        """
        return self.couleur_2d

    def get_objet(self) -> Objet:
        """Retourne l'objet affilié à cet affichage

        Returns:
            Objet: objet affilié à cet affichage
        """
        return self.objet
    
class Objet_Physique:
    """Classe représentant une physique pour un objet
    """

    def __init__(self, objet: Objet) -> None:
        """Créer une physique pour un objet
        """
        self.objet = objet # Objet affilié à cet physique

    def get_objet(self) -> Objet:
        """Retourne l'objet affilié à cette physique

        Returns:
            Objet: objet affilié à cette physique
        """
        return self.objet