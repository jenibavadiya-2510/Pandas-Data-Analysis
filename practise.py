import pandas as pd

# Pandas : Topic 1
# Point 1: Pandas su che?

# Pandas Python ni library che je mainly data analysis ane data cleaning mate use thay che.

# Data Analyst tarike Pandas thi aapde:

# Data read kariye
# Data clean kariye
# Data filter kariye
# Data analyze kariye
# Calculations kariye
# Reports mate data prepare kariye

# Pandas import karva:
# import pandas as pd

# pd Pandas nu short name che.

# Point 2: DataFrame su che?

# Excel jevu samjo:

# Name	Age	Salary
# Amit	22	30000
# Priya	21	35000
# Rahul	24	40000

# Pandas ma aa table ne DataFrame kevay.

# DataFrame create karva
# import pandas as pd

# data = {
#     "Name": ["Amit", "Priya", "Rahul"],
#     "Age": [22, 21, 24],
#     "Salary": [30000, 35000, 40000]
# }

# df = pd.DataFrame(data)

# print(df)
# Output
#     Name  Age  Salary
# 0   Amit   22   30000
# 1  Priya   21   35000
# 2  Rahul   24   40000

# Point 2 : Practice Questions
# Q1
# Ek DataFrame create karo:

# Name: Amit, Neha, Raj
# Age: 20, 22, 21

# import pandas as pd
# data = {
#         "name" : ["Amit", "neha", "raj"],
#         "age" :  [20, 22, 21]
# }
# df = pd.DataFrame(data)
# print(df)

# Q2.
# Ek Student DataFrame create karo:

# Name: A, B, C, D
# Marks: 75, 88, 65, 92
# Attendance: 80, 90, 75, 95

# data = {
#     "name" : ["A", "B", "C", "D"],
#     "marks" : [75, 88, 65, 92],
#     "attendance" : [80, 90, 75, 95]
# }
# df = pd.DataFrame(data)
# print(df)


# Q3.
# Ek Product DataFrame create karo:

# Product: Laptop, Mobile, Watch
# Price: 50000, 25000, 5000
# Quantity: 2, 5, 10

# data = {
#     "product" : ["Laptop", "Mobile", "watch"],
#     "price" : [50000, 25000, 5000],
#     "Quantity" : [2, 5, 10]
# }
# df = pd.DataFrame(data)
# print(df)

# Q4.
# Ek Employee DataFrame create karo:

# Name: Amit, Priya, Rahul
# Department: IT, HR, Sales
# Salary: 45000, 35000, 40000

# data = {
#     "Name" : ["Amit", "Priya", "Rahul"],
#     "Department" : ["IT", "HR", "Sales"],
#     "Salary" : [45000, 35000, 40000]
# }
# df = pd.DataFrame(data)
# print(df)

# Q5. ⭐
# Ek E-commerce DataFrame create karo:

# Product: Laptop, Mobile, Tablet, Headphone
# Price: 55000, 25000, 30000, 3000
# Quantity: 2, 5, 3, 10
# City: Surat, Ahmedabad, Rajkot, Vadodara

# data = {
#     "product" : ["laptop", "Mobile", "tablet", "headphone"],
#     "price" : [55000, 25000, 30000, 3000],
#     "quantity" : [2, 5, 3, 10],
#     "city" : ["surat", "ahmedabad", "rajkot", "vadodara"]

# }
# df = pd.DataFrame(data)
# print(df)

# Point 3: shape

# Syntax
# df.shape

# Example:

# import pandas as pd

# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha"],
#     "Age": [22, 21, 24, 23],
#     "Salary": [30000, 35000, 40000, 45000]
# }

# df = pd.DataFrame(data)
# print(df.shape)

# 📝 Point 3 — Practice Questions
# Q1.

# Aa DataFrame banao:
# Name: Amit, Priya, Rahul
# Age: 21, 22, 23

# shape find karo.

# data = {
#     "name" : ["amit", "priya", "rahul"],
#     "age" : [21, 22, 23]
# }
# df = pd.DataFrame(data)
# print(df.shape)

# Q2.

# Student DataFrame ma:

# Name: A, B, C, D, E
# Marks: 70, 80, 65, 90, 85
# Attendance: 85, 90, 75, 95, 88
# Rows ane columns ketla che te shape thi find karo.

# students = {
#     "name" : ["A", "B", "C", "D", "E"],
#     "marks" : [70, 80, 65, 90, 85],
#     "attendance" : [85, 90, 75, 95, 88]
# }
# df = pd.DataFrame(students)
# print(df.shape)

# Q3.

# Product DataFrame ma 6 products ane 4 columns hoy.
# shape thi result shu aavse?

# import pandas as pd

# df = pd.DataFrame({
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Mouse", "Keyboard"],
#     "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories"],
#     "Price": [50000, 30000, 20000, 5000, 1000, 1500],
#     "Quantity": [10, 20, 15, 25, 50, 30]
# })

# print(df.shape)

# Point 4: size

# Syntax
# df.size

# Example
# import pandas as pd

# data = {
#     "Name": ["Amit", "Priya", "Rahul"],
#     "Age": [22, 21, 24],
#     "Salary": [30000, 35000, 40000]
# }

# df = pd.DataFrame(data)

# print(df.size)

#  Point 4 — Practice Questions
# Q1.
# DataFrame ma 4 rows ane 3 columns che.
# size ketlu aavse?

# data = {
#     "name" : ["jeni", "jensi", "mahi"],
#     "marks" : [67, 90, 99],
#     "Grade" : ["A", "B", "C"]
# }
# df = pd.DataFrame(data)
# print(df.size)

# Q2.
# DataFrame ma 5 rows ane 4 columns che.
# size find karo.

# import pandas as pd

# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha", "Jay"],
#     "Age": [22, 21, 24, 23, 25],
#     "City": ["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Surat"],
#     "Salary": [30000, 35000, 40000, 45000, 38000]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.size)

# # Q3.
# Product DataFrame ma:
# 6 products
# 4 columns
# df.size no result shu aavse?

# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Headphone", "Keyboard"],
#     "Price": [55000, 25000, 30000, 5000, 3000, 1500],
#     "Quantity": [2, 5, 3, 10, 8, 6],
#     "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories"]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.size)

# Q4.
# Employee DataFrame ma 10 employees ane 5 columns che.
# Total cells find karo using size.

# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha", "Jay", "Riya", "Karan", "Meera", "Dev", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance", "HR", "IT", "Sales", "Finance", "IT"],
#     "Age": [24, 25, 26, 23, 28, 24, 27, 26, 29, 25],
#     "Salary": [40000, 35000, 42000, 45000, 50000, 38000, 55000, 43000, 60000, 47000],
#     "City": ["Surat", "Ahmedabad", "Rajkot", "Surat", "Vadodara", "Surat", "Rajkot", "Ahmedabad", "Surat", "Vadodara"]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.size)

# Q5. ⭐
# E-commerce DataFrame ma 20 rows ane 6 columns che.
# df.size no output shu aavse?

# data = {
#     "Product": [
#         "Laptop", "Mobile", "Tablet", "Watch", "Headphone",
#         "Keyboard", "Mouse", "Monitor", "Camera", "Speaker",
#         "Printer", "Charger", "Power Bank", "Earbuds", "Webcam",
#         "Router", "SSD", "USB Drive", "Smart TV", "Mic"
#     ],

#     "Category": [
#         "Electronics", "Electronics", "Electronics", "Accessories", "Accessories",
#         "Accessories", "Accessories", "Electronics", "Electronics", "Electronics",
#         "Electronics", "Accessories", "Accessories", "Accessories", "Electronics",
#         "Electronics", "Storage", "Storage", "Electronics", "Accessories"
#     ],

#     "Price": [
#         55000, 25000, 30000, 5000, 3000,
#         1500, 800, 18000, 45000, 4000,
#         12000, 1200, 2000, 2500, 6000,
#         3000, 7000, 1000, 45000, 3500
#     ],

#     "Quantity": [
#         2, 5, 3, 10, 8,
#         6, 12, 4, 2, 7,
#         3, 15, 10, 9, 5,
#         6, 4, 12, 2, 8
#     ],

#     "City": [
#         "Surat", "Ahmedabad", "Rajkot", "Vadodara", "Surat",
#         "Ahmedabad", "Rajkot", "Surat", "Vadodara", "Ahmedabad",
#         "Surat", "Rajkot", "Vadodara", "Surat", "Ahmedabad",
#         "Rajkot", "Surat", "Vadodara", "Ahmedabad", "Surat"
#     ],

#     "Rating": [
#         4.5, 4.2, 4.0, 4.5, 4.1,
#         4.3, 4.0, 4.6, 4.4, 4.2,
#         4.1, 4.5, 4.3, 4.6, 4.0,
#         4.2, 4.7, 4.1, 4.5, 4.3
#     ]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.size)

# Point 5: columns

# Syntax
# df.columns

# Example
# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mobile", "Watch"],
#     "Price": [55000, 25000, 5000],
#     "Quantity": [2, 5, 10],
#     "Category": ["Electronics", "Electronics", "Accessories"]
# }

# df = pd.DataFrame(data)

# print(df.columns)

# Point 5 — df.columns Practice
# Q1. Employee Data

# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha", "Jay"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [40000, 35000, 45000, 50000, 38000],
#     "City": ["Surat", "Ahmedabad", "Rajkot", "Surat", "Vadodara"]
# }

# df = pd.DataFrame(data)
# print(df.columns)

# Task: df.columns use kari ne badha column names display karo.

# Q2. Sales Data

# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch"],
#     "Sales": [120000, 95000, 75000, 45000],
#     "Month": ["January", "January", "February", "February"],
#     "Region": ["West", "North", "West", "South"],
#     "Profit": [20000, 15000, 12000, 8000]
# }

# df = pd.DataFrame(data)
# print(df.columns)

# Task: Dataset ma available badha columns display karo.

# Q3. Student Data
# data = {
#     "Student": ["Amit", "Priya", "Rahul", "Neha", "Jay", "Riya"],
#     "Marks": [78, 92, 65, 88, 74, 95],
#     "Age": [20, 21, 20, 22, 21, 20],
#     "City": ["Surat", "Rajkot", "Surat", "Ahmedabad", "Vadodara", "Surat"]
# }

# df = pd.DataFrame(data)
# print(df.columns)

# Task: df.columns thi column names check karo.

# Point 6: index

# DataFrame ni darek row ne ek index number hoy che.
# By default Pandas index 0 thi start thay che.

# Example:

# import pandas as pd

# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha"],
#     "Salary": [30000, 35000, 40000, 45000]
# }

# df = pd.DataFrame(data)

# print(df)


# 📝 Point 6 — Practice Questions

# Q1. Employee Data
# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha"],
#     "Department": ["IT", "HR", "Sales", "Finance"],
#     "Salary": [40000, 35000, 45000, 50000]
# }

# df = pd.DataFrame(data)
# print(df)

# Task: df.index use kari ne DataFrame na indexes check karo.

# Q2. Product Data
# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Mouse"],
#     "Price": [55000, 25000, 30000, 5000, 800]
# }

# df = pd.DataFrame(data)
# print(df)

# Task: DataFrame na indexes display karo.

# Q3. Student Data
# data = {
#     "Name": ["Amit", "Priya", "Raj", "Neha", "Jay", "Riya"],
#     "Marks": [75, 88, 69, 92, 81, 95],
#     "City": ["Surat", "Rajkot", "Surat", "Ahmedabad", "Vadodara", "Surat"]
# }

# df = pd.DataFrame(data)
# print(df)

# Task: df.index use kari ne indexes check karo.

# Point 7: head()

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Mouse", "Keyboard"],
#     "Price": [55000, 25000, 30000, 5000, 800, 1500],
#     "Quantity": [2, 5, 3, 10, 12, 6]
# }

# df = pd.DataFrame(data)

# print(df.head(6))

# 📝 Point 7 — Practice Questions
# Q1. Employee Data
# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha", "Jay", "Riya"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance", "HR"],
#     "Salary": [40000, 35000, 45000, 50000, 38000, 42000]
# }

# df = pd.DataFrame(data)
# print(df.head(5))

# Task: DataFrame ni first 5 rows display karo.

# Q2. Product Data
# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Mouse", "Keyboard"],
#     "Price": [55000, 25000, 30000, 5000, 800, 1500],
#     "Quantity": [2, 5, 3, 10, 12, 6]
# }

# df = pd.DataFrame(data)
# print(df.head(3))

# Task: First 3 rows display karo using head().

# Q3. Student Data
# data = {
#     "Student": ["Amit", "Priya", "Raj", "Neha", "Jay", "Riya", "Dev"],
#     "Marks": [75, 88, 69, 92, 81, 95, 72],
#     "City": ["Surat", "Rajkot", "Surat", "Ahmedabad", "Vadodara", "Surat", "Rajkot"]
# }

# df = pd.DataFrame(data)
# print(df.head(2))

# Task: First 2 rows display karo.

# Q4. Sales Data
# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Camera", "Speaker"],
#     "Sales": [120000, 95000, 75000, 45000, 85000, 55000],
#     "Region": ["West", "North", "West", "South", "North", "West"]
# }

# df = pd.DataFrame(data)
# print(df.head(5))

# Task: head() use kari ne first 5 rows display karo.

# Q5. ⭐ E-commerce Data
# data = {
#     "Product": ["Laptop", "Mobile", "Headphone", "Watch", "Tablet", "Keyboard", "Mouse", "Monitor"],
#     "Price": [55000, 25000, 3000, 5000, 30000, 1500, 800, 18000],
#     "Quantity": [2, 5, 8, 10, 3, 6, 12, 4],
#     "City": ["Surat", "Ahmedabad", "Rajkot", "Surat", "Vadodara", "Surat", "Rajkot", "Ahmedabad"]
# }

# df = pd.DataFrame(data)
# print(df.head(5))

# Task: 
# Dataset ni first 5 rows display karo using head().

# Point 8: tail()

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Mouse", "Keyboard"],
#     "Price": [55000, 25000, 30000, 5000, 800, 1500],
#     "Quantity": [2, 5, 3, 10, 12, 6]
# }

# df = pd.DataFrame(data)
# print(df.tail())

# 📝 Practice — Point 8

# Q1.

# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha", "Jay", "Riya"],
#     "Salary": [30000, 35000, 40000, 45000, 38000, 42000]
# }

# df = pd.DataFrame(data)
# print(df.tail(5))

# Task: Last 5 rows display karo.

# Q2.

# data = {
#     "Product": ["Laptop", "Mobile", "Tablet", "Watch", "Mouse", "Keyboard", "Monitor"],
#     "Price": [55000, 25000, 30000, 5000, 800, 1500, 18000]
# }

# df = pd.DataFrame(data)
# print(df.tail(3))

# Task: Last 3 rows display karo.

# Q3.

# data = {
#     "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
#     "Marks": [75, 88, 65, 92, 81, 95, 70, 85]
# }

# df = pd.DataFrame(data)
# print(df.tail(2))

# Task: Last 2 rows display karo.

# 🐼 Point 9: info()

# import pandas as pd

# data = {
#     "Name": ["Amit", "Priya", "Rahul"],
#     "Age": [22, 21, 24],
#     "Salary": [30000, 35000, 40000]
# }

# df = pd.DataFrame(data)
# df.info()

# 📝 Practice — Point 9

# Q1.
# data = {
#     "Name": ["Amit", "Priya", "Rahul", "Neha"],
#     "Age": [22, 21, 24, 23],
#     "Salary": [30000, 35000, 40000, 45000]
# }

# df = pd.DataFrame(data)
# df.info()

# Task: info() thi DataFrame ni information check karo.

# Q2.
# data = {
#     "Product": ["Laptop", "Mobile", "Watch", "Tablet", "Mouse"],
#     "Price": [55000, 25000, 5000, 30000, 800],
#     "Quantity": [2, 5, 10, 3, 12],
#     "Rating": [4.5, 4.2, 4.6, 4.3, 4.0]
# }

# df = pd.DataFrame(data)
# df.info()

# Task: info() use kari ne dataset inspect karo.

# Q3. ⭐
# data = {
#     "Employee_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Priya", "Rahul", "Neha", "Jay", "Riya"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance", "HR"],
#     "Salary": [45000, 38000, 42000, 50000, 55000, 40000],
#     "Experience": [2, 3, 1, 4, 5, 2]
# }

# df = pd.DataFrame(data)
# df.info()

# Task: 
# df.info() use kari ne complete DataFrame information check karo.

# Topic 2: Series

# Point 1: Series su che?

# import pandas as pd
# sales = pd.Series([12000, 15000, 18000, 14000])
# print(sales)

# 📝 Point 1 — Practice Questions

# Q1. Salary Series

# salary = [30000, 35000, 40000, 45000, 50000]
# Task: Aa list mathi Pandas Series create karo.

# salary = pd.Series([30000, 35000, 40000, 45000, 50000])
# print(salary)

# Q2. Product Price

# price = [500, 800, 1200, 1500, 2000]
# Task: price ni Series create karo.

# price = pd.Series([500, 800, 1200, 1500, 2000])
# print(price)

# Q3. Monthly Sales

# sales = [120000, 135000, 128000, 150000, 175000, 190000]
# Task: Sales ni Pandas Series create karo ane print karo.

# sales = pd.Series([120000, 135000, 128000, 150000, 175000, 190000])
# print(sales)

# Q4. Employee Experience
# experience = [1, 3, 2, 5, 4, 7]
# Task: Experience ni Series create karo.

# experience = pd.series([1, 3, 2, 5, 4, 7])
# print(exoerience)

# Q5. ⭐ Customer Ratings
# rating = [4.5, 4.0, 3.5, 5.0, 4.2, 3.8, 4.7]
# Task: Customer rating ni Pandas Series create kari ne print karo.

# rating = pd.Series([4.5, 4.0, 3.5, 5.0, 4.2, 3.8, 4.7])
# print(rating)

# Point 2: Custom Index

# import pandas as pd

# sales = pd.Series(
#     [120000, 150000, 180000],
#     index=["January", "February", "March"]
# )

# print(sales)

# 📝 Point 2 — Practice Questions

# Q1. Monthly Sales

# sales = pd.Series([120000, 150000, 135000, 180000],
#         index = ["January", "February", "March", "April"])

