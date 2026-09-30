
import pandas as pd

df = pd.read_csv('marketing_campaign_data.csv')

df['CTR'] = df['Clicks'] / df['Impressions']
df['Conversion Rate'] = df['Conversions'] / df['Clicks']
df['ROI'] = (df['Revenue'] - df['Cost']) / df['Cost']

summary = df.groupby('Campaign')[['CTR','Conversion Rate','ROI']].mean()
print(summary)
