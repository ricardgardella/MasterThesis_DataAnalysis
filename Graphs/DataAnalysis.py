from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


#HORIZON ANALYSIS

data = pd.read_csv("PlotData/horizon.csv")
dataArima = data.loc[data['Algorithm'] == 'ARIMA']
dataRZ = data.loc[data['Algorithm'] == 'RZ']
dataNN = data.loc[data['Algorithm'] == 'NN']
#Horizon Congested
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot(data['Horizon'].unique(),dataArima['NRMSE'].loc[dataArima['Scenario'] == "Con"], 'c', label='ARIMA')
plt.plot(data['Horizon'].unique(),dataRZ['NRMSE'].loc[dataRZ['Scenario'] == "Con"], 'm', label='RZ')
plt.plot(data['Horizon'].unique(), dataNN['NRMSE'].loc[dataNN['Scenario'] == "Con"], 'y', label='NN')
plt.title('Prediction Horizon in the Congested Scenario')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()
#Horizon Normal
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot(data['Horizon'].unique(),dataArima['NRMSE'].loc[dataArima['Scenario'] == "Nor"], 'c', label='ARIMA')
plt.plot(data['Horizon'].unique(),dataRZ['NRMSE'].loc[dataRZ['Scenario'] == "Nor"], 'm', label='RZ')
plt.plot(data['Horizon'].unique(), dataNN['NRMSE'].loc[dataNN['Scenario'] == "Nor"], 'y', label='NN')
plt.title('Prediction Horizon in the Normal Scenario')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


#AGGREGATION ANALYSIS
data = pd.read_csv("PlotData/aggregation.csv")
dataArima = data.loc[data['Algorithm'] == 'ARIMA']
dataRZ = data.loc[data['Algorithm'] == 'RZ']
dataNN = data.loc[data['Algorithm'] == 'NN']
#aggregation congested
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot(data['aggregation'].unique(),dataArima['NRMSE'].loc[dataArima['Scenario'] == "Con"], 'c', label='ARIMA')
plt.plot(data['aggregation'].unique(),dataRZ['NRMSE'].loc[dataRZ['Scenario'] == "Con"], 'm', label='RZ')
plt.plot(data['aggregation'].unique(), dataNN['NRMSE'].loc[dataNN['Scenario'] == "Con"], 'y', label='NN')
plt.title('Aggregation in the Congested Scenario')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()
#aggregation normal
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot(data['aggregation'].unique(),dataArima['NRMSE'].loc[dataArima['Scenario'] == "Nor"], 'c', label='ARIMA')
plt.plot(data['aggregation'].unique(),dataRZ['NRMSE'].loc[dataRZ['Scenario'] == "Nor"], 'm', label='RZ')
plt.plot(data['aggregation'].unique(), dataNN['NRMSE'].loc[dataNN['Scenario'] == "Nor"], 'y', label='NN')
plt.title('Aggregation in the Normal Scenario')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()

#AMOUNT OF DATA ANALYSIS
data = pd.read_csv("PlotData/amount.csv")
dataArima = data.loc[data['Algorithm'] == 'ARIMA']
dataRZ = data.loc[data['Algorithm'] == 'RZ']
dataNN = data.loc[data['Algorithm'] == 'NN']
#aggregation congested
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot(data['Amount'].unique(),dataArima['NRMSE'].loc[dataArima['Scenario'] == "Con"], 'c', label='ARIMA')
plt.plot(data['Amount'].unique(),dataRZ['NRMSE'].loc[dataRZ['Scenario'] == "Con"], 'm', label='RZ')
plt.plot(data['Amount'].unique(), dataNN['NRMSE'].loc[dataNN['Scenario'] == "Con"], 'y', label='NN')
plt.title('Amount in the Congested Scenario')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()
#aggregation normal
plt.figure(figsize=(10,7)) # 10 is width, 7 is height
plt.plot(data['Amount'].unique(),dataArima['NRMSE'].loc[dataArima['Scenario'] == "Nor"], 'c', label='ARIMA')
plt.plot(data['Amount'].unique(),dataRZ['NRMSE'].loc[dataRZ['Scenario'] == "Nor"], 'm', label='RZ')
plt.plot(data['Amount'].unique(), dataNN['NRMSE'].loc[dataNN['Scenario'] == "Nor"], 'y', label='NN')
plt.title('Amount in the Normal Scenario')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()

