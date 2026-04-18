import pandas as pd
from pathlib import Path

ROOT = Path(__file__).parent
CSV = ROOT / 'Superstore_Management_System.csv'
REPORT = ROOT / 'report.md'

# Load and clean
if not CSV.exists():
    raise FileNotFoundError(f'{CSV} is missing')

df = pd.read_csv(CSV, encoding='utf-8', low_memory=False)

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

df['Shipping Delay Days'] = (df['Ship Date'] - df['Order Date']).dt.days

df['Discount Rate'] = df['Discount (%)'] / 100.0
df['Cancelled/Returned'] = df['Delivery Status'].isin(['Cancelled', 'Returned'])

# Segment and category aggregated metrics
summary = {
    'Total orders': len(df),
    'Period start': df['Order Date'].min(),
    'Period end': df['Order Date'].max(),
    'Total sales': df['Sales Amount'].sum(),
    'Total cost': df['Cost Price'].sum(),
    'Total profit': df['Profit'].sum(),
    'Average order quantity': df['Quantity'].mean(),
    'Average unit price': df['Unit Price'].mean(),
    'Average discount %': df['Discount (%)'].mean(),
    'Average shipping delay (days)': df['Shipping Delay Days'].mean(),
    'Cancelled rate': (df['Delivery Status'] == 'Cancelled').mean(),
    'Returned rate': (df['Delivery Status'] == 'Returned').mean(),
    'Pending rate': (df['Delivery Status'] == 'Pending').mean(),
}

by_segment = df.groupby('Customer Segment').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
    avg_discount=('Discount (%)', 'mean'),
).sort_values('sales', ascending=False)

by_category = df.groupby('Category').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
)
by_category['avg_margin'] = by_category['profit'] / by_category['sales']
by_category = by_category.sort_values('sales', ascending=False)

by_region = df.groupby('Region').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
    avg_delay=('Shipping Delay Days', 'mean'),
).sort_values('sales', ascending=False)

by_payment = df.groupby('Payment Mode').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
).sort_values('orders', ascending=False)

by_delivery = df.groupby('Delivery Status').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
).sort_values('orders', ascending=False)

# Leaders and risk areas
best_products = df.groupby('Product Name').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
).sort_values('sales', ascending=False).head(10)

best_customers = df.groupby('Customer Name').agg(
    orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
).sort_values('sales', ascending=False).head(10)

low_stock = df[df['Stock Left'] <= 10].copy().sort_values(['Stock Left', 'Sales Amount'])

risk_orders = df[df['Delivery Status'].isin(['Cancelled', 'Returned'])].copy()

# Fine segmentation and recommendations
region_risk = df.groupby('Region').agg(
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
    orders=('Order ID', 'count'),
    risk_orders=('Cancelled/Returned', 'sum')
)
region_risk['risk_rate'] = region_risk['risk_orders'] / region_risk['orders']
region_risk = region_risk.sort_values('risk_rate', ascending=False)

category_margin = by_category[['sales', 'profit', 'avg_margin']].sort_values('avg_margin')
category_risk = df[df['Cancelled/Returned']].groupby('Category').agg(
    risk_orders=('Order ID', 'count'),
    sales=('Sales Amount', 'sum')
).sort_values('risk_orders', ascending=False)

product_performance = df.groupby('Product Name').agg(
    sales=('Sales Amount', 'sum'),
    profit=('Profit', 'sum'),
    orders=('Order ID', 'count')
)
product_performance['avg_margin'] = product_performance['profit'] / product_performance['sales']
product_rebalance = product_performance.sort_values(['sales', 'avg_margin'], ascending=[False, True]).head(10)

# Create report markdown
with REPORT.open('w', encoding='utf-8') as f:
    f.write('# Analyse des données Superstore Management System\n\n')
    f.write('## Résumé global\n')
    for k, v in summary.items():
        if isinstance(v, pd.Timestamp):
            v = v.date().isoformat()
        elif isinstance(v, float):
            v = f'{v:,.2f}'
        f.write(f'- **{k}**: {v}\n')
    f.write('\n## Top 3 segments\n')
    f.write(by_segment.head(3).to_string() + '\n\n')
    f.write('## Top 3 catégories\n')
    f.write(by_category.head(3).to_string() + '\n\n')
    f.write('## Top 3 régions\n')
    f.write(by_region.head(3).to_string() + '\n\n')
    f.write('## État des livraisons\n')
    f.write(by_delivery.to_string() + '\n\n')
    f.write('## Meilleurs produits par chiffre d\'affaires\n')
    f.write(best_products.to_string() + '\n\n')
    f.write('## Meilleurs clients par chiffre d\'affaires\n')
    f.write(best_customers.to_string() + '\n\n')
    f.write('## Flotte de réapprovisionnement (stock ≤ 10)\n')
    f.write(low_stock[['Product Name','Supplier Name','Stock Left','Auto Reorder','Reorder Quantity']].head(20).to_string() + '\n\n')
    f.write('## Segmentation régionale détaillée\n')
    f.write(region_risk.to_string() + '\n\n')
    f.write('## Catégories à faible marge\n')
    f.write(category_margin.head(5).to_string() + '\n\n')
    f.write('## Catégories à risque élevé (annulations / retours)\n')
    f.write(category_risk.head(5).to_string() + '\n\n')
    f.write('## Produits à fort volume mais marge faible\n')
    f.write(product_rebalance.to_string() + '\n\n')
    f.write('## Recommandations métier\n')
    f.write('- Prioriser les campagnes commerciales dans les régions à fort risque de retours, notamment : **' + ', '.join(region_risk.head(3).index.tolist()) + '**.\n')
    f.write('- Suivre de près les catégories à faible marge : **' + ', '.join(category_margin.head(3).index.tolist()) + '**.\n')
    f.write('- Renforcer la tarification et les promotions pour les produits à fort volume / faible marge : **' + ', '.join(product_rebalance.head(5).index.tolist()) + '**.\n')
    f.write('- Déployer un plan de réapprovisionnement prioritaire pour les références critiques en stock.\n')
    f.write('- Améliorer le suivi logistique sur les régions où le taux d\'annulation / retour est le plus élevé.\n')

print('Report generated in', REPORT)
print('Top 3 segments:')
print(by_segment.head(3))
print('Top 3 categories:')
print(by_category.head(3))
print('Top 3 regions:')
print(by_region.head(3))
print('Top 10 products:')
print(best_products)
print('Top 10 customers:')
print(best_customers)
print('Orders with Cancelled or Returned:', len(risk_orders))
print('Low stock rows (<=10):', len(low_stock))
