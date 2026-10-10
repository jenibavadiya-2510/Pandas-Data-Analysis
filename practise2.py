# advanced operations

import pandas as pd
# df = pd.read_csv("sales.csv")
# print(df)

# 1. explode()

# Practice 1 :Skills column ને explode કરો.
# df = pd.read_csv("sales.csv")
# df["Skills"] = df["Skills"].str.split(",")
# result = df.explode("Skills")
# print(result)

# Practice 2 :Explode કર્યા પછી માત્ર Employee અને Skills columns display કરો.
# df = pd.read_csv("Sales.csv")
# df["Skills"] = df["Skills"].str.split(",")
# result = df.explode("Skills")[["Employee", "Skills"]]
# print(result)

# 2. melt()

# Practice 1
# Jan, Feb, Mar ને Month column માં convert કરો.
# df = pd.read_csv("sales.csv")
# result = df.melt(
#     id_vars=["Employee", "Department", "Skills"],
#     value_vars=["Jan", "Feb", "Mar"],
#     var_name="Month",
#     value_name="Sales"
# )
# print(result)

# Practice 2
# Long format બનાવો જેમાં columns હોય:
# Employee
# Month
# Sales

# df = pd.read_csv("sales.csv")
# result = df.melt(
#     id_vars=["Employee"],
#     value_vars=["Jan", "Feb", "Mar"],
#     var_name="Month",
#     value_name="Sales"
# )
# print(result)

# 3. stack()

# Practice 1
# Employee ને index બનાવીને Jan, Feb, Mar ને stack કરો.
# df = pd.read_csv("sales.csv")
# small_df = df[["Employee", "Jan", "Feb", "Mar"]]
# result = small_df.set_index("Employee").stack()
# print(result)

# Practice 2
# Employee અને Department રાખીને monthly sales ને stack કરો.
# df = pd.read_csv("sales.csv")
# result = df.set_index(["Employee", "Department"])[["Jan", "Feb", "Mar"]].stack()
# print(result)

# 4. unstack()

# Practice 1
# Stacked data ને પાછું columns માં convert કરો.
# df = pd.read_csv("sales.csv")
# small_df = df[["Employee", "Jan", "Feb", "Mar"]]
# stacked = small_df.set_index("Employee").stack()
# result = stacked.unstack()
# print(result)

# Practice 2
# Department અને Employee ને index બનાવીને data unstack() કરો.
# df = pd.read_csv("sales.csv")
# result = df.set_index(["Employee", "Department"])[["Jan", "Feb", "Mar"]].stack()
# r = result.unstack()
# print(r)

# 5. transpose()

# Practice 1
# Employee, Jan, Feb, Mar columns નું transpose કરો.
# df = pd.read_csv("sales.csv")
# small_df = df[["Employee", "Jan", "Feb", "Mar"]]
# result = small_df.T
# print(result)

# Practice 2
# Transpose કર્યા પછી resulting DataFrame display કરો.
# df = pd.read_csv("sales.csv")
# small_df = df[["Employee", "Jan", "Feb", "Mar"]]
# result = small_df.transpose()
# print(result)

# 6. clip()

# Practice 1
# Feb sales માટે minimum 14000 અને maximum 20000 રાખીને clip કરો.
# df = pd.read_csv("sales.csv")
# df["Feb_Clipped"] = df["Feb"].clip(
#     lower=14000,
#     upper=30000
# )
# print(df)

# Practice 2
# Mar sales ને 15000 થી 22000 વચ્ચે clip કરો.
# df = pd.read_csv("sales.csv")
# df["Mar_Clipped"] = df["Mar"].clip(
#    lower= 15000,
#    upper= 22000
# )
# print(df)

# 7. pivot() vs melt()

# Practice 1 — Melt
# આપણા original df ને long format માં convert કરો.
# df = pd.read_csv("sales.csv")

# long_df = df.melt(
#     id_vars=["Employee", "Department", "Skills"],
#     value_vars=["Jan", "Feb", "Mar"],
#     var_name="Month",
#     value_name="Sales"
# )

