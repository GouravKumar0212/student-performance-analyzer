import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sample.csv")

data["Average"] = (data["Math"] + data["Science"] + data["English"]) / 3
grades = []
for avg in data["Average"]:
    if avg >= 90:
        grades.append("A+")

    elif avg >= 75:
        grades.append("A")

    elif avg >= 60:
        grades.append("B")

    elif avg >= 40:
        grades.append("C")

    else:
        grades.append("Fail")

data["Grade"] = grades
topper = data.loc[data["Average"].idxmax()]

math_topper = data.loc[data["Math"].idxmax()]
science_topper = data.loc[data["Science"].idxmax()]
english_topper = data.loc[data["English"].idxmax()]

print("\n========== STUDENT PERFORMANCE REPORT ==========\n")

print(data)

print("\n========== OVERALL TOPPER ==========\n")

print(f"Name : {topper['Name']}")
print(f"Average Marks : {topper['Average']:.2f}")

print("\n========== SUBJECT WISE TOPPERS ==========\n")

print(f"Math Topper : {math_topper['Name']} ({math_topper['Math']})")

print(f"Science Topper : {science_topper['Name']} ({science_topper['Science']})")

print(f"English Topper : {english_topper['Name']} ({english_topper['English']})")
print("\n========== RESULT STATUS ==========\n")

for index, row in data.iterrows():

    if row["Average"] >= 40:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"{row['Name']} --> {status}")

data.to_csv("final_report.csv", index=False)

print("\nFinal report saved as final_report.csv")

plt.figure(figsize=(8,5))

plt.bar(data["Name"], data["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")

plt.tight_layout()

# Save Bar Graph
plt.savefig("performance_graph.png")

plt.show()

print("\nBar graph saved as performance_graph.png")

grade_counts = data["Grade"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct='%1.1f%%'
)

plt.title("Grade Distribution")

# Save Pie Chart
plt.savefig("grade_pie_chart.png")

plt.show()

print("\nPie chart saved as grade_pie_chart.png")
