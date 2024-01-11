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
import math

def calculer_vecteur(angle: float) -> tuple:
    """Retourne un vecteur selon l'angle

    Args:
        angle (float): angle pour calculer le vecteur

    Returns:
        tuple: vecteur final
    """
    return normaliser_vecteur((math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0))

def distance(position_1: tuple, position_2: tuple) -> float:
    """Retourne la distance entre deux points

    Args:
        position_1 (tuple): premier point
        position_2 (tuple): deuxième point

    Returns:
        float: distance entre les points
    """
    return math.sqrt((position_1[0] - position_2[0]) ** 2 + (position_1[1] - position_2[1]) ** 2)

def normaliser_vecteur(vecteur: tuple) -> tuple:
    """Normaliser un vecteur

    Args:
        vecteur (tuple): vecteur à normaliser

    Returns:
        tuple: vecteur normalisé
    """
    somme = math.sqrt((math.pow(vecteur[0], 2) + math.pow(vecteur[1], 2)) + math.pow(vecteur[2], 2))
    multiplier = 1/somme
    return (vecteur[0] * multiplier, vecteur[1] * multiplier, vecteur[2] * multiplier)

class Objet:
    """Classe représentant un objet dans le jeu
    """

    def __init__(self, nom: str, position: tuple = (0, 0, 0)) -> None:
        """Créer un objet dans le jeu
        """
        self.angle = 0 # Angle de l'objet
        self.mouvement = (0, 0, 0) # Mouvement de l'objet
        self.nom = nom # Nom de l'objet dans le jeu
        self.position = position # Position de l'objet dans le jeu

        self.vecteur_avant = (1, 0, 0) # Vecteur pour aller en avant dans le jeu

        self.calculer_vecteurs()

    def calculer_vecteurs(self) -> None:
        """Recalculer les vecteurs
        """

        # Calculer le vecteur avant en utilisant de la trigonométrie
        self.vecteur_avant = calculer_vecteur(self.get_angle())

    def get_angle(self) -> float:
        """Retourne l'angle de l'objet

        Returns:
            float: angle de l'objet
        """
        return self.angle

    def get_mouvement(self) -> tuple:
        """Retourne le mouvement de l'objet

        Returns:
            tuple: mouvement de l'objet
        """
        return self.mouvement

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
    
    def get_vecteur_avant(self) -> tuple:
        """Retourne le vecteur avant de l'objet

        Returns:
            tuple: vecteur avant de l'objet
        """
        return self.vecteur_avant
    
    def frame(self, delta_time: float) -> None:
        """Effectue une frame de l'objet, dédié à l'héritage

        Args:
            delta_time (float): temps entre la dernière frame et la frame actuelle
        """

    def move(self, mouvement: tuple) -> None:
        """Bouge l'objet

        Args:
            mouvement (tuple): mouvement à appliquer à l'objet
        """
        self.mouvement = mouvement
        position = self.get_position()
        self.set_position((position[0] + self.get_mouvement()[0], position[1] + self.get_mouvement()[1], position[2] + self.get_mouvement()[2]))

    def rotate(self, angle: float) -> None:
        """Tourne l'objet d'un certain angle

        Args:
            angle (float): angle pour faire tourner l'objet
        """
        if self.get_angle() != angle:
            self.set_angle(self.get_angle() + angle)
            self.calculer_vecteurs()

    def set_angle(self, angle: float) -> None:
        """Change la valeur de l'angle

        Args:
            angle (float): nouvelle valeur de l'angle
        """
        self.angle = angle
    
    def set_position(self, position: tuple) -> None:
        """Change la position de l'objet

        Args:
            position (tuple): nouvelle position de l'objet
        """
        self.position = position
    
class Objet_Graphique:
    """Classe représentant un affichage pour un objet
    """

    def __init__(self, objet: Objet, couleur_2d: tuple = (0, 0, 0), forme_2d: str = "rectangle") -> None:
        """Créer un affichage pour un objet
        """
        self.couleur_2d = couleur_2d # Couleur affiché sur un rendu 2D
        self.forme_2d = forme_2d # Forme affiché sur un rendu 2D
        self.objet = objet # Objet affilié à cet affichage

    def frame(self, delta_time: float) -> None:
        """Effectue une frame de l'objet, dédié à l'héritage

        Args:
            delta_time (float): temps entre la dernière frame et la frame actuelle
        """

    def get_couleur_2d(self) -> tuple:
        """Retourne la couleur affiché sur un rendu 2D

        Returns:
            tuple: couleur affiché sur un rendu 2D
        """
        return self.couleur_2d
    
    def get_forme_2d(self) -> str:
        """Retourne la forme affiché sur un rendu 2D

        Returns:
            str: forme affiché sur un rendu 2D
        """
        return self.forme_2d

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

    def frame(self, delta_time: float) -> None:
        """Effectue une frame de l'objet, dédié à l'héritage

        Args:
            delta_time (float): temps entre la dernière frame et la frame actuelle
        """

    def get_objet(self) -> Objet:
        """Retourne l'objet affilié à cette physique

        Returns:
            Objet: objet affilié à cette physique
        """
        return self.objet
    
class Joueur(Objet):
    """Classe représentant le joueur, héritant de Objet
    """

    def __init__(self, position: tuple = (0, 0, 0)) -> None:
        """Créer un joueur

        Args:
            position (tuple, optionnel): position du joueur, par défaut à (0, 0, 0)
        """
        super().__init__("joueur", position)

        self.vitesse = 5 # Vitesse du joueur
        self.vitesse_rotation = 90 # Vitesse de rotation du joueur

    def frame(self, delta_time: float) -> None:
        """Effectue une frame du joueur

        Args:
            delta_time (float): temps entre la dernière frame et la frame actuelle
        """

    def get_vitesse(self) -> float:
        """Retourne la vitesse du joueur

        Returns:
            float: vitesse du joueur
        """
        return self.vitesse
    
    def get_vitesse_rotation(self) -> float:
        """Retourne la vitesse de rotation du joueur

        Returns:
            float: vitesse de rotation du joueur
        """
        return self.vitesse_rotation