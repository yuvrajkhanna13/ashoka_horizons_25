import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix
from sklearn.cluster import KMeans

scores = [55, 92, 78, 60, 85, 78, 90, 66, 73, 88]
scores_np = np.array(scores)
print("Mean:", np.mean(scores_np))
print("Median:", np.median(scores_np))
print("Mode (manual):", max(set(scores), key=scores.count))
print("Range:", np.max(scores_np) - np.min(scores_np))
print("Variance:", np.var(scores_np))
print("Std Deviation:", np.std(scores_np))


X = np.array([1,2,3,4,5,6,7,8]).reshape(-1, 1)
Y = np.array([45,50,60,65,75,80,90,95])
model = LinearRegression().fit(X, Y)
pred = model.predict(X)
print("\n--- Linear Regression ---")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("MSE:", mean_squared_error(Y, pred))
print("R2 Score:", r2_score(Y, pred))
plt.scatter(X, Y)
plt.plot(X, pred, color='red')
plt.title("Experience vs Salary")
plt.savefig("linear_regression_plot.png")
plt.close()

X_prep = np.array([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]).reshape(-1, 1)
Y_pass = np.array([0,0,0,0,1,0,1,1,1,1])
log_model = LogisticRegression(solver='liblinear')
log_model.fit(X_prep, Y_pass)
Y_pred = log_model.predict(X_prep)
print("\n--- Logistic Regression ---")
print("Accuracy:", accuracy_score(Y_pass, Y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_pass, Y_pred))

X_cluster = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])
kmeans = KMeans(n_clusters=2, random_state=42, n_init='auto').fit(X_cluster)
print("\n--- KMeans ---")
print("Centroids:\n", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
plt.scatter(X_cluster[:, 0], X_cluster[:, 1], c=kmeans.labels_, cmap='coolwarm')
plt.scatter(*kmeans.cluster_centers_.T, color='black', marker='x', s=100)
plt.title("KMeans Clustering")
plt.savefig("kmeans_plot.png")
plt.close()
