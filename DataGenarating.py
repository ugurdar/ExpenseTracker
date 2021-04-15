import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random 

random.seed(26)
# Generating random variable from UNIF(50,100) size = 10
Travel = np.random.uniform(50,100,10)
# Generating random variable from UNIF(1,150) size = 200
Food = np.random.uniform(1,150,200)
# Generating random variable from UNIF(100,500) size = 10
Entertainment = np.random.uniform(100,500,10)
# Generating random variable from UNIF(20,100) size = 10
SelfImp = np.random.uniform(20,100,10)
# Generating random variable from UNIF(10,300) size = 5
PerCare = np.random.uniform(10,300,5)
# Generating random variable from UNIF(300,1200) size = 5
RentBills = np.random.uniform(300,1200,5)

# Sector names
Sector = ["Travel","Food","Entertainment","SelfImp","PerCare","RentBills"]

# Synthetic inflation rates by months
Sektorur = {'Travel': [1,1.1,1.3,1.5,1.7,1.9] ,
           'Food': [1,1.9,2.5,2.9,3.2,3.80],
           'Entertainment' : [1,1.11,1.3,1.4,1.8,1.9],
           'SelfImp' : [2,2.4,2.1,2.9,2.1,2.2],
           'PerCare': [1,1,1.45,1.75,2.3,2.8],
           'RentBills': [1,1.6,1.3,1.5,1.89,2]}

liste0,liste1,liste2,liste3,liste4,liste5 = [],[],[],[],[],[]

# j represent names of Sector
for j in range(6):
    for i in range(6):
        globals()['liste'+str(j)].append(Sektorur[Sector[j]][i] * globals()[Sector[j]])
    
    # Burası aylar için
    for i in range(6):
        globals()['df'+str(i)]= pd.DataFrame(globals()['liste'+str(j)][i])
        globals()['df'+str(i)] ['Month'] = i+1
        globals()['df'+str(i)] ['Sector'] = Sector[j]
    # df0,df1,...,df5 are data.frame for each month
    globals()['df_'+Sector[j]] = pd.concat([df0,df1,df2,df3,df4,df5], axis=0)

    
# df_Travel,...,df_RentBills are data.frame for each Sector and df is their combined form.
df = pd.concat([df_Travel,df_Food,df_Entertainment,df_SelfImp,df_PerCare,df_RentBills], axis=0)
# to arrange idexes
data = df.reset_index(drop=True)
data.columns = ['Expenses','Month','Sector']
#data.head(15)
data.to_csv('data2020.csv',index=False)

