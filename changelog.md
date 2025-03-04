# Changelog - Qui est-ce ?

## [Unreleased]
### Added
- Support for character images via automatic path generation based on character names
- Added image field to Character model
- Added static file serving to expose character images via HTTP
- Added image_url field to Character model to provide web-accessible image paths

### Changed
- Modified main.py to serve static files from the images directory
- Modification du système de réponse de l'IA pour ne répondre que par Oui/Non
- Mise à jour des messages pour indiquer clairement aux joueurs que les questions doivent pouvoir être répondues par Oui/Non
- Implémentation d'un système d'analyse des questions pour l'IA
- L'IA répond maintenant en fonction des vrais attributs du personnage secret
- Support des questions sur: cheveux, yeux, lunettes, barbe et chapeau

## Fonctionnalités développées

### Gestion des personnages
- Chargement des personnages depuis un fichier JSON
- Sélection aléatoire des personnages pour une partie
- Choix aléatoire du personnage à deviner

### Affichage
- Affichage formaté des détails d'un personnage
- Affichage de la liste des personnages en jeu

### Structure des données
- Format JSON pour stocker les personnages avec leurs attributs :
  - Nom
  - Couleur des cheveux
  - Couleur des yeux
  - Port de lunettes
  - Présence de barbe
  - Port de chapeau

### Initialisation du jeu
- Fonction d'initialisation complète
- Configuration du nombre de personnages par défaut (9)

### Interface utilisateur
- Système de questions interactif
- Affichage de la question posée
- Option pour quitter le jeu (commandes : quit, q, exit)
