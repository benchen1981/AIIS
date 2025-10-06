# Linear Regression Streamlit App

## Project Overview
This project is an interactive **Linear Regression demo** built using Python and **Streamlit**. Users can generate synthetic data points with configurable slope, intercept, noise, and number of points. The app fits a linear regression model to the data and visualizes the results.

## Key Features
- Adjust slope (`a`) and intercept (`b`) of the line
- Control noise level and number of points
- Real-time interactive visualization
- Display regression parameters and R² score
- Fully deployable on **Replit** and ready for **GitHub** upload

## CRISP-DM Steps Followed
1. **Business Understanding** – Demonstrate linear regression interactively
2. **Data Understanding** – Generate synthetic dataset
3. **Data Preparation** – Create DataFrame, add noise
4. **Modeling** – Fit linear regression using scikit-learn
5. **Evaluation** – Show R² score and compare fitted vs actual data
6. **Deployment** – Deploy on Streamlit via Replit


Follow the CRISP-DM methodology:
Business Understanding
    Goal: Build a simple app that demonstrates linear regression y = ax + b with noise, letting users modify parameters.
Data Understanding
    Generate synthetic data based on user input:
        a (slope)
        b (intercept)
        noise (random variation)
        n_points (number of points)
Data Preparation
    Create a Pandas DataFrame for x and y.
    Add noise to simulate real-world data.
Modeling
    Use scikit-learn LinearRegression to fit the generated data.
Evaluation
    Show model parameters a and b.
    Display R² score and a chart of predicted vs actual points.
Deployment
    Deploy via Streamlit on Replit.
    Provide GitHub-ready structure.