# print(long_df)

# Practice 2 — Pivot
# Melt થયેલા data ને પાછું wide format માં convert કરો.
# df = pd.read_csv("sales.csv")

# long_df = df.melt(
#     id_vars=["Employee", "Department", "Skills"],
#     value_vars=["Jan", "Feb", "Mar"],
#     var_name="Month",
#     value_name="Sales"
# )

# print(long_df)

# wide_df = long_df.pivot(
#     index=["Employee", "Department", "Skills"],
#     columns="Month",
#     values="Sales"
# )

# print(wide_df)

# Multiindex
# import pandas as pd
# df = pd.read_csv("sales_multiindex.csv")
# print(df)

# 1. MultiIndex — Region → Category

# Example
# result = df.set_index(["Region", "Category"])
# print(result)

# Practice 1
# Region અને Category ને MultiIndex બનાવો.
# df = pd.read_csv("sales_multiindex.csv")
# result = df.set_index(["Region", "Category"])
# print(result)

# Practice 2
# MultiIndex બનાવ્યા પછી માત્ર Sales અને Profit columns display કરો.
# df = pd.read_csv("sales_multiindex.csv")
# result = df.set_index(["Sales", "Profit"])
# print(result)

# 2. Multi-Level Columns — Sales → Amount, Profit

# Example:

# report = df.pivot_table(
#     index="Region",
#     columns="Category",
#     values=["Amount", "Profit"]
# )
# print(report)

# Practice 1 Region ને index અને Amount, Profit ને values રાખીને Category પ્રમાણે grouped columns બનાવો.
# df = pd.read_csv("sales_multiindex.csv")
# report = df.pivot_table(
#     index = "Region",
#     columns="Category",
#     values=["Amount", "Profit"]
# )
# print(report)

# Practice 2
# Sales અને Profit બંને માટે Region → Category based report બનાવો.
# df = pd.read_csv("sales_multiindex.csv")
# report = df.pivot_table(
#     index = "Region",
#     columns="Category",
#     values=["Amount", "Profit"]
# )
# print(report)

# 3. Creating MultiIndex — Region + Category as Index

# Practice 1
# Region અને Category ને index બનાવીને complete DataFrame display કરો.
# df = pd.read_csv("sales_multiindex.csv")
# result = df.set_index(["Region", "Category"])
# print(result)

# Practice 2
# MultiIndex બનાવ્યા પછી Amount column display કરો.
# df = pd.read_csv("sales_multiindex.csv")
# result = df.set_index(["Region", "Category", "Amount"])
# print(result)

# 4. IndexSlice — Select West → Laptop

# Practice 1
# West → Laptop નો Sales data select કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# idx = pd.IndexSlice
# result = df.loc[idx["West", "Laptop"], "Sales"]
# print(result)

# Practice 2
# East → Mobile નો Amount અને Profit select કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# idx = pd.IndexSlice
# result = df.loc[idx["East", "Mobile"], "Sales"]
# print(result)

# 5. swaplevel() — Category → Region

# Practice 1
# Region → Category ને Category → Region માં change કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# result = df.swaplevel("Category", "Region")
# print(result)

# 6. droplevel() — Remove Category Level

# Practice 1
# Category level remove કર્યા પછી Sales અને Profit display કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# result = df.droplevel("Category")[["Sales", "Profit"]]
# print(result)


# 7. Selecting MultiIndex Data — Only West

# Practice 1
# માત્ર West region નો complete data select કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# result = df.loc["West"]
# print(result)

# Practice 2
# માત્ર South region નો Sales અને Profit data select કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# result = df.loc["South", ["Sales", "Profit"]]
# print(result)

# 8. Sorting MultiIndex

# Practice 1
# Region અને Category બંને પ્રમાણે MultiIndex sort કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# result = df.sort_index()
# print(result)

# Practice 2
# Category level પ્રમાણે descending order માં sort કરો.
# df = pd.read_csv("sales_multiindex.csv")
# df = df.set_index(["Region", "Category"])
# result = df.sort_index(
#     level = "Category",
#     ascending=False
# )
# print(result)

