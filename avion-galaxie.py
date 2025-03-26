import pygame
import random
import sys

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Space Invaders")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0, 0, 255)

# Variables du jeu
vaisseau_x = largeur // 2
vaisseau_y = hauteur - 70
vitesse_vaisseau = 5
projectiles = []
ennemis = []
vitesse_projectile = 7
vitesse_ennemi = 2
score = 0

# Taille des objets
taille_vaisseau = 50
taille_ennemi = 50
taille_projectile = (5, 10)

# Police pour le score
police = pygame.font.Font(None, 36)

# Fonction pour afficher le score
def afficher_score():
    texte = police.render(f"Score : {score}", True, blanc)
    fenetre.blit(texte, (10, 10))

# Fonction principale
def jeu_space_invaders():
    global vaisseau_x, projectiles, ennemis, score
    clock = pygame.time.Clock()
    jeu_en_cours = True

    while jeu_en_cours:
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Gérer les touches
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and vaisseau_x > 0:
            vaisseau_x -= vitesse_vaisseau
        if touches[pygame.K_RIGHT] and vaisseau_x < largeur - taille_vaisseau:
            vaisseau_x += vitesse_vaisseau
        if touches[pygame.K_SPACE]:
            projectiles.append([vaisseau_x + taille_vaisseau // 2, vaisseau_y])

        # Mettre à jour les projectiles
        for projectile in projectiles:
            projectile[1] -= vitesse_projectile
            if projectile[1] < 0:
                projectiles.remove(projectile)

        # Ajouter des ennemis
        if random.randint(1, 50) == 1:
            ennemis.append([random.randint(0, largeur - taille_ennemi), 0])

        # Mettre à jour les ennemis
        for ennemi in ennemis:
            ennemi[1] += vitesse_ennemi
            if ennemi[1] > hauteur:
                ennemis.remove(ennemi)

        # Vérifier les collisions
        for projectile in projectiles:
            for ennemi in ennemis:
                if (
                    projectile[0] > ennemi[0]
                    and projectile[0] < ennemi[0] + taille_ennemi
                    and projectile[1] > ennemi[1]
                    and projectile[1] < ennemi[1] + taille_ennemi
                ):
                    projectiles.remove(projectile)
                    ennemis.remove(ennemi)
                    score += 1
                    break

        # Vérifier si un ennemi touche le vaisseau
        for ennemi in ennemis:
            if (
                vaisseau_x < ennemi[0] + taille_ennemi
                and vaisseau_x + taille_vaisseau > ennemi[0]
                and vaisseau_y < ennemi[1] + taille_ennemi
                and vaisseau_y + taille_vaisseau > ennemi[1]
            ):
                afficher_message("Game Over")
                jeu_en_cours = False

        # Dessiner l'écran
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, bleu, (vaisseau_x, vaisseau_y, taille_vaisseau, taille_vaisseau))  # Vaisseau
        for projectile in projectiles:
            pygame.draw.rect(fenetre, rouge, (projectile[0], projectile[1], *taille_projectile))  # Projectile
        for ennemi in ennemis:
            pygame.draw.rect(fenetre, vert, (ennemi[0], ennemi[1], taille_ennemi, taille_ennemi))  # Ennemi
        afficher_score()

        # Mettre à jour l'affichage
        pygame.display.update()
        clock.tick(60)

# Fonction pour afficher un message de fin
def afficher_message(message):
    fenetre.fill(noir)
    texte = police.render(message, True, blanc)
    texte_rect = texte.get_rect(center=(largeur // 2, hauteur // 2))
    fenetre.blit(texte, texte_rect)
    pygame.display.update()
    pygame.time.wait(3000)

# Lancer le jeu
if __name__ == "__main__":
    jeu_space_invaders()