# print(sales)

# Task: sales ni Series create karo ane months ne custom index tarike use karo.

# Q2. Department Salary

# salary = [45000, 38000, 50000, 42000]
# department = ["IT", "HR", "Finance", "Sales"]
# Task: Department ne index banavi ne Salary Series create karo.

# salary = pd.Series([45000, 38000, 50000, 42000],
#           index = ["IT", "HR", "Finance", "Sales"])
# print(salary)

# Q3. City Orders
# orders = [120, 95, 150, 80]
# cities = ["Surat", "Ahmedabad", "Rajkot", "Vadodara"]

# Task: City-wise Orders ni Series create karo using custom index.

# orders = pd.Series([120, 95, 150, 80],
#          index = ["surat", "Ahmedabad", "Rajkot", "Vadodara"])
# print(orders)

# Q4. Product Price
# price = [55000, 25000, 30000, 5000]
# products = ["Laptop", "Mobile", "Tablet", "Watch"]

# Task: Product names ne custom index tarike use kari ne Price Series create karo.

# price = pd.Series([55000, 25000, 30000, 5000],
#         index = ["Laptop", "Mobile", "Tablet", "Watch"])
# print(price)

# Q5. ⭐ Branch Sales
# sales = [250000, 180000, 220000, 150000, 275000]
# branches = ["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai"]

# Task: Branch-wise Sales ni Series create karo ane branch names ne index tarike use karo.

# sales = pd.Series([250000, 180000, 220000, 150000, 275000],
#         index = ["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai"])
# print(sales)

# Point 3: Series ma value access karvi

# import pandas as pd

# sales = pd.Series(
#     [120000, 150000, 135000, 180000],
#     index=["January", "February", "March", "April"]
# )

# print(sales["January"])

# 📝 Point 3 — Practice Questions
# Q1. Monthly Sales
# sales = pd.Series(
#     [120000, 150000, 135000, 180000],
#     index=["January", "February", "March", "April"]
# )
# Task: February ni sales display karo.

# sales = pd.Series(
#     [120000, 150000, 135000, 180000],
#     index=["January", "February", "March", "April"]
# )
# print(sales["February"])

# Q2. Department Salary
# salary = pd.Series(
#     [45000, 38000, 50000, 42000],
#     index=["IT", "HR", "Finance", "Sales"]
# )

# Task: Finance department ni salary display karo.

# salary = pd.Series(
#     [45000, 38000, 50000, 42000],
#     index=["IT", "HR", "Finance", "Sales"]
# )
# print(salary["Finance"])

# Q3. City Orders
# orders = pd.Series(
#     [120, 95, 150, 80],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara"]
# )

# Task: Rajkot na orders display karo.

# orders = pd.Series(
#     [120, 95, 150, 80],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara"]
# )
# print(orders["Rajkot"])

# Q4. Product Price
# price = pd.Series(
#     [55000, 25000, 30000, 5000],
#     index=["Laptop", "Mobile", "Tablet", "Watch"]
# )

# Task: Laptop ane Watch banne ni price display karo.
# price = pd.Series(
#     [55000, 25000, 30000, 5000],
#     index=["Laptop", "Mobile", "Tablet", "Watch"]
# )
# print(price["Laptop"])

# Q5. ⭐ Branch Sales
# sales = pd.Series(
#     [250000, 180000, 220000, 150000, 275000],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai"]
# )

# Task: Surat ane Mumbai ni sales banne display karo.

# sales = pd.Series(
#     [250000, 180000, 220000, 150000, 275000],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai"]
# )
# print(sales["Surat"], sales["Mumbai"])

# Point 4: index અને values

# import pandas as pd

# sales = pd.Series(
#     [120000, 150000, 135000, 180000],
#     index=["January", "February", "March", "April"]
# )

# print(sales.index)
# print(sales.values)

# 📝 Point 4 — Practice Questions
# Q1. Monthly Sales
# sales = pd.Series(
#     [120000, 150000, 135000, 180000, 200000],
#     index=["January", "February", "March", "April", "May"]
# )

# Task: Series ના બધા index labels display કરો.

# sales = pd.Series(
#     [120000, 150000, 135000, 180000, 200000],
#     index=["January", "February", "March", "April", "May"]
# )
# print(sales.index)
# print(sales.values)

# Q2. Product Price
# price = pd.Series(
#     [55000, 25000, 30000, 5000],
#     index=["Laptop", "Mobile", "Tablet", "Watch"]
# )

# Task: Series ની બધી values display કરો.

# price = pd.Series(
#     [55000, 25000, 30000, 5000],
#     index=["Laptop", "Mobile", "Tablet", "Watch"]
# )
# print(price.index)
# print(price.values)

# Q3. Department Salary
# salary = pd.Series(
#     [45000, 38000, 50000, 42000],
#     index=["IT", "HR", "Finance", "Sales"]
# )

# Task:
# બધા index labels display કરો.
# બધી salary values display કરો.

# salary = pd.Series(
#     [45000, 38000, 50000, 42000],
#     index=["IT", "HR", "Finance", "Sales"]
# )
# print(salary.index)
# print(salary.values)

# Q4. City Orders
# orders = pd.Series(
#     [120, 95, 150, 80, 110],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai"]
# )

# Task: orders ના બધા index અને values display કરો.

# orders = pd.Series(
#     [120, 95, 150, 80, 110],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai"]
# )
# print(orders.index)
# print(orders.values)

# Q5. ⭐ E-commerce Rating
# rating = pd.Series(
#     [4.5, 4.2, 4.0, 4.6, 4.3, 4.1],
#     index=["Laptop", "Mobile", "Tablet", "Watch", "Headphone", "Mouse"]
# )

# Task:
# Product names/index display કરો.
# Ratings/values display કરો.

# rating = pd.Series(
#     [4.5, 4.2, 4.0, 4.6, 4.3, 4.1],
#     index=["Laptop", "Mobile", "Tablet", "Watch", "Headphone", "Mouse"]
# )
# print(rating.index)
# print(rating.values)

# Point 5: len() — Series માં કેટલા values છે?

# import pandas as pd

# sales = pd.Series(
#     [120000, 150000, 135000, 180000, 200000],
#     index=["January", "February", "March", "April", "May"]
# )
# print(len(sales))

# 📝 Point 5 — Practice Questions
# Q1. Employee Salary

# salary = pd.Series(
#     [30000, 35000, 40000, 45000, 50000, 55000],
#     index=["Amit", "Priya", "Rahul", "Neha", "Jay", "Riya"]
# )
# print(len(salary))

# Task: Series માં total કેટલા salary values છે તે len() થી find કરો.

# Q2. Product Price

# price = pd.Series(
#     [500, 800, 1200, 1500, 2000],
#     index=["Pen", "Book", "Bag", "Shoes", "Watch"]
# )
# print(len(price))
# Task: Total products કેટલા છે તે len() થી find કરો.

# Q3. Monthly Sales

# sales = pd.Series(
#     [120000, 135000, 128000, 150000, 175000, 190000, 210000],
#     index=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
# )
# print(len(sales))

# Task: Total months/data points કેટલા છે તે find કરો.

# Q4. Customer Rating

# rating = pd.Series(
#     [4.5, 4.0, 3.8, 5.0, 4.2, 3.5, 4.7, 4.1],
#     index=["C101", "C102", "C103", "C104", "C105", "C106", "C107", "C108"]
# )
# print(len(rating))

# Task: Total customer ratings કેટલા છે તે len() થી find કરો.

# Q5. ⭐ E-commerce Orders
# orders = pd.Series(
#     [120, 95, 150, 80, 110, 175, 130, 90, 200, 145],
#     index=["Surat", "Ahmedabad", "Rajkot", "Vadodara", "Mumbai",
#            "Pune", "Delhi", "Jaipur", "Bangalore", "Chennai"]
# )
# print(len(orders))

# Task: Series માં total કેટલા city-wise order values છે તે len() થી find કરો.

# Point 6: dtype
# salary = pd.Series([30000, 35000, 40000, 45000])
# print(salary.dtype)

# Practice — Point 6

# Q1.
# age = pd.Series([21, 22, 23, 24, 25])
# print(age.dtype)

# dtype check karo.

# Q2.

# price = pd.Series([500.5, 800.0, 1200.5, 1500.0])
# print(price.dtype)

# dtype check karo.

# Q3.

# rating = pd.Series([4.5, 4.0, 3.5, 5.0])
# print(rating.dtype)

# dtype check karo.

# Q4.

# product = pd.Series(["Laptop", "Mobile", "Tablet", "Watch"])
# print(product.dtype)

# dtype check karo.

# Q5. ⭐

# quantity = pd.Series([2, 5, 10, 3, 8, 6])
# print(quantity.dtype)

# dtype check karo.

# part 2:

# Topic 1: Creating a Series from List

# Example
# import pandas as pd
# sales = [12000, 15000, 18000, 14000]
# s = pd.Series(sales)

# print(s)
# 📝 Practice – 5 Questions

# Data:

# marks = [78, 85, 92, 67, 88]
# marks list ને Pandas Series માં convert કરો.
# Series print કરો.
# Series માંથી first value display કરો.
# Series માંથી last value display કરો.
# Series નો sum() અને mean() find કરો.

