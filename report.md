# Analyse des données Superstore Management System

## Résumé global
- **Total orders**: 1000
- **Period start**: 2023-10-24
- **Period end**: 2025-10-23
- **Total sales**: 12,737,842.60
- **Total cost**: 9,551,377.86
- **Total profit**: 3,186,464.74
- **Average order quantity**: 5.46
- **Average unit price**: 2,555.57
- **Average discount %**: 10.20
- **Average shipping delay (days)**: 4.08
- **Cancelled rate**: 0.26
- **Returned rate**: 0.26
- **Pending rate**: 0.23

## Top 3 segments
                  orders       sales      profit  avg_discount
Customer Segment                                              
Home Office          354  4553993.80  1132599.52     10.395480
Consumer             347  4321851.25  1086157.19      9.971182
Corporate            299  3861997.55   967708.03     10.234114

## Top 3 catégories
                 orders       sales     profit  avg_margin
Category                                                  
Electronics         244  3345715.25  826746.52    0.247106
Grocery             252  3282944.65  846039.25    0.257707
Office Supplies     240  3078885.80  741395.77    0.240800

## Top 3 régions
        orders       sales     profit  avg_delay
Region                                          
North      262  3462624.00  874618.16   4.087786
South      268  3355359.20  824210.75   4.212687
East       240  3134608.55  776484.98   3.950000

## État des livraisons
                 orders       sales     profit
Delivery Status                               
Cancelled           263  3246639.90  822424.11
Returned            262  3431526.15  850772.19
Delivered           246  3030683.20  739037.28
Pending             229  3028993.35  774231.16

## Meilleurs produits par chiffre d'affaires
              orders      sales     profit
Product Name                              
Stapler           53  803632.70  205798.86
Rice Bag          62  792718.05  207134.18
Snacks            54  762495.00  200575.25
Monitor           54  739203.85  194597.30
Sugar             51  719827.55  179204.17
Dining Table      65  709434.70  176424.84
Headphones        52  705447.60  168894.25
Pen               52  680178.05  151977.86
Mouse             39  670733.35  165259.93
Office Chair      47  663710.55  169570.62

## Meilleurs clients par chiffre d'affaires
                  orders    sales    profit
Customer Name                              
Alan Sanders           1  45500.0   4950.90
Andrea Anderson        1  44559.0   5630.35
Sarah Williams         2  44124.8  12397.29
Erin Benton            1  43985.0  12117.29
Chad Knox              1  42579.0   4866.91
Daniel Bryant          1  42021.0  10920.87
Shane Murphy           1  41923.5   6293.26
David Perez            1  41496.0  14364.39
Miranda Williams       1  41463.0  12513.24
Judy Jordan            1  41184.0  10176.89

## Flotte de réapprovisionnement (stock ≤ 10)
     Product Name              Supplier Name  Stock Left Auto Reorder  Reorder Quantity
671    Headphones              Hernandez Ltd           0          Yes                41
893    Juice Pack     Jones, Castro and Cook           0          Yes                30
446         Mouse                Kelly-Blake           0          Yes                30
31    Cooking Oil             Watts-Mcdonald           0          Yes                34
276    Juice Pack             Lloyd and Sons           0          Yes                27
23   Dining Table  Saunders, Sims and Miller           0          Yes                39
193           Pen                Perkins Inc           0          Yes                44
385   Study Table           Clements-Watkins           0          Yes                50
563  Dining Table             Haynes-Collins           0          Yes                34
134     Bookshelf    Dunn, Parrish and Drake           0          Yes                49
162      Rice Bag             Hodges-Benitez           0          Yes                40
577    Headphones               Daniels-Bell           0          Yes                48
450  Dining Table             Griffin-Weaver           0          Yes                27
760      Rice Bag            Chavez and Sons           0          Yes                21
500   Study Table                 Nelson Ltd           0          Yes                36
967          Sofa   Combs, Sutton and Porter           0          Yes                24
959      Keyboard            Alvarez-Lindsey           0          Yes                42
332        Laptop           Chandler-Schultz           0          Yes                29
177    Headphones  Lamb, Tucker and Williams           0          Yes                47
187  Office Chair               Clark-Meyers           0          Yes                27

## Remarques clés
- Le jeu de données contient **1000 commandes** sans valeurs manquantes détectées.
- Le total des ventes est de **12,737,842.60** avec une marge brute de **3,186,464.74**.
- Le segment le plus important par chiffre d'affaires est probablement en tête du tableau par segment.
- Les statuts `Cancelled` et `Returned` doivent être surveillés : ces ordres représentent des risques de trésorerie et de satisfaction client.
- Plusieurs références sont en stock critique (≤10), ce qui nécessite un plan de réapprovisionnement prioritaire.
