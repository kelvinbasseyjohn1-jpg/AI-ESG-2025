# AI Adoption and ESG-Related Management Practices in UK Firms
import pandas as pd

df = pd.read_excel('data/raw/ONS_MES_2023.xlsx')

# Example cleaning
df = df.dropna(subset=['ai_indicator_1'])
df.to_csv('data/cleaned/esg_ai_cleaned.csv', index=False)
