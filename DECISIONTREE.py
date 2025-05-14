import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("sensor_log_synthetic_500.csv")

# Convert labels to numbers
df['Condition'] = df['Condition'].map({'Safe': 0, 'Unsafe': 1})

# Split features and target
X = df.drop('Condition', axis=1)
y = df['Condition']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Test Accuracy:", accuracy)

# Plot the tree
plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns, class_names=["Safe", "Unsafe"], filled=True)
plt.show()
