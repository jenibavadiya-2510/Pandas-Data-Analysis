import pandas as pd
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df)

# 1. Data Exploring

# Dataset ma kutla rows ane columns che? Shape check karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.shape)

# Badha columns na data types (dtype) joi ne kayu column numeric ane kayu categorical che te kaho.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.dtypes)

# price ane rating column na basic statistics kadho — mean, min, max, median.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[["price", "rating"]].describe())

# Kayi category sauthi vadhu vaar (frequency) aavi che?
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df["category"] .value_counts())

# Kayi city ma sauthi ochha orders thaya che?
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df["city"]. value_counts().idxmin())
# print(df["city"]. value_counts().min())

# Dataset ma koi missing (null) values che ke nai, check karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.isnull().sum())

# payment_method na unique values kaya kaya che, list karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df["payment_method"].unique())

# 2. Selecting (Filtering) Data

# Fakt customer_name, city, ane total_amount — aa 3 columns select karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[["customer_name", "city", "total_amount"]])

# Jya category = "Electronics" hoy tevi badhi rows kadho.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["category"] == "Electronics"])

# Jya total_amount > 20000 hoy tevi rows select karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["total_amount"] > 20000])

# Jya city = "Surat" ane payment_method = "UPI" hoy (bannne condition sathe) tevi rows kadho.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[(df["city"]== "Surat") & (df["payment_method"] == "UPI")])

# Jya rating < 3 hoy tevi rows kadho — aa low-rated orders che.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["rating"] < 3])

# product = "Mobile" athva "Laptop" hoy tevi rows filter karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[(df["product"] == "Mobile") | (df["product"] == "Laptop")])

# Jya order_date January 2025 na mahina ma aavto hoy tevi rows kadho.
# df = pd.read_csv("D:\sales_data (1).csv")
# df['order_date'] = pd.to_datetime(df['order_date'])
# result = df[(df['order_date'].dt.year == 2025) & (df['order_date'].dt.month == 1)]
# print(result)

# customer_name ma "Patel" avtu hoy tevu koi pan naam dhundho (partial text match).
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["customer_name"].str.contains("Patel")])

# 3. Sorting Data

# Dataset ne total_amount na aadhare descending order ma sort karo (sauthi motu order pehla).
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.sort_values("total_amount", ascending=False))

# price ne ascending order ma sort karo ane top 5 sasta products joi.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.sort_values("total_amount").head(5))

# rating na aadhare descending sort kari sauthi vadhu rating vada 10 orders kadho.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.sort_values("rating", ascending=False).head(10))

# Pehla category na aadhare, pachi teni andar total_amount na aadhare sort karo (multi-column sort).
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.sort_values(["category", "total_amount"], ascending=[True, False]))

# order_date na aadhare sabse recent (latest) order pehla aave tevi rite sort karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df.sort_values("order_date", ascending=False))

# 4. Combined Practice (Select + Filter + Sort)

# Jya category = "Furniture" hoy, temathi total_amount na aadhare descending sort kari top 5 orders kadho.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["category"] == "Furniture"].sort_values("total_amount", ascending=False).head(5))

# Har ek city ma sauthi vadhu total_amount vado 1-1 order kadho (group by city + max).
# df = pd.read_csv("D:\sales_data (1).csv")
# result = df.loc[df.groupby("city")["total_amount"].idxmax()]
# print(result)

# payment_method = "Cash on Delivery" vada orders ma thi, rating sauthi ochhu hoy tevo order shodho.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["payment_method"] == "Cash on Delivery"].sort_values("rating").head(1))

# price 1000 thi 5000 ni vachche hoy tevi rows kadho ane temne price na aadhare ascending sort karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# print(df[df["price"].between(1000, 5000)].sort_values("total_amount"))

# Dataset ne category pramane group kari, dareh category nu total revenue (total_amount no sum) kadho, 
# ane sauthi vadhu revenue vali category upar aave tem sort karo.
# df = pd.read_csv("D:\sales_data (1).csv")
# result = df.groupby("category")["total_amount"].sum().sort_values(ascending=False)
# print(result)

# 5.filtering data
# import pandas as pd
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df)

# 20 Filtering Practice Questions

# Basic + Single Condition

# Price ₹50,000 કરતાં વધારે હોય તે બધા orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Price"]> 50000])

# Quantity 3 કરતાં વધારે હોય તે orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Quantity"] > 3])

# Status "Delivered" હોય તે બધા orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Status"] == "Delivered"])

# Category "Electronics" હોય તે બધા products filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Category"] == "Electronics"])

# Multiple Conditions — &
# Category = Electronics AND Price > ₹20,000 હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[(df["Category"] == "Electronics") & (df["Price"] > 20000)])

# Status = Delivered AND Quantity >= 3 હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[(df["Status"] == "Delivered") & (df["Quantity"] >= 3)])

# City = Surat AND Category = Electronics હોય તે orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[(df["City"] == "Surat") & (df["Category"] == "Category")])

# OR — |
# City = Surat OR Mumbai હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[(df["City"] == "Surat") | (df["City"] == "Mumbai")])

# Status = Pending OR Shipped હોય તે orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[(df["Status"] == "Pending") | (df["Status"] == "Shipped")])

# NOT — ~
# Status = Cancelled સિવાયના બધા orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[~(df["Status"] == "Cancelled")])

# Category = Electronics સિવાયના બધા orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[~(df["Category"] == "Electronics")])

# isin()
# City Surat, Ahmedabad અથવા Rajkot હોય તે orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["City"].isin(["Surat", "Ahmedabad", "Rajkot"])])

# Category Electronics અથવા Fashion હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Category"].isin(["Electronics", "Fashion"])])

# between()
# Price ₹10,000 થી ₹30,000 વચ્ચે હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Price"].between(10000, 30000)])

# Quantity 2 થી 5 વચ્ચે હોય તે orders filter કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df[df["Quantity"].between(2, 5)])

# query()
# query() નો ઉપયોગ કરીને Price > ₹40,000 હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df.query("Price > 40000"))

# query() નો ઉપયોગ કરીને Category = Electronics AND Quantity >= 3 હોય તે orders શોધો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df.query("Category == 'Electonics' and Quantity >= 3"))

# where()
# where() નો ઉપયોગ કરીને Price >= ₹20,000 હોય ત્યારે Price રાખો અને બાકીના values NaN કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df["Price"].where(df["Price"]>= 20000))

# mask()
# mask() નો ઉપયોગ કરીને Price < ₹5,000 હોય ત્યાં NaN કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df["Price"].mask(df["Price"] < 5000))

# mask() નો ઉપયોગ કરીને Quantity == 1 હોય ત્યાં NaN કરો.
# df = pd.read_excel("D:\orders_filtering_practice.xlsx")
# print(df["Quantity"].mask(df["Quantity"] == 1))

# Data cleaning question

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# print(df)

# Data Cleaning — 20 Practice Questions
# 1. rename()
# Player_Name column નું નામ બદલીને PlayerName કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df = df.rename(columns={"Player_Name":"PlayerName"})
# print(df)

# 2. drop()
# Temp_Data column datasetમાંથી remove કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df = df.drop(columns=["Temp_Data"])
# print(df)