# marks = [78, 85, 92, 67, 88]
# m = pd.Series(marks)
# print(m)
# print(m.head(1))
# print(m.tail(1))
# print("sum is:", m.sum())
# print("mean is:", m.mean())

# 🔹 Topic 2: Dictionary to DataFrame

# import pandas as pd
# student = {
#     "Name": ["Raj", "Amit", "Neha"],
#     "Age": [20, 21, 22],
#     "City": ["Surat", "Rajkot", "Ahmedabad"]
# }
# df = pd.DataFrame(student)
# print(df)

# 📝 Practice – 5 Questions

# Data:

# employee = {
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Department": ["IT", "HR", "Sales", "IT"],
#     "Salary": [45000, 38000, 52000, 48000]
# }

# employee dictionary ને DataFrame માં convert કરો.
# employee = {
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Department": ["IT", "HR", "Sales", "IT"],
#     "Salary": [45000, 38000, 52000, 48000]
# }
# df = pd.DataFrame(employee)
# print(df)

# Complete DataFrame display કરો.
# employee = {
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Department": ["IT", "HR", "Sales", "IT"],
#     "Salary": [45000, 38000, 52000, 48000]
# }
# df = pd.DataFrame(employee)
# print(df)

# માત્ર Name column display કરો.
# employee = {
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Department": ["IT", "HR", "Sales", "IT"],
#     "Salary": [45000, 38000, 52000, 48000]
# }
# df = pd.DataFrame(employee)
# print(df["Name"])

# માત્ર Salary column display કરો.
# employee = {
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Department": ["IT", "HR", "Sales", "IT"],
#     "Salary": [45000, 38000, 52000, 48000]
# }
# df = pd.DataFrame(employee)
# print(df["salary"])

# DataFrame નો shape find કરો.
# employee = {
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Department": ["IT", "HR", "Sales", "IT"],
#     "Salary": [45000, 38000, 52000, 48000]
# }
# df = pd.DataFrame(employee)
# print(df.shape)

# 3️⃣ List to DataFrame
# import pandas as pd

# data = [
#     ["Rahul", "IT", 45000],
#     ["Priya", "HR", 38000],
#     ["Amit", "Sales", 52000],
#     ["Neha", "IT", 48000]
# ]
# df = pd.DataFrame(data)
# print(df)

# Practice data:

# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500],
#     ["Table", "Furniture", 7000],
#     ["Keyboard", "Electronics", 1500]
# ]

# 5 Questions:

# Convert data into DataFrame.
# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500],
#     ["Table", "Furniture", 7000],
#     ["Keyboard", "Electronics", 1500]
# ]
# df = pd.DataFrame(data)


# Display the complete DataFrame.
# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500],
#     ["Table", "Furniture", 7000],
#     ["Keyboard", "Electronics", 1500]
# ]
# df = pd.DataFrame(data)
# print(df)

# Find the shape of DataFrame.
# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500],
#     ["Table", "Furniture", 7000],
#     ["Keyboard", "Electronics", 1500]
# ]
# df = pd.DataFrame(data)
# print(df.shape)

# Display the first 3 rows.
# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500],
#     ["Table", "Furniture", 7000],
#     ["Keyboard", "Electronics", 1500]
# ]
# df = pd.DataFrame(data)
# print(df.head(3))

# Display the last 2 rows.
# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500],
#     ["Table", "Furniture", 7000],
#     ["Keyboard", "Electronics", 1500]
# ]
# df = pd.DataFrame(data)
# print(df.head(2))

# 4️⃣ DataFrame from Single List

# import pandas as pd
# products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
# df = pd.DataFrame(products)
# print(df)

# Practice data:

# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

# 5 Questions:

# Create a DataFrame from products.
# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
# df = pd.DataFrame(products)

# Display the DataFrame.
# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
# df = pd.DataFrame(products)
# print(df)

# Find its shape.
# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
# df = pd.DataFrame(products)
# print(df.shape)

# Display the first 3 products.
# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
# df = pd.DataFrame(products)
# print(df.head(3))

# Display the last 2 products.
# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
# df = pd.DataFrame(products)
# print(df.tail(2))

# 5️⃣ DataFrame with Custom Column Name
# import pandas as pd

# data = [
#     ["Laptop", "Electronics", 50000],
#     ["Mouse", "Electronics", 800],
#     ["Chair", "Furniture", 4500]
# ]
# df = pd.DataFrame(data, columns=["Product", "Category", "Price"])
# print(df)

# Practice data:

# data = [
#     ["Mobile", "Electronics", 25000],
#     ["Sofa", "Furniture", 30000],
#     ["Headphones", "Electronics", 2000],
#     ["Desk", "Furniture", 8000]
# ]

# 5 Questions:

# Convert data into DataFrame with columns Product, Category, Price.
# Display complete DataFrame.
# data = [
#     ["Mobile", "Electronics", 25000],
#     ["Sofa", "Furniture", 30000],
#     ["Headphones", "Electronics", 2000],
#     ["Desk", "Furniture", 8000]
# ]
# df = pd.DataFrame(data, columns=["product", "Category", "price"])
# print(df)

# Display only Product column.
# data = [
#     ["Mobile", "Electronics", 25000],
#     ["Sofa", "Furniture", 30000],
#     ["Headphones", "Electronics", 2000],
#     ["Desk", "Furniture", 8000]
# ]
# df = pd.DataFrame(data, columns=["product", "Category", "price"])
# print(df["product"])

# Display only Price column.
# data = [
#     ["Mobile", "Electronics", 25000],
#     ["Sofa", "Furniture", 30000],
#     ["Headphones", "Electronics", 2000],
#     ["Desk", "Furniture", 8000]
# ]
# df = pd.DataFrame(data, columns=["product", "Category", "price"])
# print(df["price"])

# Find the shape.
# data = [
#     ["Mobile", "Electronics", 25000],
#     ["Sofa", "Furniture", 30000],
#     ["Headphones", "Electronics", 2000],
#     ["Desk", "Furniture", 8000]
# ]
# df = pd.DataFrame(data, columns=["product", "Category", "price"])
# print(df.shape)

# 6️⃣ NumPy Array to DataFrame
# import pandas as pd
import numpy as np


# Practice data:

# data = np.array([
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Printer", 9000]
# ])

# 5 Questions:

# Convert NumPy array into DataFrame.
# data = np.array([
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Printer", 9000]
# ])
# df = pd.DataFrame(data)
# print(data)

# Give column names Product and Price.
# data = np.array([
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Printer", 9000]
# ])
# df = pd.DataFrame(data, columns=["Product", "price"])

# Display complete DataFrame.
# data = np.array([
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Printer", 9000]
# ])
# df = pd.DataFrame(data, columns=["Product", "price"])
# print(df)

# Display Price column.
# data = np.array([
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Printer", 9000]
# ])
# df = pd.DataFrame(data, columns=["Product", "price"])
# print(df["price"])

# Find the shape.
# data = np.array([
#     ["Laptop", 50000],
#     ["Mouse", 800],
#     ["Keyboard", 1500],
#     ["Monitor", 12000],
#     ["Printer", 9000]
# ])
# df = pd.DataFrame(data, columns=["Product", "price"])
# print(df.shape)

# 7️⃣ DataFrame from List of Dictionaries

# Practice data:

# data = [
#     {"Product": "Mobile", "Category": "Electronics", "Price": 25000},
#     {"Product": "Sofa", "Category": "Furniture", "Price": 30000},
#     {"Product": "Headphones", "Category": "Electronics", "Price": 2000},
#     {"Product": "Desk", "Category": "Furniture", "Price": 8000}
# ]


# 5 Questions:

# Convert data into DataFrame.
# data = [
#     {"Product": "Mobile", "Category": "Electronics", "Price": 25000},
#     {"Product": "Sofa", "Category": "Furniture", "Price": 30000},
#     {"Product": "Headphones", "Category": "Electronics", "Price": 2000},
#     {"Product": "Desk", "Category": "Furniture", "Price": 8000}
# ]
# df = pd.DataFrame(data)

# Display complete DataFrame.
# data = [
#     {"Product": "Mobile", "Category": "Electronics", "Price": 25000},
#     {"Product": "Sofa", "Category": "Furniture", "Price": 30000},
#     {"Product": "Headphones", "Category": "Electronics", "Price": 2000},
#     {"Product": "Desk", "Category": "Furniture", "Price": 8000}
# ]
# df = pd.DataFrame(data)
# print(df)

# Display only Product column.
# data = [
#     {"Product": "Mobile", "Category": "Electronics", "Price": 25000},
#     {"Product": "Sofa", "Category": "Furniture", "Price": 30000},
#     {"Product": "Headphones", "Category": "Electronics", "Price": 2000},
#     {"Product": "Desk", "Category": "Furniture", "Price": 8000}
# ]
# df = pd.DataFrame(data, columns=["Products", "Category", "Price"])
# print(df)

# Display only Price column.
# data = [
#     {"Product": "Mobile", "Category": "Electronics", "Price": 25000},
#     {"Product": "Sofa", "Category": "Furniture", "Price": 30000},
#     {"Product": "Headphones", "Category": "Electronics", "Price": 2000},
#     {"Product": "Desk", "Category": "Furniture", "Price": 8000}
# ]
# df = pd.DataFrame(data, columns=["Products", "Category", "Price"])
# print(df["Price"])

