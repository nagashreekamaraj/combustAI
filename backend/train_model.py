import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import os

print("Loading dataset...")

data = pd.read_csv("dataset.csv")

print("Dataset loaded successfully")
print(data.head())

# Create combustion label based on CO emission
data["Combustion"] = data["CO"].apply(lambda x: 0 if x > 0.7 else 1)

# Features
X = data[['AT','AP','AH','AFDP','GTEP','TIT','TAT','TEY','CDP','CO','NOX']]
y = data['Combustion']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(11,)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=30, batch_size=32)

loss, accuracy = model.evaluate(X_test, y_test)

print("Model Accuracy:", accuracy)

# Save model
model_path = os.path.join(os.getcwd(), "combustion_model.keras")
model.save(model_path)

print("Model saved successfully at:", model_path)