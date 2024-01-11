#-------------------------------------
#        Structure_de_base.py
#-------------------------------------

# Fichier pour rendre accessible tous ce qui est nécessaire pour le jeu facilement.

# Importer les librairies

class Structure_De_Base:
    """Classe représentant une structure de base
    """

    def __init__(self, taille_fenetre: tuple) -> None:
        """Créer une structure de base
        """
        self.delta_time = 0
        self.taille_fenetre = taille_fenetre
        self.touches_pressees = []

    def get_delta_time(self) -> float:
        """Retourne le temps entre la dernière frame et cette frame

        Returns:
            float: temps entre la dernière frame et cette frame
        """
        return self.delta_time

    def get_taille_fenetre(self) -> tuple:
        """Retourne la taille de la fenêtre

        Returns:
            tuple: taille de la fenêtre
        """
        return self.taille_fenetre
    
    def get_touches_pressees(self) -> list:
        """Retourne une liste de touches pressées

        Returns:
            list: liste de touches pressées
        """
        return self.touches_pressees
    
    def set_delta_time(self, delta_time: float) -> None:
        """Change la valeur entre la dernière frame et cette frame

        Args:
            delta_time (float): valeur entre la dernière frame et cette frame
        """
        self.delta_time = delta_time