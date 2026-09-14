import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('Venky.py.csv')
print(df)
# Variables & Keywords
print('Variables & Keywords')
city= 'Dublin'
print(city)
my_quantity = 35
print(type(my_quantity))
my_revenue= 4578.75
print(type(my_revenue))
distributor= "Apex Pharma"
print(type(distributor))
a= "200"
print(type(a))
# Lists
print('Lists')
regions= ["Dublin", "Cork", "Gaiway", "Dublin", "Limerick"]
quantities= [120, 210, 175, 145, 260]
print(regions)
print(quantities)
print(sum(quantities))
dubli_count = regions.count("Dublin")
print("How many orders came from dublin")
print(dubli_count)
print(min(quantities))
regions.append("Galway")
print(regions)
# Tuples
print('Tuples')
products = tuple(df["Product"])
print(products)
total_items = len(products)
print(total_items)
unique_products = set(products)
print(unique_products)
from collections import Counter
product_count = Counter(products)
print(product_count)
quantities = tuple(df["Quantity"])
smallest_sale = min(quantities)
print(smallest_sale)
largest_sale = max(quantities)
print(largest_sale)
print(df.columns)
revenue = tuple(df["Revenue_EUR"])
total_revenue = sum(revenue)
print(total_revenue)
regions = tuple(df["Region"])
sorted_regions = sorted(set(regions))
print(sorted_regions)
# Sets
print('Sets')
unique_products = set(df["Product"])
print(unique_products)
unique_regions = set(df["Region"])
print(unique_regions)
unique_genders = set(df["Gender"])
print(unique_genders)
unique_therapy = set(df["Therapeutic_Area"])
print(unique_therapy)
unique_distributors = set(df["Distributor"])
print(unique_distributors)
count_unique = len(set(df["Product"]))
print(count_unique)
sorted_set_regions = sorted(set(df["Region"]))
print(sorted_set_regions)
has_vaccine = "Flu Vaccine" in set(df["Product"])
print(has_vaccine)
# Distionary
print('Dictionary')
product_prices = {"Insulin": 11.4, "Flu Vaccine" : 6.2}
print(product_prices)
# Extract Keys
all_products = product_prices.keys()
print(all_products)
# Values
all_prices = product_prices.values()
print(all_prices)
# Pairs
for product, price in product_prices.items():
 print(f"{product} costs €{price}")
 # Safe Fetching
 price = product_prices.get("Insulin", 0)
 print(price)
 has_asthma = "Asthma" in product_prices
print(has_asthma)

has_insulin = "Insulin" in product_prices
print(has_insulin)
# Loops & Iteration
print('Loops & Iteration')
regions= ["Dublin", "Cork", "Gaiway", "Dublin", "Limerick"]
for region in regions :
 print(f"Checking distribution center in :{region}")
 for i in range(3):
  print(f"Record{i+1}: {region [i]}")
  for index, text in enumerate(region, start=1):
   print(f"Serial No{index} -> Character: {text}")

# Functions
print('Functions')
def show_region(name):
       print(f"Selected Region is: {name}")
       def print_all_regions(any_list):
        for place in any_list:
         print(f"Target Location -> {place}")
       def count_dublin(any_list):
        counter = 0
       for place in any_list:
        if place == "Dublin":
            counter = counter + 1
class Medicine:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price
# Object -Oriented Programming System
print('object-Oriented Programming System')
# First row from your CSV
medicine1 = Medicine( "HSE Generic Medicines", 120, 18.5)
print("Product:", medicine1.product)
print("Quantity:", medicine1.quantity)
print("Price:", medicine1.price)
print("Total:", medicine1.total())
# Numpy
print('numpy')
import numpy as np
quantity = np.array([120, 210, 175, 145, 260])
print(quantity)
print("Total:", np.sum(quantity))
print("Average:", np.mean(quantity))
print("Maximum:", np.max(quantity))
print("Minimum:", np.min(quantity))
# Pandas
print('Pandas')
import pandas as pd
df = pd.read_csv("Venky.py.csv")
print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.tail)
print(df.tail(3))
print(df.info())
print(df.describe())
df["Revenue_EUR"]
print(df["Quantity"])
print(df["Product"])
print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[0, 0:3])
print(df.iloc[0:5, 0:3])
print(df.loc[0])
print(df.loc[0, "Product"])
print(df.loc[0:4, "Product"])
df2 = pd.DataFrame({'Region': ['Dublin', 'Cork', 'Galway', 'Limerick'],'Manager': ['John', 'David', 'Sarah', 'Mike']})
inner_join = pd.merge( df,df2, on='Region',how='inner')
print(inner_join)
left_join = pd.merge( df,df2, on='Region',how='left')
print(left_join)
right_join = pd.merge( df,df2, on='Region',how='right')
print(right_join)
outer_join = pd.merge( df,df2, on='Region',how='outer')
print(outer_join)
# Data Visualization
print('Data Visualization')
region_revenue = df.groupby("Region")["Revenue_EUR"].sum()
print(region_revenue)
import matplotlib.pyplot as plt
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (€)")
plt.show()
product_revenue = df.groupby("Product")["Revenue_EUR"].sum()
product_revenue = product_revenue.sort_values(ascending=False)
print(product_revenue)
product_revenue = product_revenue.sort_values()
product_revenue.plot(kind="barh")
plt.title("Revenue by Product")
plt.xlabel("Revenue (€)")
plt.ylabel("Product")
product_revenue = product_revenue.sort_values()
product_revenue.plot(kind="barh")
plt.title("Revenue by Product")
plt.xlabel("Revenue (€)")
plt.ylabel("Product")
plt.savefig("region_revenue.png")
region_revenue.plot(kind="line", marker="o")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (€)")
plt.show()
customer_revenue = df.groupby("Customer_Type")["Revenue_EUR"].sum()
print(customer_revenue)
customer_revenue.plot(  kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution by Customer Type")
plt.ylabel("")
plt.show()
df["Revenue_EUR"].plot(kind="hist", bins=10)
plt.title("Distribution of Revenue")
plt.xlabel("Revenue (€)")
plt.ylabel("Frequency")
plt.show()
# Matplotlib
print('Matplotlib')
import seaborn as sns
import matplotlib.pyplot as plt
sns.barplot( data=df,x="Region",y="Revenue_EUR")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (€)")
plt.show()
sns.countplot(data=df, x="Customer_Type")
plt.title("Number of Transactions by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Number of Transactions")
plt.show()
sns.histplot(data=df, x="Revenue_EUR", kde=True)
plt.title("Distribution of Revenue")
plt.xlabel("Revenue (€)")
plt.ylabel("Frequency")
plt.show()
sns.boxplot(data=df, y="Revenue_EUR")
plt.title("Revenue Distribution and Outliers")
plt.ylabel("Revenue (€)")
plt.show()
sns.violinplot(data=df, y="Revenue_EUR")
plt.title("Revenue Distribution")
plt.ylabel("Revenue (€)")
plt.show()
sns.scatterplot(data=df,x="Quantity", y="Revenue_EUR", hue="Product_Type")
plt.title("Quantity vs Revenue by Product Type")
plt.xlabel("Quantity")
plt.ylabel("Revenue (€)")
plt.show()
sns.regplot(data=df, x="Quantity", y="Revenue_EUR")
plt.title("Quantity vs Revenue with Trend Line")
plt.xlabel("Quantity")
plt.ylabel("Revenue (€)")
plt.show()
correlation = df[ ["Quantity", "Unit_Price_EUR", "Discount_Rate", "Revenue_EUR"]].corr()
print(correlation)
sns.heatmap( correlation,annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()