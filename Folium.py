import matplotlib.pyplot as plt
import pandas as pd
import sklearn as skl
import numpy as np
import seaborn as sns
import folium
def foliumheart():
    path = "heart.csv"
    df = pd.read_csv(path)
    df = df.drop(columns = ['Class','Topic','DataSource','Data_Value_Footnote_Symbol','Data_Value_Footnote', 'StratificationCategory1'])
    df = df.drop(columns = ['Data_Value_Type', 'StratificationCategory2', 'TopicID', 'Georeference Column','Data_Value_Unit'])
    df = df.drop(columns = ['LocationID','LocationDesc','States','Counties'])
    df.rename(columns={"Stratification1": "Gender", "Stratification2": "Race", "Y_lat":"Y","X_lon":"X"},inplace = True)
    df.dropna(inplace = True)

    '''
    incidents = folium.map.FeatureGroup()
    limit = 100
    dfinc = df.iloc[0:limit, :]
    for lat, lng, in zip(dfinc.Y, dfinc.X):
        incidents.add_child(
            folium.CircleMarker(
                [lat, lng],
                radius=5,  # define how big you want the circle markers to be
                color='yellow',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6
            )
        )

    # add pop-up text to each marker on the map
    latitudes = list(dfinc.Y)
    longitudes = list(dfinc.X)

    for lat, lng, in zip(latitudes, longitudes):
        folium.Marker([lat, lng]).add_to(m)

        # add incidents to map
    m.add_child(incidents)
    '''

    url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    state_geo = state_geo = f'{url}/us-states.json'
    state_unemployment = f'{url}/US_Unemployment_Oct2012.csv'
    frequency = df['LocationAbbr'].value_counts().to_dict()
    flist = list(frequency.keys())
    fvalues = list(frequency.values())
    df['State'] = pd.Series(flist)
    df['Occurence'] = pd.Series(fvalues)
    m = folium.Map(location=[39.0119, -98.4842], zoom_start=5)
    
    folium.Choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=df,
        columns=['State','Occurence'],
        key_on='feature.id',
        fill_color='OrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Heart Disease Rate'
    ).add_to(m)

    folium.LayerControl().add_to(m)
    m.save('mapChoro.html')
foliumheart()