# Find shape.
# data = [
#     {"Product": "Mobile", "Category": "Electronics", "Price": 25000},
#     {"Product": "Sofa", "Category": "Furniture", "Price": 30000},
#     {"Product": "Headphones", "Category": "Electronics", "Price": 2000},
#     {"Product": "Desk", "Category": "Furniture", "Price": 8000}
# ]
# df = pd.DataFrame(data, columns=["Products", "Category", "Price"])
# print(df.shape)

# 8️⃣ DataFrame from Dictionary of Series
# Practice data:

# data = {
#     "Product": pd.Series(["Mobile", "Laptop", "Tablet", "Monitor"]),
#     "Price": pd.Series([25000, 50000, 20000, 12000]),
#     "Quantity": pd.Series([10, 5, 8, 6])
# }

# 5 Questions:

# Convert data into DataFrame.
# data = {
#     "Product": pd.Series(["Mobile", "Laptop", "Tablet", "Monitor"]),
#     "Price": pd.Series([25000, 50000, 20000, 12000]),
#     "Quantity": pd.Series([10, 5, 8, 6])
# }
# df = pd.DataFrame(data)

# Display complete DataFrame.
# data = {
#     "Product": pd.Series(["Mobile", "Laptop", "Tablet", "Monitor"]),
#     "Price": pd.Series([25000, 50000, 20000, 12000]),
#     "Quantity": pd.Series([10, 5, 8, 6])
# }
# df = pd.DataFrame(data)
# print(df)

# Display only Product.
# data = {
#     "Product": pd.Series(["Mobile", "Laptop", "Tablet", "Monitor"]),
#     "Price": pd.Series([25000, 50000, 20000, 12000]),
#     "Quantity": pd.Series([10, 5, 8, 6])
# }
# df = pd.DataFrame(data, columns=["Product", "Price", "Quantity"])
# print(df["Product"])

# Display only Quantity.
# data = {
#     "Product": pd.Series(["Mobile", "Laptop", "Tablet", "Monitor"]),
#     "Price": pd.Series([25000, 50000, 20000, 12000]),
#     "Quantity": pd.Series([10, 5, 8, 6])
# }
# df = pd.DataFrame(data, columns=["Product", "Price", "Quantity"])
# print(df["Quantity"])

# Find shape.
# data = {
#     "Product": pd.Series(["Mobile", "Laptop", "Tablet", "Monitor"]),
#     "Price": pd.Series([25000, 50000, 20000, 12000]),
#     "Quantity": pd.Series([10, 5, 8, 6])
# }
# df = pd.DataFrame(data, columns=["Product", "Price", "Quantity"])
# print(df.shape)

# 9️⃣ DataFrame from Tuple

# Practice data:

# data = (
#     ("iPhone", "Apple", 70000),
#     ("Galaxy", "Samsung", 55000),
#     ("Pixel", "Google", 60000),
#     ("OnePlus", "OnePlus", 35000),
#     ("Vivo X", "Vivo", 28000)
# )

# 5 Questions:

# data ne DataFrame ma convert karo.
# data = (
#     ("iPhone", "Apple", 70000),
#     ("Galaxy", "Samsung", 55000),
#     ("Pixel", "Google", 60000),
#     ("OnePlus", "OnePlus", 35000),
#     ("Vivo X", "Vivo", 28000)
# )
# df = pd.DataFrame(data)

# Columns Product, Brand, Price aapo.
# data = (
#     ("iPhone", "Apple", 70000),
#     ("Galaxy", "Samsung", 55000),
#     ("Pixel", "Google", 60000),
#     ("OnePlus", "OnePlus", 35000),
#     ("Vivo X", "Vivo", 28000)
# )
# df = pd.DataFrame(data, columns=["Product", "Brand", "Price"])

# Complete DataFrame display karo.
# data = (
#     ("iPhone", "Apple", 70000),
#     ("Galaxy", "Samsung", 55000),
#     ("Pixel", "Google", 60000),
#     ("OnePlus", "OnePlus", 35000),
#     ("Vivo X", "Vivo", 28000)
# )
# df = pd.DataFrame(data, columns=["Product", "Brand", "Price"])
# print(df)

# Only Price column display karo.
# data = (
#     ("iPhone", "Apple", 70000),
#     ("Galaxy", "Samsung", 55000),
#     ("Pixel", "Google", 60000),
#     ("OnePlus", "OnePlus", 35000),
#     ("Vivo X", "Vivo", 28000)
# )
# df = pd.DataFrame(data, columns=["Product", "Brand", "Price"])
# print(df["Price"])

# shape find karo.
# data = (
#     ("iPhone", "Apple", 70000),
#     ("Galaxy", "Samsung", 55000),
#     ("Pixel", "Google", 60000),
#     ("OnePlus", "OnePlus", 35000),
#     ("Vivo X", "Vivo", 28000)
# )
# df = pd.DataFrame(data, columns=["Product", "Brand", "Price"])
# print(df.shape)

# part 3
# 1️⃣ Selecting Data — Single Column
# Example — Sales Data
# import pandas as pd

# data = {
#     "Product": ["Pen", "Notebook", "Bag", "Bottle"],
#     "Sales": [1200, 2500, 1800, 900],
#     "Quantity": [20, 35, 15, 12]
# }
# df = pd.DataFrame(data)
# print(df["Sales"])

# Practice Data
# data = {
#     "Customer": ["Asha", "Ravi", "Kiran", "Maya", "Dev"],
#     "City": ["Surat", "Rajkot", "Vadodara", "Ahmedabad", "Surat"],
#     "Orders": [5, 8, 3, 6, 10]
# }

# df = pd.DataFrame(data)

# 5 Questions:

# Display only Customer column.
# data = {
#     "Customer": ["Asha", "Ravi", "Kiran", "Maya", "Dev"],
#     "City": ["Surat", "Rajkot", "Vadodara", "Ahmedabad", "Surat"],
#     "Orders": [5, 8, 3, 6, 10]
# }

# df = pd.DataFrame(data)
# print(df["Customer"])

# Display only City column.
# data = {
#     "Customer": ["Asha", "Ravi", "Kiran", "Maya", "Dev"],
#     "City": ["Surat", "Rajkot", "Vadodara", "Ahmedabad", "Surat"],
#     "Orders": [5, 8, 3, 6, 10]
# }

# df = pd.DataFrame(data)
# print(df["City"])

# Display only Orders column.
# data = {
#     "Customer": ["Asha", "Ravi", "Kiran", "Maya", "Dev"],
#     "City": ["Surat", "Rajkot", "Vadodara", "Ahmedabad", "Surat"],
#     "Orders": [5, 8, 3, 6, 10]
# }

# df = pd.DataFrame(data)
# print(df["Orders"])

# Display the Customer column and check its type.
# data = {
#     "Customer": ["Asha", "Ravi", "Kiran", "Maya", "Dev"],
#     "City": ["Surat", "Rajkot", "Vadodara", "Ahmedabad", "Surat"],
#     "Orders": [5, 8, 3, 6, 10]
# }

# df = pd.DataFrame(data)
# print(df["Customer"])
# print(df["Customer"].dtype)

# Find the total of Orders.
# data = {
#     "Customer": ["Asha", "Ravi", "Kiran", "Maya", "Dev"],
#     "City": ["Surat", "Rajkot", "Vadodara", "Ahmedabad", "Surat"],
#     "Orders": [5, 8, 3, 6, 10]
# }

# df = pd.DataFrame(data)
# print(df["Orders"].sum())

# 2️⃣ Selecting Data — Multiple Columns

# Example — Movie Data
# import pandas as pd

# data = {
#     "Movie": ["Avatar", "Titanic", "Jawan", "Dangal"],
#     "Genre": ["Action", "Drama", "Action", "Sports"],
#     "Rating": [8.5, 8.8, 7.2, 8.3]
# }
# df = pd.DataFrame(data)
# print(df[["Movie", "Rating"]])

# Practice Data
# data = {
#     "Employee": ["Riya", "Jay", "Nisha", "Om", "Tina"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 42000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)

# 5 Questions:

# Display Employee and Salary.
# data = {
#     "Employee": ["Riya", "Jay", "Nisha", "Om", "Tina"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 42000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)
# print(df[["Employee", "Salary"]])

# Display Department and Experience.
# data = {
#     "Employee": ["Riya", "Jay", "Nisha", "Om", "Tina"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 42000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)
# print(df[["Department", "Experience"]])

# Display Employee, Department and Salary.
# data = {
#     "Employee": ["Riya", "Jay", "Nisha", "Om", "Tina"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 42000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)
# print(df[["Department", "Salary"]])

# Display Employee and Experience.
# data = {
#     "Employee": ["Riya", "Jay", "Nisha", "Om", "Tina"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 42000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)
# print(df[["Employee", "Experience"]])

# Display Salary and Experience.
# data = {
#     "Employee": ["Riya", "Jay", "Nisha", "Om", "Tina"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 42000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)
# print(df[["Salary", "Experience"]])

# 3️⃣ Selecting One Row — iloc[]

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
#     "Price": [50000, 800, 1500, 12000],
#     "Sales": [10, 25, 18, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[1])


# Practice — 5 Questions

# આ data use કરો:

# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }

# df = pd.DataFrame(data)

# Select the first row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }

# df = pd.DataFrame(data)
# print(df.iloc[0])

# Select the second row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }

# df = pd.DataFrame(data)
# print(df.iloc[1])

# Select the third row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }

# df = pd.DataFrame(data)
# print(df.iloc[2])

# Select the fourth row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }

# df = pd.DataFrame(data)
# print(df.iloc[3])

# Select the last row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }

# df = pd.DataFrame(data)
# print(df.iloc[4])

# 4️⃣ Selecting Multiple Rows — iloc[]

# Example:

# print(df.iloc[[0, 3]])
# Practice — 5 Questions

# એ જ ઉપરનો data use કરો:

# Select rows at index 0 and 2.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[0, 2]])

# Select rows at index 1 and 4.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[1, 4]])

# Select rows at index 0, 2, and 4.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[0, 2, 4]])

# Select rows at index 1 and 3.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[1,3]])

# Select rows at index 2, 3, and 4.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[2,3,4]])

# 5️⃣ Selecting One Value — iloc[]

# print(df.iloc[1, 0])
# Practice Data
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)

# 5 Practice Questions:

# Select the Product of second row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[1,0])

# Select the Price of third row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[2, 0])

# Select the Category of first row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[2, 1])

# Select the Quantity of fifth row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[4, 3])

# Select the Price of fourth row.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[3, 2])

# 6️⃣ Selecting Multiple Rows and Columns — iloc[]

# print(df.iloc[[0, 2], [0, 3]])
# 5 Practice Questions:

# Select rows 0, 2 and columns 0, 1.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[0, 2], [0, 1]])

# Select rows 1, 3 and columns 0, 2.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[1, 3], [0, 2]])

# Select rows 0, 4 and columns 1, 3.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[0, 4], [1, 3]])

# Select rows 2, 3, 4 and columns 0, 2.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[2, 3, 4], [0, 2]])

# Select rows 1, 2, 4 and columns 0, 3.
# data = {
#     "Product": ["Phone", "Tablet", "Laptop", "Headphone", "Watch"],
#     "Category": ["Mobile", "Electronics", "Computer", "Audio", "Wearable"],
#     "Price": [25000, 18000, 55000, 3000, 5000],
#     "Quantity": [15, 10, 8, 25, 12]
# }
# df = pd.DataFrame(data)
# print(df.iloc[[1, 2, 4], [0, 3]])

# 7️⃣ Selecting a Range of Rows — iloc[]

# df.iloc[0:3]

# Practice Data
# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
#     "Price": [55000, 800, 1500, 12000, 9000, 18000],
#     "Sales": [12, 35, 20, 15, 10, 18]
# }
# df = pd.DataFrame(data)

# 5 Practice Questions
# Select rows from index 0 to 2.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
#     "Price": [55000, 800, 1500, 12000, 9000, 18000],
#     "Sales": [12, 35, 20, 15, 10, 18]
# }
# df = pd.DataFrame(data)
# print(df.iloc[0:2])

# Select rows from index 1 to 3.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
#     "Price": [55000, 800, 1500, 12000, 9000, 18000],
#     "Sales": [12, 35, 20, 15, 10, 18]
# }
# df = pd.DataFrame(data)
# print(df.iloc[1:3])

# Select rows from index 2 to 5.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
#     "Price": [55000, 800, 1500, 12000, 9000, 18000],
#     "Sales": [12, 35, 20, 15, 10, 18]
# }
# df = pd.DataFrame(data)
# print(df.iloc[2:5])

# Select first 4 rows.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
#     "Price": [55000, 800, 1500, 12000, 9000, 18000],
#     "Sales": [12, 35, 20, 15, 10, 18]
# }
# df = pd.DataFrame(data)
# print(df.iloc[0:4])

# Select last 3 rows.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
#     "Price": [55000, 800, 1500, 12000, 9000, 18000],
#     "Sales": [12, 35, 20, 15, 10, 18]
# }
# df = pd.DataFrame(data)
# print(df.iloc[3:6])

# 8️⃣ loc[] — Selecting Rows Using Labels

# PDF મુજબ loc[] row labels અને column names થી data select કરવા માટે use થાય છે.

# Example
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha"],
#     "Department": ["IT", "HR", "Sales", "Finance"],
#     "Salary": [50000, 45000, 55000, 60000]
# }
# df = pd.DataFrame(data)
# print(df.loc[1])

# 5 Practice Questions
# Select row with label 0.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha"],
#     "Department": ["IT", "HR", "Sales", "Finance"],
#     "Salary": [50000, 45000, 55000, 60000]
# }
# df = pd.DataFrame(data)
# print(df.loc[0])

# Select row with label 2.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha"],
#     "Department": ["IT", "HR", "Sales", "Finance"],
#     "Salary": [50000, 45000, 55000, 60000]
# }
# df = pd.DataFrame(data)
# print(df.loc[2])

# Select Employee from row label 1.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha"],
#     "Department": ["IT", "HR", "Sales", "Finance"],
#     "Salary": [50000, 45000, 55000, 60000]
# }
# df = pd.DataFrame(data)
# print(df.loc[1, "Employee"])

# Select Salary from row label 2.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha"],
#     "Department": ["IT", "HR", "Sales", "Finance"],
#     "Salary": [50000, 45000, 55000, 60000]
# }
# df = pd.DataFrame(data)
# print(df.loc[2, "Salary"])

# 9️⃣ loc[] — Selecting Multiple Rows and Columns

# df.loc[[0, 2], ["Name", "Marks"]]

# Practice Data
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }
# df = pd.DataFrame(data)

# 5 Practice Questions

# Select rows 0 and 2, columns Employee and Salary.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }

# df = pd.DataFrame(data)
# print(df.loc[[0, 2], ["Employee", "Salary"]])

# Select rows 1 and 3, columns Department and Experience.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }

# df = pd.DataFrame(data)
# print(df.loc[[1, 3], ["Department", "Experience"]])

# Select rows 0, 2, 4, columns Employee and Salary.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }

# df = pd.DataFrame(data)
# print(df.loc[[0, 2, 4], ["Employee", "Salary"]])

# Select rows 2, 3, 4, columns Department and Salary.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }

# df = pd.DataFrame(data)
# print(df.loc[[2, 3, 4], ["Department", "Salary"]])

# Select rows 1, 2, 4, columns Employee and Experience.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000],
#     "Experience": [3, 2, 4, 6, 5]
# }

# df = pd.DataFrame(data)
# print(df.loc[[1, 2, 4], ["Employee", "Experience"]])

# 10️⃣ loc[] vs iloc[]

# Example
# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
#     "Price": [55000, 800, 1500, 12000, 9000]
# }

# df = pd.DataFrame(data)
# print(df.loc[2])
# print(df.iloc[2])

# Practice — 5 Questions
# loc[] થી row label 1 select કરો.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
#     "Price": [55000, 800, 1500, 12000, 9000]
# }

# df = pd.DataFrame(data)
# print(df.loc[1])

# iloc[] થી position 3 select કરો.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
#     "Price": [55000, 800, 1500, 12000, 9000]
# }

# df = pd.DataFrame(data)
# print(df.iloc[3])

# loc[] થી row label 0 અને 2 select કરો.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
#     "Price": [55000, 800, 1500, 12000, 9000]
# }

# df = pd.DataFrame(data)
# print(df.loc[[0, 2]])

# iloc[] થી position 1 અને 4 select કરો.
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
#     "Price": [55000, 800, 1500, 12000, 9000]
# }

# df = pd.DataFrame(data)
# print(df.iloc[[1, 4]])


# 11️⃣ Slicing

# import pandas as pd

# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch", "Camera", "Printer"],
#     "Price": [25000, 55000, 18000, 5000, 35000, 9000],
#     "Sales": [20, 12, 18, 30, 10, 15]
# }

# df = pd.DataFrame(data)
# print(df.iloc[1:4])

# Practice — 5 Questions

# Use same data:

# First 3 rows select કરો.
# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch", "Camera", "Printer"],
#     "Price": [25000, 55000, 18000, 5000, 35000, 9000],
#     "Sales": [20, 12, 18, 30, 10, 15]
# }

# df = pd.DataFrame(data)
# print(df.iloc[0:3])

# Rows from index 2 to 4 select કરો.
# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch", "Camera", "Printer"],
#     "Price": [25000, 55000, 18000, 5000, 35000, 9000],
#     "Sales": [20, 12, 18, 30, 10, 15]
# }

# df = pd.DataFrame(data)
# print(df.iloc[2:5])

# Index 3 થી end સુધીના rows select કરો.
# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch", "Camera", "Printer"],
#     "Price": [25000, 55000, 18000, 5000, 35000, 9000],
#     "Sales": [20, 12, 18, 30, 10, 15]
# }

# df = pd.DataFrame(data)
# print(df.iloc[3:])

# All rows અને only Price, Sales columns select કરો.
# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch", "Camera", "Printer"],
#     "Price": [25000, 55000, 18000, 5000, 35000, 9000],
#     "Sales": [20, 12, 18, 30, 10, 15]
# }

# df = pd.DataFrame(data)
# print(df[["Price", "Sales"]])

