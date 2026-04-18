# Analyse Exploratoire des Données Complète - Superstore Management System

## Vue d'ensemble du Dataset

- **Taille** : 1 000 commandes, 31 colonnes (après préparation)
- **Période** : Octobre 2023 - Octobre 2025
- **Qualité** : Aucune valeur manquante
- **Variables clés** :
  - Ventes totales : 12 737 842,60 €
  - Profit total : 3 186 464,74 €
  - Marge moyenne : 25,07 %
  - Taux de retours/annulations : 52,5 %

## Analyse Univariée

### Statistiques Numériques
| Variable | Moyenne | Écart-type | Min | Max | Médiane |
|----------|---------|------------|-----|-----|---------|
| Quantité | 5,46 | 2,82 | 1 | 10 | 5 |
| Prix unitaire | 2 555,57 € | 1 400,13 € | 102 € | 4 986 € | 2 546,50 € |
| Remise (%) | 10,20 % | 7,01 % | 0 % | 20 % | 10 % |
| Montant ventes | Variable | Variable | Variable | Variable | Variable |
| Profit | Variable | Variable | Variable | Variable | Variable |
| Délai livraison | 4,08 jours | 1,98 jours | 1 jour | 7 jours | 4 jours |
| Marge | 25,07 % | 9,00 % | 10 % | 40 % | 25,31 % |

### Fréquences Catégorielles
- **Segments** : Home Office (35,4%), Consumer (34,7%), Corporate (29,9%)
- **Catégories** : Furniture (26,4%), Grocery (25,2%), Electronics (24,4%), Office Supplies (24,0%)
- **Régions** : South (26,8%), North (26,2%), East (24,0%), West (23,0%)
- **Paiements** : UPI (26,3%), Net Banking (24,7%), Credit Card (24,7%), Cash (24,3%)
- **Livraisons** : Cancelled (26,3%), Returned (26,2%), Delivered (24,6%), Pending (22,9%)

## Analyse Bivariée

### Corrélations Fortes (|r| > 0,5)
1. **Montant ventes ↔ Coût** : 0,984 (très forte corrélation logique)
2. **Montant ventes ↔ Profit** : 0,877 (forte relation)
3. **Prix unitaire ↔ Montant ventes** : 0,695
4. **Quantité ↔ Montant ventes** : 0,665
5. **Prix unitaire ↔ Profit** : 0,615

### Insights Clés
- Le profit est fortement corrélé aux ventes et au prix unitaire
- Les remises n'ont pas d'impact significatif sur la marge
- Les délais de livraison n'affectent pas significativement les performances financières

## Analyse Temporelle

### Ventes Mensuelles (2023-2025)
- **Octobre 2023** : 104 569 €
- **Août 2024** : 664 944 € (pic mensuel)
- **Avril 2024** : 372 710 € (creux)

### Saisonnalité Moyenne par Mois
- **Août** : 13 357,88 € (pic)
- **Juin** : 14 040,88 € (meilleur mois)
- **Avril** : 11 459,99 € (moins bon mois)

## Analyse par Catégories

### Segments Clients
| Segment | Ventes Totales | Ventes Moyennes | Profit Moyen | Marge Moyenne |
|---------|----------------|-----------------|--------------|---------------|
| Home Office | 4 553 993,80 € | 12 864,39 € | 3 199,43 € | 25,00 % |
| Consumer | 4 321 851,25 € | 12 454,90 € | 3 130,14 € | 25,09 % |
| Corporate | 3 861 997,55 € | 12 916,38 € | 3 236,48 € | 25,00 % |

### Catégories Produits
| Catégorie | Ventes Totales | Ventes Moyennes | Profit Moyen | Marge Moyenne |
|-----------|----------------|-----------------|--------------|---------------|
| Electronics | 3 345 715,25 € | 13 711,95 € | 3 388,31 € | 24,71 % |
| Grocery | 3 282 944,65 € | 13 027,56 € | 3 357,30 € | 25,77 % |
| Office Supplies | 3 078 885,80 € | 12 828,69 € | 3 089,15 € | 24,08 % |
| Furniture | 3 030 296,90 € | 11 478,40 € | 2 925,32 € | 24,00 % |

