import os
import pandas as pd
import streamlit as st

FILE = "Superstore_Management_System.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, low_memory=False)
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")
    df["Ship Delay Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df["Margin Rate"] = df["Profit"].div(df["Sales Amount"], fill_value=0)
    df["Discount Rate"] = df["Discount (%)"] / 100
    df["Cancelled/Returned"] = df["Delivery Status"].str.lower().isin(["cancelled", "returned"])
    return df


def region_recommendations(region_df):
    low_margin = region_df.groupby("Category")["Margin Rate"].mean().sort_values().head(3)
    high_risk = region_df[region_df["Cancelled/Returned"]].groupby("Category")["Order ID"].count().sort_values(ascending=False).head(3)
    return low_margin, high_risk


def product_recommendations(df):
    top_sales = df.groupby("Product Name")["Sales Amount"].sum().sort_values(ascending=False).head(5)
    low_margin_high_sales = df.groupby("Product Name").agg(
        sales=("Sales Amount", "sum"),
        profit=("Profit", "sum"),
        orders=("Order ID", "count"),
    )
    low_margin_high_sales["margin"] = low_margin_high_sales["profit"] / low_margin_high_sales["sales"]
    low_margin_high_sales = low_margin_high_sales.sort_values(["sales", "margin"], ascending=[False, True]).head(5)
    return top_sales, low_margin_high_sales


def main():
    st.title("Analyse des ventes Superstore")
    st.markdown(
        "Dashboard interactif enrichi avec segmentation régionale, analyse produit, performance commerciale et recommandations métier."
    )

    path = os.path.join(os.path.dirname(__file__), FILE)
    df = load_data(path)

    st.header("Résumé général")
    col1, col2, col3 = st.columns(3)
    col1.metric("Commandes", f"{len(df):,}")
    col2.metric("Ventes totales", f"{df['Sales Amount'].sum():,.0f}")
    col3.metric("Profit total", f"{df['Profit'].sum():,.0f}")

    min_date = df["Order Date"].min()
    max_date = df["Order Date"].max()
    min_date_str = min_date.date().isoformat() if pd.notna(min_date) else "N/A"
    max_date_str = max_date.date().isoformat() if pd.notna(max_date) else "N/A"
    st.markdown(
        f"- Période : **{min_date_str}** à **{max_date_str}**\n"
        f"- Marge moyenne : **{df['Margin Rate'].mean():.2%}**\n"
        f"- Taux de retours/annulations : **{df['Cancelled/Returned'].mean():.2%}**"
    )

    st.header("Analyse multi-dimensionnelle")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ventes par segment")
        segment_sales = df.groupby("Customer Segment")["Sales Amount"].sum().sort_values(ascending=False)
        st.bar_chart(segment_sales)
    with col2:
        st.subheader("Profit par catégorie")
        category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
        st.bar_chart(category_profit)

    st.subheader("Régions : ventes, profit et risque")
    region_metrics = df.groupby("Region").agg(
        sales=("Sales Amount", "sum"),
        profit=("Profit", "sum"),
        risk_orders=("Cancelled/Returned", "sum"),
        orders=("Order ID", "count"),
    )
    region_metrics["risk_rate"] = region_metrics["risk_orders"] / region_metrics["orders"]
    st.dataframe(region_metrics.style.format({"sales": "{:,.0f}", "profit": "{:,.0f}", "risk_rate": "{:.2%}"}))
    st.bar_chart(region_metrics["sales"])
    st.bar_chart(region_metrics["risk_rate"])

    st.subheader("Variations produit")
    top_products = df.groupby("Product Name")["Sales Amount"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_products)

    st.subheader("Produits à fort volume / faible marge")
    _, low_margin_high_sales = product_recommendations(df)
    st.dataframe(low_margin_high_sales)

    st.header("Segmentation granulaire")
    seg_cols = ["Customer Segment", "Category", "Region", "Payment Mode", "Delivery Status"]
    dimension = st.selectbox("Dimension de segmentation", seg_cols)
    metric = st.selectbox("Métrique", ["Sales Amount", "Profit", "Margin Rate", "Ship Delay Days"])
    st.dataframe(
        df.groupby(dimension)[metric].agg(["sum", "mean", "count"]).sort_values(by="sum", ascending=False)
    )

    st.header("Recommandations métier")
    selected_region = st.selectbox("Choisir une région", sorted(df["Region"].unique()))
    region_df = df[df["Region"] == selected_region]
    low_margin, high_risk = region_recommendations(region_df)
    st.subheader(f"Région : {selected_region}")
    st.markdown(
        f"- Catégories à faible marge dans {selected_region} : **{', '.join(low_margin.index.tolist())}**  \n"
        f"- Catégories à risque élevé "
        f"(annulations/retours) : **{', '.join(high_risk.index.tolist())}**"
    )

    st.subheader("Recommandations produit")
    top_sales, low_margin_high_sales = product_recommendations(df)
    st.markdown(
        "- Produits à prioriser pour l’accroissement du chiffre d’affaires : **" + 
        ", ".join(top_sales.index.tolist()) + "**  \n"
        "- Produits à réviser en prix ou marketing en raison d’un fort volume mais faible marge : **" + 
        ", ".join(low_margin_high_sales.index.tolist()) + "**"
    )

    st.subheader("Livraisons et délais")
    st.write(df["Ship Delay Days"].describe())
    st.bar_chart(df["Ship Delay Days"].value_counts().sort_index())

    if st.checkbox("Voir les 20 premières lignes de données"):
        st.dataframe(df.head(20))


if __name__ == "__main__":
    main()
