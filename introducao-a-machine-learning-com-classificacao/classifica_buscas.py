# using panda data analysis - sudo pip install pandas --upgrade
import pandas as pd
# data frame
df = pd.read_csv('busca.csv')

X = df[['home', 'busca', 'logado']]
Y = df['comprou']

Xdummies = pd.get_dummies(X);
Ydummies = Y;

print(Xdummies)
print(Ydummies)