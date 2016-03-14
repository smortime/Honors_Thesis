#Schuyler Mortimer Honors Thesis
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('/home/schuyler/Desktop/Honors_Thesis/data_sets/data_frame.csv')

df = data[np.isfinite(data['difference'])]


results = smf.ols(formula='difference ~ Normalized_Count', data=df).fit()

print results.summary()
print results.params

graph = df.plot(kind='scatter', x='Normalized_Count', y='difference')
#graph2 = df.plot(kind='scatter', x='norm_followers', y='difference')
plt.show()
