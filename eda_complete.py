import pandas as pd
import numpy as np
from pathlib import Path

# Configuration
ROOT = Path(__file__).parent
CSV = ROOT / 'Superstore_Management_System.csv'

def load_and_prepare_data():
    """Charge et prépare les données pour l'EDA"""
    df = pd.read_csv(CSV, encoding='utf-8', low_memory=False)

    # Conversion des dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

    # Calculs dérivés
    df['Ship Delay Days'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Margin Rate'] = df['Profit'].div(df['Sales Amount'], fill_value=0)
    df['Discount Rate'] = df['Discount (%)'] / 100
    df['Cancelled/Returned'] = df['Delivery Status'].str.lower().isin(['cancelled', 'returned'])

    # Mois et année pour analyse temporelle
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Year'] = df['Order Date'].dt.year

    return df

def univariate_analysis(df):
    """Analyse univariée : statistiques descriptives et distributions"""
    print("=" * 60)
    print("ANALYSE UNIVARIÉE")
    print("=" * 60)

    # Statistiques numériques
    numeric_cols = ['Quantity', 'Unit Price', 'Discount (%)', 'Sales Amount', 'Cost Price',
                   'Profit', 'Ship Delay Days', 'Margin Rate']

    print("\nStatistiques descriptives des variables numériques :")
    print(df[numeric_cols].describe().round(2))

    # Statistiques catégorielles
    categorical_cols = ['Customer Segment', 'Category', 'Region', 'State', 'Payment Mode', 'Delivery Status']

    print("\nFréquences des variables catégorielles :")
    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts().head(10))

    # Valeurs manquantes
    print("\nValeurs manquantes :")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    missing_df = pd.DataFrame({'Count': missing, 'Percentage': missing_pct})
    print(missing_df[missing_df['Count'] > 0])

def bivariate_analysis(df):
    """Analyse bivariée : corrélations et relations"""
    print("\n" + "=" * 60)
    print("ANALYSE BIVARIÉE")
    print("=" * 60)

    # Matrice de corrélation
    numeric_cols = ['Quantity', 'Unit Price', 'Discount (%)', 'Sales Amount', 'Cost Price',
                   'Profit', 'Ship Delay Days', 'Margin Rate']

    corr_matrix = df[numeric_cols].corr().round(3)
    print("\nMatrice de corrélation :")
    print(corr_matrix)

    # Corrélations fortes
    print("\nCorrélations fortes (|r| > 0.5) :")
    strong_corr = corr_matrix.where(np.triu(np.ones_like(corr_matrix), k=1).astype(bool))
    strong_corr = strong_corr.stack().reset_index()
    strong_corr.columns = ['Variable 1', 'Variable 2', 'Correlation']
    strong_corr = strong_corr[abs(strong_corr['Correlation']) > 0.5].sort_values('Correlation', ascending=False)
    print(strong_corr)

def temporal_analysis(df):
    """Analyse temporelle"""
    print("\n" + "=" * 60)
    print("ANALYSE TEMPORELLE")
    print("=" * 60)

    # Évolution mensuelle des ventes
    monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales Amount'].sum().reset_index()

    print("\nVentes mensuelles :")
    print(monthly_sales.head(12))

    # Saisonnalité par mois
    monthly_avg = df.groupby('Order Month')['Sales Amount'].mean().round(2)
    print("\nMoyenne des ventes par mois :")
    print(monthly_avg)

