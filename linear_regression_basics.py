import numpy as np
from sklearn.linear_model import LinearRegression

# Данные
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Модель
model = LinearRegression()
model.fit(X, y)

# Предсказание
prediction = model.predict([[6]])
print(f"Предсказание для числа 6: {prediction[0]}")
