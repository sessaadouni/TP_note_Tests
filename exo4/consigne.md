Exercice 4: test avec des données externes

On veut réaliser une fonction qui prend en argument l'adresse
d'une page Web et renvoie le titre de la page et, le cas échéant,
le lien vers son flux de syndication RSS.

Un lien vers un flux RSS est:
- un élément HTML <link>
- avec l'une de ses propriétés rel définie à "alternate" (on peut avoir plusieurs "rel" sur un même élément)
- et la propriété type=application/rss+xml

On pourra utiliser la bibliothèque BeautifulSoup à installer avec la commande
pip install bs4
ainsi que la bibliothèque requests pour faire des requêtes http à installer avec
pip install requests

1) Écrire un test unitaire utilisant le site gameblog.fr et vérifiant que le titre contient bien la chaîne "Gameblog.fr"

2) Réaliser le test unitaire de la fonctionnalité d'extraction RSS.

3) Réaliser la fonction de recherche du lien RSS et du titre.