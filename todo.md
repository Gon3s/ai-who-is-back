# Jeu Qui est-ce en Python avec IA

## Description

Le jeu Qui est-ce est un jeu de société qui se joue à deux. Chaque joueur choisit un personnage mystère et pose des questions pour découvrir le personnage mystère de l'autre joueur. Le premier joueur qui trouve le personnage mystère de l'autre joueur a gagné.

Dans cette version du jeu, nous allons jouer contre une intelligence artificielle (IA). L'IA va choisir un personnage mystère et nous devrons poser des questions pour découvrir le personnage mystère de l'IA.

## Fonctionnalités

- Le jeu se joue à deux joueurs : le joueur humain et l'IA.
- Le joueur humain commence par poser une question à l'IA pour découvrir le personnage mystère de l'IA.
- L'IA répond par "Oui" ou "Non" à la question posée par le joueur humain.
- Le joueur humain peut poser jusqu'à 5 questions pour découvrir le personnage mystère de l'IA.
- Si le joueur humain trouve le personnage mystère de l'IA, il a gagné.
- Si le joueur humain n'a pas trouvé le personnage mystère de l'IA après 5 questions, l'IA a gagné.

## BDD Personnage

Dans un premier temps, nous allons utiliser un fichier JSON stub_data.json pour stocker les personnages du jeu. Chaque personnage est représenté par un objet JSON avec les attributs suivants :
- id : l'identifiant unique du personnage (entier).
- name : le nom du personnage (chaîne de caractères).
- hair : la couleur des cheveux du personnage (chaîne de caractères).
- eyes : la couleur des yeux du personnage (chaîne de caractères).
- glasses : le personnage porte-t-il des lunettes ? (booléen).
- beard : le personnage porte-t-il une barbe ? (booléen).
- hat : le personnage porte-t-il un chapeau ? (booléen).
