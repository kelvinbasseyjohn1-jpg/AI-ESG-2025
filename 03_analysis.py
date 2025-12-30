import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('data/cleaned/esg_ai_cleaned.csv')

X = df[['ai_index','firm_size']]
X = sm.add_constant(X)
y = df['environmental_score']

model = sm.OLS(y,X).fit()
print(model.summary())
