import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random 

# Import Database
data = pd.read_csv('data2020.csv')
maxmonth = data['Month'].max()

# Inflation Rate - Deniz
def infrate(cpi1,cpi):
    return (cpi1- cpi )/cpi

Sector = ["Travel","Food","Entertainment","SelfImp","PerCare","RentBills"]


for j in Sector:
    globals()['inf_'+str(j)] = [0]*(maxmonth-1)
    a = globals()['inf_'+str(j)] 
    for i in range(0,maxmonth):
        if i == maxmonth-1:
            break
        cpi1 =  data.loc[(data['Sector'] == j) & (data['Month'] == i+2)]['Expenses'].mean()
        cpi =  data.loc[(data['Sector'] == j) & (data['Month'] == i+1)]['Expenses'].mean()
        a[i] = infrate(cpi1,cpi)
        globals()['inf_'+str(j)] = a

list_inf = {
        'Month' : np.arange(2,maxmonth+1),
        'Travel' : inf_Travel,
        'Food' : inf_Food,
        'Entertainment' : inf_Entertainment,
        'SelfImp' : inf_SelfImp,
        'PerCare' : inf_PerCare,
        'RentBills' : inf_RentBills
        }
inf_df = pd.DataFrame(list_inf)

while True:
    print("""
# Main Menu
------------------------------------------
(0) Show the Data                             
(1) Inflation Rate by Monthly and Sectoral
(2) Expenses Statistics 
(3) Expenses Graphs
(4) New Data Entry
(q) Quit
""")


    islem = input("Please select operation: ")
    if islem == '0':
        print(data)
    if islem == "q":
        print("Have a nice day.")
        break
    elif islem == "1":
        print(""" # Inflation Rate by Monthly and Sectoral Menu
                  ----------------------------------------------""")
        print(inf_df)

    elif islem == "2":

        while True:
            print("""
          # Expenses Statistics Menu
          (1) Monthly Statistics
          (2) Sectoral Statistics
          (3) Monthly and Sectoral Statistics
          (q) Back to Main Menu
          """)
            islem3= input("Please select operation: ")

            if islem3 == "q":
                print('Switching to the Main Menu...')
                break
              
            if islem3 == "1":
                islem4 = input("If you want to view statistics for a specific month, enter the month number, enter ""All"" for all months.")
                if islem4 == 'All':
                    print(data.groupby(['Month']).describe()['Expenses'])
                else:
                    islem4 = int(islem4)
                    print(data.loc[data['Month'] == islem4,['Expenses']].describe()) 
            elif islem3 == "2":
                print("""
                  Sector         Input
                  --------------------
                  Travel          :1
                  Food            :2  
                  Entertainment   :3
                  SelfImp         :4
                  PerCare         :5
                  RentBills       :6
                  All             :All
                  """)
                islem4 = input("Please select operation: ")
                if islem4 == "All":
                      print(data.groupby(['Sector']).describe()['Expenses'])
                else:
                    islem4 = int(islem4)
                    print(data.loc[data['Sector'] == Sector[islem4-1],['Expenses']].describe()) 
               
                  
            elif islem3 == "3":
                print("""
                  Sector         Input
                  --------------------
                  Travel          :1
                  Food            :2  
                  Entertainment   :3
                  SelfImp         :4
                  PerCare         :5
                  RentBills       :6
                  All             :All
                  """)
                islem4 = input("Select Sector :")
                islem5 = input("If you want to view statistics for a specific month, enter the month number, enter ""All"" for all months.")
                if(islem4 != "All") & (islem5 != "All"):
                    print(data.loc[(data['Sector'] == Sector[int(islem4)-1]) & (data['Month'] ==int(islem5)),['Expenses']].describe())
                elif(islem4 == "All") & (islem5 != "All"):
                    print(data.loc[(data["Month"] == int(islem5)) & (data["Sector"]),'Expenses'].describe())
                elif(islem5 == "All") & (islem4 != "All"):
                    print(data.loc[(data["Month"] ) & (data['Sector'] == Sector[int(islem4)-1]),'Expenses'].describe())
                else:
                    print(data.groupby(['Month','Sector']).describe()['Expenses'])
                
    elif islem == "3":
        while True:
            print("""
            # Expenses Graphs Menu
            -------------------------------------------
            (1) Line Graph Based on Months and Secotrs
            (2) Box-Plot based on Months
            (3) Box-Plot based on Sectors
            (4) Bar Chart based on Months and Sectors
            (5) Bar Chart based on Months
            (6) Bar Chart based on Sectors
            (q) Back to Main Menu
            """)
            islem1 = input("Please select operation :")
            if islem1 == "q":
                print('Switching to the Main Menu...')
                break
            if islem1 == "1":
                fig, ax = plt.subplots(figsize=(10,7)) # Graph size 
                data.groupby(['Month','Sector']).mean()['Expenses'].unstack().plot(ax=ax)
                ax.set_xlabel('Months')
                ax.set_ylabel('Mean of Expenses')
                plt.show()
            elif islem1 == "2":
                fig, ax = plt.subplots(figsize=(10,7))
                data.boxplot(by ='Month', column =['Expenses'], grid = False,ax=ax)
                ax.set_ylabel('Expenses')
                ax.set_xlabel('Months')
                plt.show()
            elif islem1 == "3":
                fig, ax = plt.subplots(figsize=(10,7))
                data.boxplot(by ='Sector', column =['Expenses'], grid = False,ax=ax)
                ax.set_ylabel('Expenses')
                ax.set_xlabel('Sectors')
                plt.show()
            elif islem1 == "4": 
                fig, ax = plt.subplots(figsize=(10,7))
                data.groupby(['Month','Sector']).mean()['Expenses'].unstack().plot.bar(ax=ax)
                ax.set_ylabel('Expenses')
                ax.set_ylabel('Mean of Expenses')
                plt.show()
            elif islem1 == "5":
                df_grouped = data.groupby(['Month']).mean()['Expenses']
                fig, ax = plt.subplots(figsize=(10,7))
                df_grouped.plot(x="Month", y='Expenses', kind="bar",ax=ax,rot=0)
                ax.set_ylabel('Mean of Expenses')
                ax.set_xlabel('Months')
                plt.show()
                
            elif islem1 == "6":
                df_grouped = data.groupby(['Sector']).mean()['Expenses']
                fig, ax = plt.subplots(figsize=(10,7))
                df_grouped.plot(x="Sector", y='Expenses', kind="bar",ax=ax,rot=0)
                ax.set_ylabel('Mean of Expenses')
                ax.set_xlabel('Sectors')
                plt.show()
        
    elif islem == "4":
        while True:
            
            print("""
                  # New Data Entry Menu
                  ---------------------
                  Sector         Input
                  Travel          :1
                  Food            :2  
                  Entertainment   :3
                  SelfImp         :4
                  PerCare         :5
                  RentBills       :6
                  SaveData        :s
                  Quit            :q
                  """)
    
            sec = input('Sector : ')
            if sec == 's':
                print(data)
                confirm1 = input('If you confirm to save the data input 1, if not 0')
                if confirm1 == '1':
                    data.to_csv('data2020.csv',index=False)
                    print('Data saved succesfully.')
                    print('Switching to the Main Menu...')
                    break
                else:
                    print('Data is not saved.')
                    print('Switching to the Main Menu...')
                    break
            if sec == 'q':
                print('Switching to the Main Menu...')
                break
            expense = input('Input expense ')
            liste_input = {'Expenses' : [float(expense)],
                          'Month': [maxmonth+1],
                          'Sector':[Sector[int(sec)-1]]}
            print("Sector : %s and Expense : %d" % (Sector[int(sec)-1],float(expense)))
            confirm = input("If you confirm input 1, if not input 0 ")
            if confirm == '1':
                df_in = pd.DataFrame(liste_input)
                data = data.append(df_in)
                print('Data updated succesfully.')
