# TP_note_Tests

## Installation
après avoir cloné le projet, il faut installer les dépendances avec la commande suivante:
```bash
make venv
```

## Utilisation
Pour lancer les tests, il faut activer l'environnement virtuel avec la commande suivante:
```bash
source .venv/bin/activate
```

Pour tester chaque exercice, il faut faire:
```bash
cd exo{nb} # remplacer {nb} par le numéro de l'exercice
```

Pour lancer les tests, il faut faire:
```bash
pytest . | tee test-report.txt
```

Pour avoir un rapport de couverture, il faut faire:
```bash
coverage run -m pytest .;coverage report -m | tee coverage.txt
```