import pandas as pd

grade_map = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0
}

data = pd.read_csv("setting.csv")
data = data.sort_values(by=["Result"], ascending=True)
data = data.drop_duplicates(subset=["CourseName"], keep="first")
data = data.sort_values(by=["CourseName"], ascending=True)

data["GradeValue"] = data["Result"].map(grade_map)
data["WeightedGradePoints"] = data["GradeValue"] * data["AKTS"]

TA = data["AKTS"].sum()
WGP = data["WeightedGradePoints"].sum()
GPA = WGP / TA

print(data)
print("Weighted Grade Points", WGP)
print("Total AKTS", TA)
print("GPA: %.2f"%GPA)