# Rows 1 to 4 અને columns Product, Price select કરો.
# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch", "Camera", "Printer"],
#     "Price": [25000, 55000, 18000, 5000, 35000, 9000],
#     "Sales": [20, 12, 18, 30, 10, 15]
# }

# df = pd.DataFrame(data)
# print(df.iloc[1:5, 0:2])

# 12️⃣ Boolean Indexing

# import pandas as pd

# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Salary"] > 50000])

# Practice — 5 Questions

# Salary > 50000 હોય એવા employees શોધો.

# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Salary"] > 50000])

# Salary < 50000 હોય એવા employees શોધો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Salary"] < 50000])

# Salary >= 58000 હોય એવા employees શોધો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Salary"] >= 50000])

# Department "IT" હોય એવા employees શોધો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Department"] == "IT"])

# Salary == 45000 હોય એવો employee શોધો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Salary"] == 45000])

# 13️⃣ Conditional Selection with loc[]

# Condition પ્રમાણે rows filter કરવા અને સાથે specific columns select કરવા.

# Example
# import pandas as pd

# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [45000, 52000, 38000, 65000, 58000]
# }
# df = pd.DataFrame(data)
# print(df.loc[df["Salary"] > 50000, ["Employee", "Salary"]])

# Practice — 5 Questions

# આ data use કરો:

# data = {
#     "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
#     "Category": ["Computer", "Mobile", "Electronics", "Computer", "Office"],
#     "Price": [55000, 25000, 18000, 12000, 9000],
#     "Sales": [15, 30, 22, 18, 12]
# }
# df = pd.DataFrame(data)

# # Price > 20000 વાળા products માંથી Product અને Price select કરો.
# data = {
#     "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
#     "Category": ["Computer", "Mobile", "Electronics", "Computer", "Office"],
#     "Price": [55000, 25000, 18000, 12000, 9000],
#     "Sales": [15, 30, 22, 18, 12]
# }
# df = pd.DataFrame(data)
# print(df.loc[df["Price"] > 20000, ["Product", "Price"]])

# Sales > 20 વાળા products માંથી Product અને Sales select કરો.
# data = {
#     "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
#     "Category": ["Computer", "Mobile", "Electronics", "Computer", "Office"],
#     "Price": [55000, 25000, 18000, 12000, 9000],
#     "Sales": [15, 30, 22, 18, 12]
# }
# df = pd.DataFrame(data)
# print(df.loc[df["Sales"] > 20, ["Product", "Sales"]])

# Category == "Computer" વાળા products માંથી Product અને Price select કરો.
# data = {
#     "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
#     "Category": ["Computer", "Mobile", "Electronics", "Computer", "Office"],
#     "Price": [55000, 25000, 18000, 12000, 9000],
#     "Sales": [15, 30, 22, 18, 12]
# }
# df = pd.DataFrame(data)
# print(df.loc[df["Category"] == "Computer", ["Product", "Price"]])

# Price < 15000 વાળા products માંથી Product, Category, Price select કરો.
# data = {
#     "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
#     "Category": ["Computer", "Mobile", "Electronics", "Computer", "Office"],
#     "Price": [55000, 25000, 18000, 12000, 9000],
#     "Sales": [15, 30, 22, 18, 12]
# }
# df = pd.DataFrame(data)
# print(df.loc[df["Price"] < 15000, ["Product", "Category", "Price"]])

# Sales >= 18 વાળા products માંથી Product અને Sales select કરો.
# data = {
#     "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer"],
#     "Category": ["Computer", "Mobile", "Electronics", "Computer", "Office"],
#     "Price": [55000, 25000, 18000, 12000, 9000],
#     "Sales": [15, 30, 22, 18, 12]
# }
# df = pd.DataFrame(data)
# print(df.loc[df["Sales"] >= 18, ["Product", "Sales"]])

# 14️⃣ Conditional Selection with iloc[]

# PDF મુજબ iloc[] direct Boolean condition accept કરતું નથી. પહેલા condition બનાવીને positions મેળવવાની હોય છે.

# Example
# import pandas as pd

# data = {
#     "Student": ["Riya", "Aman", "Neha", "Dev", "Karan"],
#     "Marks": [78, 92, 85, 67, 95],
#     "City": ["Surat", "Rajkot", "Ahmedabad", "Surat", "Vadodara"]
# }

# df = pd.DataFrame(data)

# condition = df["Marks"] > 85
# positions = df.index[condition]
# print(df.iloc[positions, [0, 1]])

# Practice — 5 Questions

# આ જ data use કરો:

# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }
# df = pd.DataFrame(data)

# Salary > 50000 વાળા employees ના Employee અને Salary select કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }
# df = pd.DataFrame(data)
# condition = df["Salary"] > 50000
# position = df.index[condition]
# print(df.iloc[position, [0, 2]])

# Salary < 50000 વાળા employees ના Employee અને Department select કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }
# df = pd.DataFrame(data)
# condition = df["Salary"] < 50000
# position = df.index[condition]
# print(df.iloc[position, [0, 1]])

# Salary >= 58000 વાળા employees ના Employee અને Salary select કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }
# df = pd.DataFrame(data)
# condition = df["Salary"] >= 58000
# position = df.index[condition]
# print(df.iloc[position, [0, 2]])

# Department == "IT" વાળા employees ના Employee અને Department select કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }
# df = pd.DataFrame(data)
# condition = df["Department"] == "IT"
# position = df.index[condition]
# print(df.iloc[position, [0, 1]])

# Salary > 45000 વાળા employees ના Employee અને Salary select કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [52000, 45000, 48000, 65000, 58000]
# }
# df = pd.DataFrame(data)
# condition = df["Salary"] > 45000
# position = df.index[condition]
# print(df.iloc[position, [0, 2]])

# 15️⃣ Sorting Data — sort_values()

# Column ના values પ્રમાણે data sort કરવા માટે sort_values() વપરાય છે.

# Example
# import pandas as pd

# data = {
#     "Product": ["Bag", "Shoes", "Watch", "Jacket", "Cap"],
#     "Price": [1200, 2500, 1800, 3200, 700]
# }
# df = pd.DataFrame(data)
# print(df.sort_values("Price"))

# આ Price ની smallest → largest order માં data આપશે.

# Practice — 5 Questions
# data = {
#     "Product": ["Keyboard", "Mouse", "Monitor", "Laptop", "Speaker"],
#     "Price": [1500, 800, 12000, 55000, 2500],
#     "Sales": [20, 45, 15, 10, 30]
# }

# df = pd.DataFrame(data)

# Price પ્રમાણે ascending order માં sort કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Monitor", "Laptop", "Speaker"],
#     "Price": [1500, 800, 12000, 55000, 2500],
#     "Sales": [20, 45, 15, 10, 30]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Price"))

# Price પ્રમાણે descending order માં sort કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Monitor", "Laptop", "Speaker"],
#     "Price": [1500, 800, 12000, 55000, 2500],
#     "Sales": [20, 45, 15, 10, 30]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Price", ascending=False))

# Sales પ્રમાણે ascending order માં sort કરો.
# Price પ્રમાણે descending order માં sort કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Monitor", "Laptop", "Speaker"],
#     "Price": [1500, 800, 12000, 55000, 2500],
#     "Sales": [20, 45, 15, 10, 30]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Sales"))

# Sales પ્રમાણે descending order માં sort કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Monitor", "Laptop", "Speaker"],
#     "Price": [1500, 800, 12000, 55000, 2500],
#     "Sales": [20, 45, 15, 10, 30]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Sales", ascending=False))

# 1️⃣6️⃣ sort_index()

# Example
# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
#     "Price": [55000, 800, 1500, 12000]
# }

# df = pd.DataFrame(data, index=[3, 1, 4, 2])
# print(df)
# print(df.sort_index())


# 📝 Practice — 5 Questions

# આ data use કરો:

# data = {
#     "Customer": ["Amit", "Riya", "Karan", "Neha", "Vivek"],
#     "Sales": [25000, 18000, 32000, 15000, 28000]
# }

# df = pd.DataFrame(data, index=[4, 2, 5, 1, 3])

# Index પ્રમાણે ascending order માં DataFrame sort કરો.
# data = {
#     "Customer": ["Amit", "Riya", "Karan", "Neha", "Vivek"],
#     "Sales": [25000, 18000, 32000, 15000, 28000]
# }

# df = pd.DataFrame(data, index=[4, 2, 5, 1, 3])
# print(df.sort_index())

# Index પ્રમાણે descending order માં DataFrame sort કરો.
# data = {
#     "Customer": ["Amit", "Riya", "Karan", "Neha", "Vivek"],
#     "Sales": [25000, 18000, 32000, 15000, 28000]
# }

# df = pd.DataFrame(data, index=[4, 2, 5, 1, 3])
# print(df.sort_index(ascending=False))

# Index 1, 2, 3, 4, 5 order માં data display કરો.
# data = {
#     "Customer": ["Amit", "Riya", "Karan", "Neha", "Vivek"],
#     "Sales": [25000, 18000, 32000, 15000, 28000]
# }

# df = pd.DataFrame(data, index=[1, 2, 3, 4, 5])
# print(df.sort_index())