# 3. duplicated()
# Datasetમાં duplicate player records શોધો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# duplicates = df[df.duplicated()]
# print(duplicates)

# 4. drop_duplicates()
# બધા duplicate records remove કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df = df.drop_duplicates()
# print(df)

# 5. astype()
# Level column ને float datatype માં convert કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Level"] = df["Level"].astype(float)
# print(df.dtypes)

# 6. strip()
# Player_Name માં રહેલા beginning અને ending extra spaces remove કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Player_Name"] = df["Player_Name"].str.strip()
# print(df["Player_Name"])

# 7. lower()
# Game columnની બધી values lowercaseમાં convert કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Game"] = df["Game"].str.lower()
# print(df["Game"])

# 8. upper()
# Country columnની બધી values uppercaseમાં convert કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Country"] = df["Country"].str.upper()
# print(df["Country"])

# 9. replace()
# Country માં:

# IND → India
# INDIA → India
# india → India

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Country"] = df["Country"].replace({
#     "IND":"India",
#     "INDIA":"India",
#     "india":"India"
# })
# print(df)

# 10. replace() — Game
# Game columnમાં pubg, PUBG વગેરેને એક standard format PUBG માં convert કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Game"] = df["Game"].replace({
#     "pubg":"PUBG",
#     "PUBG":"PUBG"
# })
# print(df)

# 11. map()
# Status ને numerical codeમાં convert કરો:

# Active → 1
# Inactive → 0
# 12. Wrong Data Types

# Datasetના બધા columnsના datatypes check કરો અને કયો column data analysis માટે inappropriate datatype ધરાવે છે તે identify કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Status_code"] = df["Status"].map({"Active":1,
#                                       "Inactive":0})
# print(df["Status_code"])

# 13. Inconsistent Values
# Country columnમાં એક જ country અલગ-अलग formatમાં કેટલી રીતે છે તે identify કરો અને તેને standard formatમાં convert કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# print(df["Country"].unique())
# df["Country"] = df["Country"].replace({
#     "IND": "India",
#     "INDIA": "India",
#     "india": "India",
#     "Nepal":"Nepal",
#     "nepal":"Nepal",
#     "USA":"USA",
#     "usa":"USA",
#     "uk":"UK",
#     "UK":"UK"
# })

# print(df["Country"].unique())

# 14. Duplicate Data
# Duplicate records કેટલા છે તે શોધો અને પછી duplicates remove કરો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# dupliates = df[df.duplicated()]
# print(dupliates)
# df = df.drop_duplicates()
# print(df)

# 15. Invalid Data
# Age માં 10 કરતાં ઓછી અથવા 100 કરતાં વધારે age ધરાવતા players શોધો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# print(df[(df["Age"] < 10) | (df["Age"] > 100)])

# 16. Invalid Data — Fix
# Invalid Age values ને NaN માં convert કરો.
# import numpy as np

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df.loc[(df["Age"] < 10) | (df["Age"] > 100), "Age"] = np.nan
# print(df)

# 17. Missing Data
# Score columnમાં missing values કેટલી છે તે શોધો.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# print(df.isna().sum())

# 18. Extra Spaces
# Player_Name માંથી extra spaces remove કર્યા પછી check કરો કે હવે કોઈ leading/trailing spaces બાકી છે કે નહીં.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Player_Name"] = df["Player_Name"].str.strip()
# print(df["Player_Name"])

# 19. Standardizing Text
# Game columnને standard formatમાં લાવો જેથી:

# minecraft
# Minecraft
# બંને Minecraft બને અને

# free fire
# FREE FIRE
# Free Fire
# બધા Free Fire બને.

# df = pd.read_excel("D:\game_players_cleaning_practice.xlsx")
# df["Game"] = df["Game"].replace({
#     "minecraft":"Minecraft",
#     "Minecraft":"Minecraft",
#     "free fire":"Free Fire",
#     "FREE FIRE":"Free Fire",
#     "Free Fire":"Free Fire"
# })
# print(df)

# Complete Practice — Adding & Modifying Data

# Part A — Creating & Modifying Columns
# Q1. Creating New Column
# Score પરથી Double_Score column બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# print(df)

# Q2. Creating New Column
# Price માં ₹200 add કરીને New_Price column બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["New_Price"] = df["Price"] + 200
# print(df["New_Price"])

# Q3. Updating Existing Column
# Score માં દરેક player માટે 5 marks add કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Double_score"] = df["Score"] + 5
# print(df["Double_score"])

# Q4. Updating Existing Column
# Price માં 10% increase કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["New_Price"] = df["Price"] * 0.10
# print(df["New_Price"])

# Part B — insert()
# Q5.Player_Name પછી Player_Level નામનો column insert કરો અને બધા values "Beginner" રાખો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df.insert(2, "Player_Level", "Beginner")
# print(df)

# Q6. Index 2 પર Bonus column insert કરો અને value 500 રાખો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df.insert(2, "Bonus", 500)
# print(df)

# Part C — assign()
# Q7.assign() નો ઉપયોગ કરીને Double_Matches column બનાવો.
# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df = df.assign(Double_Matches = df["Matches"] * 2)
# print(df)

# Q8.assign() નો ઉપયોગ કરીને એકસાથે:
# Total_Value
# Double_Score

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df = df.assign(Total_Value = df["Price"] * df["Quantity"])
# df = df.assign(Double_score = df["Score"] * 2)
# print(df)

# Formula:

# Total_Value = Price × Quantity
# Double_Score = Score × 2

# Part D — apply()
# Q9.Score પર apply() use કરીને દરેક score માં 10 add કરો અને Updated_Score બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# def add_score(x):
#     return x + 10
# df["Updated_score"] = df["Score"].apply(add_score)
# print(df)

# Q10.Price પર apply() use કરીને price ને 18% GST સાથે calculate કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# def add_price(x):
#     return x * 1.18
# df["New_price"] = df["Price"].apply(add_price)
# print(df)

# Part E — Lambda Functions
# Q11.Lambda function use કરીને:

# Score >= 50 → Pass
# Score < 50 → Fail
# Result column બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Result"] = df["Score"].apply(lambda x:"Pass" if x>= 50 else "Fail")
# print(df)

# Q12.Lambda function use કરીને Age પરથી:

# Age < 25 → Young
# Age >= 25 → Adult
# Age_Group બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Result"] = df["Age"].apply(lambda x:"Young" if x < 25 else "Adult")
# print(df)

# Q13.Lambda function use કરીને Price ને double કરીને Double_Price બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Result"] = df["Price"].apply(lambda x: x * 2)
# print(df)

# Part F — Conditional Column Creation
# Q14.Score પ્રમાણે Grade column બનાવો:

# Score >= 80 → A
# Score >= 60 → B
# Score >= 40 → C
# Score < 40  → F

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Grade"] = df["Score"].apply(lambda x:"A" if x >= 80 else "B" if x>= 60 else "C" if x>= 40 else "F")
# print(df)

# Q15.Quantity પ્રમાણે Order_Type બનાવો:

# Quantity >= 4 → High
# Quantity >= 2 → Medium
# Quantity < 2  → Low

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Order_type"] = df["Quantity"].apply(lambda x:"High" if x >= 4 else "Medium" if x >= 2 else "Low")
# print(df)