# Windows function
# import pandas as pd

# data = {
#     "Day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "Sales": [1000, 1500, 1200, 1800, 2000, 1700, 2200, 2500, 2100, 2800]
# }
# df = pd.DataFrame(data)
# print(df)

# 1. rolling()
# Practice 1
# Last 3 days ની sales નો total શોધો.
# df = pd.DataFrame(data)
# df["Rolling_sum"] = df["Sales"].rolling(window=3).sum()
# print(df)

# Practice 2
# Last 4 days ની sales નો total શોધો.
# df = pd.DataFrame(data)
# df["Rolling_sum"] = df["Sales"].rolling(window=4).sum()
# print(df)

# 2. expanding()
# Practice 1
# Business start થી અત્યાર સુધીનું total sales calculate કરો.
# df = pd.DataFrame(data)
# df["Total_Sales"] = df["Sales"].expanding().sum()
# print(df)

# Practice 2
# expanding() નો ઉપયોગ કરીને running average sales calculate કરો.
# df = pd.DataFrame(data)
# df["Avg_sales"] = df["Sales"].expanding().mean()
# print(df)

# 3. cumsum()

# Practice 1
# Running sales total બનાવો.
# df = pd.DataFrame(data)
# df["Running_total"] = df["Sales"].cumsum()
# print(df)

# Practice 2
# cumsum() વડે Day 7 સુધીની total sales શોધો.
# df = pd.DataFrame(data)
# df["Cum_sum"] = df["Sales"].cumsum()
# print(df)

# 4. cumprod()

# Practice 1
# આ monthly growth factors માટે compounded growth calculate કરો:
# growth = pd.Series([1.05, 1.10, 1.03, 1.06])
# result = growth.cumprod()
# print(result)

# Practice 2
# આ growth factors માટે cumprod() calculate કરો:

# growth = pd.Series([1.02, 1.04, 1.03, 1.05, 1.02])
# result = growth.cumprod()
# print(result)

# 5. cummax()
# Practice 1
# Highest daily sales so far calculate કરો.

# df = pd.DataFrame(data)
# df["Highest_sales"] = df["Sales"].cummax()
# print(df)

# Practice 2
# cummax() નો ઉપયોગ કરીને record-high sales track કરો.

# df = pd.DataFrame(data)
# df["High_sale"] = df["Sales"].cummax()
# print(df)

# 6. cummin()
# Practice 1
# Lowest daily sales so far calculate કરો.

# df = pd.DataFrame(data)
# df["Low_sales"] = df["Sales"].cummin()
# print(df)

# Practice 2
# cummin() નો ઉપયોગ કરીને lowest performance track કરો.
# df = pd.DataFrame(data)
# df["Low_Performance"] = df["Sales"].cummin()
# print(df)

# 7. rolling().mean()

# Practice 1
# Last 3 days ની average sales calculate કરો.
# df = pd.DataFrame(data)
# df["Last_day"] = df["Sales"].rolling(window=3).mean()
# print(df)

# Practice 2
# Last 5 days ની average sales calculate કરો.
# df = pd.DataFrame(data)
# df["Last_day"] = df["Sales"].rolling(window=5).mean()
# print(df)

# 8. rolling().sum()

# Practice 1
# Last 3 days ની total sales calculate કરો.
# df = pd.DataFrame(data)
# df["Last_day"] = df["Sales"].rolling(window=3).sum()
# print(df)

# Practice 2
# Last 5 days ની total sales calculate કરો.
# df = pd.DataFrame(data)
# df["Last_day"] = df["Sales"].rolling(window=5).sum()
# print(df)

# 9. rolling().max()
# Practice 1
# Last 3 days ની highest sales શોધો.
# df = pd.DataFrame(data)
# df["Highest_sale"] = df["Sales"].rolling(window=3).max)
# print(df)

# Practice 2
# Last 5 days ની highest sales શોધો.
# df = pd.DataFrame(data)
# df["Highest_sale"] = df["Sales"].rolling(window=5).max()
# print(df)

