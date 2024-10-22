import pandas as pd
from ucimlrepo import fetch_ucirepo

# Fetch dataset
hepatitis = fetch_ucirepo(id=46)

# Data (as pandas dataframes)
X = hepatitis.data.features
y = hepatitis.data.targets

# metadata 
print(hepatitis.metadata) 
  
# variable information 
print(hepatitis.variables)

# Combine features and targets into a single DataFrame
df = pd.concat([X, y], axis=1)

# Save DataFrame to a CSV file
df.to_csv("hepatitis_data.csv", index=False)
