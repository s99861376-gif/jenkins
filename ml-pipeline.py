import pickle
import numpy as np
import sys
from sklearn.linear_model import LinearRegression

print("=== ML CI Pipeline ===")
X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression()
model.fit(X, y)
print("Model trained successfully.")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved to model.pkl.")
prediction = model.predict([[4]])[0]
print(f"Prediction: {prediction:.1f}(Expected: 8.0)")
if abs(prediction - 8.0) < 0.1:
    print("Test passed.")
    sys.exit(0)
else:
    print("Test failed.")
    sys.exit(1)