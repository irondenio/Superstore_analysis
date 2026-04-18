# Superstore Management System Data Analysis

Projet d'analyse de données pour le fichier `Superstore_Management_System.csv`.

## Contenu

- `analysis.py`: script générant un rapport Markdown enrichi avec segmentation, risques et recommandations métier.
- `data_analysis.py`: script d'analyse exploratoire pour sortie console.
- `eda_complete.py`: script d'Analyse Exploratoire des Données (EDA) complète avec analyses univariée, bivariée, temporelle, catégorielle, détection d'outliers et analyse des risques.
- `streamlit_app.py`: tableau de bord interactif Streamlit.
- `report.md`: rapport généré automatiquement.
- `EDA_Summary.md`: résumé complet de l'EDA avec tous les insights clés.
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

- Effectuer l'EDA complète :
  ```bash
  python eda_complete.py
  ```

- Démarrer le dashboard Streamlit :
  ```bash
  streamlit run streamlit_app.py
  ```

## Résumé de l'EDA

Consultez `EDA_Summary.md` pour un résumé complet de l'analyse exploratoire incluant :
- Statistiques descriptives
- Analyses de corrélation
- Segmentation par catégories
- Détection d'outliers
- Analyse des risques
- Recommandations opérationnelles et commerciales

## Déploiement Streamlit

### Option 1 : Déploiement Automatique (Recommandé)

1. **Publier le dépôt sur GitHub** :
   - Le dépôt est déjà sur : `https://github.com/irondenio/Superstore_analysis.git`

2. **Se connecter à Streamlit Cloud** :
   - Aller sur [https://share.streamlit.io](https://share.streamlit.io)
   - Se connecter avec votre compte GitHub

3. **Déployer l'application** :
   - Cliquer sur "New app"
   - Sélectionner le repository `irondenio/Superstore_analysis`
   - Branch : `master`
   - Main file path : `streamlit_app.py`
   - Cliquer sur "Deploy"

4. **Configuration avancée** (optionnel) :
   - Dans le repo, créer un fichier `packages.txt` si besoin de dépendances système
   - Le `requirements.txt` est automatiquement détecté

### Option 2 : Déploiement Local avec Streamlit Sharing

```bash
# Installation des dépendances
pip install -r requirements.txt

# Test local
streamlit run streamlit_app.py

# Pour le déploiement, pousser sur GitHub puis utiliser Streamlit Cloud
```

### Option 3 : Déploiement avec Docker (Avancé)

Créer un `Dockerfile` :
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Vérification du Déploiement

Après déploiement, l'application sera accessible via une URL comme :
`https://superstoreanalyse.streamlit.app/`

### Dépannage

- **Erreur de dépendances** : Vérifier que `requirements.txt` contient toutes les dépendances
- **Erreur de données** : S'assurer que `Superstore_Management_System.csv` est dans le repo
- **Timeout** : Les apps gratuites peuvent avoir des limites de ressources

### Fonctionnalités du Dashboard

- Résumé général avec métriques clés
- Analyse multi-dimensionnelle (segments, catégories, régions)
- Segmentation granulaire interactive
- Recommandations métier par région
- Exploration des données brutes
