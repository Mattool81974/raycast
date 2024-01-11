#-------------------------------------
#             Scene.py
#-------------------------------------

# Informations importantes :
# -Chaques classes représente un style de scène différent :
#     -Scene permet de créer un contexte de jeu.
#     -Scene_Graphique permet un affichage graphique.
#     -Scene_Physique permet de donner une physique au jeu.

# Importer les librairies
import objet as ob
import os
import pygame as pg
import structure_de_base as sb

class Scene_Physique:
    """Class représentant une scène physique
    """

    def __init__(self, structure_de_base: sb.Structure_De_Base) -> None:
        """Créer une scène physique

        Args:
            structure_de_base (sb.Structure_De_Base): structure de base du jeu
        """
        self.objets = {}
        self.structure_de_base = structure_de_base

    def get_structure_de_base(self) -> sb.Structure_De_Base:
        """Retourne la structure de base du jeu

        Returns:
            sb.Structure_De_Base: structure de base du jeu
        """
        return self.structure_de_base

class Scene_Graphique:
    """Classe représentant une scène graphique
    """

    def __init__(self, nom: str, taille: tuple, taille_fenetre: tuple, structure_de_base: sb.Structure_De_Base) -> None:
        """Créer une scène graphique

        Args:
            nom (str): nom de la scène graphique
            taille (tuple): taille de la fenêtre graphique
            structure_de_base (sb.Structure_De_Base): structure de base du jeu
        """
        self.carte = []
        self.nom = nom
        self.objets = {}
        self.structure_de_base = structure_de_base
        self.taille = taille
        self.taille_fenetre = taille_fenetre

        self.remplir_carte()

    def ajouter_objet(self, nom: str, objet: ob.Objet_Graphique) -> None:
        """Ajoute un objet dans la scène

        Args:
            nom (str): nom de l'objet
            objet (ob.Objet_Graphique): objet à ajouter dans la scène
        """
        assert list(self.get_objets().keys()).count(nom) <= 0, ("Scene graphique \"" + self.get_nom() + "\" : un objet de nom \"" + nom + "\" existe déjà.") # Si l'objet n'existe pas déjà
        position = objet.get_objet().get_position()
        self.get_carte()[position[0]][position[1]] = objet # Placer l'objet dans la carte
        self.get_objets()[nom] = objet # Ajouter l'objet à la scène

    def frame(self) -> None:
        """Réalise une frame de la scène graphique
        """

    def get_carte(self) -> list:
        """Retourne la carte de la scène

        Returns:
            list: carte de la scène
        """
        return self.carte

    def get_nom(self) -> str:
        """Retourne le nom de la scène graphique

        Returns:
            str: nom de la scène graphique
        """
        return self.nom
    
    def get_objet_de_nom(self, nom: str) -> ob.Objet_Graphique:
        """Retourne un objet selon son nom dans la scène

        Args:
            nom (str): nom de l'objet dans la scène

        Returns:
            ob.Objet_Graphique: objet selon son nom dans la scène
        """
        return self.get_objets()[nom]
    
    def get_objet_sur_carte(self, x: int, y: int) -> ob.Objet_Graphique:
        """Retourne un objet selon sa position sur la carte

        Args:
            x (int): coordonnée x de l'objet
            y (int): coordonnée y de l'objet

        Returns:
            ob.Objet_Graphique: objet selon sa position sur la carte
        """
        return self.get_carte()[x][y]
    
    def get_objets(self) -> dict:
        """Retourne un dictionnaire des objets dans la scène

        Returns:
            dict: objets dans la scène
        """
        return self.objets
    
    def get_structure_de_base(self) -> sb.Structure_De_Base:
        """Retourne la structure de base du jeu

        Returns:
            sb.Structure_De_Base: structure de base du jeu
        """
        return self.structure_de_base

    def get_taille(self) -> tuple:
        """Retourne la taille de la scène

        Returns:
            tuple: taille de la scène
        """
        return self.taille
    
    def get_taille_fenetre(self) -> tuple:
        """Retourne la taille de la fenêtre du jeu

        Returns:
            tuple: taille de la fenêtre du jeu
        """
        return self.taille_fenetre

    def nouvel_objet(self, nom: str, objet: ob.Objet, couleur_2d: tuple = (0, 0, 0), forme_2d: str = "rectangle") -> ob.Objet_Graphique:
        """Crée un nouvel objet dans la scène graphique et le retourne

        Args:
            nom (str): nom de l'objet
            objet (ob.Objet): objet à lié à cet objet dans la scène graphique
            couleur_2d (tuple, optionnel): couleur de l'objet lors d'un rendu 2D
            forme_2d (tuple, optionnel): forme de l'objet lors d'un rendu 2D

        Return:
            ob.Objet_Graphique: objet crée
        """
        assert list(self.objets.keys()).count(nom) <= 0, ("Scene graphique \"" + self.get_nom() + "\" : un objet de nom \"" + nom + "\" existe déjà.") # Si l'objet n'existe pas déjà
        objet_graphique = ob.Objet_Graphique(objet, couleur_2d = couleur_2d, forme_2d = forme_2d)
        self.ajouter_objet(nom, objet_graphique)
        return objet_graphique
    
    def remplir_carte(self) -> None:
        """Rempli la carte avec du vide
        """
        self.get_carte().clear() # Vider la carte
        for _ in range(self.get_taille()[0]): # Remplir la carte selon la taille défini
            partie = []
            for __ in range(self.get_taille()[1]):
                partie.append(0)
            self.get_carte().append(partie)

    def rendu_2d(self) -> pg.Surface:
        """Retourne le rendu 2D de la scène

        Returns:
            pg.Surface: rendu 2D de la scène
        """
        retour = pg.Surface(self.get_taille_fenetre()).convert_alpha() # Créer la surface d'affichage
        retour.fill((0, 0, 0))
        hauteur_carre = self.get_taille_fenetre()[1] / len(self.get_carte()[0])
        largeur_carre = self.get_taille_fenetre()[0] / len(self.get_carte())
        for objet in self.get_objets().keys():
            objet = self.get_objet_de_nom(objet)
            position = objet.get_objet().get_position()
            if objet.get_forme_2d() == "rectangle":
                pg.draw.rect(retour, objet.get_couleur_2d(), (position[0] * largeur_carre, position[1] * hauteur_carre, largeur_carre, hauteur_carre))
            elif objet.get_forme_2d() == "cercle":
                pg.draw.circle(retour, objet.get_couleur_2d(), (position[0] * largeur_carre + largeur_carre / 2, position[1] * hauteur_carre + largeur_carre / 2), largeur_carre / 2)
        return retour

