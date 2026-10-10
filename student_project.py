# Pandas Practice - Student Course Records
import pandas as pd
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df)

# Section 1: Reading & Exploring Data

# Q1. Read the file Student_Course_Records.csv into a DataFrame.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df)

# Q2. Display the first 5 rows of the dataset.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.head(5))

# Q3. Display the first 20 rows of the dataset.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.head(20))

# Q4. Display the last 5 rows of the dataset.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.tail())

# Q5. Display the last 15 rows of the dataset.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.tail(15))

# Q6. Find the total number of rows and columns.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.shape)

# Q7. Display all column names of the dataset.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.columns)

# Q8. Display column data types, non-null counts, and memory usage.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.info())

# Q9. Display the statistical summary of all numeric columns.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df.describe())

# Q10. Count how many students are enrolled in each Course_Name.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df["Course_Name"].value_counts())

# Q11. Count how many students study in each Learning_Mode.
# df = pd.read_csv("D:\Student_Course_Records.csv")
# print(df["Learning_Mode"].value_counts())

# Q12. Find the number of unique cities students come from.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["City"].nunique())

# Q13. Display all unique values of the Course_Status column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["City"].unique())

# Q14. Check only the data type of every column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.dtypes)

# Q15. Display any 10 random students from the dataset.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.sample(10))

# Section 2: Selecting Data
# Q16. Select only the Student_Name column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Student_Name"])

# Q17. Select Student_ID, Course_Name, and Course_Fees columns together.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df[["Student_ID", "Course_Name", "Course_Fees"]])

# Q18. Select the first student using position.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.iloc[0])

# Q19. Select the row with index label 2000.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.loc[2000])

# Q20. Select rows from position 100 to 110.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.iloc[100:111])

# Q21. Select rows 0 to 500 with only Student_Name and Grade using labels.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.loc[0:500, ["Student_Name", "Grade"]])

# Q22. Select the value at row position 7 and column position 4.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.iloc[7, 4])

# Q23. Select every 10th row from the first 200 rows.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.iloc[0:200:10])

# Q24. Select the last 25 rows using negative indexing.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.iloc[-25:])

# Q25. Select only the first 8 columns for all rows.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.iloc[:, 0:8])

# Q26. Select the Theory_Marks of the student at row label 777.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.loc[777, "Theory_Marks"])

# Q27. Select all columns from Course_Name to Grade using labels.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.loc[:, "Course_Name" : "Grade"])

# Section 3: Sorting Data
# Q28. Sort the dataset by Course_Fees in ascending order.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Course_Fees"].sort_values(ascending=True))

# Q29. Sort the dataset by Course_Fees in descending order.
# Answer: sort_values(ascending=False)
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Course_Fees"].sort_values(ascending=False))

# Q30. Sort students by Theory_Marks from highest to lowest.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Theory_Marks"].sort_values(ascending=False))

# Q31. Sort the dataset by Student_Name alphabetically.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Student_Name"].sort_values(ascending=True))

# Q32. Sort by Course_Name first and then by Theory_Marks within each course.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.sort_values(by=["Course_Name", "Theory_Marks"]))

# Q33. Sort by City ascending and Attendance_Percent descending together.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.sort_values(by=["City", "Attendance_Percent"],
#                      ascending=[True, False]))

# Q34. Sort the dataset by its index.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.sort_index(ascending=True))

# Q35. Sort the dataset by index in descending order.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.sort_index(ascending=False))

# Q36. Sort by Student_Rating and place all NaN values at the top.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Student_Rating"].sort_values(na_position="first"))

# Q37. Find the top 10 students with the highest Package_Offered.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["Package_Offered"].sort_values().head(10))

# Section 4: Filtering Data

# Q38. Filter all students whose Course_Fees is above 50000.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# print(df["Course_Fees"] > 50000)

# Q39. Filter all students from the city Surat.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df["City"] == "Surat")


# Q40. Filter all students with Attendance_Percent greater than or equal to 75.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Attendance_Percent"] >= 75
# print(df["Attendance_Percent"])

# Q41. Filter all students whose Theory_Marks is below 35 (failed students).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Theory_Marks"] < 35
# print(df["Theory_Marks"])

# Q42. Filter Data Science students with marks above 80 (both conditions).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[(df["Course_Name"] == "Data Science") & 
#             (df["Theory_Marks"] > 80)]
# print(result)

