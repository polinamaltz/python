import pandas as pd
import folium
import json

def get_color(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation <3000:
        return 'orange'
    else:
        return 'red'

data  = pd.read_csv("volcanoes_USA.txt")
countries_geojson = json.load(open("world_stat.json", 'r', encoding = 'utf-8-sig'))
m = folium.Map(location=[48.8, -121.8],
               zoom_start=6,
               tiles='openstreetmap')
volcanoes = folium.FeatureGroup(name = 'Volcanoes in the USA')
population = folium.FeatureGroup(name = 'Population (2005)')
folium.GeoJson(data = countries_geojson,
               style_function = lambda x : {'color' : 'green' if x["properties"]["POP2005"] < 10000000 else 'orange' if x["properties"]["POP2005"] < 20000000 else 'red',
                                            "fillOpacity": 0.4,
                                            "weight": 0}).add_to(population)

for i in range(0,62):
    folium.CircleMarker([data['LAT'][i], data['LON'][i]],
                popup=f"<i>{data['ELEV'][i]} metres</i>", 
                tooltip=f"{data['NAME'][i]}",
                radius = 6,
                color =  'grey', 
                fill_color =  get_color(data['ELEV'][i]), 
                fill= True,
                fill_opacity = 0.7,
                icon = folium.Icon(color = get_color(data['ELEV'][i]))).add_to(volcanoes)
volcanoes.add_to(m)
population.add_to(m)
folium.LayerControl().add_to(m)
m.save("test_map.html")