class Scene:
    """Classe représentant une scène normal
    """

    def __init__(self, nom: str, carte: str, taille_fenetre: tuple, structure_de_base: sb.Structure_De_Base, graphique: bool = True, physique: bool = True) -> None:
        """Créer une scène

        Args:
            nom (str): nom de la scène
            carte (str): chemin d'accés vers la carte représentant la scène
            structure_de_base (sb.Structure_De_Base): structure de base du jeu
            graphique (bool, optionnel): si la scène contient une partie graphique ou non, par défaut à "True"
            physique (bool, optionnel): si la scène contient une partie physique ou non, par défaut à "True"
        """
        contenu = self.contenu_carte(carte)

        self.carte = [] # Contenu de la carte de la scène
        self.graphique = graphique #Si la scène utilise une scène graphique
        self.nom = nom # Nom de la scène
        self.objets = {} # Objets dans la scène, de clé leur nom et de valeur l'objet
        self.physique = physique # Si la scène utilise une scène physique
        self.scene_graphique = None #Scène graphique de la scène
        self.scene_physique = None # Scène physique de la scène
        self.structure_de_base = structure_de_base # Structure du base de jeu
        self.taille = (int(contenu[0].split(" ")[0]), int(contenu[0].split(" ")[0])) # Obtenir la taille de la carte

        if graphique: # Si la scène contient une partie graphique
            self.scene_graphique = Scene_Graphique(self.get_nom(), self.get_taille(), taille_fenetre, self.get_structure_de_base())

        if physique: # Si la scène contient une partie physique
            self.scene_physique = Scene_Physique(self.get_structure_de_base())

        self.remplir_carte() # Préparer la carte
        self.charger_carte(contenu[1:])

        self.joueur = self.nouvel_objet("joueur", 1, 1, couleur_2d = (0, 255, 0), graphique = True, physique = False, type = "joueur")

    def ajouter_objet(self, nom: str, objet: ob.Objet) -> None:
        """Rajoute un objet déjà crée dans le jeu

        Args:
            nom (str): nom de l'objet à rajouter
            objet (ob.Objet): objet à rajouter
        """
        assert list(self.get_objets().keys()).count(nom) <= 0, ("Scene \"" + self.get_nom() + "\" : un objet de nom \"" + nom + "\" existe déjà.") # Si l'objet n'existe pas déjà
        self.objets[nom] = objet

    def charger_carte(self, carte: list) -> None:
        """Charge la carte depuis le retour de contenu_carte

        Args:
            carte (list): retour de contenu_carte
        """
        assert len(carte) == self.get_taille()[1], ("Scene \"" + self.get_nom() + "\" : la carte que vous voulez chargé n'a pas la même hauteur en métadonnée qu'en contenu.")
        for i in range(len(carte)): # Parcourir la carte
            assert len(carte[i]) == self.get_taille()[0], ("Scene \"" + self.get_nom() + "\" : la carte que vous voulez chargé n'a pas la même largeur en métadonnée qu'en contenu.")
            for j in range(len(carte[i])):
                if int(carte[i][j]) != 0:
                    nom = str(j) + "," + str(i) # Demander la création de l'objet
                    self.nouvel_objet(nom, j, i)

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
    
    def frame(self) -> None:
        """Réalise une frame de la scène
        """
        for objet in self.get_objets().values(): # Réaliser une frame dans chaques objets
            objet.frame(self.get_structure_de_base().get_delta_time())

        if self.is_graphique(): # Réalise une frame de la scène graphique si il y en a une
            self.get_scene_graphique().frame()

        self.simuler_joueur() # S'occuper du joueur

    def get_joueur(self) -> ob.Joueur:
        """Retourne le joueur dans la scène

        Returns:
            ob.Joueur: joueur dans la scène
        """
        return self.joueur

    def get_nom(self) -> str:
        """Retourne le nom de la scène

        Returns:
            str: nom de la scène
        """
        return self.nom
    
    def get_objets(self) -> dict:
        """Retourne le dictionnaire d'objets dans le jeu

        Returns:
            dict: dictionnaire d'objets dans le jeu
        """
        return self.objets

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
    
    def get_structure_de_base(self) -> sb.Structure_De_Base:
        """Retourne la structure de base du jeu

        Returns:
            sb.Structure_De_Base: structure de base du jeu
        """
        return self.structure_de_base
    
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
    
    def nouvel_objet(self, nom: str, x: int, y: int, couleur_2d: tuple = (255, 0, 0), graphique: bool = True, physique: bool = True, type: str = "") -> ob.Objet:
        """Crée un objet dans la scène et le retourne

        Args:
            nom (str): nom de l'objet
            x (int): position x de l'objet
            y (int): position y de l'objet
            couleur_2d (tuple, optionnel): couleur de l'objet pour un rendu 2D, par défaut à (255, 0, 0)
            graphique (bool, optionnel): si l'objet à une partie graphique, par défaut à "True"
            physique (bool, optionnel): si l'objet à une partie physique, par défaut à "True"
            type (str, optionnel): type de l'objet a crée, apr défaut à ""

        Return:
            ob.Objet: objet crée
        """
        assert list(self.get_objets().keys()).count(nom) <= 0, ("Scene \"" + self.get_nom() + "\" : un objet de nom \"" + nom + "\" existe déjà.") # Si l'objet n'existe pas déjà
        objet = None
        if type == "joueur":
            objet = ob.Joueur(position = (x, y, 0)) # Création du joueur

            if self.is_graphique() and graphique: # Créer un nouvel objet graphique pour le joueur
                self.get_scene_graphique().nouvel_objet(nom, objet, couleur_2d, forme_2d = "cercle")
        else:
            objet = ob.Objet(nom, position = (x, y, 0)) # Création de l'objet

            if self.is_graphique() and graphique: # Créer un nouvel objet graphique
                self.get_scene_graphique().nouvel_objet(nom, objet, couleur_2d)

        self.ajouter_objet(nom, objet) # Ajouter l'objet à la scène
        return objet
    
    def remplir_carte(self) -> None:
        """Rempli la carte avec du vide
        """
        self.carte.clear() # Vider la carte
        for _ in range(self.get_taille()[0]): # Remplir la carte selon la taille défini
            partie = []
            for __ in range(self.get_taille()[1]):
                partie.append(0)
            self.carte.append(partie)

    def rendu(self) -> pg.Surface:
        """Retourne le rendu de la scène

        Returns:
            pg.Surface: rendu de la scène
        """
        if self.is_graphique():
            return self.get_scene_graphique().rendu_2d()
        retour = pg.image.load("textures/inconnu.png").convert_alpha()
        return retour
    
    def simuler_joueur(self) -> None:
        """Simule la frame pour le joueur
        """
        joueur = self.get_joueur()
        vecteur_avant = joueur.get_vecteur_avant()

        # Vérifier si les touches sont pressées
        touches_h = (self.get_structure_de_base().get_touches_pressees().count(pg.K_LEFT) > 0, self.get_structure_de_base().get_touches_pressees().count(pg.K_RIGHT) > 0)
        touches_v = (self.get_structure_de_base().get_touches_pressees().count(pg.K_UP) > 0, self.get_structure_de_base().get_touches_pressees().count(pg.K_DOWN) > 0)
        vitesse = joueur.get_vitesse() * self.get_structure_de_base().get_delta_time()
        vitesse_rotation = joueur.get_vitesse_rotation() * self.get_structure_de_base().get_delta_time()

        mouvement_avant = (vitesse * vecteur_avant[0] * touches_v[0] - vitesse * vecteur_avant[0] * touches_v[1], vitesse * vecteur_avant[1] * touches_v[0] - vitesse * vecteur_avant[1] * touches_v[1], 0)
        joueur.move(mouvement_avant) # Faire bouger le joueur vers l'avant

        rotation = (vitesse_rotation * touches_h[1] - vitesse_rotation * touches_h[0])
        joueur.rotate(rotation)