# Q43. Filter students who study in Morning or Evening batch.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[df["Batch_Time"].isin(["Morning", "Evening"])]
# print(result)

# Q44. Filter students from Surat, Ahmedabad, or Rajkot.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[df["City"].isin(["Surat", "Ahmedabad", "Rajkot"])]
# print(result)

# Q45. Filter students whose fees is between 20000 and 60000.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# result = df[df["Course_Fees"].between(20000, 80000)]
# print(result)

# Q46. Filter students whose Attendance_Percent is between 60 and 80.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Attendance_Percent"] = df["Attendance_Percent"].between(60, 80)
# print(df["Attendance_Percent"])

# Q47. Filter students who are either from Surat or placed (any one condition).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[(df["City"] == "Surat") | (df["Placement_Status"] == "Placed")]
# print(result)

# Q48. Filter all students NOT enrolled in Digital Marketing.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[df["Course_Name"] != "Digital Marketing"]
# print(result)

# Q49. Filter Graduate students with attendance above 80 using a query string.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.query(
#     'Education == "Graduate" and Attendance_Percent > 80'
# )[["Student_Name", "Attendance_Percent"]]
# print(result)

# Q50. Hide (replace with NaN) all Theory_Marks below 35.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Theory_Marks"] = df["Theory_Marks"].mask(
#     df["Theory_Marks"] < 35
# )
# print(df[["Student_Name", "Theory_Marks"]])

# Q51. Keep only rows where Age is between 15 and 60 (valid ages).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[df["Age"].between(15, 60)]
# print(result[["Student_Name" , "Age"]])

# Section 5: Handling Missing Values

# Q52. Check which cells of the dataset are missing.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.isnull()
# print(result)

# Q53. Count total missing values in every column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.isnull().sum()
# print(result)

# Q54. Check which cells are NOT missing.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.notnull()
# print(result)

# Q55. Count missing values only in the Package_Offered column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Package_Offered"].isnull().sum()
# print(result)

# Q56. Remove all rows containing any missing value.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.dropna()
# print(result)

# Q57. Remove rows only where Email is missing.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.dropna(subset=["Email"])
# print(result)

# Q58. Remove columns that contain any missing value.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.dropna(axis=1)
# print(result)

# Q59. Fill missing Company_Name values with 'Not Placed'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Company_Name"].fillna("Not Placed")
# print(result)

# Q60. Fill missing Theory_Marks with the average marks.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Theory_Marks"].fillna(df["Theory_Marks"].mean())
# print(result)

# Q61. Fill missing Project_Marks with 0.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Project_Marks"].fillna(0)
# print(result)

# Q62. Fill missing Attendance_Percent using the previous row's value.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Attendance_Percent"].ffill()
# print(result)

# Q63. Fill missing Attendance_Percent using the next row's value.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Attendance_Percent"].bfill()
# print(result)

# Q64. Fill missing numeric values using interpolation.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# numeric_cols = df.select_dtypes(include="number").columns
# df[numeric_cols] = df[numeric_cols].interpolate()
# print(df)

# Q65. Replace all 99 values in Student_Rating with NaN.
# import numpy as np
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Student_Rating"].replace(99, np.nan)
# print(result)

# Section 6: Handling Duplicates

# Q66. Check which rows are duplicates.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df[df.duplicated()])

# Q67. Count the total duplicate rows in the dataset.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.duplicated().sum())

# Q68. Remove all duplicate rows keeping the first occurrence.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.drop_duplicates())

# Q69. Remove duplicate rows keeping the last occurrence.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.drop_duplicates(keep="last"))

# Q70. Find duplicates based only on the Student_ID column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df[df.duplicated(subset=["Student_ID"])])

# Q71. Keep only one row per Phone number.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# print(df.drop_duplicates(subset=["Phone"]))

# Section 7: Data Cleaning

# Q72. Rename the column Course_Fees to Total_Fees.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.rename(columns={"Course_Fees" : "Total_Fees"})
# print(result)

# Q73. Rename Student_Name to Name and City to Student_City together.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.rename(columns={"Student_Name" : "Name",
#                             "City" : "Student_City"})
# print(result)

# Q74. Delete the Referral_Source column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.drop(columns=["Referral_Source"])
# print(result)