# Q16.Score >= 70 અને Matches >= 10 હોય તો "Excellent" નહીં તો "Normal".

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Performance"] = df.apply(lambda row: "Excellent"
#                              if (row["Score"] >= 70) & (row["Matches"] >= 10)
#                              else "Normal", axis = 1)
# print(df)

# Part G — Column Arithmetic
# Q17.Total_Value = Price × Quantity

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Total_Value"] = df["Price"] * df["Quantity"]
# print(df)

# Q18.# Price_Per_Match = Price / Matches

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Price_Per_Month"] = df["Price"] / df["Matches"]
# print(df)

# Q19. Score_Per_Match = Score / Matches

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Score_Per_Match"] = df["Score"] / df["Matches"]
# print(df)

# Q20. Estimated_Revenue = Price × Quantity × 1.18

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Estimated_Revenue"] = df["Price"] * df["Quantity"] * 1.18
# print(df)

# Part H — Feature Creation
# Q21.
# Create Performance_Score:Score × Matches

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Performance_Score"] = df["Score"] * df["Matches"]
# print(df)

# Q22.Create Revenue_Per_Player:Price × Quantity

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Revenue_per_player"] = df["Price"] * df["Quantity"]
# print(df)

# Q23.
# Create High_Performer:
# Score >= 80 → Yes
# Otherwise → No

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["High_Performer"] = df["Score"].apply(
#     lambda x: "Yes" if x >= 80 else "No"
# )
# print(df)

# Q24.
# Create Player_Category:
# Age < 25 → Young
# 25–30 → Adult
# >30 → Senior

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Player_Category"] = df["Age"].apply(
#     lambda x:"Young" if x < 25 else "Adult" if x <= 30
#     else "Senior"
# )
# print(df)

# Part I — Dropping / Removing Column

# Q25.Temp_Data column remove કરો.
# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df = df.drop(columns=["Temp_Data"])
# print(df)

# Q26.Temp_Data અને Player_ID બંને remove કરો.
# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df = df.drop(columns=["Temp_Data" , "Player_ID"])
# print(df)

# Q27.drop() use કરીને Matches column remove કરો.
# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df = df.drop(columns=["Matches"])
# print(df)

# 🔥 Part J — String Functions
# Q28 — str.strip()
# Player_Name માંથી starting અને ending extra spaces remove કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Player_Name"] = df["Player_Name"].str.strip()
# print(df)

# Q29 — str.lower()
# Game column ને completely lowercase કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Game"] = df["Game"].str.lower()
# print(df)

# Q30 — str.upper()
#City column ને uppercase કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["City"] = df["City"].str.upper()
# print(df)

# Q31 — str.title()
# Player_Name ને proper title format માં convert કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Player_Name"] = df["Player_Name"].str.title()
# print(df)

# Q32 — str.capitalize()
# City column ને capitalize કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["City"] = df["City"].str.strip().str.capitalize()
# print(df)

# Q33 — str.replace()
# Game column માં:

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Game"] = df["Game"].replace("free fire", "FreeFire")
# print(df)

# Q34 — str.len()
# Player_Name ની length calculate કરીને:
# Name_Length column બનાવો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Name_Length"] = df["Player_Name"].str.len()
# print(df)

# Q35 — str.contains()
# જે players ના names માં "shah" આવે છે તે records display કરો.
# Hint: case-insensitive search કરજો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# print(df[df["Player_Name"].str.contains("shah", case=False, na=False)])

# Q36 — str.startswith()
# જે Player_Name "A" થી start થાય છે તે players શોધો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# print(df[df["Player_Name"].str.startswith("A")])

# Q37 — str.endswith()
# જે Player_Name "patel" થી end થાય છે તે players શોધો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# result = df[df["Player_Name"].str.strip().str.lower().str.endswith("patel", na=False)]
# print(result)

# Q38 — str.split()
# Player_Name ને first name અને last name માં split કરો.

# Create:
# First_Name
# Last_Name

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Name_Parts"] = df["Player_Name"].str.strip().str.split()
# print(df[["Player_Name", "Name_Parts"]]) 

# Q39 — str.get()
# Player_Name split કરીને first word First_Name તરીકે કાઢો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["First_Name"] = df["Player_Name"].str.strip().str.split().str.get(0)
# print(df[["Player_Name", "First_Name"]])

# Q40 — str.find()
# Player_Name માં "a" કયા position પર આવે છે તે શોધો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["A_Position"] = df["Player_Name"].str.lower().str.find("a")
# print(df[["Player_Name", "A_Position"]])

# Q41 — str.count()
# દરેક Player_Name માં "a" કેટલા વખત આવે છે તે calculate કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["A_Count"] = df["Player_Name"].str.lower().str.count("a")
# print(df[["Player_Name", "A_Count"]])

# Q42 — str.isalpha()
# Player_Name માં only alphabets છે કે નહીં check કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["isalpha"] = df["Player_Name"].str.isalpha()
# print(df[["Player_Name", "isalpha"]])

# Q43 — str.isnumeric()
# Player_ID ને string માં convert કરીને check કરો કે values numeric છે કે નહીં.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["isnumeric"] = df["Player_ID"].astype(str).str.isnumeric()
# print(df[["Player_ID", "isnumeric"]])

# Q44 — str.isalnum()
# Player_ID string માં alphanumeric values છે કે નહીં check કરો.

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Is_Alnum"] = df["Player_ID"].astype(str).str.isalnum()
# print(df[["Player_ID", "Is_Alnum"]])

# Q45 — str.zfill()
# Player_ID ને 5-digit format માં convert કરો.

# Example:
# 101 → 00101
# 102 → 00102

# df = pd.read_excel("D:\pandas_adding_modifying_practice.xlsx")
# df["Formatted_ID"] = df["Player_ID"].astype(str).str.zfill(5)
# print(df[["Player_ID", "Formatted_ID"]])

# Date $ Time function

# import pandas as pd

# data = {
#     "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
#     "Customer": ["Jeni", "Rahul", "Amit", "Priya", "Karan", "Neha", "Riya", "Vikas"],
#     "Order_Date": [
#         "2026-01-15 10:30:00",
#         "2026-02-20 14:45:00",
#         "2026-03-05 09:15:00",
#         "2026-03-18 18:20:00",
#         "2026-04-10 11:00:00",
#         "2026-05-25 16:30:00",
#         "2026-06-12 20:15:00",
#         "2026-07-08 08:45:00"
#     ],
#     "Delivery_Date": [
#         "2026-01-18",
#         "2026-02-23",
#         "2026-03-08",
#         "2026-03-22",
#         "2026-04-14",
#         "2026-05-29",
#         "2026-06-16",
#         "2026-07-11"
#     ],
#     "Amount": [1200, 2500, 1800, 3200, 1500, 2800, 4500, 2100]
# }

# df = pd.DataFrame(data)
# print(df)

# Part 1 — pd.to_datetime()
# Q1 Order_Date column ને proper datetime format માં convert કરો.
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df)

# Q2 Delivery_Date column ને પણ datetime માં convert કરો.

# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])
# print(df)

# Q3 Check કરો કે બંને columns નો datatype datetime થયો છે કે નહીં.
# print(df[["Order_Date", "Delivery_Date"]].dtypes)

