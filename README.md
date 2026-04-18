# Superstore Management System Data Analysis

Projet d'analyse de données pour le fichier `Superstore_Management_System.csv`.

## Contenu

- `analysis.py`: script générant un rapport Markdown enrichi avec segmentation, risques et recommandations métier.
- `data_analysis.py`: script d'analyse exploratoire pour sortie console.
- `streamlit_app.py`: tableau de bord interactif Streamlit.
- `report.md`: rapport généré automatiquement.
- `.gitignore`: exclusions pour le dépôt Git.
- `requirements.txt`: dépendances Python nécessaires.

## Installation

```bash
pip install -r requirements.txt
```

## Exécution

- Générer le rapport Markdown :
  ```bash
  python analysis.py
  ```

- Lancer l’analyse console :
  ```bash
  python data_analysis.py
  ```

- Démarrer le dashboard Streamlit :
  ```bash
  streamlit run streamlit_app.py
  ```

## Déploiement Streamlit

1. Publier le dépôt sur GitHub.
2. Connecter le dépôt à Streamlit Cloud.
3. Déployer `streamlit_app.py` depuis le repo.
