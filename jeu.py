#-------------------------------------
#               Jeu.py
#-------------------------------------

# Importer les librairies
import pygame as pg
import scene as sc
import structure_de_base as sb
import sys

class Moteur_De_Jeu:
    """Classe représentant un moteur de jeu
    """

    def __init__(self, taille_fenetre: tuple) -> None:
        """Créer un moteur de jeu
        """
        self.scene_actuelle = "" # Scène actuelle affichée
        self.scenes = {} # Dictionnaire des scène créees avec en clé le nom de la scène et en valeur la scène
        self.structure_de_base = sb.Structure_De_Base(taille_fenetre = taille_fenetre)
        self.taille_fenetre = taille_fenetre

        pg.init()
        self.fenetre = pg.display.set_mode(self.get_taille_fenetre())
        self.horloge = pg.time.Clock()

    def ajouter_scene(self, nom: str, scene: sc.Scene) -> None:
        """Ajoute une scène dans le jeu

        Args:
            nom (str): nom de la scène à ajouter
            scene (sc.Scene): scène à ajouter
        """
        assert list(self.get_scenes().keys()).count(nom) <= 0, ("Moteur de jeu : la scène \"" + nom + "\" existe déjà dans le jeu.")
        self.get_scenes()[nom] = scene

    def frame(self) -> None:
        """Réaliser une frame du jeu
        """
        self.get_scene_actuelle().frame()
        rendu = self.get_scene_actuelle().rendu()
        self.get_fenetre().blit(rendu, (0, 0, rendu.get_width(), rendu.get_height()))

    def gerer_evenements(self) -> None:
        """Gère les évènements du jeu
        """
        evenements = pg.event.get()
        for evenement in evenements: # Parcourir les évènements
            if evenement.type == pg.QUIT: # Quitter le jeu
                pg.quit()
                sys.exit()
            elif evenement.type == pg.KEYDOWN: # Si une touche est pressé
                if self.get_structure_de_base().get_touches_pressees().count(evenement.key) <= 0:
                    self.get_structure_de_base().get_touches_pressees().append(evenement.key)
            elif evenement.type == pg.KEYUP: # Si une touche est laché
                if self.get_structure_de_base().get_touches_pressees().count(evenement.key) > 0:
                    self.get_structure_de_base().get_touches_pressees().remove(evenement.key)

    def get_fenetre(self) -> pg.Surface:
        """Retourne la fenêtre du jeu

        Returns:
            pg.Surface: fenêtre du jeu
        """
        return self.fenetre
    
    def get_horloge(self) -> pg.time.Clock:
        """Retourne l'horloge du jeu

        Returns:
            pg.time.Clock: horloge du jeu
        """
        return self.horloge

    def get_nom_scene_actuelle(self) -> str:
        """Retourne le nom de la scène actuelle dans le jeu

        Returns:
            str: nom de la scène actuelle dans le jeu
        """
        return self.scene_actuelle
    
    def get_scene_actuelle(self) -> sc.Scene:
        """Retourne la scène actuelle dans le jeu

        Returns:
            sc.Scene: scène actuelle dans le jeu
        """
        return self.get_scenes()[self.get_nom_scene_actuelle()]

    def get_scenes(self) -> dict:
        """Retourne le dictionnaire des scène dans le jeu

        Returns:
            dict: dictionnaire des scène dans le jeu
        """
        return self.scenes
    
    def get_structure_de_base(self) -> sb.Structure_De_Base:
        """Retourne la structure de base dans le jeu

        Returns:
            tuple: structure de base dans le jeu
        """
        return self.structure_de_base
    
    def get_taille_fenetre(self) -> tuple:
        """Retourne la taille de la fenêtre

        Returns:
            tuple: taille de la fenêtre
        """
        return self.taille_fenetre
    
    def lancer(self) -> None:
        """Lance le jeu
        """
        while True: # Boucle infini pour simuler le jeu
            self.gerer_evenements()
            self.frame()
            pg.display.flip()
            self.get_structure_de_base().set_delta_time(self.get_horloge().tick(120) * 0.001)
    
    def nouvelle_scene(self, nom: str, carte: str, graphique: bool = True, physique: bool = True) -> sc.Scene:
        """Crée une nouvelle scène dans le jeu et la retoure

        Args:
            nom (str): nom de la scène à créer
            carte (str): chemin d'accés vers une carte à charger
            graphique (bool): si la scène utilise une partie graphique, par défaut à "True"
            physique (bool): si la scène utilise une partie physique, par défaut à "True"

        Returns:
            sc.Scene: scène crée
        """
        assert list(self.get_scenes().keys()).count(nom) <= 0, ("Moteur de jeu : la scène \"" + nom + "\" existe déjà dans le jeu.")
        scene = sc.Scene(nom, carte, self.get_taille_fenetre(), self.get_structure_de_base(), graphique = graphique, physique = physique)
        self.ajouter_scene(nom, scene)
        return scene
    
    def set_scene_actuelle(self, nom: str) -> None:
        """Change la valeur de la scène actuelle

        Args:
            nom (str): valeur de la scène actuelle
        """
        assert list(self.get_scenes().keys()).count(nom) > 0, ("Moteur de jeu : la scène \"" + nom + "\" que vous essayez de mettre en scène actuelle n'existe pas.")
        self.scene_actuelle = nom