# Part 2 — .dt.year, .dt.month, .dt.day
# Q4 Order_Date માંથી Year કાઢીને Order_Year column બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Year"] = df["Order_Date"].dt.year
# print(df[["Order_Date", "Order_Year"]])

# Q5 Order_Date માંથી Month કાઢીને Order_Month column બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Month"] = df["Order_Date"].dt.month
# print(df[["Order_Date", "Order_Month"]])

# Q6  Order_Date માંથી Day કાઢીને Order_Day column બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Day"] = df["Order_Date"].dt.day
# print(df[["Order_Date", "Order_Day"]])

# Part 3 — Day & Time
# Q7 Order_Date માંથી Day Name કાઢો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Dayname"] = df["Order_Date"].dt.day_name()
# print(df[["Order_Date", "Order_Dayname"]])

# Q8 Order_Date માંથી Hour કાઢીને Order_Hour column બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Hour"] = df["Order_Date"].dt.hour
# print(df[["Order_Date", "Order_Hour"]])

# Q9 કયા orders evening (6 PM અથવા પછી) થયા હતા તે filter કરો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df[df["Order_Date"].dt.hour >= 18])

# Part 4 — Date Difference
# Q10 Order_Date અને Delivery_Date વચ્ચે કેટલા દિવસનો difference છે તે Delivery_Days column માં બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Delivery_Days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days

# print(df[["Order_Date", "Delivery_Date", "Delivery_Days"]])

# Q11 જે orders 3 દિવસથી વધારે સમયમાં delivered થયા છે તે filter કરો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Delivery_Days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days

# print(df[df["Delivery_Days"] > 3])

# Q12 સૌથી વધારે delivery time ધરાવતો order શોધો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Delivery_Days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days

# highest_delivery = df.loc[df["Delivery_Days"].idxmax()]
# print(highest_delivery)

# Part 5 — Date Filtering
# Q13 March 2026 માં થયેલા બધા orders શોધો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# march_Orders = df[df["Order_Date"].dt.month == 3]
# print(march_Orders)

# Q14 2026-04-01 પછીના બધા orders શોધો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df[df["Order_Date"] > "2026-04-01"])

# Q15 January થી March 2026 વચ્ચેના orders શોધો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# orders = df[
#     (df["Order_Date"] >= "2026-01-01") &
#     (df["Order_Date"] <= "2026-03-31")
# ]

# print(orders)

# Part 6 — strftime()
# Q16 Order_Date ને આ format માં convert કરો:

# 15-01-2026
# 20-02-2026
# 05-03-2026

# અને Formatted_Date column બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Formatted_Date"] = df["Order_Date"].dt.strftime(" %d-%m-%y")
# print(df)

# Q17

# Order_Date ને:
# 15 Jan 2026
# 20 Feb 2026
# 05 Mar 2026
# આ format માં convert કરો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Formatted_Date"] = df["Order_Date"].dt.strftime(" %d-%b-%y")
# print(df[["Order_Date", "Formatted_Date"]])


# 🎯 Challenge
# Q18

# એક Order_Month_Name column બનાવો જેમાં:

# January
# February
# March

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Month_Name"] = df["Order_Date"].dt.month_name()
# print(df[["Order_Date", "Order_Month_Name"]])

# Q19 Order_Date પરથી Order_Year, Order_Month, Order_Day, Day_Name, અને Order_Hour એકસાથે બનાવો.

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# df["Order_Year"] = df["Order_Date"].dt.year
# df["Order_Month"] = df["Order_Date"].dt.month
# df["Order_Day"] = df["Order_Date"].dt.day
# df["Order_DayName"] = df["Order_Date"].dt.day_name()
# df["Order_Hour"] = df["Order_Date"].dt.hour

# print(df[[
#     "Order_Date",
#     "Order_Year",
#     "Order_Month",
#     "Order_Day",
#     "Order_DayName",
#     "Order_Hour"
# ]])

# Q20 Complete task:

# Order_Date → datetime
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df["Order_Date"])

# # Delivery_Date → datetime
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])
# print(df["Delivery_Date"])

# # Delivery days calculate કરો
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Delivery_Days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days

# print(df[["Order_Date", "Delivery_Date", "Delivery_Days"]])

# Month Name બનાવો
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Month"] = df["Order_Date"].dt.month
# print(df[["Order_Date", "Order_Month"]])

# Day Name બનાવો
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Order_Day_Name"] = df["Order_Date"].dt.day_name()
# print(df[["Order_Date", "Order_Day_Name"]])

# Amount > 2500 અને delivery days <= 3 હોય એવા orders filter કરો.
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])

# df["Delivery_Days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days

# result = df[
#     (df["Amount"] > 2500) &
#     (df["Delivery_Days"] <= 3)
# ]

# print(result)

# GroupBy — Syntax + Examples + Practice

# આ dataset બધા examples માટે use કરીશું:

# import pandas as pd

# data = {
#     "City": ["Surat", "Ahmedabad", "Surat", "Rajkot", "Ahmedabad",
#              "Surat", "Rajkot", "Vadodara", "Surat", "Ahmedabad"],
    
#     "Category": ["Electronics", "Fashion", "Electronics", "Grocery", "Fashion",
#                  "Grocery", "Electronics", "Fashion", "Grocery", "Electronics"],
    
#     "Sales": [50000, 30000, 45000, 20000, 35000,
#               25000, 40000, 28000, 32000, 55000],
    
#     "Profit": [8000, 5000, 7000, 3000, 6000,
#                4000, 6500, 4500, 5200, 9000],
    
#     "Quantity": [5, 3, 4, 2, 4, 3, 5, 2, 4, 6]
# }

# df = pd.DataFrame(data)
# print(df)

# 1. groupby()

# Q1. Category પ્રમાણે data group કરો.
# result = df.groupby("Category")
# print(result)

# Q2. City પ્રમાણે total Quantity calculate કરો.
# result = df.groupby("City")["Sales"].sum()
# print(result)

# 2. sum()

# Q1. દરેક Category નું total Sales શોધો.
# result = df.groupby("Category")["Sales"].sum()
# print(result)

# Q2. દરેક City નું total Profit શોધો.
# result = df.groupby("City")["Sales"].sum()
# print(result)

# 3. mean()

# Q1. દરેક Category ની average Sales શોધો.
# result = df.groupby("Category")["Sales"].mean()
# print(result)

# Q2. દરેક City ની average Profit શોધો.
# result = df.groupby("City")["Profit"].mean()
# print(result)

# 4. count()

# Q1. દરેક Category માં કેટલા orders છે તે શોધો.
# result = df.groupby("Category")["Sales"].count()
# print(result)

# Q2. દરેક City માં કેટલા products/orders છે તે count કરો.
# result = df.groupby("City")["Sales"].count()
# print(result)

# 5. max()

# Q1. દરેક City માં highest Sales શોધો.
# result = df.groupby("City")["Sales"].max()
# print(result)

# Q2. દરેક Category માં highest Profit શોધો.
# result = df.groupby("Category")["Profit"].max()
# print(result)

# 6. min()

# Q1. દરેક Category માં lowest Sales શોધો.
# result = df.groupby("Category")["Sales"].min()
# print(result)

