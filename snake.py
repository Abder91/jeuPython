# Importer les bibliothèques nécessaires
import pygame
import time
import random

# Initialiser Pygame
pygame.init()

# Définir les couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Dimensions de la fenêtre
largeur = 600
hauteur = 400

# Créer la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu du Serpent')

# Définir la vitesse du serpent
clock = pygame.time.Clock()
vitesse_serpent = 15

# Taille des blocs du serpent
taille_bloc = 10

# Définir les polices pour le texte
police_style = pygame.font.SysFont("bahnschrift", 25)
police_score = pygame.font.SysFont("comicsansms", 35)

# Fonction pour afficher le score
def afficher_score(score):
    valeur = police_score.render("Score : " + str(score), True, noir)
    fenetre.blit(valeur, [0, 0])

# Fonction pour dessiner le serpent
def dessiner_serpent(taille_bloc, serpent):
    for segment in serpent:
        pygame.draw.rect(fenetre, vert, [segment[0], segment[1], taille_bloc, taille_bloc])

# Fonction pour afficher un message de fin de jeu
def message(msg, couleur):
    texte = police_style.render(msg, True, couleur)
    fenetre.blit(texte, [largeur / 6, hauteur / 3])

# Fonction principale du jeu
def jeu():
    # Variables pour gérer l'état du jeu
    game_over = False
    game_close = False

    # Position initiale du serpent
    x1 = largeur / 2
    y1 = hauteur / 2

    # Variables pour le mouvement
    x1_change = 0
    y1_change = 0

    # Corps du serpent
    serpent = []
    longueur_serpent = 1

    # Position initiale de la nourriture
    nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
    nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0

    # Boucle principale du jeu
    while not game_over:

        # Boucle pour gérer l'écran de fin de jeu
        while game_close:
            fenetre.fill(vert)
            message("Tu as perdu ! Q pour Quitter ou C pour Recommencer", rouge)
            afficher_score(longueur_serpent - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quitter le jeu
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Recommencer le jeu
                        jeu()

        # Gérer les événements (clavier, fermeture de fenêtre)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = taille_bloc
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -taille_bloc
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = taille_bloc
                    x1_change = 0

        # Vérifier si le serpent touche les bords de l'écran
        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True

        # Mettre à jour la position du serpent
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(blanc)

        # Dessiner la nourriture
        pygame.draw.rect(fenetre, rouge, [nourriture_x, nourriture_y, taille_bloc, taille_bloc])

        # Ajouter la tête du serpent
        serpent_tete = [x1, y1]
        serpent.append(serpent_tete)

        # Supprimer l'excès de segments si le serpent n'a pas mangé
        if len(serpent) > longueur_serpent:
            del serpent[0]

        # Vérifier si le serpent se mord lui-même
        for segment in serpent[:-1]:
            if segment == serpent_tete:
                game_close = True

        # Dessiner le serpent et afficher le score
        dessiner_serpent(taille_bloc, serpent)
        afficher_score(longueur_serpent - 1)

        # Mettre à jour l'affichage
        pygame.display.update()

        # Vérifier si le serpent a mangé la nourriture
        if x1 == nourriture_x and y1 == nourriture_y:
            nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
            nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0
            longueur_serpent += 1

        # Contrôler la vitesse du jeu
        clock.tick(vitesse_serpent)

    # Quitter Pygame
    pygame.quit()
    quit()

# Lancer le jeu
jeu()