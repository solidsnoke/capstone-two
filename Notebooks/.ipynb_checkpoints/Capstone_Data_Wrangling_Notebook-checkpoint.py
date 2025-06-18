
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
# Checking for missing values
missing_values = df.isnull().sum()
missing_percent = (missing_values / len(df)) * 100
missing_df = pd.DataFrame({'Missing Values': missing_values, 'Percent (%)': missing_percent})
missing_df = missing_df[missing_df['Missing Values'] > 0].sort_values(by='Percent (%)', ascending=False)
print(missing_df)

# Handling missing values - drop rows/columns or fill where appropriate
# For example, we may choose to drop columns with over 90% missing
threshold = 0.9
cols_to_drop = missing_df[missing_df['Percent (%)'] > threshold * 100].index.tolist()
df_cleaned = df.drop(columns=cols_to_drop)

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Re-check dataset info
df_cleaned.info()
```

---

### Notes

- Further cleaning (like filtering countries or selecting specific years) will depend on project focus.
- Keep this notebook in your GitHub repo, and include markdown cells to explain each step.
