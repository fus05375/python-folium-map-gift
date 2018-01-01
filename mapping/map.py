import folium
import pandas
""" początek fajnego projektu z wykorzystaniem python + folium (mapy) """
data = pandas.read_csv("example.txt")

lon= list(data["LON"])
lat= list(data["LAT"])

map=folium.Map(location=[49.4763117,20.0281912],zoom_start=15,tiles='Stamen Toner')
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker([49.4761859,20.0296225], popup='Dom mój',icon=folium.Icon(color='green')))
fg.add_child(folium.Marker([49.4802504,20.0174443], popup='Gdzieś tu Twój domek',icon=folium.Icon(color='red')))

for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker([lt,ln], popup='.',icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