### Régions Géographiques
| Région | Ventes Totales | Ventes Moyennes | Profit Moyen | Délai Moyen | Taux Risque |
|--------|----------------|-----------------|--------------|-------------|-------------|
| North | 3 462 624,00 € | 13 216,12 € | 3 342,06 € | 4,09 jours | 59,9 % |
| South | 3 355 359,20 € | 12 519,99 € | 3 099,50 € | 4,21 jours | 50,0 % |
| East | 3 134 608,55 € | 13 060,87 € | 3 227,37 € | 3,95 jours | 50,4 % |
| West | 2 785 250,85 € | 12 109,79 € | 3 011,59 € | 4,07 jours | 49,1 % |

## Détection des Valeurs Aberrantes

### Résumé des Outliers (méthode IQR)
- **Quantité** : 0 outliers (distribution normale)
- **Prix unitaire** : 0 outliers
- **Montant ventes** : 3 outliers (0,3 %) - valeurs élevées de 43 985 € à 45 500 €
- **Profit** : 34 outliers (3,4 %) - plage normale : -4 914 € à 10 601 €
- **Délai livraison** : 0 outliers

## Analyse des Risques

### Vue d'ensemble
- **Commandes à risque** : 525 (52,5 % du total)
- **Ventes perdues** : 6 678 166,05 €
- **Profit perdu** : 1 673 196,30 €

### Risques par Catégorie
| Catégorie | Commandes à Risque | Ventes Perd. | Taux Risque |
|-----------|-------------------|--------------|-------------|
| Grocery | 147 | 1 953 485,65 € | 58,3 % |
| Furniture | 130 | 1 513 690,70 € | 49,2 % |
| Office Supplies | 126 | 1 738 858,40 € | 52,5 % |
| Electronics | 122 | 1 472 131,30 € | 50,0 % |

### Risques par Région
| Région | Commandes à Risque | Ventes Perd. | Taux Risque |
|--------|-------------------|--------------|-------------|
| North | 157 | 1 895 410,60 € | 59,9 % |
| South | 134 | 1 687 669,50 € | 50,0 % |
| East | 121 | 1 781 751,30 € | 50,4 % |
| West | 113 | 1 313 334,65 € | 49,1 % |

## Insights et Recommandations

### Points Forts
1. **Qualité des données** : Dataset complet sans valeurs manquantes
2. **Performance Grocery** : Meilleure marge (25,77 %) et bonnes ventes
3. **Stabilité temporelle** : Pas de saisonnalité marquée, ventes régulières
4. **Corrélations logiques** : Relations cohérentes entre prix, quantité et ventes

### Points de Vigilance
1. **Taux de retours élevé** : 52,5 % des commandes sont annulées/retournées
2. **Région North** : Plus fort taux de risque (59,9 %)
3. **Catégorie Grocery** : Plus touchée par les retours (58,3 %)
4. **Outliers sur profit** : 3,4 % des profits sont aberrants

### Recommandations Opérationnelles
1. **Améliorer la qualité produit** : Focus sur Grocery et Furniture pour réduire retours
2. **Surveiller la région North** : Taux de risque le plus élevé
3. **Optimiser la logistique** : Délais moyens de 4 jours pourraient être réduits
4. **Analyser les outliers** : Comprendre pourquoi certains profits sont extrêmes

### Recommandations Commerciales
1. **Prioriser Electronics** : Bon volume et marge acceptable
2. **Développer Home Office** : Segment le plus rentable
3. **Réduire remises** : Impact limité sur les ventes
4. **Campagnes saisonnières** : Renforcer juin-août (pics de ventes)

---

*Analyse réalisée avec Python (pandas, numpy) - Script disponible : `eda_complete.py`*"