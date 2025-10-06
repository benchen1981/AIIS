import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Linear Regression App", layout="centered")
st.title("Interactive Linear Regression Demo")

# --- User inputs ---
st.sidebar.header("Configure your data")
a = st.sidebar.number_input("Slope (a)", value=2.0, step=0.1)
b = st.sidebar.number_input("Intercept (b)", value=1.0, step=0.1)
noise = st.sidebar.number_input("Noise", value=1.0, step=0.1)
n_points = st.sidebar.number_input("Number of points", value=50, step=1)

# --- Data Generation ---
x = np.linspace(0, 10, int(n_points))
y = a * x + b + np.random.normal(0, noise, size=int(n_points))
df = pd.DataFrame({"x": x, "y": y})

st.subheader("Generated Data")
st.write(df.head())

# --- Linear Regression ---
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))

st.subheader("Regression Results")
st.write(f"Fitted slope (a): {model.coef_[0]:.3f}")
st.write(f"Fitted intercept (b): {model.intercept_:.3f}")
st.write(f"R² score: {model.score(x.reshape(-1,1), y):.3f}")

# --- Plot ---
st.subheader("Data Visualization")
fig, ax_plot = plt.subplots()
ax_plot.scatter(x, y, color='blue', label="Data points")
ax_plot.plot(x, y_pred, color='red', label="Fitted line")
ax_plot.set_xlabel("x")
ax_plot.set_ylabel("y")
ax_plot.legend()
st.pyplot(fig)
