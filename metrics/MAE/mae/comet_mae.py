import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, median_absolute_error
import numpy as np


# Load the COMET CFP details from the Excel file
file_path = 'MAE_COMET.xlsx'
df = pd.read_excel(file_path)

# Extract y_true and y_pred columns
y_true = df['y_true']
y_pred = df['y_pred']

# Compute COMET metrics
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_true, y_pred)
mdae = median_absolute_error(y_true, y_pred)

# print the results
print("COMET RESULTS")
print("-------------------------------------")
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'R-squared (R²): {r2}')
print(f'Median Absolute Error (MdAE): {mdae}')


# Load the DEEP-COSMIC-UC CFP details from the Excel file
file_path = 'MAE_DEEP-COSMIC-UC.xlsx'
df = pd.read_excel(file_path)

# Extract y_true and y_pred columns
y_true = df['y_true']
y_pred = df['y_pred']

# Compute DEEP-COSMIC-UC metrics
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_true, y_pred)
mdae = median_absolute_error(y_true, y_pred)

# print the results
print("DEEP-COSMIC-UC RESULTS")
print("-------------------------------------")
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'R-squared (R²): {r2}')
print(f'Median Absolute Error (MdAE): {mdae}')