# Q2. દરેક City માં lowest Quantity શોધો.
# result = df.groupby("City")["Quantity"].min()
# print(result)

# 7. agg()

# Q1. દરેક Category ની Sales માટે sum, mean, max, min શોધો.
# result = df.groupby("Category")["Sales"].agg(
#     ("sum", "mean", "max", "min")
# )
# print(result)

# Q2. દરેક City ની Profit માટે sum, mean, max, min શોધો.
# result = df.groupby("City")["Profit"].agg(
#     ("sum", "mean", "max", "min")
# )
# print(result)

# 8. Multiple Aggregation


# result = df.groupby("City").agg({
#     "Sales": "sum",
#     "Profit": "mean",
#     "Quantity": "count"
# })

# print(result)

# Q1. દરેક Category માટે:

# Sales → sum
# Profit → mean

# result = df.groupby("Category").agg({
#     "Sales" : "sum",
#     "Profit" : "mean"
# })
# print(result)

# Q2. દરેક City માટે:

# Sales → sum
# Profit → max
# Quantity → mean

# result = df.groupby("City").agg({
#     "Sales" : "sum",
#     "Profit" : "max",
#     "Quantity" : "mean"
# })
# print(result)

# 9. GroupBy Multiple Columns


# result = df.groupby(
#     ["City", "Category"]
# )["Sales"].sum()

# print(result)

# Q1. City અને Category પ્રમાણે total Profit શોધો.
# result = df.groupby(
#     ["City", "Category"])["Profit"].sum()
# print(result)

# Q2. City અને Category પ્રમાણે total Quantity શોધો.
# result = df.groupby(
#     ["City", "Category"])["Quantity"].sum()
# print(result)

# 10. GroupBy + Filtering

# Solved Example:

# ₹70,000 કરતાં વધારે total sales ધરાવતા cities:

# result = (
#     df.groupby("City")["Sales"]
#     .sum()
#     .loc[lambda x: x > 70000]
# )

# print(result)

# Q1. Total Sales ₹80,000 કરતાં વધારે હોય તેવી Cities શોધો.
# result = (
#     df.groupby("City")["Sales"]
#     .sum()
#     .loc[lambda x: x > 80000]
# )

# Q2. Total Profit ₹10,000 કરતાં વધારે હોય તેવી Categories શોધો.
# result = (
#     df.groupby("Category")["Profit"]
#     .sum()
#     .loc[lambda x: x > 10000]
# )

# 11. GroupBy + Sorting

# Highest Sales → Lowest Sales:

# result = (
#     df.groupby("City")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# print(result)

# Practice — No Answer

# Q1. Cities ને total Sales પ્રમાણે highest to lowest sort કરો.
# result = (
#     df.groupby("City")["Sales"]
#     .sum()
#     .sort_values(ascending=False)
# )
# print(result)

# Q2. Categories ને average Profit પ્રમાણે lowest to highest sort કરો.
# result = (
#     df.groupby("Category")["Profit"]
#     .mean()
#     .sort_values(ascending=True)
# )
# print(result)

# 12. transform()

# Q1. દરેક order માટે તેની Category ની average Sales Category_Avg_Sales column માં બનાવો.
# df["Category_Avg_Sales"] = (
#     df.groupby("Category")["Sales"]
#     .transform("mean")
# )
# print(df[["Category", "Sales", "Category_Avg_Sales"]])

# Q2. દરેક order માટે તેના City નું total Sales City_Total_Sales column માં બનાવો.
# df["City_Total_Sales"] = (
#     df.groupby("City")["Sales"]
#     .transform("sum")
# )
# print(df[["City", "Sales", "City_Total_Sales"]])

# Pivot Table — Pandas



# Pivot table topic
# Topic 1 — pivot()

# Example
# result = df.pivot(
#     index="City",
#     columns="Category",
#     values="Sales"
# )

# print(result)

# df = pd.read_excel("D:\pivot_table_practice.xlsx")
# print(df)

# Topic 1 — pivot() Practice

# Q1. City × Category પ્રમાણે Sales show કરો using pivot().
# import pandas as pd

# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")

# result = df.pivot_table(
#     index="City",
#     columns="Category",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Q2. City × Category પ્રમાણે Profit show કરો using pivot().
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="City",
#     columns="Category",
#     values="Profit",
#     aggfunc="sum"
# )
# print(result)

# Q3. City ને index અને Product ને columns બનાવીને Sales show કરો.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="City",
#     columns="Product",
#     values="Sales",
#     aggfunc="sum"
# )
# print(result)

# Topic 2 — pivot_table()

# Practice Q1 — No Answer

# City × Category પ્રમાણે total Profit શોધો using pivot_table().
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="City",
#     columns="Category",
#     values="Profit",
#     aggfunc="sum"
# )
# print(result)

# Practice Q2 —
# Category × City પ્રમાણે average Sales શોધો using pivot_table().
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="Category",
#     columns="City",
#     values="Sales",
#     aggfunc="mean"
# )
# print(result)

# Topic 3 — crosstab()

# Practice Q1 — 
# Category × City પ્રમાણે કેટલા orders છે તે crosstab() થી શોધો.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = pd.crosstab(
#     df["Category"],
#     df["City"]
# )
# print(result)

# Practice Q2 —
# City × Product પ્રમાણે કેટલા orders છે તે crosstab() થી શોધો.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = pd.crosstab(
#     df["City"],
#     df["Product"]
# )
# print(result)

# Topic 4 — Multiple Index

# Practice Q1 — No Answer
# City → Category multiple index રાખીને total Profit શોધો.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index=["City", "Category"],
#     values="Profit",
#     aggfunc="sum"
# )
# print(result)

# Practice Q2 — No Answer
# City → Category → Product multiple index રાખીને total Quantity શોધો.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index=["City", "Category", "Product"],
#     values="Quantity",
#     aggfunc="sum"
# )
# print(result)

# Topic 5 — Multiple Values

# Practice Q1 — 
# દરેક Category માટે Sales, Profit, અને Quantity નો total શોધો.

# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="Category",
#     values=["Sales", "Profit", "Quantity"],
#     aggfunc="sum"
# )
# print(result)

# Practice Q2 — 
# દરેક City માટે Sales અને Profit નો average શોધો.

# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="City",
#     values=["Sales", "Profit"],
#     aggfunc="mean"
# )
# print(result)

# Topic 6 — Aggregation in Pivot Table

# Different Aggregations

# Practice Q1 — 
# દરેક Category માટે highest Sales શોધો using pivot_table().
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="Category",
#     values="Sales",
#     aggfunc="max"
# )
# print(result)

# Practice Q2 — No Answer
# દરેક City માટે average Profit શોધો using pivot_table().
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index="City",
#     values="Profit",
#     aggfunc="mean"
# )
# print(result)

# Topic 7 — margins=True

# import pandas as pd

# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")

# result = df.pivot_table(
#     index="City",
#     columns="Category",
#     values="Sales",
#     aggfunc="sum",
#     margins=True
# )

# print(result)

# Practice Q1 —
# City × Category પ્રમાણે total Profit બનાવો અને Grand Total પણ બતાવો using margins=True.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index = "City",
#     columns="Category",
#     values="Sales",
#     aggfunc="sum",
#     margins=True
# )
# print(result)

