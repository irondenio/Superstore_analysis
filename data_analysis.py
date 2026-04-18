import os
import pandas as pd

FILE = "Superstore_Management_System.csv"


def load_data(path):
    df = pd.read_csv(path, low_memory=False)
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")
    df["Ship Delay Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df["Margin Rate"] = df["Profit"] / df["Sales Amount"]
    return df


def summarize(df):
    print("DATASET SUMMARY")
    print("===============")
    print(f"Total lignes: {len(df):,}")
    print(f"Total colonnes: {len(df.columns)}")
    print("Date minimale de commande:", df["Order Date"].min())
    print("Date maximale de commande:", df["Order Date"].max())
    print("Plage de livraison (jours):", df["Ship Delay Days"].min(), "à", df["Ship Delay Days"].max())
    print("Valeur totale des ventes:", f"{df['Sales Amount'].sum():,.2f}")
    print("Profit total:", f"{df['Profit'].sum():,.2f}")
    print("Marge moyenne:", f"{df['Margin Rate'].mean():.2%}")
    print("Taux de marge médian:", f"{df['Margin Rate'].median():.2%}")
    print()

    print("TOP 5 SEGMENTS")
    print(df.groupby("Customer Segment")["Sales Amount"].sum().sort_values(ascending=False).head(5).to_string())
    print()

    print("TOP 5 CATEGORIES")
    print(df.groupby("Category")["Sales Amount"].sum().sort_values(ascending=False).head(5).to_string())
    print()

    print("TOP 5 REGIONS")
    print(df.groupby("Region")["Sales Amount"].sum().sort_values(ascending=False).head(5).to_string())
    print()

    print("STATUTS DE LIVRAISON")
    print(df["Delivery Status"].value_counts().to_string())
    print()

    returns = df[df["Delivery Status"].str.lower().isin(["returned", "cancelled"])].copy()
    print("COMMANDES RETOURNÉES/ANNULÉES")
    print(f"Nombre: {len(returns)}")
    print(f"Part des commandes: {len(returns)/len(df):.2%}")
    print(f"Impact sur les ventes: {returns['Sales Amount'].sum():,.2f}")
    print(f"Impact sur le profit: {returns['Profit'].sum():,.2f}")
    print()

    print("TOP 10 PRODUITS PAR VENTES")
    print(df.groupby(["Product ID", "Product Name"])["Sales Amount"].sum().sort_values(ascending=False).head(10).to_string())
    print()

    print("TOP 10 PRODUITS PAR PROFIT")
    print(df.groupby(["Product ID", "Product Name"])["Profit"].sum().sort_values(ascending=False).head(10).to_string())
    print()

    print("TOP 10 ÉTATS PAR VENTES")
    print(df.groupby("State")["Sales Amount"].sum().sort_values(ascending=False).head(10).to_string())
    print()

    reorder = df[df["Auto Reorder"].str.lower() == "yes"]
    print("COMMANDES AVEC AUTO REORDER")
    print(f"Nombre: {len(reorder)}")
    print(f"Contribution aux ventes: {reorder['Sales Amount'].sum():,.2f}")
    print(f"Contribution au profit: {reorder['Profit'].sum():,.2f}")
    print()

    print("DÉLAIS DE LIVRAISON")
    print(df["Ship Delay Days"].describe().to_string())
    print()

    print("DISTANCE DE REMISE")
    print(df["Discount (%)"].describe().to_string())
    print()

    print("TOP 5 MÉTHODES DE PAIEMENT")
    print(df.groupby("Payment Mode")["Sales Amount"].sum().sort_values(ascending=False).to_string())
    print()


if __name__ == "__main__":

    path = os.path.join(os.path.dirname(__file__), FILE)
    df = load_data(path)
    summarize(df)
