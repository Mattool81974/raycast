#-------------------------------------
#             Scene.py
#-------------------------------------

# Informations importantes :
# -Chaques classes représente un style de scène différent :
#     -Scene permet de créer un contexte de jeu.
#     -Scene_Graphique permet un affichage graphique.
#     -Scene_Physique permet de donner une physique au jeu.

# Importer les librairies
import os
import pygame as pg

class Scene_Physique:
    """Class représentant une scène physique
    """

    def __init__(self) -> None:
        """Créer une scène physique
        """

class Scene_Graphique:
    """Classe représentant une scène graphique
    """

    def __init__(self) -> None:
        """Créer une scène graphique
        """
        self.objets = {}

class Scene:
    """Classe représentant une scène normal
    """

    def __init__(self, nom: str, carte: str, graphique: bool = True, physique: bool = True) -> None:
        """Créer une scène

        Args:
            nom (str): nom de la scène
            carte (str): chemin d'accés vers la carte représentant la scène
            graphique (bool, optionnel): si la scène contient une partie graphique ou non, par défaut à "True"
            physique (bool, optionnel): si la scène contient une partie physique ou non, par défaut à "True"
        """
        contenu = self.contenu_carte(carte)

        self.carte = [] # Contenu de la carte de la scène
        self.graphique = graphique #Si la scène utilise une scène graphique
        self.nom = nom # Nom de la scène
        self.physique = physique # Si la scène utilise une scène physique
        self.scene_graphique = None #Scène graphique de la scène
        self.scene_physique = None # Scène physique de la scène
        self.taille = (int(contenu[0].split(" ")[0]), int(contenu[0].split(" ")[0])) # Obtenir la taille de la carte

        if graphique: # Si la scène contient une partie graphique
            self.scene_graphique = Scene_Graphique()

        if physique: # Si la scène contient une partie physique
            self.scene_graphique = Scene_Graphique()

        self.charger_carte(contenu[1:])

    def charger_carte(self, carte: list) -> None:
        """Charge la carte depuis le retour de contenu_carte

        Args:
            carte (list): retour de contenu_carte
        """
        assert len(carte) == self.get_taille()[1], ("Scene \"" + self.get_nom() + "\" : la carte que vous voulez chargé n'a pas la même hauteur en métadonnée qu'en contenu.")
        for i in carte: # Parcourir la carte
            assert len(i) == self.get_taille()[0], ("Scene \"" + self.get_nom() + "\" : la carte que vous voulez chargé n'a pas la même largeur en métadonnée qu'en contenu.")
            ligne = []
            for j in i:
                ligne.append(j)
            self.carte.append(ligne)

    def contenu_carte(self, carte: str) -> list:
        """Retourne le contenu d'une carte

        Args:
            carte (str): chemin d'accés vers la carte

        Return:
            list: contenu de la carte découpé par ligne
        """
        # Vérifier si le fichier existe
        assert os.path.exists(carte), ("Scene \"" + self.get_nom() + "\" : la carte que vous voulez chargé, de chemin d'accés \"" + carte + "\", n'existe pas.")
        
        # Vérifier si l'extension correspond à une carte
        extension = carte.split(".")[-1]
        assert extension == "wad", ("Scene \"" + self.get_nom() + "\" : la carte que vous voulez chargé, de chemin d'accés \"" + carte + "\", n'a pas la bonne extension (seul le .wad est autorisé).")
        
        fichier = open(carte, "r")
        contenu = fichier.readlines() # Ouvrir et lire le fichier
        for c in range(len(contenu) - 1): contenu[c] = contenu[c][:-1] # Enlever les "\n" à la fin
        fichier.close()

        return contenu

    def get_nom(self) -> str:
        """Retourne le nom de la scène

        Returns:
            str: nom de la scène
        """
        return self.nom

    def get_scene_graphique(self) -> Scene_Graphique:
        """Retourne la scène graphique dans la scène

        Returns:
            Scene_Graphique: scène graphique dans la scène
        """
        return self.scene_graphique

    def get_scene_physique(self) -> Scene_Physique:
        """Retourne la scène physique dans la scène

        Returns:
            Scene_Physique: scène physique dans la scène
        """
        return self.scene_physique
    
    def get_taille(self) -> tuple:
        """Retourne la taille de la scène

        Returns:
            tuple: taille de la scène
        """
        return self.taille

    def is_graphique(self) -> bool:
        """Retourne si la scène contient une partie graphique

        Returns:
            bool: si la scène contient une partie graphique
        """
        return self.graphique
    
    def is_physique(self) -> bool:
        """Retourne si la scène contient une partie physique

        Returns:
            bool: si la scène contient une partie physique
        """
        return self.physique