# Q75. Delete rows at index 5, 6, and 7.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.drop(index=[5, 6, 7])
# print(result)

# Q76. Remove extra spaces from City values.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["City"] = df["City"].str.strip()
# print(df["City"])

# Q77. Convert all Student_Name values to lowercase.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Student_Name"] = df["Student_Name"].str.lower()
# print(df["Student_Name"])

# Q78. Convert all Student_Name values to UPPERCASE.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Student_Name"] = df["Student_Name"].str.upper()
# print(df["Student_Name"])

# Q79. Convert City values to proper case.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["City"] = df["City"].str.title()
# print(df["City"])

# Q80. Standardize Gender by converting M/male to Male and F/female to Female.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Gender"] = df["Gender"].replace({"M" : "Male",
#                                     "male" : "Male",
#                                     "F" : "Female",
#                                     "female" : "Female"})
# print(df["Gender"])

# Q81. Standardize Batch_Time so morning/EVENING become Morning and Evening.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Batch_Time"] = df["Batch_Time"].replace({"morning" : "Morning",
#                                              "EVENING" : "Evening"})
# print(df["Batch_Time"])

# Section 8: Data Type Conversion

# Q82. Check the current data type of Course_Fees.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = df["Course_Fees"].dtypes
# print(df["Course_Fees"])

# Q83. Remove commas from Course_Fees values stored as text.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = df["Course_Fees"].astype(str).str.replace(
#     ",", "", regex=False
# )
# print(df["Course_Fees"])

# Q84. Convert the cleaned Course_Fees to float type.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# print(df["Course_Fees"].astype(float))

# Q85. Convert Age to integer type after cleaning missing values.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Age"] = pd.to_numeric(
#     df["Age"],
#     errors="coerce"
# )
# df["Age"] = df["Age"].fillna(df["Age"].median())
# df["Age"] = df["Age"].astype(int)

# print(df["Age"])

# Q86. Convert Admission_Date from text to datetime type.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     errors="coerce"
# )
# print(df["Admission_Date"])

# Q87. Convert Course_Name to category data type.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Name"] = df["Course_Name"].astype("category")
# print(df["Course_Name"])

# Q88. Convert Theory_Marks to numeric and force invalid values to NaN.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Theory_Marks"] = pd.to_numeric(
#     df["Theory_Marks"],
#     errors="coerce"
# )
# print(df["Theory_Marks"])


# Section 9: Adding & Modifying Columns

# Q89. Create a column Total_Marks = Theory_Marks + Practical_Marks + Project_Marks.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Total_Marks"] = df["Theory_Marks"] + df["Practical_Marks"] + df["Project_Marks"]
# print(df["Total_Marks"])

# Q90. Create a column Pending_Fees = Course_Fees minus Fees_Paid.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# df["Fees_Paid"] = pd.to_numeric(
#     df["Fees_Paid"],
#     errors="coerce"
# )
# df["Pending_Fees"] = df["Course_Fees"] - df["Fees_Paid"]
# print(df["Pending_Fees"])

# Q91. Insert a column Institute with value 'Skywin IT Academy' at position 2.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.insert(2, "Institute_Name", "skywin IT Academy")
# print(result)

# Q92. Create a column Percentage = Total_Marks divided by 3.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Total_Marks"] = df["Theory_Marks"] + df["Practical_Marks"] + df["Project_Marks"]
# df["Percentage"] = df["Total_Marks"] / 3
# print(df["Percentage"])

# Q93. Create a column Result: 'Pass' if Theory_Marks >= 35 else 'Fail'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Result"] = df["Theory_Marks"].apply(lambda x: "Pass" if x>= 35 else "Fail")
# print(df["Result"])

# Q94. Create a column Attendance_Status: 'Regular' if attendance >= 75 else 'Irregular'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Attendance_Status"] = df["Attendance_Percent"].apply(lambda x: "Regular" if x>=75 else "Irregular")
# print(df["Attendance_Status"])

# Q95. Apply a lambda to add 5 grace marks to every Theory_Marks value.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Theory_Marks"] = df["Theory_Marks"].apply(lambda x:x+5)
# print(df["Theory_Marks"])

# Q96. Create a column Age_Group: Teen (17-19), Young (20-25), Adult (26+).
# import numpy as np
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Age_Group"] = pd.cut(df["Age"],
#                          bins=[16, 19, 25, np.inf],
#                          labels=["Teen", "Young", "Adult"])
# print(df[["Age", "Age_Group"]])