# 10. rolling().min()

# practise 1
# Last 3 days ની lowest sales શોધો.
# df = pd.DataFrame(data)
# df["Lowest_sale"] = df["Sales"].rolling(window=3).min()
# print(df)   

# Practice 2
# Last 5 days ની lowest sales શોધો.
# df = pd.DataFrame(data)
# df["Lowest_sale"] = df["Sales"].rolling(window=5).min()
# print(df)  

# Ranking & statistic

data = {
 "Date": ["2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04", "2026-08-05"],
 "Sales": [10000, 12000, 9000, 15000, 18000],
 "Advertising": [2000, 2500, 1800, 3000, 3500],
 "Profit": [2000, 2800, 1500, 4000, 5000]
}
df = pd.DataFrame(data)
print(df)

# 1. rank()

# Practice 1
# Sales પ્રમાણે highest sales ને Rank 1 આપો.
# df = pd.DataFrame(data)
# df["Sales_rank"] = df["Sales"].rank()
# print(df)

# Practice 2
# Profit પ્રમાણે employees/customers ને highest profitથી lowest profit rank કરો.
# df = pd.DataFrame(data)
# df["Profit_rank"] = df["Profit"].rank(ascending=False)
# print(df)

# 2. pct_change()

# Practice 1
# Day-to-day Sales percentage change calculate કરો.
# df = pd.DataFrame(data)
# result = df["Sales"].pct_change()
# print(result)

# Practice 2
# Day-to-day Profit percentage growth/decline calculate કરો.
# Profit = [2000, 2800, 1500, 4000, 5000]
# df["Profit_Growth"] = df["Profit"].pct_change() * 100
# print(df)

# 3. diff()

# Practice 1
# દરેક દિવસની Sales માં previous day કરતાં કેટલો actual change થયો તે શોધો.

# df = pd.DataFrame(data)
# result = df["Sales"].diff()
# print(result)

# Practice 2
# દરેક દિવસના Profit માં previous day કરતાં actual difference શોધો.

# df = pd.DataFrame(data)
# result = df["Profit"].diff()
# print(result)

# 4. shift()

# Practice 1
# નવી Previous_Sales column બનાવો જેમાં દરેક દિવસની previous day's Sales આવે.

# df = pd.DataFrame(data)
# df["Previous_sales"] = df["Sales"].shift(1)
# print(df)

# Practice 2
# નવી Previous_Profit column બનાવો જેમાં previous day's Profit આવે.
# df = pd.DataFrame(data)
# df["Previous_profit"] = df["Profit"].shift(1)
# print(df)

# 5. corr()

# Real-time use: Advertising spending અને Sales વચ્ચે relationship check કરવી.

# Syntax
# df["Advertising"].corr(df["Sales"])

# Practice 1
# Advertising અને Sales વચ્ચે correlation calculate કરો.
# df = pd.DataFrame(data)
# result = df["Advertising"].corr(df["Sales"])
# print(result)

# Practice 2
# Advertising અને Profit વચ્ચે correlation calculate કરો.
# df = pd.DataFrame(data)
# result = df["Advertising"].corr(df["Profit"])
# print(result)

# 6. cov()

# Practice 1
# Advertising અને Sales વચ્ચે covariance calculate કરો.
# df = pd.DataFrame(data)
# result = df["Advertising"].cov(df["Sales"])
# print(result)

# Practice 2
# Advertising અને Profit વચ્ચે covariance calculate કરો.
# df = pd.DataFrame(data)
# result = df["Advertising"].cov(df["Profit"])
# print(result)

# 7. Percentage Change Analysis

# Practice 1
# Sales percentage change calculate કરીને નવી column બનાવો:
# Sales_Growth

# df = pd.DataFrame(data)
# df["Sales_Growth"] = df["Sales"].pct_change() * 100
# print(df)


# 8. Previous / Next Value Analysis

# Practice 1
# Previous_Sales column બનાવો જેમાં previous day's Sales આવે.
# df = pd.DataFrame(data)
# result = df["Sales"].shift(1)
# print(result)