def categorical_analysis(df):
    """Analyse des variables catégorielles"""
    print("\n" + "=" * 60)
    print("ANALYSE DES CATÉGORIES")
    print("=" * 60)

    # Analyse par segment
    segment_analysis = df.groupby('Customer Segment').agg({
        'Sales Amount': ['sum', 'mean', 'count'],
        'Profit': ['sum', 'mean'],
        'Margin Rate': 'mean',
        'Discount (%)': 'mean'
    }).round(2)
    print("\nAnalyse par segment client :")
    print(segment_analysis)

    # Analyse par catégorie
    category_analysis = df.groupby('Category').agg({
        'Sales Amount': ['sum', 'mean', 'count'],
        'Profit': ['sum', 'mean'],
        'Margin Rate': 'mean',
        'Discount (%)': 'mean'
    }).round(2)
    print("\nAnalyse par catégorie :")
    print(category_analysis)

    # Analyse par région
    region_analysis = df.groupby('Region').agg({
        'Sales Amount': ['sum', 'mean', 'count'],
        'Profit': ['sum', 'mean'],
        'Ship Delay Days': 'mean',
        'Cancelled/Returned': 'mean'
    }).round(3)
    print("\nAnalyse par région :")
    print(region_analysis)

def outlier_detection(df):
    """Détection des valeurs aberrantes"""
    print("\n" + "=" * 60)
    print("DÉTECTION DES VALEURS ABERRANTES")
    print("=" * 60)

    numeric_cols = ['Quantity', 'Unit Price', 'Sales Amount', 'Profit', 'Ship Delay Days']

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_count = len(outliers)

        print(f"\n{col}:")
        print(f"  - Valeurs aberrantes: {outlier_count} ({outlier_count/len(df)*100:.1f}%)")
        if outlier_count > 0:
            print(f"  - Plage normale: [{lower_bound:.2f}, {upper_bound:.2f}]")
            print(f"  - Min/Max aberrants: {outliers[col].min():.2f} / {outliers[col].max():.2f}")

def risk_analysis(df):
    """Analyse des risques"""
    print("\n" + "=" * 60)
    print("ANALYSE DES RISQUES")
    print("=" * 60)

    # Analyse des retours/annulations
    risk_df = df[df['Cancelled/Returned']].copy()

    print(f"\nCommandes à risque: {len(risk_df)} ({len(risk_df)/len(df)*100:.1f}%)")
    print(f"Ventes perdues: {risk_df['Sales Amount'].sum():,.2f} €")
    print(f"Profit perdu: {risk_df['Profit'].sum():,.2f} €")

    # Risques par catégorie
    risk_by_category = risk_df.groupby('Category').agg({
        'Order ID': 'count',
        'Sales Amount': 'sum'
    }).sort_values('Order ID', ascending=False)
    risk_by_category['Risk Rate'] = risk_by_category['Order ID'] / df.groupby('Category')['Order ID'].count()
    risk_by_category['Risk Rate'] = risk_by_category['Risk Rate'].round(3)

    print("\nRisques par catégorie :")
    print(risk_by_category)

    # Risques par région
    risk_by_region = risk_df.groupby('Region').agg({
        'Order ID': 'count',
        'Sales Amount': 'sum'
    }).sort_values('Order ID', ascending=False)
    risk_by_region['Risk Rate'] = risk_by_region['Order ID'] / df.groupby('Region')['Order ID'].count()
    risk_by_region['Risk Rate'] = risk_by_region['Risk Rate'].round(3)

    print("\nRisques par région :")
    print(risk_by_region)

def create_visualizations(df):
    """Création de visualisations (non disponible sans matplotlib)"""
    print("\nVisualisations non générées (matplotlib non installé)")
    print("Pour des graphiques, installez matplotlib et seaborn : pip install matplotlib seaborn")

def main():
    """Fonction principale"""
    print("EXPLORATORY DATA ANALYSIS - Superstore Management System")
    print("=" * 60)

    # Chargement des données
    df = load_and_prepare_data()
    print(f"Dataset chargé: {len(df)} lignes, {len(df.columns)} colonnes")

    # Analyses
    univariate_analysis(df)
    bivariate_analysis(df)
    temporal_analysis(df)
    categorical_analysis(df)
    outlier_detection(df)
    risk_analysis(df)
    create_visualizations(df)

    print("\n" + "=" * 60)
    print("EDA TERMINÉE")
    print("=" * 60)

if __name__ == "__main__":
    main()