# Q97. Update all Course_Status values of 'completed' to 'Completed'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Status"] = df["Course_Status"].replace({"completed" : "Completed"})
# print(df["Course_Status"])

# Q98. Create a column Fees_Status: 'Paid' where Pending_Fees is 0 else 'Pending'.
# import pandas as pd
# import numpy as np

# df = pd.read_csv(r"D:\Student_Course_Records.csv")

# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )

# df["Fees_Paid"] = pd.to_numeric(
#     df["Fees_Paid"],
#     errors="coerce"
# )

# # First create Pending_Fees
# df["Pending_Fees"] = df["Course_Fees"] - df["Fees_Paid"]

# # Then create Fees_Status
# df["Fees_Status"] = np.where(
#     df["Pending_Fees"] == 0,
#     "Paid",
#     "Pending"
# )
# print(df[["Pending_Fees", "Fees_Status"]])

# Q99. Increase Course_Fees of all courses by 10%.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# df["Increses_Fee"] = df["Course_Fees"] * 1.10
# print(df["Increses_Fee"])

# Q100. Delete the newly created Institute column.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.drop(columns=["Institute_Name"],inplace=True)
# print(result)

# Section 10: String Functions

# Q101. Find the length of each Student_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Student_Name"] = df["Student_Name"].str.len()
# print(df["Student_Name"])

# Q102. Split Student_Name into First_Name and Last_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Student_Name"] = df["Student_Name"].str.split()
# print(df["Student_Name"])

# Q103. Filter all students whose name contains 'Patel'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Student_Name"] = df["Student_Name"].str.contains("Patel", case=False, na=False)
# print(df["Student_Name"])

# Q104. Filter all students whose name starts with 'K'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Student_Name"].str.startswith("K", na=False)
# print(result)

# Q105. Filter all students whose name ends with 'Shah'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[df["Student_Name"].str.endswith("Shah", na=False)]
# print(result)

# Q106. Extract the year part from Student_ID (e.g. 2023 from STU-2023-000123).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Year"] = df["Student_ID"].str.split("-").str[1]
# print(df[["Student_ID", "Year"]])

# Q107. Extract only the numeric part from Student_ID.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Numeric_ID"] = df["Student_ID"].str.extract(r"(\d+)$")
# print(df[["Student_ID", "Numeric_ID"]])

# Q108. Filter all Email values that do NOT contain '@'.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[~df["Email"].str.contains("@", na=False)]
# print(result)

# Q109. Extract the domain name from Email addresses.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Email"] = df["Email"].str.split()
# print(df["Email"])

# Q110. Remove '+91-' from Phone values.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Phone"] = df["Phone"].astype(str).str.replace("+91-", "", regex=False)
# print(df[["Phone"]])

# Q111. Capitalize only the first letter of each City.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["City"] = df["City"].str.capitalize()
# print(df["City"])

# Q112. Count how many students have 'Desai' in their name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Student_Name"] = df["Student_Name"].str.contains("Desai", case=False, na=False).sum()
# print(df["Student_Name"])

# Section 11: Date & Time Functions

# Q113. Convert Admission_Date with mixed formats into proper datetime.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df["Admission_Date"])

# Q114. Extract the year from Admission_Date.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df["Admission_Date"].dt.year)

# Q115. Extract the month number from Admission_Date.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df["Admission_Date"].dt.month)

# Q116. Extract the day from Admission_Date.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df["Admission_Date"].dt.day)

# Q117. Extract the day name from Admission_Date.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df["Admission_Date"].dt.day_name())

# Q118. Extract the month name from Admission_Date.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df["Admission_Date"].dt.month_name())

# Q119. Filter all admissions of the year 2024.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df[df["Admission_Date"].dt.year == 2024])

# Q120. Filter all admissions taken in the month of June.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")

# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )

# print(df[df["Admission_Date"].dt.month == 6])

# Q121. Filter all admissions done on Sunday.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# print(df[df["Admission_Date"].dt.day_name() == "Sunday"])

# Q122. Calculate how many days each student has been enrolled (today minus Admission_Date).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )

# df["Enrolled_Days"] = (pd.Timestamp.today() - df["Admission_Date"]).dt.days
# print(df[["Student_Name", "Admission_Date", "Enrolled_Days"]])

