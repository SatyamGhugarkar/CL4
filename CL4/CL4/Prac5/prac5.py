# Usingmapreduce to analyze the Titanic dataset, we will calculate the average age of deceased males
# Titanic Data Analysis using MapReduce

import pandas as pd
from collections import defaultdict

# Load Titanic Dataset
df = pd.read_csv("titanic.csv")

mapped = []

# ---------- Mapper Phase ----------
for _, row in df.iterrows():

    gender = row["Sex"]
    age = row["Age"]
    survived = row["Survived"]
    pclass = row["Pclass"]

    # Average age of deceased males
    if gender == "male" and survived == 0 and pd.notna(age):
        mapped.append(("male_age", age))

    # Female casualties in each class
    if gender == "female" and survived == 0:
        mapped.append((f"class_{pclass}", 1))


# ---------- Shuffle Phase ----------
grouped = defaultdict(list)

for key, value in mapped:
    grouped[key].append(value)


# ---------- Reduce Phase ----------

# Average age of deceased males
male_ages = grouped["male_age"]

average_age = sum(male_ages) / len(male_ages)

print("Average Age of Deceased Males =", round(average_age, 2))


# Female casualties in each class
print("\nFemale Casualties by Class:")

for key in sorted(grouped):

    if key.startswith("class_"):
        print(f"{key} =", sum(grouped[key]))