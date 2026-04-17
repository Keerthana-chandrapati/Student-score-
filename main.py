# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 2: Load dataset
data = pd.read_csv("data.csv")

print("Dataset:")
print(data)

# Step 3: Select input (X) and output (y)
X = data[['hours_studied', 'previous_scores', 'sleep_hours']]
y = data['final_score']

# Step 4: Split data into training & testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 5: Create model
model = LinearRegression()

# Step 6: Train model
model.fit(X_train, y_train)

# Step 7: Predict
predictions = model.predict(X_test)

print("\nPredictions:", predictions)

# Step 8: Check error
error = mean_absolute_error(y_test, predictions)
print("\nModel Error:", error)

# Step 9: Test with your own input
print("\nTest your own data:")
hours = float(input("Enter hours studied: "))
prev = float(input("Enter previous score: "))
sleep = float(input("Enter sleep hours: "))

result = model.predict([[hours, prev, sleep]])
print("Predicted Final Score:", result[0])
