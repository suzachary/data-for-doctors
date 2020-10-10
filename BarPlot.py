import matplotlib.pyplot as plt
import pandas as pd
import sklearn as skl
import numpy as np
import seaborn as sns
import folium
def heartbar():
    path = "heart.csv"
    df = pd.read_csv(path)
    df = df.drop(columns=['Class', 'Topic', 'DataSource', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'StratificationCategory1'])
    df = df.drop(columns=['Data_Value_Type', 'StratificationCategory2', 'TopicID', 'Georeference Column', 'Data_Value_Unit'])
    df = df.drop(columns=['LocationID', 'LocationDesc', 'States', 'Counties'])
    df.rename(columns={"Stratification1": "Gender", "Stratification2": "Race", "Y_lat": "Y", "X_lon": "X"}, inplace=True)
    print(df.head())
    df.sort_values(by = ['Data_Value'], ascending=False, axis=0, inplace=True)
    df_top25 = df.iloc[0:275,:]
    print(df_top25.head())
    plt.style.use('seaborn-pastel')
    plt.figure(figsize=(20, 3))
    plt.bar(df_top25['LocationAbbr'],df_top25['Data_Value'], color = 'red', width = 0.5)
    plt.title('Heart Disease Trends In Top 25 States')
    plt.ylabel('Heart Attacks per 100,000')
    plt.xlabel('State')
    plt.show()
heartbar()