# Practice Q2 — 
# Category × City પ્રમાણે total Quantity બનાવો અને row/column totals પણ બતાવો using margins=True.
# df = pd.read_excel(r"D:\pivot_table_practice.xlsx")
# result = df.pivot_table(
#     index = "Category",
#     columns="City",
#     values="Quantity",
#     aggfunc="sum",
#     margins=True
# )
# print(result)


# Merge $ join

# customers
# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# print(customers)

# orders
# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# print(orders)

# products
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# print(products)


# Topic 1 — merge()
# Q1 Customers અને Orders DataFrames ને Customer_ID ના આધારે merge() કરો.

# Final result માં આ columns રાખો:

# Customer_ID
# Customer
# City
# Order_ID
# Product_ID
# Quantity
# Sales

# import pandas as pd

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )

# result = pd.merge(
#     customers,
#     orders,
#     on="Customer_ID"
# )

# print(result)

# Q2 Orders અને Products DataFrames ને Product_ID ના આધારે merge() કરો.
# Final result માં આ columns રાખો:

# Order_ID
# Product_ID
# Product
# Category
# Price
# Quantity
# Sales

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# result = pd.merge(
#     orders,
#     products,
#     on="Product_ID"
# )
# print(result)

# Topic 2 — Inner Join
# Customers અને Orders ને Inner Join કરો using Customer_ID.
# માત્ર એવા records બતાવો જ્યાં Customer_ID બંને DataFrames માં common છે.

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# result = pd.merge(
#     customers,
#     orders,
#     on="Customer_ID",
#     how="inner"
# )
# print(result)

# Q2 Orders અને Products ને Inner Join કરો using Product_ID.
# Final result માં માત્ર matching products સાથેના orders બતાવો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# result = pd.merge(
#     orders,
#     products,
#     on="Product_ID",
#     how="inner"
# )
# print(result)

# Topic 3 — Left Join
# Practice Q1 —
# Customers અને Orders ને Customer_ID પર Left Join કરો.

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# result = pd.merge(
#     customers,
#     orders,
#     on="Customer_ID",
#     how="left"
# )
# print(result)

# Practice Q2 — Products અને Orders ને Product_ID પર Left Join કરો.
# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# result = pd.merge(
#     orders,
#     products,
#     on="Product_ID",
#     how="left"
# )
# print(result)

# Topic 4 — Right Join
# Practice Q1 — Customers અને Orders ને Customer_ID પર Right Join કરો.

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# result = pd.merge(
#     customers,
#     orders,
#     on="Customer_ID",
#     how="right"
# )
# print(result)

# Practice Q2 — Orders અને Products ને Product_ID પર Right Join કરો.
# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# result = pd.merge(
#     orders,
#     products,
#     on="Product_ID",
#     how="right"
# )
# print(result)

# Topic 5 — Outer Join
# Practice Q1 — Customers અને Orders ને Customer_ID પર Outer Join કરો.

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# result = pd.merge(
#     customers,
#     orders,
#     on="Customer_ID",
#     how="outer"
# )
# print(result)

# Practice Q2 — Orders અને Products ને Product_ID પર Outer Join કરો.
# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# result = pd.merge(
#     orders,
#     products,
#     on="Product_ID",
#     how="outer"
# )
# print(result)

# Topic 6 — concat()

# Practice Q1 — Customers DataFrame ને તેની જ copy સાથે vertical concat() કરો.
# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# result = pd.concat(
#     [customers, customers],
#     axis=0,
#     ignore_index=True
# )

# print(result)

# Practice Q2 — Customers અને Orders ને horizontal concat() કરો અને result print કરો.
# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# result = pd.concat(
#   [customers, orders],
#   axis = 0,
#   ignore_index=True
# )
# print(result)

# Topic 7 — append()

# Practice Q1 — 
# Orders DataFrame ની copy બનાવીને બંનેને vertically append/concat કરો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# result = pd.concat(
#     [orders, orders],
#     axis=0,
#     ignore_index=True
# )
# print(result)

# Practice Q2 — 
# Products DataFrame ને તેની copy સાથે vertically combine કરો અને new continuous index રાખો.

# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# result = pd.concat(
#     [products, products],
#     axis=0,
#     ignore_index=True
# )
# print(result)

# Topic 8 — Multiple-column Merge

# Practice Q1 — 
# Orders અને order_details ને Customer_ID + Product_ID બંને columns પર merge કરો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )

# # Example second DataFrame
# order_details = orders[
#     ["Customer_ID", "Product_ID", "Quantity"]
# ].copy()

# result = pd.merge(
#     orders,
#     order_details,
#     on=["Customer_ID", "Product_ID"],
#     how="inner"
# )
# print(result)

# Practice Q2 — 
# બંને DataFrames ને Customer_ID + Product_ID પર merge કરીને માત્ર matching records બતાવો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )

# # Example second DataFrame
# order_details = orders[
#     ["Customer_ID", "Product_ID", "Quantity"]
# ].copy()

# result = pd.merge(
#     orders,
#     order_details,
#     on=["Customer_ID", "Product_ID"],
#     how="inner"
# )
# print(result)

# Topic 9 — left_on / right_on

# Practice Q1 — No Answer

# Customers માં Customer_ID ને Cust_ID rename કરો. પછી Orders અને Customers ને:

# left_on="Customer_ID"
# right_on="Cust_ID"
# how="left"
# using merge કરો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )
# customers2 = customers.rename(
#     columns={"Customer_ID": "Cust_ID"}
# )
# result = pd.merge(
#     orders,
#     customers2,
#     left_on="Customer_ID",
#     right_on="Cust_ID",
#     how="left"
# )
# print(result)

# Practice Q2 — No Answer

# Products માં Product_ID ને Prod_ID rename કરો. પછી Orders અને Products ને:

# left_on="Product_ID"
# right_on="Prod_ID"
# how="inner"

# using merge કરો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# products2 = products.rename(
#     columns={"Product_ID" : "Pro_ID"}
# )
# result = pd.merge(
#     orders,
#     products2,
#     left_on="Product_ID",
#     right_on="Pro_ID",
#     how="inner"
# )
# print(result)

# Topic 10 — join()

# Practice Q1 — 
# Customers અને Orders માં Customer_ID ને index બનાવો અને join() દ્વારા inner join કરો.

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )

# customers_index = customers.set_index("Customer_ID")
# orders_index = orders.set_index("Customer_ID")

# result = customers_index.join(
#     orders_index,
#     how="inner",
#     lsuffix="_customer",
#     rsuffix="_order"
# )

# print(result)

# Practice Q2 — 
# Orders અને Products માં Product_ID ને index બનાવો અને join() દ્વારા left join કરો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# products = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Products"
# )
# orders_index = orders.set_index("Product_ID")
# products_index = products.set_index("Product_ID")

# result = products_index.join(
#     orders_index,
#     how="left",
#     lsuffix="_customer",
#     rsuffix="_order"
# )

# print(result)

# Topic 11 — keys with concat()

# Practice Q1 — 
# Customers અને તેની copy ને concat() કરો અને:
# keys=["Customers", "Customers_Copy"] use કરો.

# customers = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Customers"
# )
# customers2 = customers.copy()
# result = pd.concat(
#     [customers, customers2],
#     keys=["Original", "Copy"]
# )
# print(result)

