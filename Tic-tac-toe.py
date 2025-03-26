# Importer les bibliothèques nécessaires
import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur, hauteur = 600, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tic Tac Toe")

# Définir les couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)

# Définir les dimensions des cases
taille_case = largeur // 3

# Initialiser le plateau de jeu
plateau = [' ' for _ in range(9)]

# Définir la police pour le texte
police = pygame.font.Font(None, 100)

# Fonction pour dessiner la grille
def dessiner_grille():
    for i in range(1, 3):
        # Lignes horizontales
        pygame.draw.line(fenetre, noir, (0, i * taille_case), (largeur, i * taille_case), 5)
        # Lignes verticales
        pygame.draw.line(fenetre, noir, (i * taille_case, 0), (i * taille_case, hauteur), 5)

# Fonction pour dessiner les symboles (X et O)
def dessiner_symboles():
    for i in range(9):
        # Calculer la position de la case
        x = (i % 3) * taille_case
        y = (i // 3) * taille_case

        # Vérifier si la case contient un symbole
        if plateau[i] == 'X':
            texte = police.render('X', True, rouge)
            # Centrer le symbole dans la case
            texte_rect = texte.get_rect(center=(x + taille_case // 2, y + taille_case // 2))
            fenetre.blit(texte, texte_rect)
        elif plateau[i] == 'O':
            texte = police.render('O', True, bleu)
            # Centrer le symbole dans la case
            texte_rect = texte.get_rect(center=(x + taille_case // 2, y + taille_case // 2))
            fenetre.blit(texte, texte_rect)

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(joueur):
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinaison in combinaisons:
        if plateau[combinaison[0]] == plateau[combinaison[1]] == plateau[combinaison[2]] == joueur:
            return True
    return False

# Fonction pour afficher un message de victoire ou de match nul
def afficher_message(message):
    fenetre.fill(blanc)  # Effacer l'écran
    texte = police.render(message, True, noir)
    texte_rect = texte.get_rect(center=(largeur // 2, hauteur // 2))
    fenetre.blit(texte, texte_rect)
    pygame.display.update()
    pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter
    pygame.quit()
    sys.exit()

# Fonction principale du jeu
def jeu_tic_tac_toe():
    joueur_actuel = 'X'  # Le joueur 'X' commence
    jeu_en_cours = True

    while jeu_en_cours:
        # Remplir l'écran avec une couleur blanche
        fenetre.fill(blanc)

        # Dessiner la grille et les symboles
        dessiner_grille()
        dessiner_symboles()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtenir la position de la souris
                x, y = event.pos
                # Calculer l'index de la case cliquée
                ligne = y // taille_case
                colonne = x // taille_case
                index = ligne * 3 + colonne

                # Vérifier si la case est vide
                if plateau[index] == ' ':
                    plateau[index] = joueur_actuel

                    # Vérifier si le joueur actuel a gagné
                    if verifier_victoire(joueur_actuel):
                        dessiner_symboles()  # Dessiner le dernier symbole
                        afficher_message(f" joueur {joueur_actuel} a gagné !")
                        jeu_en_cours = False

                    # Passer au joueur suivant
                    joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

        # Vérifier si le plateau est plein (match nul)
        if ' ' not in plateau and jeu_en_cours:
            afficher_message("Match nul !")
            jeu_en_cours = False

        # Mettre à jour l'affichage
        pygame.display.update()

    # Quitter le jeu proprement
    pygame.quit()

# Lancer le jeu
if __name__ == "__main__":
    jeu_tic_tac_toe()