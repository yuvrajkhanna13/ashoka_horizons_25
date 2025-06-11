import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



starbucks = pd.read_csv("starbucks.csv")
netflix = pd.read_csv("netflix_titles.csv")
pima = pd.read_csv("pima_diabetes.csv")



sns.histplot(starbucks["Calories"], bins=20).set(title="Starbucks Calories")
plt.savefig("starbucks_hist.png")
plt.clf()

sns.boxplot(x=starbucks["Calories"]).set(title="Starbucks Calories Boxplot")
plt.savefig("starbucks_boxplot.png")
plt.clf()


sns.countplot(x="type", data=netflix).set(title="Netflix Content Types")
plt.savefig("netflix_count_type.png")
plt.clf()


sns.histplot(pima["Age"], kde=True).set(title="PIMA Age Distribution")
plt.savefig("pima_age_kde.png")
plt.clf()


sns.scatterplot(x="Calories", y="Sugar (g)", data=starbucks).set(title="Calories vs Sugar")
plt.savefig("starbucks_scatter_sugar.png")
plt.clf()

sns.boxplot(x="Outcome", y="Glucose", data=pima).set(title="Glucose by Outcome")
plt.savefig("pima_glucose_outcome.png")
plt.clf()


netflix["release_year"] = pd.to_numeric(netflix["release_year"], errors="coerce")
netflix["release_year"].dropna().value_counts().sort_index().plot()
plt.title("Netflix Releases by Year")
plt.savefig("netflix_years.png")
plt.clf()


sns.scatterplot(x="BMI", y="Age", data=pima, hue="Outcome", size="Pregnancies", sizes=(20, 100)).set(title="BMI vs Age by Outcome")
plt.savefig("pima_multivariate.png")
plt.clf()

sns.heatmap(pima[["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]].corr(), annot=True, cmap="coolwarm")
plt.title("PIMA Correlation Heatmap")
plt.savefig("pima_heatmap.png")
plt.clf()