# Practice Q2 — 
# Orders અને Orders ની copy ને concat() કરો અને બંને DataFrames માટે અલગ keys આપો.

# orders = pd.read_excel(
#     r"D:\merge_join_complete_practice.xlsx",
#     sheet_name="Orders"
# )
# orders2 = orders.copy()
# result = pd.concat(
#     [orders, orders2],
#     keys=["Original", "Copy"]
# )
# print(result)

# Aggregation function

df = pd.DataFrame({
 "Sales": [1000, 2000, 1500, 3000, 2500],
 "Quantity": [2, 4, 3, 6, 5],
 "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Shoes"]
})

# result = df["Sales"].sum()
# print(result)

# mean = df["Sales"].mean()
# print(mean)

# median = df["Sales"].median()
# print(median)

# mode = df["Category"].mode()
# print(mode)

# max = df["Sales"].max()
# print(max)

# min = df["Sales"].min()
# print(min)

# count = df["Sales"].count()
# print(count)

# std = df["Sales"].std()
# print(std)

# var = df["Sales"].var()
# print(var)

# quantile = df["Sales"].quantile(0.75)
# print(quantile)

# nunique = df["Category"].nunique()
# print(nunique)

# prod = df["Quantity"].prod()
# print(prod)

# Apply function

import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "City": ["Surat", "Ahmedabad", "Rajkot", "Surat",
             "Vadodara", "Ahmedabad", "Surat", "Rajkot"],
    "Category": ["Electronics", "Fashion", "Grocery", "Electronics",
                 "Fashion", "Grocery", "Electronics", "Fashion"],
    "Sales": [50000, 30000, 20000, 45000, 35000, 25000, 60000, 28000],
    "Cost": [42000, 25000, 17000, 37000, 29000, 21000, 50000, 23000],
    "Profit": [8000, 5000, 3000, 8000, 6000, 4000, 10000, 5000],
    "Quantity": [5, 3, 2, 4, 4, 3, 6, 2],
    "Price": [10000, 5000, 8000, 12000, 7000, 9000, 15000, 6000],
    "Status": ["Active", "Inactive", "Active", "Active",
               "Inactive", "Active", "Active", "Inactive"]
}

df = pd.DataFrame(data)
print(df)

# 1. apply()

# df["New_Sales"] = df["Sales"].apply(lambda x: x * 1.10)
# print(df)

# Practice Q1 — 
# Price column પર apply() અને lambda use કરીને Double_Price બનાવો.
# df["Double_Price"] = df["Price"].apply(lambda x: x * 2)
# print(df)

# Practice Q2 —
# Quantity column પર apply() use કરીને દરેક value માં 5 add કરો અને New_Quantity બનાવો.
# df["New_Quantity"] = df["Quantity"].apply(lambda x: x + 5)
# print(df)

# 2. map()

# Example
# df["State"] = df["City"].map({
#     "Surat": "Gujarat",
#     "Ahmedabad": "Gujarat",
#     "Rajkot": "Gujarat"
# })

# print(df)

# Practice Q1 — 

# Category માં:

# Electronics → E
# Fashion → F
# Grocery → G

# એ પ્રમાણે Category_Code બનાવો.

# df["Category_Code"] = df["Category"].map({
#     "Electronics" : "E",
#     "Fashion" : "F",
#     "Grocery" : "G"
# })
# print(df)

# Practice Q2 — No Answer

# Status માં:

# Active → 1
# Inactive → 0

# એ પ્રમાણે Status_Code બનાવો.

# df["Status_code"] = df["Status"].map({
#     "Active" : 1,
#     "Inactive" : 0
# })
# print(df)

# 3. DataFrame map()

# Example
# result = df.map(lambda x: str(x).strip())
# print(result)

# Practice Q1 — 
# DataFrame ના દરેક value ને string માં convert કરવા માટે map() use કરો.

# result = df.map(lambda x: str(x).strip())
# print(result)

# Practice Q2 —
# DataFrame ના દરેક value માટે str(x).upper() apply કરો.

# result = df.map(lambda x: str(x).upper())
# print(result)

# 4. Lambda Function

# Example
# df["Double_Sales"] = df["Sales"].apply(lambda x: x * 2)

# Practice Q1 —
# Sales ને 20% increase કરીને Increased_Sales બનાવો.

# df["Increased_Sales"] = df["Sales"].apply(lambda x: x * 1.20)
# print(df)

# Practice Q2 — 
# Price માં ₹500 add કરીને Updated_Price બનાવો.

# df["Updated_Price"] = df["Sales"].apply(lambda x: x + 500)
# print(df)

# 5. Applying Function to Rows — axis=1

# Example
# df["Profit"] = df.apply(
#     lambda row: row["Sales"] - row["Cost"],
#     axis=1
# )

# Practice Q1 — 
# Sales - Cost કાઢીને Profit column બનાવો using axis=1.

# df["Profit"] = df.apply(
#     lambda row: row["Sales"] - row["Cost"],
#     axis=1
# )
# print(df)

# Practice Q2 — 
# Sales + cost કાઢીને Final_Amount column બનાવો using axis=1.

# df["Total_Amount"] = df.apply(
#     lambda row: row["Sales"] + row["Cost"],
#     axis=1
# )
# print(df)

# 6. Applying Function to Columns — axis=0

# Example
# result = df.apply(lambda col: col.max() - col.min())
# print(result)

# Practice Q1 —
# દરેક numeric column નું:
# maximum - minimum find કરો.

# result = df.select_dtypes(include="number").apply(
#     lambda col: col.max() - col.min(),
#     axis=0
# )

# print(result)

# Practice Q2 — 
# દરેક numeric column નું max() find કરો using axis=0.

# result = df.select_dtypes(include="number").apply(
#     lambda col: col.max(),
#     axis=0
# )
# print(result)

# 7. Custom Function

# df["Discounted_Sales"] = df["Sales"].apply(discount)
# print(df)

# Practice Q1 — 
# Price પર 15% discount માટે discount() function બનાવો અને Final_Price column બનાવો.

# def discount(x):
#     return x * 0.85

# df["Final_Price"] = df["Price"].apply(discount)
# print(df)

# 8. std()

# Practice Q1 — 
# Sales નું standard deviation find કરો.

# result = df["Sales"].std()
# print(result)

# Practice Q2 — 
# Profit નું standard deviation find કરો.

# result = df["Profit"].std()
# print(result)

# 9. var()

# Practice Q1 — 
# Sales નું variance find કરો.

# result = df["Sales"].var()
# print(result)

# Practice Q2 — 
# Quantity નું variance find કરો.

# result = df["Quantity"].var()
# print(result)

# 10. quantile()

# Practice Q1 — 
# Sales નો 75th percentile find કરો.

# result = df["Sales"].quantile(0.75)
# print(result)

# Practice Q2 — 
# Sales નો 25th percentile find કરો.

# result = df["Sales"].quantile(0.25)
# print(result)

# 11. nunique()

# Example
# print(df["City"].nunique())

# Practice Q1 — 
# Category માં કેટલા unique categories છે તે find કરો.

# print(df["Category"].nunique())

# Practice Q2 — 
# City માં કેટલા unique cities છે તે find કરો.

