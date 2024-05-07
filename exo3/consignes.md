Exercice 3: test de performance

On veut comparer deux méthodes pour calculer une suite de Fibonacci.

Rappel: la suite de Fibonacci est une suite mathématique F définie ainsi:

F(0) = 1
F(1) = 1
pour tout n entier supérieur à 1, F(n) = F(n-2) + F(n-1)

ainsi F(2) = F(0) + F(1) = 2
      F(3) = F(1) + F(2) = 3
      F(4) = F(2) + F(3) = 5
      F(5) = F(3) + F(4) = 8
      ...


La première méthode est l'approche récursive traditionnelle (fonction fibo_r).
La seconde méthode n'utilise pas la récursion mais une boucle (fonction fibo_i).

On souhaite savoir laquelle est la plus rapide en temps processeur.

La première implémentation est garantie comme correcte pour tout nombre entier
positif.

1) Implémenter un test unitaire vérifiant pour tout nombre de la suite F()
jusqu'à F(n) > 23788 que la seconde fonction est correcte aussi. Quel est l'élément?

2) En utilisant la fonction timeit.timeit qui est faite pour mesurer la performance de 
code établir une comparaison de performance sur 1000 itérations entre la fonction fibo_i()
et la fonction fibo_r() jusqu'au nombre trouvé à l'exercice 1.

On testera en utilisant `pytest -rP exercice3.py`. Le test de performance pourra être
exécuté avec `python exercice3.py`.