# Q123. Display Admission_Date in the format 15-Jan-2024.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# df["Formatted_Date"] = df["Admission_Date"].dt.strftime("%d-%b-%Y")
# print(df[["Admission_Date", "Formatted_Date"]])

# Q124. Find the earliest and latest admission dates.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# df["Earliest_date"] = df["Admission_Date"].min()
# print(df["Earliest_date"])

# df["Latest_date"] = df["Admission_Date"].max()
# print(df["Latest_date"])

# Section 12: GroupBy & Aggregation

# Q125. Find total Course_Fees collected for each Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Course_Fees"].sum()
# print(result)

# Q126. Find the average Theory_Marks for each Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Theory_Marks"].mean()
# print(result)

# Q127. Count the number of students in each Batch_Time.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Batch_Time")["Student_Name"].count()
# print(result)

# Q128. Find the maximum Package_Offered for each Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Package_Offered"].max()
# print(result)

# Q129. Find the minimum Attendance_Percent in each Learning_Mode.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Learning_Mode")["Attendance_Percent"].min()
# print(result)

# Q130. Find total Fees_Paid collected from each City.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("City")["Fees_Paid"].sum()
# print(result)

# Q131. Find the average Age of students in each Education level.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Education")["Age"].mean()
# print(result)

# Q132. Find sum, mean, and max of Course_Fees for each Course_Name in one output.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Course_Fees"].agg(["sum", "mean", "max"])
# print(result)

# Q133. Apply different functions: sum of Fees_Paid and mean of Theory_Marks per Course.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name").agg(
#     Fees_Paid_Total = ("Fees_Paid", "sum"),
#     Theory_Marks_Average = ("Theory_Marks", "mean")
# )
# print(result)

# Q134. Group by Course_Name and Learning_Mode together and count students.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby(["Course_Name", "Learning_Mode"])["Student_Name"].count()
# print(result)

# Q135. Find the top 5 cities by number of admissions.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("City").value_counts().head(5)
# print(result)

# Q136. Group by Course_Name, find average marks, and sort descending.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Theory_Marks"].mean().sort_values(ascending=False)
# print(result)

# Q137. Add a column showing the average marks of each Course next to every student.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")

# df["Course_Average_Marks"] = (
#     df.groupby("Course_Name")["Theory_Marks"]
#       .transform("mean")
# )
# print(df[["Student_Name", "Course_Name", "Theory_Marks", "Course_Average_Marks"]])

# Q138. Count unique companies where students got placed, per Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result= df.groupby("Course_Name")["Company_Name"].nunique()
# print(result)

# Section 13: Pivot Table & Crosstab

