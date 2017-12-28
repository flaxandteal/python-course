# Acknowledgment
# The associated dataset nimdm-2010.csv is used under
# UK-OGL from NISRA
# https://www.opendatani.gov.uk/dataset/https-www-nisra-gov-uk-statistics-deprivation/resource/a9837273-0d5e-46e0-bf9c-55742659a553
import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import statsmodels.api as sm
from patsy import dmatrices

# City, HealthIndex, Population, InfectionRate, SurvivalRate
df = pandas.read_csv('nimdm-2010.csv')

y, X = dmatrices('Education ~ Employment + Crime', data=df)
model = sm.OLS(y, X)
fitted_results = model.fit()

df.plot(kind='scatter', x='Crime', y='Employment', s=(df['Education'] + 1) * 0.1)
plt.show()

print(fitted_results.summary())  # Lots of detailed statistical output