# Practice 2
# Next_Sales column બનાવો જેમાં next day's Sales આવે.
# df = pd.DataFrame(data)
# result = df["Sales"].shift(-1)
# print(result)

# Resampling

# import pandas as pd

# data = {
#     "Date": [
#         "2026-01-01", "2026-01-05", "2026-01-12", "2026-01-20",
#         "2026-02-02", "2026-02-10", "2026-02-18", "2026-02-25",
#         "2026-03-03", "2026-03-12", "2026-03-20", "2026-03-28",
#         "2026-04-05", "2026-04-15", "2026-04-25",
#         "2026-05-05", "2026-05-15", "2026-05-25",
#         "2026-06-05", "2026-06-15", "2026-06-25",
#         "2026-07-05", "2026-07-15", "2026-07-25",
#         "2026-08-05", "2026-08-15", "2026-08-25",
#         "2026-09-05", "2026-09-15", "2026-09-25",
#         "2026-10-05", "2026-10-15", "2026-10-25",
#         "2026-11-05", "2026-11-15", "2026-11-25",
#         "2026-12-05", "2026-12-15", "2026-12-25"
#     ],
#     "Sales": [
#         10000, 12000, 11000, 14000,
#         13000, 15000, 16000, 17000,
#         14000, 15500, 16500, 18000,
#         19000, 20000, 21000,
#         18000, 19500, 22000,
#         23000, 24000, 25000,
#         21000, 22500, 24000,
#         26000, 27500, 29000,
#         25000, 27000, 28500,
#         30000, 31500, 33000,
#         28000, 30000, 32000,
#         34000, 35500, 37000
#     ]
# }

# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# print(df)

# 1. resample()

# Practice 1
# Daily sales ને monthly sales માં convert કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# result = df.resample("ME")["Sales"].sum()
# print(result)

# Practice 2
# Daily sales ને monthly average sales માં convert કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# result = df.resample("ME")["Sales"].mean()
# print(result)

# 2. Daily → Monthly

# Practice 1
# દરેક month ની total sales calculate કરો.

# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# result = df.resample("ME")["Sales"].sum()
# print(result)

# Practice 2
# દરેક month ની highest daily sales શોધો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# result = df.resample("ME")["Sales"].max()
# print(result)

# 3. Monthly → Yearly

# Practice 1
# 2026 ની total yearly sales calculate કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# result = df.resample("YE")["Sales"].sum()
# print(result)

# Practice 2
# Yearly average sales calculate કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# result = df.resample("YE")["Sales"].mean()
# print(result)

# 4. Frequency Conversion — Daily → Weekly

# Practice 1
# દરેક week ની total sales calculate કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# weekly_sales = df.resample("W")["Sales"].sum()
# print(weekly_sales)

# Practice 2
# દરેક week ની average sales calculate કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# weekly_sales = df.resample("W")["Sales"].mean()
# print(weekly_sales)

# 5. Monthly Sales Analysis

# Practice 1
# Monthly total sales calculate કરો અને result display કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# monthly_sales = df.resample("ME")["Sales"].sum()
# print(monthly_sales)


# Practice 2
# Monthly sales માંથી highest-sales month શોધો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# monthly_sales = df.resample("W")["Sales"].max()
# print(monthly_sales)

# 6. Quarterly Analysis

# Practice 1
# દરેક quarter ની total sales calculate કરો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# quarterly_sales = df.resample("QE")["Sales"].sum()
# print(quarterly_sales)

# Practice 2
# કયો quarter highest total sales ધરાવે છે તે શોધો.
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# quarterly_sales = df.resample("QE")["Sales"].max()
# print(quarterly_sales)


# 7. Yearly Analysis

# Practice 1
# Yearly total sales calculate કરો.

# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# yearly_sales = df.resample("YE")["Sales"].max()
# print(yearly_sales)

# Practice 2
# Yearly sales નો maximum અને minimum value શોધો.

# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# yearly_sales = df.resample("YE")["Sales"].max()
# yearly_sales1 = df.resample("YE")["Sales"].min()
# print(yearly_sales)
# print(yearly_sales1)