# print(df["City"].nunique())

# 12. prod()

# Practice Q1 —
# Quantity column નો product find કરો.

# result = df["Quantity"].prod()
# print(result)

# Practice Q2 — 
# આ values નો product find કરો:
# [2, 3, 4, 5]
# using Pandas prod().

# import pandas as pd
# data = pd.Series([2, 3, 4, 5])
# result = data.prod()
# print(result)

# indexing 

# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# print(df)

# Pandas Indexing — Topics
# 1. set_index()

# Practice Q1:
# Order_ID ને DataFrame નો index બનાવો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# result = df.set_index("Order_ID")
# print(result)

# Practice Q2:
# Customer_ID ને index બનાવીને DataFrame print કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# result = df.set_index("Customer")
# print(result)

# 2. reset_index()

# Practice Q1:
# Order_ID ને index બનાવ્યા પછી તેને પાછો normal column બનાવો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.reset_index()
# print(result)

# Practice Q2:
# Current index ને reset કરો અને old index ને પણ DataFrameમાં રાખો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.reset_index(drop=True)
# print(result)

# 3. MultiIndex
# df.set_index(["City", "Category"])

# Practice Q1:
# City અને Category ને MultiIndex બનાવો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index(["City", "Category"])
# print(df)

# Practice Q2:
# City → Category → Product ના 3-level MultiIndex બનાવો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index(["City", "Category", "Product"])
# print(df)

# 4. sort_index()

# Practice Q1:
# Order_ID ને index બનાવીને ascending orderમાં sort કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.sort_index()
# print(result)

# Practice Q2:
# Order_ID ને index બનાવીને descending orderમાં sort કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.sort_index(ascending=False)
# print(result)

# 5. Index Selection — loc[]

# Syntax:
# df.loc[101]

# Multiple labels:
# df.loc[[101, 103]]

# Practice Q1:
# Order_ID ને index બનાવીને Order_ID = 103 ની row select કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.loc[103]
# print(result)

# Practice Q2:
# Order_ID = 102, 105, 108 ની rows loc[] થી select કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.loc[[102, 105, 108]]
# print(result)

# 6. Index Renaming
# Syntax:
# df.rename(index={101: "Order_101"})

# Multiple:
# df.rename(index={
#     101: "Order_101",
#     102: "Order_102"
# })

# Practice Q1:
# Index 101 ને "Order_101" અને 102 ને "Order_102" rename કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# df = df.rename(index={101: "Order_101",
#                       102: "Order_102"})
# print(df)

# Practice Q2:
# Index 105 ને "Order_105" rename કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# df = df.rename(index={105: "Order_105"})
# print(df)

# 7. Index Filtering

# Practice Q1:
# Index 103 કરતા મોટા હોય તેવી બધી rows filter કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.loc[df.index > 103]
# print(result)

# Practice Q2:
# Index 105 કરતા નાના હોય તેવી rows filter કરો.
# df = pd.read_excel("D:\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# result = df.loc[df.index < 105]
# print(result)

# working with duplicate

import pandas as pd

data = {
    "Customer_ID": [101, 102, 103, 102, 104, 105, 103, 106],
    "Customer_Name": ["Amit", "Riya", "Raj", "Riya", "Neha", "Karan", "Raj", "Meera"],
    "City": ["Surat", "Ahmedabad", "Mumbai", "Ahmedabad", "Vadodara", "Surat", "Mumbai", "Rajkot"],
    "Amount": [2500, 3200, 1800, 3200, 4500, 2100, 1800, 3900]
}

df = pd.DataFrame(data)
print(df)

# # 1. Detecting Duplicate Rows

# Practice Question 1
# Dataset માં કઈ rows duplicate છે તે શોધો.
# result = df[df.duplicated()]
# print(result)

# Practice Question 2
# Duplicate rows ની count શોધો.
# result = df.duplicated().sum()
# print(result)

# 2. Duplicate Rows by Specific Columns

# Practice Question 1
# Customer_ID ના duplicates શોધો.
# print(df.duplicated(subset=["Customer_ID"]))

# Practice Question 2
# Customer_ID અને City ના combination માં duplicates શોધો.
# result = df[df.duplicated(subset=["Customer_ID", "City"])]
# print(result)


# 3. Keep First Duplicate

# Practice Question 1
# Customer_ID ના duplicate values માટે first occurrence keep કરીને duplicate rows identify કરો.

# result = df[df.duplicated(subset=["Customer_ID"], keep="first")]
# print(result)

# Practice Question 2
# Customer_ID અને Customer_Name પ્રમાણે first occurrence રાખીને duplicates શોધો.
# result = df[df.duplicated(subset=["Customer_ID", "Customer_Name"],keep="first")]
# print(result)

# 4. Keep Last Duplicate

# જો duplicate group માં last occurrence ને original રાખવી હોય, તો:

# Syntax
# df.duplicated(keep="last")

# Example:
# print(df.duplicated(keep="last"))

# Practice Question 1
# Customer_ID માટે last occurrence રાખીને duplicate rows identify કરો.
# result = df[df.duplicated(subset=["Customer_ID", "Customer_Name"],keep="last")]
# print(result)

# Practice Question 2
# Customer_ID અને City માટે keep="last" નો ઉપયોગ કરો.
# result = df[df.duplicated(subset=["Customer_ID", "City"],keep="last")]
# print(result)

# 5. Removing Duplicates

# Practice Question 1
# Complete duplicate rows remove કરીને નવી DataFrame બનાવો.
# new_df = df.drop_duplicates()
# print(new_df)

# Practice Question 2
# Duplicate rows remove કરીને remaining rows display કરો.
# row = df.drop_duplicates()
# print(row)


# 6. Keep First While Removing

# Example:

# new_df = df.drop_duplicates(keep="first")
#  print(new_df)

# Practice Question 1
# Customer_ID ના duplicates માં first occurrence રાખીને duplicates remove કરો.
# result = df.drop_duplicates(subset=["Customer_ID"],keep="first")
# print(result)

# Practice Question 2
# Customer_ID અને Customer_Name પ્રમાણે duplicates remove કરો અને first record રાખો.
# result = df.drop_duplicates(subset=["Customer_ID", "Customer_Name"],keep="first")
# print(result)

# 7. Keep Last While Removing

# Example
# new_df = df.drop_duplicates(keep="last")
# print(new_df)

# Practice Question 1
# Duplicate rows remove કરો અને દરેક duplicate group ની last occurrence રાખો.
# result = df.drop_duplicates(keep="last")
# print(result)

# Practice Question 2
# Customer_ID પ્રમાણે duplicates remove કરીને last occurrence રાખો.
# result = df.drop_duplicates(subset=["Customer_ID"],keep="last")
# print(result)

# 8. Remove Duplicates by Specific Columns ⭐

# Practice Question 1
# Customer_ID ના basis પર duplicates remove કરો અને first occurrence રાખો.
# result = df.drop_duplicates(
#     subset=["Customer_ID"],
#     keep="first"
# )

# print(result)

# Practice Question 2
# Customer_ID ના basis પર duplicates remove કરો અને last occurrence રાખો.
# result = df.drop_duplicates(
#     subset=["Customer_ID"],
#     keep="last"
# )
# print(result)

