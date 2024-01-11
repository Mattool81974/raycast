#-------------------------------------
#              Main.py
#-------------------------------------

# Importer les librairies
import jeu

moteur_de_jeu = jeu.Moteur_De_Jeu((550, 550))
scene = moteur_de_jeu.nouvelle_scene("test", "cartes/niveau0.wad")
moteur_de_jeu.set_scene_actuelle("test")

moteur_de_jeu.lancer()