# Categorial data

# category dtype
# Customer_Type માં repeated values છે, એટલે તેને categorical data માં convert કરી શકાય.

# Practice 1
# Customer_Type column ને category dtype માં convert કરો.
# df = pd.DataFrame(data)
# df["Customer_Type"] = df["Customer_Type"].astype("category")
# print(df)

# Practice 2
# Customer_Type નો dtype check કરો.
# df = pd.DataFrame(data)
# df["Customer_Type"] = df["Customer_Type"].astype("category")
# print(df["Customer_Type"].dtype)

# 2. cut()

# Practice 1
# Age_Group નામની નવી column બનાવો જેમાં Teen, Young, Adult categories હોય.
# df = pd.DataFrame(data)
# df["Age_Group"] = pd.cut(df["Age"], bins=[0, 18, 35, 60],
#                          labels=["Teen", "Young", "Adult"])
# print(df)

# Practice 2
# દરેક Age Group માં કેટલા customers છે તે શોધો.
# df = pd.DataFrame(data)
# df["Age_Group"] = pd.cut(df["Age"], bins=[0, 18, 35, 60],
#                          labels=["Teen", "Young", "Adult"])
# result = df["Age_Group"].value_counts()
# print(result)

# 3. qcut()

# Practice 1
# Sales ને 3 equal-sized groups માં divide કરીને Sales_Group column બનાવો.
# df = pd.DataFrame(data)
# df["Sales_group"] = pd.qcut(df["Sales"], q=3,
#                          labels=["Low", "Medium", "High"])
# print(df)

# Practice 2
# દરેક Sales Group માં કેટલા customers છે તે count કરો.
# df = pd.DataFrame(data)
# df["Sales_group"] = pd.qcut(df["Sales"], q=3,
#                          labels=["Low", "Medium", "High"])
# result = df["Sales_group"].value_counts()
# print(result)

# 4. Creating Categories
# Numerical Sales data ને meaningful categories માં convert કરવી.

# Practice 1
# Sales_Group બનાવો:

# Low
# Medium
# High
# qcut() નો ઉપયોગ કરો.
# df = pd.DataFrame(data)
# df["Sales_Group"] = pd.qcut(df["Sales"], q=3,
#                             labels=["Low","Medium","High"])

# print(df)

# Practice 2
# માત્ર Customer, Sales અને Sales_Group columns display કરો.
# df = pd.DataFrame(data)
# df["Sales_Group"] = pd.qcut(df["Sales"], q=3,
# labels=["Low","Medium","High"])
# result = df[["Customer", "Sales", "Sales_Group"]]
# print(result)

# 5. Category Ordering
# Default alphabetical order ના બદલે:
# Low → Medium → High
# logical order બનાવવો.

# Practice 1
# Sales_Group ને ordered categorical બનાવો:
# df = pd.DataFrame(data)
# df["Sales_Group"] = pd.qcut(
#     df["Sales"],
#     q=3,
#     labels=["Low", "Medium", "High"]
# )
# df["Sales_Group"] = pd.Categorical(
#     df["Sales_Group"],
#     categories=["Low", "Medium", "High"],
#     ordered=True
# )

# print(df["Sales_Group"])

# 6. Category Memory Optimization
# Categorical dtype repeated values માટે memory usage ઓછું કરવામાં મદદ કરી શકે છે.

# Practice 1
# Customer_Type ને categorical dtype માં convert કરો અને DataFrame નો memory usage check કરો.
# df = pd.DataFrame(data)
# df["Customer_Type"] = df["Customer_Type"].astype("category")
# print(df)

# Practice 2
# Customer_Type column નું memory usage પહેલાં અને પછી check કરો.
# df = pd.DataFrame(data)

# # Before
# before = df["Customer_Type"].memory_usage(deep=True)

# # Convert to category
# df["Customer_Type"] = df["Customer_Type"].astype("category")

# # After
# after = df["Customer_Type"].memory_usage(deep=True)

