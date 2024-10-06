import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_saledata = pd.read_excel("ExcelData/SaleData.xlsx", "SaleData")
# print(pd_saledata)

# print(pd_saledata.aggregate(['min', 'max']).to_string())

dfregion = df_saledata.groupby(['Region'])['Sale_amt'].max()
print(dfregion.reset_index().sort_values(['Sale_amt'], ascending=True))

df1 = df_saledata.copy()
df1['OrderDate'] = pd.to_datetime(df1['OrderDate']).dt.strftime("%d/%m/%Y")
df1 = df1.rename(columns={'Sale_amt': 'Sale Amount', 'OrderDate': 'Order Date'})
df1.plot(x='Order Date', y='Sale Amount', kind='bar')
plt.xlabel('Order Date')
plt.ylabel('Sale Amount')
plt.show()

df1.to_parquet('Output1.parquet')