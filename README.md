# Vestiaire RM2

Appli de l'équipe RM2 : calendrier des matchs, courses d'après-match, lavage des maillots et covoiturage.

- `app/vestiaire-rm2.html` : source de l'appli (publiée aussi comme Artifact Claude).
- `index.html` : site public (GitHub Pages), généré par `python3 build.py`.
- `firebase-config.json` : config web Firebase (base de données partagée de l'équipe).
- `firestore.rules` : règles de sécurité à coller dans la console Firebase.

## Mettre à jour le site

```bash
python3 build.py && git add -A && git commit -m "Mise à jour" && git push
```
