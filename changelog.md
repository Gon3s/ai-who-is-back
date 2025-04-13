# Changelog - Qui est-ce ?

## [Unreleased]
### Added
- Intégration de LangChain pour une gestion plus flexible des interactions avec les modèles de langage
- Système avancé de chaînes de traitement avec mémoire de conversation
- Support pour les chaînes de décision basées sur les attributs des personnages
- Possibilité de basculer entre chaîne simple et chaîne avancée via un flag
- Support for character images via automatic path generation based on character names
- Added image field to Character model
- Added static file serving to expose character images via HTTP
- Added image_url field to Character model to provide web-accessible image paths

### Changed
- Modified main.py to serve static files from the images directory
- Remplacement de l'utilisation directe de l'API Groq par LangChain pour une meilleure flexibilité
- Mise à jour des dépendances pour inclure LangChain et ses composants
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

### Intelligence artificielle
- Intégration de LangChain pour une gestion avancée des modèles LLM
- Système de mémoire pour suivre le contexte des conversations
- Analyse avancée des attributs du personnage