# print("Before:", before, "bytes")
# print("After :", after, "bytes")

# Missing value strategies

# data = {
#  "Employee": ["Rahul", "Amit", "Neha", "Priya", "Vivek", "Riya"],
#  "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT"],
#  "Salary": [30000, None, 40000, 45000, None, 50000],
#  "Experience": [2, 3, None, 5, 4, None]
# }
# df = pd.DataFrame(data)
# print(df)

# 1.ffill()
# Previous available value થી missing value fill કરે છે.

# Practice 1
# Salary column માં missing values ને previous salary વડે fill કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].ffill()
# print(df)

# Practice 2
# Experience column માં missing values ને previous available experience વડે fill કરો.
# df = pd.DataFrame(data)
# df["Experience"] = df["Experience"].ffill()
# print(df)

# 2. bfill()
# Next available value થી missing value fill કરે છે.

# Practice 1
# Salary column ની missing values ને next available salary વડે fill કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].bfill()
# print(df)

# Practice 2
# Experience column ની missing values ને next available experience વડે fill કરો.
# df = pd.DataFrame(data)
# df["Experience"] = df["Experience"].bfill()
# print(df)

# 3. Interpolation
# બે known values વચ્ચે missing value estimate કરે છે.

# Practice 1
# Experience column ની missing values ને interpolate() નો ઉપયોગ કરીને fill કરો.
# df = pd.DataFrame(data)
# df["Experience"] = df["Experience"].interpolate()
# print(df)

# Practice 2
# Interpolation પછી Employee અને Experience columns display કરો.
# df = pd.DataFrame(data)
# df["Experience"] = df["Experience"].interpolate()
# print(df[["Employee", "Experience"]])

# 4. Mean Filling
# Missing numerical value ને column ના average વડે fill કરે છે.

# Practice 1
# Salary ની missing values ને mean salary વડે fill કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df)

# Practice 2
# Mean filling પછી Employee અને Salary columns display કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df[["Employee", "Salary"]])

# 5. Median Filling
# Outliers હોય ત્યારે median useful છે.

# Practice 1
# Salary ની missing values ને median salary વડે fill કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# print(df)

# Practice 2
# Median filling પછી complete DataFrame display કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df)

# 6. Mode Filling
# Categorical column ની missing value ને સૌથી frequently occurring value વડે fill કરે છે.

# Practice 1
# Department માં જો missing value હોય તો તેને mode department વડે fill કરો.
# df = pd.DataFrame(data)
# df["Department"] = df["Department"].fillna(df["Department"].mode())
# print(df)

# Practice 2
# Department નો mode શોધો અને display કરો.
# df = pd.DataFrame(data)
# df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
# print(df["Department"])

# 7. Group-Based Missing Value Filling
# અહીં missing value આખા DataFrame ના mean થી નહીં, પરંતુ group પ્રમાણે fill કરવામાં આવે છે.

# Practice 1
# દરેક Department પ્રમાણે average Salary calculate કરીને તે Department ની missing Salary fill કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].fillna(df.groupby("Department")["Salary"].transform("mean"))
# print(df)

# Practice 2
# દરેક Department પ્રમાણે median Salary નો ઉપયોગ કરીને missing Salary fill કરો.
# df = pd.DataFrame(data)
# df["Salary"] = df["Salary"].fillna(
#     df.groupby("Department")["Salary"].transform("median")
# )

# print(df)


# Data validation

data = {
 "Order_ID": [101, 102, 103, 103, 104, 105],
 "Customer": ["Rahul", "Amit", "Neha", "Neha", "Priya", "Vivek"],
 "Sales": [10000, 15000, None, 12000, 18000, 20000],
 "Quantity": [2, 3, 1, 1, 4, 5],
 "Status": [
 "Completed",
 "Pending",
 "Completed",
 "Completed",
 "Cancelled",
 "Completed"
 ]
}
df = pd.DataFrame(data)
print(df)

# 1. duplicated()

# Q1. Check કરો કે કોઈ Order_ID repeat થયો છે કે નહીં.
# df = pd.DataFrame(data)
# print(df[df["Order_ID"].duplicated()])