# Q139. Create a pivot table showing average Theory_Marks by Course_Name.
# Answer: pivot_table()
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.pivot_table(
#     index="Course_Name",
#     values="Theory_Marks",
#     aggfunc="mean"
# )
# print(result)

# Q140. Create a pivot table with Course_Name as rows, Learning_Mode as columns, and total fees as values.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.pivot_table(
#     index="Course_Name",
#     columns="Learning_Mode",
#     values="Course_Fees",
#     aggfunc="sum"
# )
# print(result)

# Q141. Create a pivot table showing average Attendance_Percent by Batch_Time.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.pivot_table(
#     index="Batch_Time",
#     values="Attendance_Percent",
#     aggfunc="mean"
# )
# print(result)

# Q142. Create a pivot table with sum and mean of Course_Fees by Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# result = df.pivot_table(
#     index="Course_Name",
#     values="Course_Fees",
#     aggfunc=["sum", "mean"]
# )
# print(result)

# Q143. Add row and column totals to a pivot table of fees by Course and City.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# result = df.pivot_table(
#     index="City",
#     values="Course_Fees",
#     aggfunc="sum",
#     margins=True
# )
# print(result)

# Q144. Create a pivot table with Course_Name and Batch_Time as multiple row indexes.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.pivot_table(
#     index=["Course_Name", "Batch_Time"],
#     values="Course_Fees",
#     aggfunc="sum"
# )
# print(result)

# Q145. Create a pivot table with Theory_Marks and Practical_Marks as multiple values.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.pivot_table(
#        index="Course_Name",
#        values=["Theory_Marks", "Practical_Marks"],
#        aggfunc="sum"
# )
# print(result)

# Q146. Count students for each combination of Course_Name and Placement_Status.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = pd.crosstab(
#     df["Course_Name"],
#     df["Placement_Status"]
# )
# print(result)

# Q147. Create a crosstab of Learning_Mode vs Course_Status.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = pd.crosstab(
#     df["Learning_Mode"],
#     df["Course_Status"]
# )
# print(result)

# Q148. Fill missing combinations in a pivot table with 0.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.pivot_table(
#     index="Course_Name",
#     values="Theory_Marks",
#     aggfunc="sum",
#     fill_value=0
# )
# print(result)

# Section 14: Merge & Join

# Q149. Merge the students DataFrame with an exam results DataFrame using Student_ID.
# Answer: merge()
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# students = df[["Student_ID", "Student_Name", "Course_Name"]]
# exam_results = df[["Student_ID", "Theory_Marks", "Practical_Marks"]]
# result = pd.merge(
#     students,
#     exam_results,
#     on="Student_ID"
# )
# print(result)

# Q150. Merge two DataFrames keeping only matching Student_ID rows.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# students = df[["Student_ID", "Student_Name", "Course_Name"]]
# exam_results = df[["Student_ID", "Theory_Marks", "Practical_Marks"]]
# result = pd.merge(
#     students,
#     exam_results,
#     on="Student_ID",
#     how="inner"
# )
# print(result)

# Q151. Merge keeping all rows from the students (left) DataFrame.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# students = df[["Student_ID", "Student_Name", "Course_Name"]]
# exam_results = df[["Student_ID", "Theory_Marks", "Practical_Marks"]]
# result = pd.merge(
#     students,
#     exam_results,
#     on="Student_ID",
#     how="left"
# )
# print(result)

# Q152. Merge keeping all rows from the right DataFrame.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# students = df[["Student_ID", "Student_Name", "Course_Name"]]
# exam_results = df[["Student_ID", "Theory_Marks", "Practical_Marks"]]
# result = pd.merge(
#     students,
#     exam_results,
#     on="Student_ID",
#     how="right"
# )
# print(result)

# Q153. Merge keeping all rows from both DataFrames.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# students = df[["Student_ID", "Student_Name", "Course_Name"]]
# exam_results = df[["Student_ID", "Theory_Marks", "Practical_Marks"]]
# result = pd.merge(
#     students,
#     exam_results,
#     on="Student_ID",
#     how="outer"
# )
# print(result)

# Q154. Combine 2023 batch and 2024 batch DataFrames one below the other.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# batch_2023 = df[df["Batch_Time"] == 2023]
# batch_2024 = df[df["Batch_Time"] == 2024]
# result = pd.concat(
#     [batch_2023, batch_2024],
#     axis=0
# )
# print(result)

# Q155. Combine two DataFrames side by side (column-wise).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# batch_2023 = df[df["Batch_Time"] == 2023]
# batch_2024 = df[df["Batch_Time"] == 2024]
# result = pd.concat(
#     [batch_2023, batch_2024],
#     axis=1
# )
# print(result)

# Q156. Merge two DataFrames where key names differ (Student_ID vs Stu_ID).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# students = df[["Student_ID", "Student_Name", "Course_Name"]]
# results = df[["Student_ID", "Theory_Marks", "Practical_Marks"]].rename(
#     columns={"Student_ID": "Stu_ID"}
# )
# result = pd.merge(
#     students,
#     results,
#     left_on="Student_ID",
#     right_on="Stu_ID",
#     how="inner"
# )
# print(result)


# Section 15: Advanced Operations
# Q157. Convert the wide dataset into long format with Student_ID as identifier and the three marks columns as values.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.melt(
#     id_vars=["Student_ID"],
#     value_vars=["Theory_Marks", "Practical_Marks", "Project_Marks"],
#     var_name="Metric",
#     value_name="value"
# )
# print(result)

# Q158. Convert a column containing lists of modules into separate rows.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Module"] = df["Module"].str.split(",")
# result = df.explode("Module")
# print(result)

# Q159. Convert columns of a summary table into row index.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.stack()
# print(result)

# Q160. Convert row index back into columns.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.unstack()
# print(result)

# Q161. Interchange rows and columns of a summary table.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.transpose()
# print(result)

# Q162. Limit all Attendance_Percent values to a maximum of 100.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Attendance_Percent"] = df["Attendance_Percent"].clip(
#     lower=0,
#     upper=100
# )
# print(df["Attendance_Percent"])

# Q163. Limit Theory_Marks to a minimum of 0 (no negatives).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Theory_Marks"] = df["Theory_Marks"].clip(
#     lower=0)
# print(df["Theory_Marks"])

# Q164. Create a MultiIndex using Course_Name and Batch_Time as index.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.set_index(["Course_Name", "Batch_Time"])
# print(result)

# Q165. Swap the levels of the MultiIndex (Batch_Time first, Course_Name second).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df = df.set_index(["Batch_Time", "Course_Name"])
# result = df.swaplevel("Batch_Time", "Course_Name")
# print(result)

# Q166. Reset the MultiIndex back to normal columns.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df = df.set_index(["Batch_Time", "Course_Name"])
# result = df.reset_index()
# print(result)

# Section 16: Window Functions
# Q167. Calculate the running total (cumulative sum) of Fees_Paid.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Running_total"] = df["Fees_Paid"].cumsum()
# print(df["Running_total"])

# Q168. Calculate the cumulative product of a small numeric column for 10 rows.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# result = df["Course_Fees"].head(10).cumprod()
# print(result)

# Q169. Calculate the cumulative maximum of Theory_Marks.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Marks"] = df["Theory_Marks"].cummax()
# print(df["Marks"])

# Q170. Calculate the cumulative minimum of Attendance_Percent.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Attendance_Percent"] = df["Attendance_Percent"].cummin()
# print(df["Attendance_Percent"])

# Q171. Calculate the 7-day rolling average of daily admissions count.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# daily_admissions = (
#     df.groupby("Admission_Date")
#       .size()
#       .sort_index()
# )

# rolling_avg = daily_admissions.rolling(7).mean()

# print(rolling_avg)

# Q172. Calculate the 30-day rolling maximum of daily fees collection.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Fees_Paid"] = pd.to_numeric(
#     df["Fees_Paid"],
#     errors="coerce"
# )
# rolling_max = df["Fees_Paid"].rolling(30).max()
# print(df["Fees_Paid"])

# Q173. Calculate the 30-day rolling minimum of daily fees collection.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Fees_Paid"] = pd.to_numeric(
#     df["Fees_Paid"],
#     errors="coerce"
# )
# rolling_max = df["Fees_Paid"].rolling(30).min()
# print(df["Fees_Paid"])

# Q174. Calculate the rolling sum of Fees_Paid with window size 10.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Fees_Paid"] = pd.to_numeric(
#     df["Fees_Paid"],
#     errors="coerce"
# )
# rolling_max = df["Fees_Paid"].rolling(10).sum()
# print(df["Fees_Paid"])

# Q175. Calculate the expanding average of Theory_Marks.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Theory_Marks"] = pd.to_numeric(
#     df["Theory_Marks"],
#     errors="coerce"
# )
# rolling_max = df["Theory_Marks"].expanding().mean()
# print(df["Theory_Marks"])

# Q176. Calculate the expanding sum of Fees_Paid.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Fees_Paid"] = pd.to_numeric(
#     df["Fees_Paid"],
#     errors="coerce"
# )
# rolling_max = df["Fees_Paid"].expanding().sum()
# print(df["Fees_Paid"])

# Section 17: Ranking & Statistical Analysis

# Q177. Rank all students by Total_Marks (highest = rank 1).
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Total_Marks"] = df["Theory_Marks"] + df["Practical_Marks"] + df["Project_Marks"]

# df["Rank"] = df["Total_Marks"].rank(
#     ascending=False,
#     method="min"
# )

# print(df[["Student_Name", "Total_Marks", "Rank"]])

# Q178. Rank students by Theory_Marks within each Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Theory_Marks"].rank(ascending=False)
# print(result)

# Q179. Calculate the percentage change in monthly admissions.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# monthly_admissions = (
#     df.groupby(df["Admission_Date"].dt.to_period("M"))
#       .size()
# )
# result = monthly_admissions.pct_change() * 100
# print(result)

# Q180. Calculate the month-over-month difference in fees collection.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# monthly_fees = (
#     df.groupby(df["Admission_Date"].dt.to_period("M"))["Course_Fees"].sum()
# )
# result = monthly_fees.diff()
# print(result)

# Q181. Shift the Fees_Paid column one row down.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Fees_Paid"] = df["Fees_Paid"].shift()
# print(df[["Student_Name", "Fees_Paid", "Fees_Paid"]])

# Q182. Create a column showing the previous student's marks next to the current one.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Previous_Student_Marks"] = df["Theory_Marks"].shift(1)
# print(df[["Student_Name", "Theory_Marks", "Previous_Student_Marks"]])

# Q183. Find the correlation between Attendance_Percent and Theory_Marks.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Attendance_Percent"].corr(df["Theory_Marks"])
# print(result)

# Q184. Find the covariance between Age and Course_Fees.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# result = df["Age"].cov(df["Course_Fees"])
# print(result)

# Q185. Find the correlation matrix of all numeric columns.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.corr(numeric_only=True)
# print(result)

# Q186. Find the standard deviation of Theory_Marks for each Course_Name.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df.groupby("Course_Name")["Theory_Marks"].std()
# print(result)

# Section 18: Resampling & Categorical Data

# Q187. Convert Admission_Date to datetime and set it as the index.
# Answer: pd.to_datetime() + set_index()
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# result = df.set_index("Admission_Date")
# print(result)


# Q188. Calculate the total fees collected for each month.
# Answer: resample('M').sum()
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# result = (df.groupby(df["Admission_Date"].dt.to_period("M"))["Course_Fees"].sum())
# print(result)

# Q189. Calculate the number of admissions for each week.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# result = (
#     df.groupby(df["Admission_Date"].dt.to_period("W"))
#       .size()
# )
# print(result)

# Q190. Calculate quarterly total fees collection.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# df = df.set_index("Admission_Date")
# result = df["Fees_Paid"].resample("QE").sum()
# print(result)

# Q191. Calculate yearly total admissions.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Admission_Date"] = pd.to_datetime(
#     df["Admission_Date"],
#     format="mixed",
#     errors="coerce"
# )
# df = df.set_index("Admission_Date")
# result = df.resample("Y").count()
# print(result)

# Q192. Convert Grade to category type and display its categories.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Grade"] = df["Grade"].astype("category")
# print(df["Grade"].cat.categories)

# Q193. Divide Theory_Marks into 3 bins labeled Fail, Average, Topper.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Theory_Group"] = pd.cut(
#     df["Theory_Marks"],
#     bins=[0, 50, 75, 90],
#     labels=["Fail", "Average", "Topper"]
# )
# print(df[["Theory_Marks", "Theory_Group"]])

# Q194. Divide Course_Fees into 4 bins with an equal number of students.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Course_Fees"] = pd.to_numeric(
#     df["Course_Fees"],
#     errors="coerce"
# )
# df["Course_Group"] = pd.qcut(
#     df["Course_Fees"],
#     q=4,
#     labels=["Q1", "Q2", "Q3", "Q4"]
# )
# print(df[["Course_Fees", "Course_Group"]])

# Section 19: Data Validation & Exporting

# Q195. Check that no Attendance_Percent value is negative or above 100 after cleaning.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df["Attendance_Percent"] = pd.to_numeric(
#     df["Attendance_Percent"],
#     errors="coerce"
# )
# result = df["Attendance_Percent"].between(0, 100)
# print(result)

# Q196. Verify that all Theory_Marks values are between 0 and 100.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df["Theory_Marks"].between(0, 100).all()
# print(result)

# Q197. Export the cleaned dataset to a CSV file without the index.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df.to_csv(r"D:\Student_Course_Records.csv",index=False)

# Q198. Export the dataset to an Excel file.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# df.to_excel(r"D:\Student_Course_Records.csv",index=False)

# Q199. Export only Student_ID, Student_Name, and Total_Marks to CSV.
# df = pd.read_csv(r"D:\Student_Course_Records.csv")
# result = df[["Student_ID", "Student_Name", "Total_Marks"]]
# result.to_csv(
#     r"D:\Student_Summary.csv",
#     index=False
# )

# Q200. Export only Placed students to a separate Excel file.
# Answer: Boolean indexing + to_excel()
df = pd.read_csv(r"D:\Student_Course_Records.csv")
placed_students = df[df["Placement_Status"] == "Placed"]
placed_students.to_excel(
    r"D:\Placed_Students.xlsx",
    index=False
)