# sort_index() નો ઉપયોગ કરીને smallest index first કરો.
# data = {
#     "Customer": ["Amit", "Riya", "Karan", "Neha", "Vivek"],
#     "Sales": [25000, 18000, 32000, 15000, 28000]
# }

# df = pd.DataFrame(data, index=[1, 2, 3, 4, 5])
# print(df.sort_index())

# sort_index() નો ઉપયોગ કરીને largest index first કરો.
# data = {
#     "Customer": ["Amit", "Riya", "Karan", "Neha", "Vivek"],
#     "Sales": [25000, 18000, 32000, 15000, 28000]
# }

# df = pd.DataFrame(data, index=[1, 2, 3, 4, 5])
# print(df.sort_index(ascending=False))

# 1️⃣7️⃣ ascending

# import pandas as pd

# data = {
#     "Product": ["Phone", "Laptop", "Tablet", "Watch"],
#     "Price": [25000, 55000, 18000, 5000]
# }

# df = pd.DataFrame(data)

# # Ascending
# print(df.sort_values("Price", ascending=True))

# # Descending
# print(df.sort_values("Price", ascending=False))

# 📝 Practice — 5 Questions

# આ data use કરો:

# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Salary": [52000, 45000, 68000, 39000, 58000]
# }

# df = pd.DataFrame(data)

# Salary ને ascending order માં sort કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Salary": [52000, 45000, 68000, 39000, 58000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Salary", ascending=True))

# Salary ને descending order માં sort કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Salary": [52000, 45000, 68000, 39000, 58000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Salary", ascending=False))

# Salary smallest થી largest ascending parameter થી sort કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Salary": [52000, 45000, 68000, 39000, 58000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Salary", ascending=True))

# Salary largest થી smallest ascending parameter થી sort કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Salary": [52000, 45000, 68000, 39000, 58000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Salary", ascending=False))

# Salary descending order માં sort કરીને complete DataFrame display કરો.
# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Salary": [52000, 45000, 68000, 39000, 58000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Salary", ascending=False))

# 1️⃣8️⃣ Multiple Column Sorting

# Example
# import pandas as pd

# data = {
#     "Employee": ["Asha", "Rahul", "Meera", "Vivek", "Pooja", "Karan"],
#     "Department": ["IT", "HR", "IT", "HR", "IT", "Sales"],
#     "Salary": [60000, 45000, 50000, 55000, 70000, 40000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values(["Department", "Salary"]))

# Different sorting order


# 📝 Practice — 5 Questions

# આ data use કરો:

# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav", "Riya"],
#     "Department": ["Sales", "IT", "Sales", "HR", "IT", "HR"],
#     "Salary": [45000, 65000, 52000, 48000, 55000, 60000]
# }

# df = pd.DataFrame(data)

# Department અને પછી Salary પ્રમાણે ascending sort કરો.
# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav", "Riya"],
#     "Department": ["Sales", "IT", "Sales", "HR", "IT", "HR"],
#     "Salary": [45000, 65000, 52000, 48000, 55000, 60000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values(["Department", "Salary"]))

# Department ascending અને Salary descending sort કરો.
# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav", "Riya"],
#     "Department": ["Sales", "IT", "Sales", "HR", "IT", "HR"],
#     "Salary": [45000, 65000, 52000, 48000, 55000, 60000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values([ "Department", "Salary"], ascending=[True, False]))

# Department અને Salary બંને પ્રમાણે sort કરીને complete DataFrame display કરો.
# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav", "Riya"],
#     "Department": ["Sales", "IT", "Sales", "HR", "IT", "HR"],
#     "Salary": [45000, 65000, 52000, 48000, 55000, 60000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values([ "Department", "Salary"], ascending=[True, False]))

# Department sort કરો અને દરેક departmentમાં highest Salary first રાખો.
# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav", "Riya"],
#     "Department": ["Sales", "IT", "Sales", "HR", "IT", "HR"],
#     "Salary": [45000, 65000, 52000, 48000, 55000, 60000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values([ "Department", "Salary"], ascending=[True, False]))

# Department ascending અને Salary descending માટે ascending parameter નો ઉપયોગ કરો.
# data = {
#     "Employee": ["Aarav", "Diya", "Kabir", "Isha", "Manav", "Riya"],
#     "Department": ["Sales", "IT", "Sales", "HR", "IT", "HR"],
#     "Salary": [45000, 65000, 52000, 48000, 55000, 60000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values([ "Department", "Salary"], ascending=[False, True]))

# 1️⃣9️⃣ na_position

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Phone", "Tablet"],
#     "Price": [55000, None, 25000, None]
# }

# df = pd.DataFrame(data)

# print(df.sort_values("Price", na_position="last"))
# print(df.sort_values("Price", na_position="first"))

# 📝 Practice — 5
# data = {
#     "Customer": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Sales": [25000, None, 18000, None, 32000]
# }

# df = pd.DataFrame(data)

# Sales ascending કરો અને NaN ને last માં રાખો.
# data = {
#     "Customer": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Sales": [25000, None, 18000, None, 32000]
# }

# df = pd.DataFrame(data)

# Sales ascending કરો અને NaN ને first માં રાખો.
# print(df.sort_values("Sales", na_position="last"))
# data = {
#     "Customer": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Sales": [25000, None, 18000, None, 32000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Sales", na_position="first"))

# Sales descending કરો અને NaN ને last માં રાખો.
# data = {
#     "Customer": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Sales": [25000, None, 18000, None, 32000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Sales", na_position="last", ascending=False))

# Sales descending કરો અને NaN ને first માં રાખો.
# data = {
#     "Customer": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Sales": [25000, None, 18000, None, 32000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Sales", na_position="first", ascending=False))

# na_position નો ઉપયોગ કરીને missing Sales records ને શરૂઆતમાં લાવો.
# data = {
#     "Customer": ["Asha", "Rahul", "Meera", "Vivek", "Pooja"],
#     "Sales": [25000, None, 18000, None, 32000]
# }

# df = pd.DataFrame(data)
# print(df.sort_values("Sales", na_position="first"))

# 2️⃣0️⃣ Filtering Data

# Example
# import pandas as pd

# data = {
#     "Product": ["Laptop", "Phone", "Mouse", "Monitor", "Tablet"],
#     "Sales": [55000, 30000, 12000, 18000, 25000]
# }

# df = pd.DataFrame(data)
# print(df[df["Sales"] > 20000])

# 📝 Practice — 5
# data = {
#     "Product": ["Keyboard", "Mouse", "Laptop", "Phone", "Monitor"],
#     "Price": [1500, 800, 55000, 25000, 12000],
#     "Sales": [20, 45, 8, 30, 15]
# }

# df = pd.DataFrame(data)

# Sales > 20 હોય તેવી rows select કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Laptop", "Phone", "Monitor"],
#     "Price": [1500, 800, 55000, 25000, 12000],
#     "Sales": [20, 45, 8, 30, 15]
# }

# df = pd.DataFrame(data)
# print(df[df["Sales"] > 20])

# Price > 20000 હોય તેવી rows select કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Laptop", "Phone", "Monitor"],
#     "Price": [1500, 800, 55000, 25000, 12000],
#     "Sales": [20, 45, 8, 30, 15]
# }

# df = pd.DataFrame(data)
# print(df[df["Price"]> 20000])

# Sales < 20 હોય તેવી rows select કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Laptop", "Phone", "Monitor"],
#     "Price": [1500, 800, 55000, 25000, 12000],
#     "Sales": [20, 45, 8, 30, 15]
# }

# df = pd.DataFrame(data)
# print(df[df["Sales"] < 20])

# Price == 12000 હોય તેવી row select કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Laptop", "Phone", "Monitor"],
#     "Price": [1500, 800, 55000, 25000, 12000],
#     "Sales": [20, 45, 8, 30, 15]
# }

# df = pd.DataFrame(data)
# print(df[df["Price"] == 12000])

# Sales >= 30 હોય તેવી rows select કરો.
# data = {
#     "Product": ["Keyboard", "Mouse", "Laptop", "Phone", "Monitor"],
#     "Price": [1500, 800, 55000, 25000, 12000],
#     "Sales": [20, 45, 8, 30, 15]
# }

# df = pd.DataFrame(data)
# print(df[df["Sales"] >= 30])

# 2️⃣1️⃣ Selecting vs Filtering

# PDF પ્રમાણે:

# Selecting → કયો data/column જોઈએ તે પસંદ કરવું.

# df[["Product", "Sales"]]

# Filtering → કઈ condition satisfy કરતી rows જોઈએ તે પસંદ કરવું.

# df[df["Sales"] > 20000]


# 📝 Practice — 5
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha", "Dev"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [55000, 42000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)

# Select only Employee and Salary.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha", "Dev"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [55000, 42000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[["Employee", "Salary"]])

# Filter employees whose Salary > 50000.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha", "Dev"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [55000, 42000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Salary"] > 50000])

# Select only Department column.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha", "Dev"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [55000, 42000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df["Department"])

# Filter employees from IT department.
# data = {
#     "Employee": ["Amit", "Riya", "Karan", "Neha", "Dev"],
#     "Department": ["IT", "HR", "Sales", "IT", "Finance"],
#     "Salary": [55000, 42000, 48000, 65000, 58000]
# }

# df = pd.DataFrame(data)
# print(df[df["Department"] == "IT"])



