
# Capstone Two: Data Wrangling Notebook
## Dataset: OWID CO2 and Greenhouse Gas Emissions

---

### 1. Data Collection

```python
import pandas as pd

# Load the dataset
df = pd.read_csv("owid-co2-data.csv")

# Preview the data
df.head()
```

---

### 2. Data Organization

```python
# Checking shape and column names
print("Shape of dataset:", df.shape)
print("Column names:")
print(df.columns.tolist())
```

---

### 3. Data Definition

```python
# Summary of dataset
df.info()

# Statistical summary
df.describe(include='all')

# Checking unique values per column
df.nunique().sort_values(ascending=False)
```

---

### 4. Data Cleaning

```python
# Check for missing values
missing_values = df.isnull().sum()
missing_percent = (missing_values / len(df)) * 100
missing_df = pd.DataFrame({'Missing Values': missing_values, 'Percent (%)': missing_percent})
missing_df = missing_df[missing_df['Missing Values'] > 0].sort_values(by='Percent (%)', ascending=False)
print(missing_df)

# Drop columns with >80% missing values
sparse_cols = missing_df[missing_df['Percent (%)'] > 80].index.tolist()
df_cleaned = df.drop(columns=sparse_cols)

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Remove non-country/aggregate rows
aggregates = ['World', 'Asia', 'Africa', 'Europe', 'European Union', 
              'High-income countries', 'Low-income countries', 
              'Middle East', 'North America', 'Oceania', 'South America']
df_cleaned = df_cleaned[~df_cleaned['country'].isin(aggregates)]

# Keep only rows from 1990 onwards
df_cleaned = df_cleaned[df_cleaned['year'] >= 1990]

# Drop countries with fewer than 20 years of CO2 data
valid_countries = df_cleaned.groupby('country')['co2'].count()
valid_countries = valid_countries[valid_countries >= 20].index
df_cleaned = df_cleaned[df_cleaned['country'].isin(valid_countries)]

# Sort and forward fill missing values per country
df_cleaned = df_cleaned.sort_values(['country', 'year'])
df_cleaned = df_cleaned.groupby('country').ffill()

# Create derived features
df_cleaned['co2_per_gdp'] = df_cleaned['co2'] / df_cleaned['gdp']
df_cleaned['co2_change'] = df_cleaned.groupby('country')['co2'].pct_change()

# Final cleaning checks
df_cleaned = df_cleaned.drop_duplicates(subset=['country', 'year'])
df_cleaned['year'] = df_cleaned['year'].astype(int)

# Preview cleaned dataset
df_cleaned.info()
df_cleaned.head()
```

---

### Notes

- This notebook reflects the wrangling steps specific to the CO2 emissions forecasting and correlation analysis project.
- It prepares the data for modeling, clustering, and policy-relevant visual analysis.