# Q2. Customer column માં duplicate values check કરો.
# df = pd.DataFrame(data)
# print(df[df["Customer"].duplicated()])

# 2. equals()

# Q1. df ની copy બનાવો અને check કરો કે બંને DataFrames exactly same છે કે નહીં.
# df = pd.DataFrame(data)
# df_copy = df.copy()
# result = df.equals(df_copy)
# print(result)

# Q2. df_copy માં એક Sales value change કરો અને ફરી equals() થી check કરો.
# df_copy = df.copy()

# # Sales value change કરો
# df_copy.loc[0, "Sales"] = 50000

# # Check કરો
# result = df.equals(df_copy)
# print(result)

# 3. compare()

# Q1. df ની copy બનાવીને એક Sales value change કરો અને compare() થી difference શોધો.
# df = pd.DataFrame(data)
# df_copy = df.copy()
# df_copy.loc[0, "Sales"] = 50000
# result = df.compare(df_copy)
# print(result)

# Q2. df_copy માં Status ની એક value change કરો અને બંને DataFrames compare કરો.
# df = pd.DataFrame(data)
# df_copy = df.copy()
# df_copy.loc[1, "Status"] = "Completed"
# result = df.compare(df_copy)
# print(result)

# 4. Compare Two DataFrames

# Q1. Current sales report અને previous sales report તરીકે df અને df_previous બનાવો અને check કરો કે બંને same છે કે નહીં.
# df = pd.DataFrame(data)
# df_previous = df.copy()
# result = df.equals(df_previous)
# print(result)

# Q2. Previous report માં Quantity ની એક value change કરીને compare() થી changes શોધો.
# df = pd.DataFrame(data)
# df_previous = df.copy()
# df_previous.loc[1, "Quantity"] = 2
# result = df.equals(df_previous)
# print(result)

# 5. Check Missing Values — isnull()

# Q1. Dataset માં દરેક column માં કેટલા missing values છે તે શોધો.
# df = pd.DataFrame(data)
# result = df.isnull().sum()
# print(result)

# Q2. ખાસ કરીને Sales column માં કોઈ missing value છે કે નહીં check કરો.
# df = pd.DataFrame(data)
# result = df["Sales"].isnull().any()
# print(result)

# 6. Check Data Types — dtypes

# Q1. બધા columns ના datatypes display કરો.
# df = pd.DataFrame(data)
# print(df.dtypes)

# Q2. Check કરો કે Sales અને Quantity numeric datatype માં છે કે નહીં.
# df = pd.DataFrame(data)
# print(pd.api.types.is_numeric_dtype(df["Sales"]))
# print(pd.api.types.is_numeric_dtype(df["Quantity"]))

# 7. Validate Column Names

# Required columns:
# ["Order_ID", "Customer", "Sales", "Quantity", "Status"]

# Q1. Check કરો કે બધા required columns DataFrame માં present છે કે નહીં.
# df = pd.DataFrame(data)
# result = set(["Order_ID","Customer","Sales","Quantity","Status"]).issubset(df.columns)
# print(result)

# Q2. "Profit" ને required columns માં add કરીને check કરો કે હવે બધા required columns present છે કે નહીં.
# required_columns = [
#     "Order_ID", "Customer", "Sales", "Quantity", "Sales", "Profit"
# ]
# result = set(required_columns).issubset(df.columns)
# print(result)

# 8. Validate Unique Values

# Status માં valid values:

# Completed
# Pending
# Cancelled

# Q1. Status column માં કઈ-કઈ unique values છે તે શોધો.
# df = pd.DataFrame(data)
# result = df["Status"].isin(["Completed", "Pending", "Cancelled"]).all()
# print(result)

# Q2. Check કરો કે Status column માં આપેલા ત્રણ valid statuses સિવાય કોઈ બીજું value છે કે નહીં.
# df = pd.DataFrame(data)
# valid_status = ["Completed", "Pending", "Cancelled"]
# result = ~df["Status"].isin(valid_status)
# print(result)