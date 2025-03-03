# Exemple de partie AI Who Is

Voici un exemple de partie commentée pour comprendre le déroulement du jeu.

## Configuration initiale

Liste des personnages en jeu :
- Nicolas (Cheveux: brun, Yeux: vert, Lunettes: Non, Barbe: Oui, Chapeau: Oui)
- Raphaël (Cheveux: brun, Yeux: bleu, Lunettes: Non, Barbe: Oui, Chapeau: Non)
- Lucas (Cheveux: brun, Yeux: marron, Lunettes: Non, Barbe: Oui, Chapeau: Oui)
- Sophie (Cheveux: roux, Yeux: vert, Lunettes: Oui, Barbe: Non, Chapeau: Non)
- Antoine (Cheveux: noir, Yeux: vert, Lunettes: Oui, Barbe: Oui, Chapeau: Non)
- Pierre (Cheveux: brun, Yeux: bleu, Lunettes: Oui, Barbe: Non, Chapeau: Non)
- Chloé (Cheveux: roux, Yeux: vert, Lunettes: Oui, Barbe: Non, Chapeau: Oui)
- Clara (Cheveux: blond, Yeux: bleu, Lunettes: Oui, Barbe: Non, Chapeau: Non)
- Marc (Cheveux: roux, Yeux: bleu, Lunettes: Non, Barbe: Oui, Chapeau: Oui)

L'IA a choisi Nicolas comme personnage mystère.

## Déroulement de la partie

### Question 1
**Joueur**: Est-ce que le personnage porte des lunettes ?
**IA**: Non
> *Elimination: Sophie, Antoine, Pierre, Chloé, Clara*
> *Reste: Nicolas, Raphaël, Lucas, Marc*

### Question 2
**Joueur**: Est-ce que le personnage a les cheveux bruns ?
**IA**: Oui
> *Elimination: Marc*
> *Reste: Nicolas, Raphaël, Lucas*

### Question 3
**Joueur**: Est-ce que le personnage porte un chapeau ?
**IA**: Oui
> *Elimination: Raphaël*
> *Reste: Nicolas, Lucas*

### Question 4
**Joueur**: Est-ce que le personnage a les yeux verts ?
**IA**: Oui
> *Elimination: Lucas*
> *Reste: Nicolas*

### Solution finale
**Joueur**: Je pense que c'est Nicolas !
**IA**: Bravo ! Vous avez trouvé le personnage mystère en 4 questions !

## Analyse de la stratégie

1. Première question sur les lunettes : élimine rapidement plus de la moitié des personnages
2. Question sur la couleur des cheveux : réduit encore le groupe de suspects
3. Question sur le chapeau : ne reste plus que deux possibilités
4. Question sur les yeux : permet d'identifier le personnage avec certitude

Cette partie montre une stratégie efficace où chaque question élimine le plus de possibilités.
