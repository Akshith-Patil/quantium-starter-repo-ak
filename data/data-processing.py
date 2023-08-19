import pandas as pd

# Read the CSV files
data_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
dfs = [pd.read_csv(file) for file in data_files]

# Combine the DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Filter rows with 'product' equal to 'pink morsel'
pink_morsel_df = combined_df[combined_df['product'] == 'pink morsel']

# Convert 'price' to a numeric value without the dollar sign
pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').astype(float)

# Calculate 'sales' by multiplying 'quantity' and 'price'
pink_morsel_df['sales'] = pink_morsel_df['quantity'] * pink_morsel_df['price']

# Select and reorder columns
final_df = pink_morsel_df[['sales', 'date', 'region']]

# Save the final DataFrame to a new CSV file
final_df.to_csv('formatted_output.csv', index=False)

print("Formatted output saved to 'formatted_output.csv'")
